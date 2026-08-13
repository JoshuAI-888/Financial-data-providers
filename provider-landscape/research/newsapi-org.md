# NewsAPI.org

## 1. Snapshot
- **Owner/parent:** NewsAPI (independent; founded 2017 by Aeron Buchanan), HQ London, UK. Positioning: the simplest, most widely-cited REST API for searching headlines and articles from the open web — a developer/tutorial staple rather than a finance-specialised feed.
- **Regions/language coverage:** Global. Claims 150,000+ sources across 55 countries and **14 languages**; coverage and search quality are strongest for English-language Western outlets, with thinner non-English and emerging-market depth than GDELT or Factiva.
- **Free tier:** **YES — but heavily restricted (flag clearly).** The "Developer" plan is $0: ~100 requests/day, articles **delayed ~24 hours**, search window limited, **CORS restricted to localhost only**, and **non-commercial / development-and-testing use only**. It breaks the moment you deploy to a real domain — the single biggest community complaint.
- **Pricing model & ranges (published):** Steep jump from free to paid — **Business $449/mo** (250,000 req/mo, commercial use, no 24h delay), **Advanced $1,749/mo** (2,000,000 req/mo), **Enterprise** custom-quoted. ~20% discount on annual billing. No sub-$449 middle tier.

## 2. Data-domain coverage
- **Financial news:** Indirect — general web/business news filterable by keyword/source; no finance-specific enrichment.
- **General news:** Core strength — broad headline and article search across mainstream outlets and blogs.
- **Press releases/newswires:** Not a dedicated product; PR content appears only insofar as it is republished by indexed outlets.
- **Historical archive:** "Everything" endpoint searches up to ~5 years of history (bounded on lower tiers).
- **Sentiment/analytics:** None — no sentiment scoring.
- **Entity tagging:** None — no ticker/company entity resolution; keyword matching only.

## 3. Datasets
- Sources: 150,000+ claimed web sources/blogs (an ~80,000 "notable sources" subset is exposed via the Sources endpoint with name/description/category metadata).
- History depth: up to 5 years on the Everything endpoint; free tier is limited to a short recent window plus the 24h delay.
- Update latency: near-real-time on paid tiers; ~24h delayed on free.
- Metadata: title, description, content snippet (truncated), author, source, URL, publishedAt, image. No sentiment or entity fields, no full-body text.

## 4. APIs & technical integration
- **API type:** REST/JSON only (no streaming, no bulk/S3 delivery).
- **Auth:** API key (query param or `X-Api-Key` header).
- **Endpoints:** `/v2/everything` (full search), `/v2/top-headlines` (breaking, by country/category/source), `/v2/sources`.
- **Rate limits:** ~100 req/day free; per-plan monthly quotas on paid.
- **Delivery:** HTTP responses only — no managed feed, Snowflake/Databricks share, or file drops.
- **MCP server:** No official MCP server; community wrappers exist but are unofficial.
- **SDKs:** Official/community clients for Python, Node, etc.

## 5. Enabling technology
- Straightforward crawl-and-index pipeline with keyword/boolean query support, source/language/country/date filters and relevancy sort. No NLP enrichment, entity linking, dedup guarantees, or sentiment engine — deliberately a thin, general-purpose retrieval layer.

## 6. Customer / user feedback
- **Ratings:** Mixed. Trustpilot/SlashDot and comparison blogs give roughly 3.5–4/5; heavily reviewed because of its ubiquity in tutorials (claims 500,000+ developers).
- **Pros:** Extremely easy to start, clean REST design, good docs, wide source coverage, generous-feeling free tier for local prototyping.
- **Cons:** The localhost-only CORS + 24h delay + non-commercial free-tier restrictions frustrate developers who try to ship; $449 price cliff; no sentiment/entity enrichment; occasional source-coverage gaps.
- **User segments:** Hobbyist/prototype developers, media/news-aggregator apps, students — not quant or compliance desks.

## 7. Edge & positioning
- **Leads on:** simplicity and time-to-first-call; the default "just give me headlines" API.
- **Lags on:** finance enrichment (no sentiment/entities), production-viable free tier, and price-to-value once commercial (jumps straight to $449). Not vendor-neutral advantageous for financial modelling.
- **Best for:** quick prototypes and general-news retrieval where localhost/dev use suffices; a poor fit for institutional financial-news analytics versus Marketaux (finance-tagged) or GDELT (free at scale).

## 8. Provenance
- https://newsapi.org/pricing — official pricing tiers (accessed 2026-08-11)
- https://newsapi.org/docs/endpoints/everything — official Everything endpoint docs (accessed 2026-08-11)
- https://newsapi.org/docs/endpoints/sources — official sources endpoint (accessed 2026-08-11)
- https://thunderbit.com/blog/best-news-apis-compared — independent tiers/limits comparison (accessed 2026-08-11)
- https://apitube.io/blog/post/stop-paying-449-news-api — independent critique of $449 cliff (accessed 2026-08-11)
- https://newsmesh.co/best-news-apis — independent developer comparison (accessed 2026-08-11)
- https://slashdot.org/software/p/News-API/ — independent user reviews (accessed 2026-08-11)
