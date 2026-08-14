# Diffbot

## 1. Snapshot
- **Owner/parent:** Independent, privately held. Founded 2009 in Palo Alto/Menlo Park, CA by **Mike Tung** (Stanford PhD); first company funded by StartX (Stanford's venture fund). No known acquisition — remains an independent AI/web-data company as of 2026.
- **Coverage:** Not sector-specific — a general-purpose **Knowledge Graph of the public web**: 10–20 billion entities (organizations, people, products, articles, locations) and 1–2+ trillion structured facts (sources vary: some cite "10B entities/1T facts," others "20B entities/2T facts"), built from a continuous crawl reportedly covering 1.2 billion+ websites, refreshed roughly every 4–5 days.
- **Free tier:** Yes — **10,000 credits/month** free (credits meter API calls; e.g., 1 credit per page extraction, 25 credits per Knowledge Graph entity export).
- **Pricing model & ranges:** Credit-based subscription tiers: **Free** (10K credits/mo) → **Startup $299/month** (250,000 credits) → **Plus $899/month** (1,000,000 credits) → **Enterprise** (custom pricing, managed SLAs, private cloud/on-prem options). No seat-based licensing — usage (API calls) is the pricing unit.

## 2. Coverage
Global, multilingual web coverage (not US-listed-only, and not a market-data or financials-specific provider) — this is the key structural difference from FMP-style providers: Diffbot indexes **all public web content**, not a curated list of listed companies. For financial/company research use cases specifically, coverage strength is in organization/people entity profiles (firmographic data: employee counts, funding, executives, locations, social/news mentions) rather than financial statement line items. Coverage gaps reported in long-tail/regional markets and niche verticals where public web presence is thin.

## 3. Datasets
- **Knowledge Graph**: structured entity database (organizations, people, products, articles, locations) with resolved relationships and facts, queryable via a Diffbot Query Language (DQL).
- **Extract API**: page-type-specific structured extraction (Article, Product, Discussion, Event, Image, Video) from any URL — computer-vision + NLP page parsing with no per-site rules/config needed.
- **Natural Language API**: entity/relationship/fact/sentiment extraction from raw text, each entity resolved against the Knowledge Graph.
- **Enhance API**: given a partial identifier (name, domain, LinkedIn URL) for a person or org, returns the full known profile — usable live (single lookup) or in bulk (CSV enrichment) for firmographic/entity resolution and record enrichment.
- **Crawlbot**: configurable site-wide crawler that feeds URLs into the Extract APIs at scale.

## 4. APIs & technical integration
Pure API-first product (no significant human-workflow UI beyond a dashboard for testing/bulk enhance jobs): REST-style HTTP APIs, JSON responses, API-key authentication, one endpoint family per product (Extract, Knowledge Graph search/DQL, Enhance, Natural Language, Crawlbot management). Google Sheets add-on exists for no-code Enhance lookups. Well-suited to being wired into an automated pipeline (comparable in integration model to FMP's `client.py` REST pattern) — costs scale by credit consumption per call rather than per-seat.

## 5. Enabling technology
Combines **computer vision** (to visually parse a rendered web page the way a human would, avoiding brittle per-site scraping rules) with **NLP/ML entity and relationship extraction**, feeding a continuously-updated Knowledge Graph. Diffbot markets this as fully automated ("no rules, no per-site configuration") in contrast to rule-based scrapers, and has published an in-house NLP system launched 2020 ("Knowledge as a Service" NLP) plus ongoing large-language/knowledge-graph-grounded model work (per VentureBeat coverage of Diffbot's "trillion-fact" grounded AI model, positioned as reducing hallucination by grounding LLM outputs in verified KG facts).
Note: this stack is a plausible complementary "enrichment layer" for the Milford project's existing US-comparables universe (e.g., firmographic/executive enrichment) — not a substitute for FMP's financial-statement data.

## 6. Customer / user feedback
Cited enterprise customers/case studies include **Avast** (built a universal website privacy score using Diffbot data) and **ProQuo AI** (uses Diffbot's 200M+ organization records for predictive business development), plus "Contingent AI" (entity resolution for supply-chain risk news coverage). Reviews on Capterra/Slashdot/FinancesOnline generally frame Diffbot as strong for developers needing reliable structured extraction at scale, with the main friction points being credit-cost predictability at high volume and a learning curve for the Knowledge Graph query language (DQL). No major coverage of complaints beyond typical scraping/data-freshness edge cases inherent to any web-crawl-based product.

## 7. Edge & positioning
- **Leads on:** breadth/scale of general web entity coverage (10B+ entities), no-rules automated extraction that survives site redesigns, credit-based usage pricing well suited to programmatic/pipeline consumption, strong firmographic/company-profile enrichment.
- **Lags on:** no native financial-statement/fundamentals data (not a market-data provider), no curated "investable universe" concept, data freshness is crawl-cycle-bound (~4-5 days) rather than real-time market data, higher-volume usage can get expensive fast at credit-metered pricing.
- **Best-for:** enrichment/entity-resolution use cases (mapping company names/domains to canonical firmographic profiles, competitive/market intelligence, news/sentiment aggregation) layered on top of — not instead of — a dedicated financial-data provider like FMP.

## 8. Provenance
- https://www.diffbot.com/pricing — pricing tiers/credit costs (accessed 2026-08-14, fetch blocked, via search snippet)
- https://www.diffbot.com/products/knowledge-graph/ — Knowledge Graph entity/fact scale claims (accessed 2026-08-14)
- https://www.diffbot.com/docs/extract/ — Extract API description (accessed 2026-08-14)
- https://docs.diffbot.com/reference/introduction-to-enhance-api — Enhance API mechanics (accessed 2026-08-14)
- https://venturebeat.com/ai/diffbots-ai-model-doesnt-guess-it-knows-thanks-to-a-trillion-fact-knowledge-graph — trillion-fact KG grounded-AI coverage (accessed 2026-08-14)
- https://www.diffbot.com/customer-stories/ — Avast/ProQuo AI/Contingent AI case studies (accessed 2026-08-14)
- https://www.diffbot.com/company/news/20200916.html — 2020 NLP "Knowledge as a Service" launch (accessed 2026-08-14)
- https://data-ox.com/resources/blog/diffbot-review/ — independent 2026 pricing/feature review (accessed 2026-08-14)

Note: WebFetch to diffbot.com and docs.diffbot.com was egress-blocked in this environment; facts above are triangulated from WebSearch result snippets across ≥2 independent sources, not direct page fetches.
