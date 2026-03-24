#!/usr/bin/env python3
"""Lean 4 documentation crawler using crawl4ai.

Stages:
1) Save raw HTML pages under ./output/01_raw_html/<source>/
2) Convert each HTML file to Markdown under ./output/02_markdown/<source>/
3) Consolidate into ./output/03_jsonl/<source>.jsonl
"""

from __future__ import annotations

import asyncio
import json
import logging
import re
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlsplit, urlunsplit

from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig

try:
    from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
except ImportError:
    # Compatibility fallback for older/newer package layout.
    from crawl4ai import DefaultMarkdownGenerator  # type: ignore


OUTPUT_DIR = Path("output")
RAW_DIR = OUTPUT_DIR / "01_raw_html"
MD_DIR = OUTPUT_DIR / "02_markdown"
JSONL_DIR = OUTPUT_DIR / "03_jsonl"

MAX_DEPTH = 5
REQUEST_DELAY_SECONDS = 1.0
MAX_RETRIES = 3
BASE_BACKOFF_SECONDS = 1.0

ASSET_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".css",
    ".js",
    ".pdf",
    ".zip",
}

MAIN_CONTENT_SELECTORS = [
    "main",
    "article",
    "div.md-content",
    "div.content",
]

OTHER_LANGUAGE_MARKERS = {
    "python",
    "py",
    "bash",
    "sh",
    "shell",
    "zsh",
    "javascript",
    "js",
    "typescript",
    "ts",
    "json",
    "yaml",
    "yml",
    "toml",
    "xml",
    "html",
    "css",
    "c",
    "cpp",
    "c++",
    "java",
    "rust",
    "go",
    "sql",
    "haskell",
    "ocaml",
    "scala",
    "julia",
    "r",
}


@dataclass(frozen=True)
class SourceConfig:
    source_id: str
    root_url: str


SOURCES: list[SourceConfig] = [
    SourceConfig(
        source_id="fp_in_lean",
        root_url="https://lean-lang.org/functional_programming_in_lean/",
    ),
    SourceConfig(
        source_id="tp_in_lean4",
        root_url="https://lean-lang.org/theorem_proving_in_lean4/",
    ),
    SourceConfig(
        source_id="math_in_lean",
        root_url="https://leanprover-community.github.io/mathematics_in_lean/",
    ),
    SourceConfig(
        source_id="reference_manual",
        root_url="https://lean-lang.org/doc/reference/latest/",
    ),
]


class RateLimiter:
    def __init__(self, min_interval_seconds: float) -> None:
        self.min_interval = min_interval_seconds
        self._last_request_time: float | None = None

    async def wait(self) -> None:
        now = asyncio.get_running_loop().time()
        if self._last_request_time is not None:
            elapsed = now - self._last_request_time
            remaining = self.min_interval - elapsed
            if remaining > 0:
                await asyncio.sleep(remaining)
        self._last_request_time = asyncio.get_running_loop().time()


def ensure_output_dirs(source_id: str) -> None:
    (RAW_DIR / source_id).mkdir(parents=True, exist_ok=True)
    (MD_DIR / source_id).mkdir(parents=True, exist_ok=True)
    JSONL_DIR.mkdir(parents=True, exist_ok=True)


def strip_trailing_slash(path: str) -> str:
    if path == "/":
        return "/"
    return path[:-1] if path.endswith("/") else path


def normalize_url(url: str, root_url: str) -> str:
    """Normalize URL for deduplication and scope checks.

    Rules:
    - Remove query and fragment.
    - Normalize /index.html to /
    - Remove trailing slash except for root and site root path.
    """
    root = urlsplit(root_url)
    parts = urlsplit(url)

    scheme = parts.scheme or root.scheme
    netloc = parts.netloc or root.netloc
    path = parts.path or "/"

    if path.endswith("/index.html"):
        path = path[: -len("index.html")]

    root_path = root.path if root.path.endswith("/") else f"{root.path}/"

    if path != "/" and path.endswith("/"):
        normalized_candidate = strip_trailing_slash(path)
        # Keep the exact configured root path with trailing slash.
        if path != root_path:
            path = normalized_candidate

    normalized = urlunsplit((scheme, netloc, path, "", ""))
    return normalized


def is_asset_url(url: str) -> bool:
    lower_path = urlsplit(url).path.lower()
    return any(lower_path.endswith(ext) for ext in ASSET_EXTENSIONS)


def in_scope(url: str, root_url: str) -> bool:
    root = urlsplit(root_url)
    target = urlsplit(url)

    if target.scheme != root.scheme or target.netloc != root.netloc:
        return False

    root_path = root.path if root.path.endswith("/") else f"{root.path}/"
    target_path = target.path or "/"

    return target_path.startswith(root_path)


def iter_links_from_html(base_url: str, html: str) -> Iterable[str]:
    soup = BeautifulSoup(html, "html.parser")
    for anchor in soup.find_all("a", href=True):
        href = (anchor.get("href") or "").strip()
        if not href:
            continue
        if href.startswith("#"):
            continue
        yield urljoin(base_url, href)


