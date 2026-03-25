# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Lean 4 documentation crawler that scrapes multiple Lean language book/reference sites, converts HTML to Markdown, and outputs structured JSONL files. It follows `rel="next"` navigation links to discover pages sequentially through each book.

## Commands

```bash
# Install dependencies (uses uv package manager)
uv sync

# Run the full crawler pipeline (all sources)
uv run python crawl_lean4.py

# Explore navigation structure of a Verso book
uv run python explore.py

# Playwright browser must be installed for crawl4ai
uv run playwright install chromium
```

There are no tests, linting, or formatting tools configured.

## Architecture

### Three-Stage Pipeline (`crawl_lean4.py`)

The crawler processes each source sequentially through three stages:

1. **Discovery & HTML caching** (`discover_pages` / `fetch_page`) — Follows the `<a rel="next">` / `<link rel="next">` chain from a root URL, saving raw HTML to `output/01_raw_html/<source>/`. Cached pages are reused on re-runs.

2. **HTML-to-Markdown conversion** (`convert_to_markdown`) — Feeds cached HTML files back through crawl4ai's `DefaultMarkdownGenerator`, selecting main content via CSS selectors (`main`, `article`, `div.md-content`, `div.content`). Output goes to `output/02_markdown/<source>/`.

3. **JSONL consolidation** (`write_jsonl`) — Combines Markdown content, extracted Lean code blocks, page title, URL, and timestamp into `output/03_jsonl/<source>.jsonl`.

### Key Design Decisions

- **Rate limiting**: `RateLimiter` class enforces a minimum interval (default 1s) between requests.
- **Retry with backoff**: Up to 3 attempts per page with exponential backoff.
- **Lean code detection**: Code blocks without an explicit language class are assumed to be Lean (since the sources are Lean documentation). Blocks with known non-Lean language markers are excluded.
- **Fragment stripping**: URL fragments are stripped to prevent revisiting the same page.
- **`<base href>` awareness**: Link resolution respects `<base>` tags used by Verso-generated books.

### Data Sources

Configured in the `SOURCES` list as `SourceConfig` dataclasses:
- `fp_in_lean` — Functional Programming in Lean
- `tp_in_lean4` — Theorem Proving in Lean 4
- `math_in_lean` — Mathematics in Lean
- `reference_manual` — Lean Reference Manual

### `explore.py`

Standalone utility that walks the `rel="next"` chain from a start URL and logs each page — useful for understanding a book's navigation structure before adding it as a source.

## Tech Stack

- **Python >=3.11**, managed with **uv**
- **crawl4ai** + **Playwright** (Chromium) for rendering and crawling
- **BeautifulSoup4** for HTML parsing and link/code extraction
- Fully async (`asyncio`)
