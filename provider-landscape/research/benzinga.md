# Benzinga (News / API)

## 1. Snapshot
- **Owner/parent, HQ, founded, positioning:** Benzinga is a privately held financial media and market-data company founded in 2010, headquartered in Detroit, Michigan (Financeit/Beringer Capital acquired a majority stake in 2021). Positioning: fast, in-house-written, machine-readable stock-market news and calendar/signals data for traders, brokers and fintechs — "actionable, market-moving" content built for low latency.
- **Regions/language coverage:** US-centric. Focus is US-listed equities, US markets and English-language content; global macro headlines appear but the franchise is US equities. Not a multi-language global news aggregator.
- **Free tier:** Partial. The **Basic Financial News API tier is fee-free** and returns headline, body teaser and a hyperlink to the full story on Benzinga.com; full embeddable body content and real-time breaking content require paid premium tiers. There is no true self-serve unlimited free plan — access is arranged via sales/partners.
- **Pricing model & known ranges:** Subscription/licensing, tiered by data volume, latency and content depth (Basic free-tier → premium content tiers → custom enterprise). Exact API list prices are **not publicly disclosed** (quote-based via sales; also resold through Massive/AWS Marketplace). The consumer Benzinga Pro terminal is separately priced (roughly ~US$27–197/mo tiers) but is a product, not the API.

## 2. Data-domain coverage
- **Financial news:** Core strength — in-house-written breaking stock news, "Why Is It Moving" (WIIM), M&A, guidance, offerings.
- **General news:** Limited — market/business focused, not a general world-news wire.
- **Press releases/newswires:** Yes — Benzinga operates its own newswire/newsdesk; ingests and rewrites market-moving PR.
- **Historical archive:** Yes for structured feeds (e.g. analyst ratings history back to 2012); news retrievable via delta/updatedSince parameters.
- **Sentiment/analytics:** Limited native sentiment; strengths are structured signals, analyst ratings, price targets, calendars.
- **Entity tagging:** Yes — content tagged to tickers, making it feed-ready for per-security ingestion.

## 3. Datasets
- **Sources indexed:** Primarily Benzinga's own newsroom output plus ingested newswire/PR; not a mass-aggregator of thousands of outlets — value is proprietary, ticker-tagged content.
- **# outlets:** In-house desk (dozens of writers); complemented by aggregated wire content.
- **History depth:** Analyst Ratings history to 2012; news accessible historically via delta queries; multi-year calendars (earnings, dividends, splits, IPOs, economics).
- **Update latency:** Real-time — news "not delayed", delivered by API pull or TCP/WebSocket push; Squawk audio livestream for breaking headlines.
- **Sentiment/entity metadata:** Ticker tagging, rating actions (upgrade/downgrade/initiate/maintain), price targets, signals/volume alerts.
- **Proprietary analytics:** WIIM, Analyst Insights, Signals, Squawk, government-trades and other calendars.

## 4. APIs & technical integration
- **API type:** REST (pull) plus TCP / WebSocket streaming (push) for low-latency news, calendars, signals and ratings.
- **Auth:** API token/key (token query parameter).
- **Formats:** JSON (and XML on some endpoints).
- **Rate limits:** Plan-dependent; incremental ingestion via `updatedSince` (News) and `parameters[updated]` (Calendar/Signals) deltas to minimise latency.
- **Delivery:** Cloud REST/WebSocket; also available through partners (Massive) and AWS Marketplace; enterprise direct feeds.
- **MCP availability:** No official Benzinga MCP server identified as of 2026-08-11.

## 5. Enabling technology
- Human-in-the-loop newsdesk writing market-moving stories, combined with structured data pipelines that ticker-tag and timestamp content for machine consumption. Delta/versioned endpoints and push (TCP/WebSocket) infrastructure engineered for trading-grade latency. Squawk uses live human audio. Less emphasis on large-scale NLP sentiment scoring than pure-analytics vendors.

## 6. Customer / user feedback
- **Trustpilot (Benzinga Pro):** ~4.2–4.5/5 across ~747 reviews (multiple secondary reports cite 4.4/5); ~36 review pages.
- **Pros:** Speed and depth of real-time feed, customisable filters, audio Squawk that "pays for itself" by surfacing market-moving news early; clean, easy-to-navigate UI; strong analyst-ratings/calendar data.
- **Cons:** Limited built-in charting, no trade execution, learning curve; mixed reports on billing transparency and support responsiveness (some praise support, others report difficulty reaching the pro help desk).
- **User segments:** Active/day traders, broker-dealers and fintech apps (embedded news), quant/algo desks consuming structured feeds.

## 7. Edge & positioning
- **Leads:** Low-latency, in-house, ticker-tagged US equity news; structured analyst-ratings and calendar data; Squawk audio; feed-ready integration for brokers/fintechs.
- **Lags:** Not global/multilingual; thin on general/world news; limited native sentiment analytics vs RavenPack/Bigdata; API pricing opaque.
- **Best-for:** US-equity trading apps, brokers and quant desks needing fast, machine-readable, per-ticker news and structured calendars. The free **Basic** news tier (headline + teaser + link) is a viable low-cost entry point for lightweight display use, but full content and real-time depth are paid.

## 8. Provenance
- https://www.benzinga.com/apis/ — official API product hub (accessed 2026-08-11)
- https://www.benzinga.com/apis/cloud-product/stock-news-api/ — official stock-news API/latency (accessed 2026-08-11)
- https://www.benzinga.com/apis/cloud-product/analyst-ratings-api/ — analyst-ratings history to 2012 (accessed 2026-08-11)
- https://docs.benzinga.com/home — official API documentation home (accessed 2026-08-11)
- https://www.benzinga.com/pro/feature/squawk — Squawk audio feature page (accessed 2026-08-11)
- https://www.trustpilot.com/review/pro.benzinga.com — independent user reviews/ratings (accessed 2026-08-11)
- https://massive.com/partners/benzinga — partner reseller/integration docs (accessed 2026-08-11)
- https://aws.amazon.com/marketplace/pp/prodview-xwgvhwowjmw3g — AWS Marketplace listing (accessed 2026-08-11)