def slugify_relative_path(path: str) -> str:
    # Keep deterministic, flat filenames per source directory.
    safe = path.strip("/")
    if not safe:
        return "index"
    safe = safe.replace("/", "__")
    safe = re.sub(r"\.html?$", "", safe, flags=re.IGNORECASE)
    safe = re.sub(r"[^a-zA-Z0-9._-]+", "_", safe)
    safe = safe.strip("._-")
    return safe or "index"


def url_to_slug(url: str, root_url: str) -> str:
    root = urlsplit(root_url)
    target = urlsplit(url)

    root_path = root.path if root.path.endswith("/") else f"{root.path}/"
    relative = target.path[len(root_path) :] if target.path.startswith(root_path) else target.path
    if relative == "":
        return "index"
    return slugify_relative_path(relative)


def pick_main_selector_from_html(html: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")
    for selector in MAIN_CONTENT_SELECTORS:
        if soup.select_one(selector):
            return selector
    return None


def markdown_to_text(markdown_obj: object) -> str:
    if markdown_obj is None:
        return ""

    if isinstance(markdown_obj, str):
        return markdown_obj

    # Crawl4AI may return a MarkdownGenerationResult object.
    for attr in ("fit_markdown", "raw_markdown", "markdown_with_citations"):
        value = getattr(markdown_obj, attr, None)
        if isinstance(value, str) and value.strip():
            return value

    return str(markdown_obj)


def extract_title_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
        if title:
            return title

    h1 = soup.find("h1")
    if h1:
        text = h1.get_text(" ", strip=True)
        if text:
            return text

    return ""


def _extract_lang_markers(tag) -> set[str]:
    markers: set[str] = set()
    classes = tag.get("class") or []
    for cls in classes:
        cls_lower = str(cls).strip().lower()
        if not cls_lower:
            continue
        markers.add(cls_lower)
        if cls_lower.startswith("language-"):
            markers.add(cls_lower[len("language-") :])
    return markers


def _looks_lean_code(lang_markers: set[str]) -> bool:
    if any(marker in {"lean", "lean4", "language-lean", "language-lean4"} for marker in lang_markers):
        return True
    if lang_markers & OTHER_LANGUAGE_MARKERS:
        return False
    # In Lean documentation, unlabeled blocks are usually Lean snippets.
    return True


def extract_lean_code_blocks(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    blocks: list[str] = []
    seen: set[str] = set()

    for pre in soup.find_all("pre"):
        code = pre.find("code")
        target = code or pre
        lang_markers = _extract_lang_markers(pre) | _extract_lang_markers(target)
        text = target.get_text("\n", strip=False).rstrip()
        if not text:
            continue
        if not _looks_lean_code(lang_markers):
            continue
        normalized = text.strip()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        blocks.append(text)

    for code in soup.find_all("code"):
        if code.find_parent("pre"):
            continue
        lang_markers = _extract_lang_markers(code)
        if not _looks_lean_code(lang_markers):
            continue
        text = code.get_text("\n", strip=False).rstrip()
        normalized = text.strip()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        blocks.append(text)

    return blocks


async def fetch_page_html(
    crawler: AsyncWebCrawler,
    url: str,
    limiter: RateLimiter,
) -> str | None:
    run_cfg = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        page_timeout=60000,
        wait_until="domcontentloaded",
    )

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            await limiter.wait()
            result = await crawler.arun(url=url, config=run_cfg)
            if result.success and result.html:
                return result.html

            message = getattr(result, "error_message", "unknown error")
            raise RuntimeError(f"crawl failed: {message}")
        except Exception as exc:  # noqa: BLE001
            if attempt >= MAX_RETRIES:
                logging.error("Failed to fetch %s after %d attempts: %s", url, attempt, exc)
                return None
            backoff = BASE_BACKOFF_SECONDS * (2 ** (attempt - 1))
            logging.warning(
                "Error fetching %s (attempt %d/%d): %s. Retrying in %.1fs",
                url,
                attempt,
                MAX_RETRIES,
                exc,
                backoff,
            )
            await asyncio.sleep(backoff)

    return None


async def discover_and_cache_urls(
    crawler: AsyncWebCrawler,
    source: SourceConfig,
    limiter: RateLimiter,
) -> dict[str, str]:
    """Crawl source root with BFS and cache HTML files in stage 1.

    Returns a mapping of canonical URL -> slug.
    """
    ensure_output_dirs(source.source_id)

    root_normalized = normalize_url(source.root_url, source.root_url)

    queue: deque[tuple[str, int]] = deque([(root_normalized, 0)])
    visited: set[str] = set()
    url_to_slug_map: dict[str, str] = {}

    while queue:
        current_url, depth = queue.popleft()
        if current_url in visited:
            continue
        visited.add(current_url)

        if depth > MAX_DEPTH:
            continue

        slug = url_to_slug(current_url, source.root_url)
        raw_path = RAW_DIR / source.source_id / f"{slug}.html"
        url_to_slug_map[current_url] = slug

        logging.info("[%s] Crawling depth=%d url=%s", source.source_id, depth, current_url)

        html: str | None
        if raw_path.exists():
            html = raw_path.read_text(encoding="utf-8", errors="replace")
            logging.info("[%s] Stage1 cache hit: %s", source.source_id, raw_path)
        else:
            html = await fetch_page_html(crawler, current_url, limiter)
            if html is None:
                continue
            raw_path.write_text(html, encoding="utf-8")
            logging.info("[%s] Stage1 saved: %s", source.source_id, raw_path)

        links_discovered = 0
        for absolute_url in iter_links_from_html(current_url, html):
            candidate = normalize_url(absolute_url, source.root_url)
            if is_asset_url(candidate):
                continue
            if not in_scope(candidate, source.root_url):
                continue
            if candidate in visited:
                continue
            if depth + 1 <= MAX_DEPTH:
                queue.append((candidate, depth + 1))
                links_discovered += 1

        logging.info("[%s] Discovered %d in-scope links from %s", source.source_id, links_discovered, current_url)

    return url_to_slug_map


async def generate_markdown_stage(
    crawler: AsyncWebCrawler,
    source: SourceConfig,
    url_to_slug_map: dict[str, str],
) -> None:
    md_generator = DefaultMarkdownGenerator(
        options={
            "ignore_links": False,
            "ignore_images": True,
            "skip_internal_links": False,
            "body_width": 0,
        }
    )

    for url, slug in sorted(url_to_slug_map.items()):
        raw_path = RAW_DIR / source.source_id / f"{slug}.html"
        md_path = MD_DIR / source.source_id / f"{slug}.md"

        if not raw_path.exists():
            logging.warning("[%s] Missing raw HTML for %s", source.source_id, url)
            continue

        html = raw_path.read_text(encoding="utf-8", errors="replace")
        css_selector = pick_main_selector_from_html(html)

        run_cfg_kwargs = {
            "cache_mode": CacheMode.BYPASS,
            "markdown_generator": md_generator,
            "page_timeout": 60000,
            "wait_until": "domcontentloaded",
        }
        if css_selector:
            run_cfg_kwargs["css_selector"] = css_selector

        run_cfg = CrawlerRunConfig(**run_cfg_kwargs)

        file_url = f"file://{raw_path.resolve()}"
        result = await crawler.arun(url=file_url, config=run_cfg)

        if not result.success:
            message = getattr(result, "error_message", "unknown error")
            logging.error("[%s] Markdown conversion failed for %s: %s", source.source_id, url, message)
            continue

        markdown_text = markdown_to_text(result.markdown)
        md_path.write_text(markdown_text, encoding="utf-8")
        logging.info("[%s] Stage2 saved markdown: %s", source.source_id, md_path)


def write_jsonl_stage(source: SourceConfig, url_to_slug_map: dict[str, str]) -> None:
    jsonl_path = JSONL_DIR / f"{source.source_id}.jsonl"
    records_written = 0

    with jsonl_path.open("w", encoding="utf-8") as out:
        for url, slug in sorted(url_to_slug_map.items()):
            raw_path = RAW_DIR / source.source_id / f"{slug}.html"
            md_path = MD_DIR / source.source_id / f"{slug}.md"

            if not raw_path.exists() or not md_path.exists():
                logging.warning("[%s] Skipping missing pair raw/md for %s", source.source_id, url)
                continue

            html = raw_path.read_text(encoding="utf-8", errors="replace")
            markdown = md_path.read_text(encoding="utf-8", errors="replace")

            record = {
                "url": url,
                "title": extract_title_from_html(html),
                "markdown": markdown,
                "code_blocks": extract_lean_code_blocks(html),
                "source": source.source_id,
                "crawled_at": datetime.now(timezone.utc).isoformat(),
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            records_written += 1

    logging.info("[%s] Stage3 wrote %d records: %s", source.source_id, records_written, jsonl_path)


async def run_source(source: SourceConfig, crawler: AsyncWebCrawler, limiter: RateLimiter) -> None:
    logging.info("===== SOURCE START: %s =====", source.source_id)
    ensure_output_dirs(source.source_id)

    url_to_slug_map = await discover_and_cache_urls(crawler, source, limiter)
    await generate_markdown_stage(crawler, source, url_to_slug_map)
    write_jsonl_stage(source, url_to_slug_map)

    logging.info("===== SOURCE END: %s pages=%d =====", source.source_id, len(url_to_slug_map))


async def amain() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    browser_cfg = BrowserConfig(
        browser_type="chromium",
        headless=True,
        verbose=False,
    )

    limiter = RateLimiter(REQUEST_DELAY_SECONDS)

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        for source in SOURCES:
            await run_source(source, crawler, limiter)


if __name__ == "__main__":
    asyncio.run(amain())
