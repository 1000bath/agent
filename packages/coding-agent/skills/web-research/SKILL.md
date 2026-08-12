---
name: web-research
description: Research the public web with search, URL fetching, content extraction, source deduplication, and citations. Use when answering current/factual questions, comparing tools, researching GitHub projects, or reading online documentation. Prefer this over raw web search when sources and evidence matter.
license: MIT
---

# Web Research

Use the bundled script for bounded, source-backed research. Keep every claim tied to a URL and report when a provider or page could not be reached.

## Search

```bash
python3 scripts/web_research.py search "query" --limit 5 --timeout 20
```

The search path tries configured providers first, then a DuckDuckGo HTML fallback. Optional providers:

- `TAVILY_API_KEY` for Tavily search
- `EXA_API_KEY` for Exa search
- `BRAVE_API_KEY` for Brave Search

Never print or commit these values.

## Fetch

```bash
python3 scripts/web_research.py fetch "https://example.com/docs" --max-chars 12000 --timeout 20
```

The fetcher accepts HTML, Markdown, JSON, and plain text, removes scripts/styles/navigation noise from HTML, and emits the canonical URL plus extracted text.

## Scrape structured content

```bash
python3 scripts/web_research.py scrape "https://example.com" --tag article --max-items 20 --timeout 20
```

Use `--tag p`, `--tag h2`, `--tag a`, or `--tag article` to extract bounded page elements. This is for public pages only; respect robots.txt, terms of service, rate limits, and copyright. Do not bypass authentication, CAPTCHAs, paywalls, or access controls.

## Workflow

1. Search with a precise query and collect 3–5 independent sources.
2. Fetch the strongest primary sources (official docs, repository, release notes) first.
3. Deduplicate URLs and distinguish facts from inference.
4. Cite claims inline as `[source](URL)` and include an access date for changing information.
5. If all providers fail, say so instead of presenting guesses as facts.

All network operations must have an explicit timeout and bounded output. Use `--help` for options.
