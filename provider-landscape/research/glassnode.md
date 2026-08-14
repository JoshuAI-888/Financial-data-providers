# Glassnode

## 1. Snapshot
- **Owner/parent:** Independent, privately held; founded 2018 (some sources say 2017) in Switzerland (Zug/Baar) by Rafael Schultze-Kraft, Jan Happel, and Yann Allemann. Acquired crypto tax/portfolio platform Accointing in October 2022; no parent/acquirer of Glassnode itself identified.
- **Coverage:** On-chain metrics support for 1,500+ assets (headline: 1,527); core depth concentrated in Bitcoin and Ethereum, with 200+ tracked on-chain metrics for BTC/ETH specifically plus derivatives and spot/ETF market data layered on top.
- **Free tier:** Yes — "Discover" (free) tier in Studio with basic on-chain and spot/ETF metrics; limited history and metric set versus paid tiers. API access is not included free — it requires a paid subscription.
- **Pricing model & ranges:** Tiered subscription: Discover (free) → Advanced ~$49/mo (essential metrics, 1-year derivatives history) → Professional ~$999/mo (billed yearly; API access add-on) → Institutional/Data Bespoke (custom, sales-negotiated). API is gated behind Professional tier or an add-on, not a standalone low-cost product.

## 2. Coverage
Narrower asset breadth than CoinGecko/CoinMarketCap (on-chain metrics for ~1,500 assets vs. tens of millions of tokens) but far deeper per-asset analytical coverage, especially for Bitcoin and Ethereum where it is considered a category leader. Adds spot/ETF market data and derivatives data (funding, open interest, 1-year history on Advanced) alongside pure on-chain metrics — a hybrid on-chain + market-structure dataset rather than a broad multi-chain token price aggregator.

## 3. Datasets
On-chain metrics: network activity (active addresses, transactions), supply distribution and holder cohort analysis (HODL waves, realized cap, entity-adjusted supply), exchange flows, miner/validator metrics, profitability indicators (MVRV, SOPR, NUPL), stablecoin supply metrics. Market layer: spot and ETF flow data, derivatives (funding rates, open interest, options). "Point-in-Time" data addressing on-chain metric mutability (re-orgs/re-labeling) is a named product feature. Historical depth is tier-gated (e.g., 1-year derivatives history on Advanced; longer on Professional).

## 4. APIs & technical integration
Single REST API surface (docs.glassnode.com/basic-api) with 900+ endpoints, auth via `api_key` query param or `X-Api-Key` header. Includes metadata endpoints (metric parameters, time ranges, descriptions) and bulk/batch query endpoints. Official Python client library on GitHub (glassnode/glassnode-api-python-client). For bulk/institutional delivery, complete historical datasets are also offered via Parquet/CSV export or direct Snowflake/BigQuery access — a data-warehouse-native delivery model uncommon among the peers reviewed here. No public evidence found of WebSocket/streaming support (appears REST/batch-oriented).

## 5. Enabling technology
Proprietary blockchain-data processing pipeline computing derived on-chain metrics (entity clustering, cohort/HODL-wave analysis) rather than pass-through of raw chain data — this computation layer is the core IP. Cloud-warehouse-native distribution (Snowflake/BigQuery) suggests infrastructure built for institutional data-pipeline integration rather than purely a REST-for-apps model. No public architecture/methodology whitepaper located in this pass beyond the "Point-in-Time" data-mutability writeup.

## 6. Customer / user feedback
Strong reputation for accuracy, metric depth, and professional-grade charting/workbench tools; G2 rating cited around 4.5/5, with reviewers calling its dashboards "the best in the market." Positioned for retail traders, institutional investors, and blockchain researchers alike, with bespoke institutional analytics offered directly. Documented criticisms: the $49/mo Advanced tier's chart history is capped at a relatively short lookback (~1 month for some metrics), and a minority of reviews describe diminishing value after extended use. No major data-accuracy controversy surfaced in this pass.

## 7. Edge & positioning
- **Leads on:** Depth and rigor of on-chain analytics (holder cohorts, realized-cap/SOPR-style metrics, point-in-time data integrity); institutional-grade data-warehouse delivery (Snowflake/BigQuery, Parquet/CSV).
- **Lags on:** Asset breadth (no meaningful long-tail altcoin/DEX-token coverage vs. CoinGecko/CoinMarketCap); no qualitative research layer (vs. Messari); API is a paid-only add-on, no free API access.
- **Best-for:** Deep Bitcoin/Ethereum on-chain behavioral analysis for institutional research, quant, and risk teams that need warehouse-native delivery, not broad multi-asset price coverage.

## 8. Provenance
- https://docs.glassnode.com/basic-api/api — official API setup and auth documentation (accessed 2026-08-14)
- https://docs.glassnode.com/data/supported-assets/onchain-metrics-coverage — asset coverage count (accessed 2026-08-14)
- https://glassnode.com/products/data — data delivery via Parquet/CSV/Snowflake/BigQuery (accessed 2026-08-14)
- https://insights.glassnode.com/pricing — pricing tier structure (accessed 2026-08-14)
- https://sg.finance.yahoo.com/news/leading-crypto-market-intelligence-provider-143000087.html — Accointing acquisition (accessed 2026-08-14)
- https://comparedge.com/tools/glassnode — pricing and review summary (accessed 2026-08-14)
- https://github.com/glassnode/glassnode-api-python-client — official Python client (accessed 2026-08-14)
