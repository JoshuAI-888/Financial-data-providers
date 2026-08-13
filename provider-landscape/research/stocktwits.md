# StockTwits

## 1. Snapshot
- **Owner/parent:** StockTwits, Inc. (independent, VC-backed; leading shareholders include Foundry Group, True Ventures, Social Leverage, Times Bridge). **HQ:** New York, NY (1001 Avenue of the Americas). **Founded:** 2008 by Howard Lindzon (returned as CEO March 2024). Positioning: the original social network / real-time messaging community for retail investors and traders, organized around cashtags ($TICKER).
- **Access/region notes.** Global retail community; message stream is US-equity/crypto centric but users worldwide. Public JSON stream endpoints have historically been reachable without a key, but the developer program is in flux (see below). US-focused sentiment product.
- **Free tier:** partial/uncertain. Legacy public stream endpoints (e.g. `api.stocktwits.com/api/2/streams/symbol/{SYMBOL}.json`) return recent messages (~30 per call) without auth, but StockTwits states it is **reviewing all APIs, docs and terms and is not accepting new developer registrations** until that review completes. Treat free programmatic access as unstable/deprecating, not a reliable free tier.
- **Pricing model & known ranges — not publicly disclosed.** No public self-serve API price list. Commercial/enterprise data (bulk message + sentiment feeds) is sold via direct enterprise deals and third-party marketplaces (e.g. Databricks Marketplace "Stocktwits Messages API"); a separate Sentiment API (v2) exists behind gateway auth. Contact developers@stocktwits.com.

## 2. Data-domain coverage
- **Social posts:** yes — core asset; user-generated messages tagged with cashtags, the largest dedicated finance-social message corpus.
- **Sentiment scores:** yes — author-tagged Bullish/Bearish labels aggregated per symbol; a Sentiment v2 API exposes symbol-level bullish/bearish percentages and message volume.
- **Retail-trader signals:** yes — trending/most-active symbols, message volume spikes, watchlist counts as crowd-attention proxies.
- **Political/insider trades:** no.
- **Options flow:** no.
- **Crypto social:** yes — crypto cashtags and crypto community are first-class alongside equities.

## 3. Datasets
- Captures individual messages (body, author, timestamp, cashtags, self-reported Bull/Bear sentiment, likes/replies), symbol streams, trending symbols, and derived per-symbol sentiment aggregates. History depth on the public stream is shallow (recent messages only, ~30/call, paginated by cursor); deep historical corpora are sold as bulk feeds.
- Coverage breadth: primarily US-listed equities, ETFs and major crypto; the differentiator is community size and the **self-reported** sentiment tag rather than model-inferred sentiment.
- Proprietary signal: the aggregated Bullish/Bearish community sentiment percentage per ticker; message-volume-based attention metrics.
- Sourcing method: first-party — data is generated natively by StockTwits users on the platform (not scraped from elsewhere), which is its key provenance advantage.

## 4. APIs & technical integration
- **API type:** REST/JSON. Legacy v2 streams (`/api/2/streams/...`) plus a newer Sentiment v2 API and internal API-gateway/middleware endpoints (`api-gw-prd.stocktwits.com`). No official public streaming/websocket for third parties documented.
- **Auth:** legacy public read endpoints unauthenticated; authenticated/write and premium endpoints use OAuth 2.0 (historically) or HTTP Basic against the gateway for the sentiment detail endpoint.
- **Formats:** JSON. **Rate limits:** historically per-app hourly quotas; site is heavily rate-limited and clients are expected to back off/retry. Exact numbers not publicly documented under the current review.
- **ToS/redistribution:** restrictive — redistribution and bulk storage require a commercial agreement; the public API is for app integration, not resale. Terms explicitly under revision.
- **MCP availability:** none official.

## 5. Enabling technology
- Sentiment is primarily **human-labeled** (users tag their own posts Bull/Bear), reducing NLP error but introducing self-selection bias. Entity→ticker mapping is explicit via cashtags rather than inferred. Newer Sentiment v2 product layers aggregation/normalization and likely some ML classification on untagged messages. Data-ops centered on real-time message ingestion and de-duplication within the platform.

## 6. Customer / user feedback
- Triangulated across QuantVPS/reviewer commentary, developer forums (GitHub wrappers, API Tracker), and academic sentiment literature. **Pros:** unique first-party retail crowd data; explicit cashtag→ticker linkage; free/low-friction historical use in research; large sample on liquid US names. **Cons:** developer program instability and paused registrations frustrate builders; self-reported sentiment is noisy and gameable/pumpable; thin data on small caps and non-US names; documentation fragmented and partly stale. User segments: quant researchers and academics (sentiment factors), retail traders (community/discussion), and a smaller set of enterprise data buyers.

## 7. Edge & positioning
- **Leads** as the canonical, first-party finance-social community and the reference dataset for retail-sentiment research (widely used in academic papers). **Lags** on API stability, documentation, non-US/small-cap coverage, and modeled-sentiment sophistication versus dedicated NLP vendors (e.g. SMA/Context Analytics, which itself consumes StockTwits). **Best-for:** US retail attention/sentiment signals and community discussion. **Free pick:** partially — usable for research today via public streams, but not a dependable production free tier given the ongoing API review.

## 8. Provenance
- https://api.stocktwits.com/developers — official developer landing/status (accessed 2026-08-11)
- https://sentiment-v2-api.stocktwits.com/ — official Sentiment v2 API (Swagger) (accessed 2026-08-11)
- https://firestream-portal.stocktwits.com/documentation/sentiment-detail — official sentiment detail endpoint docs (accessed 2026-08-11)
- https://apitracker.io/a/stocktwits — third-party API/SDK/auth overview (accessed 2026-08-11)
- https://marketplace.databricks.com/details/1b5033c7-1709-4367-9a9b-3f33a54facb4/Stocktwits_Stocktwits-Messages-API — enterprise data marketplace listing (accessed 2026-08-11)
- https://github.com/janlukasschroeder/stocktwits-api — independent API wrapper/endpoint reference (accessed 2026-08-11)
- https://pitchbook.com/profiles/company/51165-19 — company ownership/funding profile (accessed 2026-08-11)
- https://mergr.com/company/stocktwits — ownership and M&A history (accessed 2026-08-11)
