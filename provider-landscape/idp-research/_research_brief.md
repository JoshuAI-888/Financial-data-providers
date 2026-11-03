# Vendor evidence refresh brief (<Mon YYYY>) — one vendor per agent

Today is <date>. Window: since the last refresh (see vendors.json idp_as_of) unless told otherwise. You are gathering sources for ONE vendor in an Investment Data Platform (IDP)
evaluation for a Databricks-strategic, ~$35bn institutional multi-asset manager based in NZ/ANZ.
Repo: /home/claude/financial-data-providers (read-only for you — DO NOT edit any repo file, DO NOT git).
Vendor files: provider-landscape/idp-research/<id>.md (fact-sheet), reqscores_*.json (requirement scores;
the 5 newer vendors are in reqscores_new_*.json), reqnotes_*.md (rubric/rationale), _v2_updates.md
(August 2026 audit — copy its style).

## Tools
- Use WebSearch (mode "standard"; "extended" only if standard is thin) to find sources.
- Use WebFetch to OPEN the key sources (at least every source behind a proposed change). Record
  `opened` if WebFetch returned the page content, `search-only` if you only saw it in search results
  (e.g. fetch failed/blocked). Never invent URLs; only use URLs you saw in search results or fetched pages.
- Sandbox curl to vendor sites is blocked — don't bother with Bash network calls.
- Be efficient: aim for ~15-30 tool calls total.

## The five gap areas (August audit)
1. Databricks & open architecture (Delta Sharing, Unity Catalog, Marketplace, zero-copy, write-back)
2. AI / agents / MCP (MCP servers, agent products, GA vs preview, buyer-own-LLM, permission-aware AI)
3. Ownership / corporate changes (M&A, funding, PE, leadership, partnerships)
4. APAC / ANZ support (offices, named Australia/NZ clients, regional staff)
5. Pricing / commercial model

## Evidence rules
- Every source: URL, title, publisher, **vendor** (vendor-authored: vendor site, vendor press release,
  vendor blog, vendor-paid PR wire, partner announcement) or **independent** (trade press, analyst,
  customer, regulator, filings), evidence type (one of: Official release note, Official docs, Vendor marketing,
  Named customer case study, News, Independent research, Official filings, Platform-standards docs),
  publication date (YYYY-MM-DD, or YYYY-MM if day unknown; "undated" if none), and opened/search-only.
- Distinguish GA vs preview vs roadmap. Don't upgrade on press-release adjectives.
- Score caps (0–5 scale, no proof of value has run): roadmap≤1.0, sales/marketing≤2.0, docs≤3.0,
  demo≤3.5, named-customer production reference≤4.0. Scores step in 0.5.
- "No new evidence located" is a valid, useful finding — say it explicitly per gap rather than padding.
- Beware SEO spam / AI-generated aggregator blogs (e.g. random .blog domains, "jingtea"): don't cite them.
- If a claim in the current fact-sheet now looks wrong or stale, flag it.

## Output — write exactly one file: <findings-dir>/<id>.md (outside the repo) with these sections
```
# <Vendor> — <Mon YYYY> refresh findings
Window searched: <dates>

## Findings by gap
### 1. Databricks & open architecture
- <finding, 1-3 sentences, with GA/preview/roadmap status> [S1][S2]
  (or: No new evidence located (as of <date>).)
### 2. AI / agents / MCP
### 3. Ownership / corporate changes
### 4. APAC / ANZ support
### 5. Pricing / commercial model
### 6. Other material changes since the last refresh (optional)
### Lead questions (answer each lead you were given explicitly: CONFIRMED / NOT CONFIRMED / CONTRADICTED, with sources)

## Sources
- [S1] <URL> | <title> | <publisher> | vendor|independent | <evidence type> | <pub date> | opened|search-only

## Proposed requirement-score changes
(only where evidence justifies; otherwise write "None proposed")
- <REQ-ID>: <old s> -> <new s> | ev=<docs|sales|roadmap|named-customer|demo|none> rel=<GA|preview|roadmap|partner|none> | type=<evidence type> | url=<best URL> | cite=<short citation> | note=<≤140 chars why>

## Proposed hard-gate changes (G01–G22; only if justified)
- G14: partial -> pass | reason [S#]

## Proposed fact-sheet text edits
- Section <n>: <replacement or added sentence(s), ready to paste, with dates>

## Recent-developments line (one sentence, ≤300 chars, dated, for the vendor card)
```
Keep the file under ~250 lines. Your final reply to me: 5 lines max summarising the most material change.
