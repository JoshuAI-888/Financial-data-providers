# RavenPack / Bigdata.com

## 1. Snapshot
- **Owner/parent:** RavenPack (independent; founded 2003 in Marbella, Spain), with investment from the Financial Times (FT Group). Bigdata.com is RavenPack's newer AI-native platform/product line (launched beta July 2024, publicly unveiled October 2024) layered on the same underlying news-analytics engine.
- **Coverage:** 12M+ named entities (companies public/private, executives, insiders/influencers, locations, products) across 40,000+ web and social/news sources in 13 languages, including premium licensed sources (Dow Jones, Wall Street Journal, Barron's, MT Newswires, Benzinga) plus regional/local press and blogs; 20+ year historical archive; 7,000+ event categories tagged per entity.
- **Free tier:** No published self-serve free tier for the core News Analytics/Edge product (enterprise quote-based). Bigdata.com introduces a **pay-per-query REST API and Python SDK** — a shift toward transparent, metered self-serve access — but RavenPack has not published standard rate-card pricing publicly.
- **Pricing model & ranges:** Historically enterprise/institutional licensing (quote-only, typically five- to six-figure annual contracts based on usage/seats). Bigdata.com adds token/query-metered pricing (2026 "tokenization of content" model charges per token of retrieved content rather than per full document, cutting effective per-query cost) — but concrete published rate cards were not found; pricing remains largely negotiated.

## 2. Coverage
One of the deepest news-analytics coverage sets among sentiment vendors: 12M+ entities (companies, executives, insiders, geographies, products/services) mapped across 7,000+ event categories, spanning 40,000+ sources in 13 languages with a 20+ year archive. Includes gated/paywalled premium content via direct licensing partnerships (Dow Jones, Benzinga, MT Newswires) alongside broad web/social aggregation. Bigdata.com additionally surfaces earnings reports, regulatory filings, pricing/fundamentals data, and analyst estimates — positioning it as a broader financial-research grounding layer, not just a news-sentiment feed.

## 3. Datasets
- **News Analytics (core RavenPack product):** structured, entity-linked sentiment and event data with 80+ fields per detection, including 20+ distinct sentiment indicators derived from both large rule-based systems and machine-learning models.
- **Factor Library (Edge platform):** pre-built, backtested quantitative factors derived from unstructured text (news/filings/transcripts) for direct use in systematic strategies.
- **Bigdata.com:** conversational/AI-agent access to the same underlying corpus — real-time research assistant, custom research-tool builder, and API/SDK for querying billions of financial documents, plus market pricing, fundamentals, P/E ratios, employment statistics, and sentiment scores in one interface.
- Update latency: near real-time processing of incoming news flow; historical archive extends 20+ years for backtesting.

## 4. APIs & technical integration
- **API type:** REST API (Bigdata.com) plus enterprise feed/API access for core News Analytics (Edge platform); Python SDK provided for Bigdata.com.
- **Auth:** API key/credential-based; enterprise contracts for the core feed, self-serve key issuance reported for Bigdata.com's metered API.
- **Formats:** Structured JSON with entity/event/sentiment tagging; also distributed via data-vendor platforms (e.g., WRDS/Wharton Research Data Services for academic access).
- **Delivery:** Real-time feed, bulk historical extracts, and now a conversational/agentic query interface (Bigdata.com) — broader delivery surface than most sentiment vendors.
- **MCP availability:** No official MCP server identified as of research date; Bigdata.com's "research assistant" functions as a chat-style interface rather than a documented MCP integration.

## 5. Enabling technology
Long-running (20+ year) proprietary NLP stack combining large-scale rule-based sentiment classifiers with modern machine-learning models for entity/event/sentiment extraction at massive scale (terabytes of news, filings, and transcripts processed). Recent (2024-2026) investment adds a generative-AI layer: a conversational research assistant and a "content tokenization" retrieval system designed to feed LLMs precise, licensed excerpts (reported ~100x reduction in tokens needed per query vs. sending full documents) — positioning RavenPack/Bigdata.com as an AI-grounding data layer for finance, not just a sentiment-score API.

## 6. Customer / user feedback
Strong, well-documented institutional adoption: RavenPack states more than 70% of top-performing quantitative hedge funds and asset managers, and over 80% of the world's top 100 hedge funds, use its News Analytics for alpha generation and risk management; a Wolfe Research quant strategist is quoted calling it "a vital source of information for quantitative investors." Over 40 institutions (including four global investment banks, a top-five credit hedge fund, and 10 of the largest asset managers) reportedly adopted Bigdata.com during its beta. Countervailing feedback: some risk officers describe it as a "black-box" sentiment engine, with limited model explainability cited by roughly 28% of prospects as a decisive adoption concern and reportedly extending sales/adoption cycles by ~45 days versus vendors offering model audits.

## 7. Edge & positioning
- **Leads on:** breadth/depth of entity-event-sentiment coverage (12M entities, 7K event types, 20+ year archive), premium licensed-source access, and institutional trust — the dominant sentiment-analytics vendor by hedge-fund adoption share; increasingly leads on AI-grounding infrastructure via Bigdata.com's token-metered retrieval.
- **Lags on:** pricing transparency (still largely quote-only/enterprise), explainability/audit-ability of proprietary sentiment models (a stated objection among prospects), and self-serve accessibility versus lower-cost API-first entrants (Marketaux, Benzinga).
- **Best-for:** quantitative hedge funds and large asset managers building systematic sentiment/event-driven factors, and (via Bigdata.com) AI/LLM vendors needing licensed, precisely-grounded financial content — not a fit for budget-constrained or hobbyist use.

## 8. Provenance
- https://www.ravenpack.com/products/edge/data/news-analytics — official News Analytics product page (accessed 2026-08-14)
- https://www.ravenpack.com/blog/ravenpack-unveils-bigdata-ai-platform — official Bigdata.com launch announcement (accessed 2026-08-14)
- https://www.prnewswire.com/news-releases/ravenpack-unveils-bigdatacom-ai-platform-boosts-financial-research-efficiency-tenfold-302281963.html — press-wire coverage of Bigdata.com launch (accessed 2026-08-14)
- https://bigdata.com/resources/bigdata-com-launches-the-tokenization-of-content — official announcement of token-based pricing model (accessed 2026-08-14)
- https://medium.com/draper-esprit-notebook/our-investment-in-ravenpack-the-big-data-platform-used-by-70-of-the-worlds-leading-hedge-funds-a8c80893a63c — investor commentary on hedge-fund adoption (accessed 2026-08-14)
- https://wrds-www.wharton.upenn.edu/pages/about/data-vendors/ravenpack/ — academic data-vendor listing (Wharton WRDS) (accessed 2026-08-14)
- https://www.ravenpack.com/products/edge/factors — official Factor Library product page (accessed 2026-08-14)

**Note:** WebFetch to ravenpack.com and bigdata.com was egress-blocked in this environment; findings rely on the WebSearch index and cited secondary sources rather than direct page retrieval. Concrete self-serve rate-card pricing for Bigdata.com's pay-per-token API was not found and should be treated as a gap.
