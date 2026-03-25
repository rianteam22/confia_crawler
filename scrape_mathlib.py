#!/usr/bin/env python3
"""Mathlib4 docs crawler.

Strategy: parse the navbar.html index to discover all module pages,
then run the same 3-stage pipeline as crawl_lean4.

Stages:
1) Discover URLs from navbar.html, fetch and cache raw HTML under ./output/01_raw_html/mathlib4_docs/
2) Convert each HTML file to Markdown under ./output/02_markdown/mathlib4_docs/
3) Consolidate into ./output/03_jsonl/mathlib4_docs.jsonl
"""

from __future__ import annotations

import argparse
import asyncio
import logging
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, BrowserConfig

from crawl_lean4 import (
    RAW_DIR,
    RateLimiter,
    REQUEST_DELAY_SECONDS,
    SourceConfig,
    convert_to_markdown,
    fetch_page,
    strip_fragment,
    url_to_slug,
    write_jsonl,
)

log = logging.getLogger(__name__)

SOURCE = SourceConfig("mathlib4_docs", "https://leanprover-community.github.io/mathlib4_docs/")
NAVBAR_URL = urljoin(SOURCE.root_url, "navbar.html")


# ---------------------------------------------------------------------------
# Stage 1 — Discover & cache raw HTML (via navbar index)
# ---------------------------------------------------------------------------


async def fetch_navbar(url: str = NAVBAR_URL) -> str:
    """Fetch the navbar HTML (static page, no browser needed)."""
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.text


def parse_module_urls(html: str, base_url: str = SOURCE.root_url) -> list[str]:
    """Extract all module URLs from nav_link elements inside module_list."""
    soup = BeautifulSoup(html, "html.parser")

    module_list = soup.find(class_="module_list")
    if not module_list:
        log.warning("No element with class 'module_list' found.")
        return []

    urls: list[str] = []
    seen: set[str] = set()

    for nav_link in module_list.find_all(class_="nav_link"):
        anchor = nav_link.find("a", href=True)
        if not anchor:
            continue
        full_url = strip_fragment(urljoin(base_url, anchor["href"]))
        if full_url not in seen:
            seen.add(full_url)
            urls.append(full_url)

    return urls


async def discover_pages(
    crawler: AsyncWebCrawler, limiter: RateLimiter, *, max_pages: int = 0,
) -> dict[str, str]:
    """Fetch navbar, parse URLs, then fetch and cache each page. Returns {url: slug}.

    Args:
        max_pages: Limit number of pages to fetch. 0 means no limit.
    """
    src = SOURCE.source_id
    (RAW_DIR / src).mkdir(parents=True, exist_ok=True)

    log.info("[%s] Fetching navbar from %s", src, NAVBAR_URL)
    navbar_html = await fetch_navbar()
    urls = parse_module_urls(navbar_html)
    if max_pages > 0:
        urls = urls[:max_pages]
        log.info("[%s] Limited to %d pages (--max-pages).", src, max_pages)
    log.info("[%s] Found %d module URLs to process.", src, len(urls))

    url_map: dict[str, str] = {}

    for i, url in enumerate(urls, 1):
        slug = url_to_slug(url, SOURCE.root_url)
        raw_path = RAW_DIR / src / f"{slug}.html"

        if raw_path.exists():
            log.info("[%s] (%d/%d) Cache hit: %s", src, i, len(urls), slug)
        else:
            log.info("[%s] (%d/%d) Fetching: %s", src, i, len(urls), url)
            html = await fetch_page(crawler, url, limiter)
            if html is None:
                log.error("[%s] Fetch failed, skipping: %s", src, url)
                continue
            raw_path.write_text(html, encoding="utf-8")

        url_map[url] = slug

    log.info("[%s] Stage 1 done: %d pages cached.", src, len(url_map))
    return url_map


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


async def amain(max_pages: int = 0) -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

    browser_cfg = BrowserConfig(browser_type="chromium", headless=True, verbose=False)
    limiter = RateLimiter(REQUEST_DELAY_SECONDS)

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        log.info("===== %s =====", SOURCE.source_id)
        url_map = await discover_pages(crawler, limiter, max_pages=max_pages)
        await convert_to_markdown(crawler, SOURCE, url_map)
        write_jsonl(SOURCE, url_map)
        log.info("===== %s done: %d pages =====", SOURCE.source_id, len(url_map))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crawl mathlib4 docs.")
    parser.add_argument("--max-pages", type=int, default=0, help="Limit pages to fetch (0 = all).")
    args = parser.parse_args()
    asyncio.run(amain(max_pages=args.max_pages))
