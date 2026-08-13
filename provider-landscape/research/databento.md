# Databento

## 1. Snapshot
- **Owner/parent:** Databento, Inc. (independent, venture-backed). HQ Boston, Massachusetts, USA. Founded February 2019 by Christina Qi (CEO, ex-Domeyard LP HFT fund) and technologist co-founders.
- Positioning one-liner: a licensed, direct-from-venue market-data provider with pay-as-you-go, self-service access to real-time and full-depth historical data — "market data APIs for every firm."
- **Regions/markets covered:** Primarily US venues (NASDAQ, NYSE, CME, OPRA, IEX, MEMX, etc.) — 50-60+ trading venues as a licensed distributor and direct connectee. Expanding into European venues (e.g. Eurex, ICE Europe) but the core strength is US equities, futures and options; not an emerging-markets/APAC-exchange provider.
- **Free tier:** No true free tier, but new users get $125 in free credits (usage-based, effectively a free trial for meaningful data pulls). No perpetual free plan.
- **Pricing model & known ranges:** Two models — (1) usage-based pay-as-you-go (pay only for data queried, priced per GB/schema/venue); (2) flat-rate subscriptions. Published Standard plan ~$199/mo (unlimited access to 7yr OHLCV history, 12 months of L0/L1 across 12 schemas, 1 month of L2/L3). Higher unlimited/enterprise tiers negotiated. Real-time live-feed licensing and exchange fees are additional per venue.

## 2. Data-domain coverage
- **public equity:** yes — US equities, full-depth order book.
- **fixed income:** partial — via futures/treasury futures venues (CME); not a cash-bond OMS.
- **options:** yes — OPRA options feed, full coverage.
- **futures:** yes — CME Globex and others (a core strength).
- **forex / crypto:** limited/emerging; not the core.
- **macro / news / fundamentals / alt-data:** no — pure market microstructure/price data.

## 3. Datasets
- Full range of schemas from top-of-book to full order book: OHLCV (multiple intervals), Trades (tick), TBBO, MBP-1 (L1), MBP-10 (L2), MBO (L3 full order book), Imbalance, Statistics, Definitions.
- History depth: 5+ years widely (7 years OHLCV on Standard); some venues deeper. 2+ petabytes of raw and normalized data.
- Coverage: 50-60+ venues, licensed direct feeds — nanosecond-precision, PTP-synchronized timestamps, no survivorship gaps.
- Real-time vs delayed vs EOD: both live (co-located, low-latency) and historical (data older than 24h via historical API; last-24h via intraday). Proprietary holdings: none exclusive — value is in normalization, completeness and delivery, not exclusive datasets.

## 4. APIs & technical integration
- API type: REST/HTTP historical API, low-latency raw TCP/WebSocket-style live streaming, and batch flat-file download. Official SDKs for Python, C++, Rust, plus others.
- Auth: API keys.
- Formats: proprietary **DBN (Databento Binary Encoding)** by default — compact, self-describing binary; also CSV and JSON output. DBN is used both on the wire and in-memory across all client libraries.
- Rate limits/latency: engineered for HFT — co-located feeds, single-digit microsecond internal processing; historical batch jobs for bulk. Latency-optimized; Zstd compression optional.
- Delivery: API, batch flat files (S3-style download), and streaming. Known for developer-grade tooling; no widely advertised native Snowflake/Databricks share (bulk files feed those pipelines). No official Claude/OpenAI MCP server as of 2026.

## 5. Enabling technology
- Architecture: built to capture and normalize direct exchange feeds into a single unified schema (DBN) so one integration spans all venues — a major reduction in the operational complexity of multi-venue market data.
- Data-sourcing: licensed distributor with direct exchange connectivity and co-location; PTP hardware timestamping for accuracy.
- AI/reliability: emphasis on completeness, deterministic replay, and lossless capture. Recognized as a WEF Technology Pioneer (2022) for lowering the cost/complexity of exchange data access.

## 6. Customer / user feedback
- Reviewed positively in third-party writeups (e.g. QuantVPS review) and quant communities as high-quality, accurate, and refreshingly transparent on pricing versus legacy vendors (Bloomberg, Refinitiv, ICE).
- Triangulated sentiment: pros = data quality/completeness, granular self-service pricing, excellent docs/SDKs, fast onboarding, no huge minimum contracts. Cons = costs escalate quickly at scale (exchange/live-feed license fees add up), DBN binary format has a learning curve, US-centric coverage, and it targets sophisticated users rather than casual retail.
- Who uses it: quant hedge funds, prop trading firms, algo developers, fintech startups and researchers needing institutional-grade tick/order-book data without an enterprise sales cycle.

## 7. Edge & positioning
- **Leads on:** data fidelity and access model — full order-book history and live feeds with usage-based pricing and modern APIs; disrupts the opaque enterprise market-data procurement model.
- **Lags on:** breadth beyond US market microstructure — no macro, fundamentals, news, or deep global/APAC exchange coverage; not a free resource and not for non-technical users.
- **Best-for:** quant/algo teams and researchers needing accurate US equities/futures/options tick and order-book data with pay-as-you-go economics. Not a free pick.

## 8. Provenance
- https://databento.com/ — official homepage/positioning (accessed 2026-08-11)
- https://databento.com/pricing — official pricing (Standard $199, credits) (accessed 2026-08-11)
- https://databento.com/historical — historical data schemas/depth (accessed 2026-08-11)
- https://databento.com/live — real-time low-latency feed (accessed 2026-08-11)
- https://github.com/databento/dbn — DBN binary encoding (open source) (accessed 2026-08-11)
- https://databento.com/blog/normalized-vs-raw-market-data — normalization design tradeoffs (accessed 2026-08-11)
- https://www.quantvps.com/blog/databento-review — independent review (accessed 2026-08-11)
- https://widgets.weforum.org/techpioneers-2022/databento/index.html — WEF Tech Pioneer profile (accessed 2026-08-11)
