#!/usr/bin/env python3
"""Explore the rel="next" navigation structure of a Verso book."""

import asyncio
import logging
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
log = logging.getLogger(__name__)

START_URL = "https://lean-lang.org/functional_programming_in_lean/"


def resolve_next_link(page_url: str, html: str) -> str | None:
    """Find <a rel="next"> and resolve its href against the page (respecting <base>)."""
    soup = BeautifulSoup(html, "html.parser")

    # Effective base URL: use <base href> if present, otherwise the page URL.
    base_tag = soup.find("base", href=True)
    base_url = urljoin(page_url, base_tag["href"]) if base_tag else page_url

    next_el = soup.find("a", rel="next")
    if not next_el or not next_el.get("href"):
        return None

    return urljoin(base_url, next_el["href"])


async def main() -> None:
    browser_cfg = BrowserConfig(browser_type="chromium", headless=True, verbose=False)
    run_cfg = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        page_timeout=60000,
        wait_until="domcontentloaded",
    )

    current_url = START_URL
    page_num = 0

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        while current_url:
            page_num += 1
            log.info("Page %d — fetching: %s", page_num, current_url)

            result = await crawler.arun(url=current_url, config=run_cfg)
            if not result.success:
                log.error("Fetch failed: %s", getattr(result, "error_message", "unknown"))
                break

            next_url = resolve_next_link(current_url, result.html)

            if next_url:
                log.info("Page %d — next → %s", page_num, next_url)
                current_url = next_url
            else:
                log.info("Page %d — no rel='next' found. End of book.", page_num)
                current_url = None

    log.info("Done. Total pages: %d", page_num)


if __name__ == "__main__":
    asyncio.run(main())
