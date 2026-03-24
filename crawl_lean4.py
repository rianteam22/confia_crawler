#!/usr/bin/env python3
"""Lean 4 documentation crawler using crawl4ai.

Strategy: follow <a rel="next"> links page by page until the end of each book.

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
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit

from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig

try:
    from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
except ImportError:
    from crawl4ai import DefaultMarkdownGenerator  # type: ignore

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

OUTPUT_DIR = Path("output")
RAW_DIR = OUTPUT_DIR / "01_raw_html"
MD_DIR = OUTPUT_DIR / "02_markdown"
JSONL_DIR = OUTPUT_DIR / "03_jsonl"

REQUEST_DELAY_SECONDS = 1.0
MAX_RETRIES = 3
BASE_BACKOFF_SECONDS = 1.0

MAIN_CONTENT_SELECTORS = ["main", "article", "div.md-content", "div.content"]

OTHER_LANGUAGE_MARKERS = {
    "python", "py", "bash", "sh", "shell", "zsh",
    "javascript", "js", "typescript", "ts",
    "json", "yaml", "yml", "toml", "xml", "html", "css",
    "c", "cpp", "c++", "java", "rust", "go", "sql",
    "haskell", "ocaml", "scala", "julia", "r",
}


@dataclass(frozen=True)
class SourceConfig:
    source_id: str
    root_url: str


SOURCES: list[SourceConfig] = [
    SourceConfig("fp_in_lean", "https://lean-lang.org/functional_programming_in_lean/"),
    SourceConfig("tp_in_lean4", "https://lean-lang.org/theorem_proving_in_lean4/"),
    SourceConfig("math_in_lean", "https://leanprover-community.github.io/mathematics_in_lean/"),
    SourceConfig("reference_manual", "https://lean-lang.org/doc/reference/latest/"),
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


class RateLimiter:
    def __init__(self, min_interval: float) -> None:
        self.min_interval = min_interval
        self._last: float | None = None

    async def wait(self) -> None:
        now = asyncio.get_running_loop().time()
        if self._last is not None:
            remaining = self.min_interval - (now - self._last)
            if remaining > 0:
                await asyncio.sleep(remaining)
        self._last = asyncio.get_running_loop().time()


def strip_fragment(url: str) -> str:
    """Remove fragment (#...) from URL."""
    p = urlsplit(url)
    return urlunsplit((p.scheme, p.netloc, p.path, p.query, ""))


def resolve_next_link(page_url: str, html: str) -> str | None:
    """Find <a rel="next"> and resolve its href (respecting <base>)."""
    soup = BeautifulSoup(html, "html.parser")

    base_tag = soup.find("base", href=True)
    base_url = urljoin(page_url, base_tag["href"]) if base_tag else page_url

    # <a rel="next"> (Verso) or <link rel="next"> (Sphinx)
    for tag in ("a", "link"):
        el = soup.find(tag, rel=lambda r: r and "next" in r, href=True)
        if el:
            href = el["href"].strip()
            if href and not href.startswith("#"):
                return urljoin(base_url, href)

    return None


def url_to_slug(url: str, root_url: str) -> str:
    """Convert URL to a flat filesystem-safe slug relative to root."""
    root_path = urlsplit(root_url).path
    if not root_path.endswith("/"):
        root_path += "/"
    target_path = urlsplit(url).path or "/"

    relative = target_path[len(root_path):] if target_path.startswith(root_path) else target_path
    if not relative:
        return "index"

    safe = relative.strip("/").replace("/", "__")
    safe = re.sub(r"\.html?$", "", safe, flags=re.IGNORECASE)
    safe = re.sub(r"[^a-zA-Z0-9._-]+", "_", safe)
    return safe.strip("._-") or "index"


def pick_main_selector(html: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")
    for sel in MAIN_CONTENT_SELECTORS:
        if soup.select_one(sel):
            return sel
    return None


def extract_title(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    if soup.title and soup.title.string:
        t = soup.title.string.strip()
        if t:
            return t
    h1 = soup.find("h1")
    if h1:
        t = h1.get_text(" ", strip=True)
        if t:
            return t
    return ""


def _lang_markers(tag) -> set[str]:
    markers: set[str] = set()
    for cls in tag.get("class") or []:
        c = str(cls).strip().lower()
        if c:
            markers.add(c)
            if c.startswith("language-"):
                markers.add(c[len("language-"):])
    return markers


def _is_lean(markers: set[str]) -> bool:
    if markers & {"lean", "lean4", "language-lean", "language-lean4"}:
        return True
    if markers & OTHER_LANGUAGE_MARKERS:
        return False
    return True


def extract_lean_code_blocks(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    blocks: list[str] = []
    seen: set[str] = set()

    for pre in soup.find_all("pre"):
        code = pre.find("code")
        target = code or pre
        markers = _lang_markers(pre) | _lang_markers(target)
        text = target.get_text("\n", strip=False).rstrip()
        norm = text.strip()
        if norm and _is_lean(markers) and norm not in seen:
            seen.add(norm)
            blocks.append(text)

    for code in soup.find_all("code"):
        if code.find_parent("pre"):
            continue
        markers = _lang_markers(code)
        text = code.get_text("\n", strip=False).rstrip()
        norm = text.strip()
        if norm and _is_lean(markers) and norm not in seen:
            seen.add(norm)
            blocks.append(text)

    return blocks


def markdown_to_text(md_obj: object) -> str:
    if md_obj is None:
        return ""
    if isinstance(md_obj, str):
        return md_obj
    for attr in ("fit_markdown", "raw_markdown", "markdown_with_citations"):
        val = getattr(md_obj, attr, None)
        if isinstance(val, str) and val.strip():
            return val
    return str(md_obj)


# ---------------------------------------------------------------------------
# Stage 1 — Discover & cache raw HTML (follow rel="next")
# ---------------------------------------------------------------------------


async def fetch_page(
    crawler: AsyncWebCrawler, url: str, limiter: RateLimiter,
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
            raise RuntimeError(getattr(result, "error_message", "unknown error"))
        except Exception as exc:
            if attempt >= MAX_RETRIES:
                log.error("Failed %s after %d attempts: %s", url, attempt, exc)
                return None
            backoff = BASE_BACKOFF_SECONDS * (2 ** (attempt - 1))
            log.warning("Retry %d/%d for %s: %s (%.1fs)", attempt, MAX_RETRIES, url, exc, backoff)
            await asyncio.sleep(backoff)
    return None


async def discover_pages(
    crawler: AsyncWebCrawler, source: SourceConfig, limiter: RateLimiter,
) -> dict[str, str]:
    """Follow rel='next' chain from root. Returns {url: slug}."""
    src = source.source_id
    (RAW_DIR / src).mkdir(parents=True, exist_ok=True)

    current_url: str | None = source.root_url
    visited: set[str] = set()
    url_map: dict[str, str] = {}
    page_num = 0

    while current_url:
        canonical = strip_fragment(current_url)
        if canonical in visited:
            break
        visited.add(canonical)
        page_num += 1

        slug = url_to_slug(canonical, source.root_url)
        raw_path = RAW_DIR / src / f"{slug}.html"

        log.info("[%s] Page %d: %s", src, page_num, canonical)

        if raw_path.exists():
            html = raw_path.read_text(encoding="utf-8", errors="replace")
            log.info("[%s] Cache hit: %s", src, raw_path.name)
        else:
            html = await fetch_page(crawler, canonical, limiter)
            if html is None:
                log.error("[%s] Fetch failed, stopping.", src)
                break
            raw_path.write_text(html, encoding="utf-8")

        url_map[canonical] = slug

        next_url = resolve_next_link(canonical, html)
        if next_url:
            log.info("[%s] Next → %s", src, strip_fragment(next_url))
            current_url = next_url
        else:
            log.info("[%s] No next link — end of book.", src)
            current_url = None

    log.info("[%s] Stage 1 done: %d pages", src, len(url_map))
    return url_map


# ---------------------------------------------------------------------------
# Stage 2 — HTML → Markdown
# ---------------------------------------------------------------------------


async def convert_to_markdown(
    crawler: AsyncWebCrawler, source: SourceConfig, url_map: dict[str, str],
) -> None:
    src = source.source_id
    (MD_DIR / src).mkdir(parents=True, exist_ok=True)

    md_gen = DefaultMarkdownGenerator(
        options={"ignore_links": False, "ignore_images": True, "skip_internal_links": False, "body_width": 0}
    )

    for url, slug in sorted(url_map.items()):
        raw_path = RAW_DIR / src / f"{slug}.html"
        md_path = MD_DIR / src / f"{slug}.md"

        if not raw_path.exists():
            continue

        html = raw_path.read_text(encoding="utf-8", errors="replace")
        css_sel = pick_main_selector(html)

        cfg = {"cache_mode": CacheMode.BYPASS, "markdown_generator": md_gen,
               "page_timeout": 60000, "wait_until": "domcontentloaded"}
        if css_sel:
            cfg["css_selector"] = css_sel

        result = await crawler.arun(url=f"file://{raw_path.resolve()}", config=CrawlerRunConfig(**cfg))
        if not result.success:
            log.error("[%s] Markdown failed for %s", src, url)
            continue

        md_path.write_text(markdown_to_text(result.markdown), encoding="utf-8")
        log.info("[%s] Stage 2: %s", src, md_path.name)


# ---------------------------------------------------------------------------
# Stage 3 — JSONL
# ---------------------------------------------------------------------------


def write_jsonl(source: SourceConfig, url_map: dict[str, str]) -> None:
    src = source.source_id
    JSONL_DIR.mkdir(parents=True, exist_ok=True)
    jsonl_path = JSONL_DIR / f"{src}.jsonl"
    written = 0

    with jsonl_path.open("w", encoding="utf-8") as out:
        for url, slug in sorted(url_map.items()):
            raw_path = RAW_DIR / src / f"{slug}.html"
            md_path = MD_DIR / src / f"{slug}.md"
            if not raw_path.exists() or not md_path.exists():
                continue

            html = raw_path.read_text(encoding="utf-8", errors="replace")
            record = {
                "url": url,
                "title": extract_title(html),
                "markdown": md_path.read_text(encoding="utf-8", errors="replace"),
                "code_blocks": extract_lean_code_blocks(html),
                "source": src,
                "crawled_at": datetime.now(timezone.utc).isoformat(),
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            written += 1

    log.info("[%s] Stage 3: %d records → %s", src, written, jsonl_path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


async def run_source(source: SourceConfig, crawler: AsyncWebCrawler, limiter: RateLimiter) -> None:
    log.info("===== %s =====", source.source_id)
    url_map = await discover_pages(crawler, source, limiter)
    await convert_to_markdown(crawler, source, url_map)
    write_jsonl(source, url_map)
    log.info("===== %s done: %d pages =====", source.source_id, len(url_map))


async def amain() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

    browser_cfg = BrowserConfig(browser_type="chromium", headless=True, verbose=False)
    limiter = RateLimiter(REQUEST_DELAY_SECONDS)

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        for source in SOURCES:
            await run_source(source, crawler, limiter)


if __name__ == "__main__":
    asyncio.run(amain())
