# Nasdaq Data Link

## 1. Snapshot
- **Owner/parent:** Nasdaq, Inc. (NASDAQ: NDAQ) — acquired Quandl, Inc. (Toronto) on Dec 4, 2018; platform folded into Nasdaq's Global Information Services / Analytics Hub and rebranded from "Quandl" to "Nasdaq Data Link" in September 2021.
- **Coverage:** 250+ curated premium databases plus a long tail of free datasets indexed from 400+ publishers/sources; financial markets, economic, and alternative data (equity fundamentals, futures/commodities, macro indicators, alt-data feeds such as web-scraped, satellite, and sentiment sets). US/global macro and financial time-series is the core strength; live exchange-traded pricing is limited relative to a Bloomberg/Refinitiv.
- **Free tier:** Yes — free registration unlocks many public/free datasets (daily-frequency data common) with a published rate limit of up to 50,000 API calls/day for authenticated free users; anonymous/unauthenticated calls are capped far lower (order of tens per 10 minutes).
- **Pricing model & ranges:** A la carte marketplace — each dataset/bundle is individually priced (some free, some subscription). Paid/premium plans raise the API rate limit to roughly 720,000 calls/day and add bulk-download rights. Flagship bundles like Sharadar Core US Fundamentals are sold as fixed-fee annual subscriptions (typically low-to-mid four figures USD/year for individuals, more for commercial/redistribution use); exact premium pricing requires a logged-in account or sales quote, so no single platform-wide price exists.

## 2. Coverage
US-centric but broad in breadth-of-source: 400+ publishers spanning central banks, exchanges, and independent data vendors (e.g., Sharadar, Zacks, EIA, IEX). Strong on US equity fundamentals (Sharadar SF1/SF2/SF3), insider/institutional holdings, and macro/economic time-series (much of it reused from FRED-like public sources). Alternative-data breadth is real but thinner than pure-play alt-data shops (Similarweb, YipitData) — it functions more as a distribution marketplace/aggregator for third-party alt-data producers than as a primary alt-data generator itself. International equities coverage is comparatively weak.

## 3. Datasets
Two structural formats: (1) **Time-series** datasets (single-metric series, e.g., commodity prices, FX, macro indicators) retrieved via `get()`; (2) **Tabular** datasets (large relational tables, e.g., full fundamentals panels) retrieved via `get_table()`/`export_table()` for bulk pulls. Notable premium bundles: Sharadar Core US Fundamentals/Insiders/Institutional data, Zacks earnings estimates, EOD equity prices, and various alt-data feeds (web traffic proxies, shipping, satellite imagery-derived series) contributed by third-party publishers. Free tier includes long-running public series (e.g., commodity benchmarks, some macro data) often at daily granularity.

## 4. APIs & technical integration
REST API is the core interface, split into a **time-series REST API**, a **tables REST API**, and a **streaming API** for select real-time feeds. Official SDKs: Python (`nasdaqdatalink` package, replacing the legacy `quandl` package), R (`NasdaqDataLink` on CRAN), plus documented usage from Excel add-ins and third-party integrations (e.g., QuantConnect, Deephaven). Authentication via a simple API key; standard REST/JSON responses with CSV export options for tabular data.

## 5. Enabling technology
Functions primarily as a data marketplace and delivery/standardization layer rather than a data-collection technology in itself — Nasdaq normalizes disparate third-party feeds (from data vendors like Sharadar, Zacks, EIA, etc.) into a single API/schema, handles caching, rate-limiting, and bulk export tooling, and layers this on Nasdaq's existing Analytics Hub infrastructure. Underlying alt-data collection methods (web scraping, satellite, sentiment) are the responsibility of the individual publishers on the marketplace, not a proprietary Nasdaq pipeline.

## 6. Customer / user feedback
Historic strength under the Quandl brand: used by 8 of the top 10 hedge funds and 14 of the top 15 largest banks at time of Nasdaq's 2018 acquisition, with 30,000+ active monthly users then and 650,000+ registered financial professionals cited at the 2021 rebrand. Independent review sites (G2) show a largely unclaimed/sparse public review profile for the rebranded product, reflecting its use as backend infrastructure by quants/developers rather than an end-user analytics tool with a large public review footprint. Commentary from trading-tool review sites (e.g., TradingToolsHub) generally frames it as strongest for macro/research time-series rather than as a comprehensive alt-data or real-time trading feed.

## 7. Edge & positioning
- **Leads on:** Breadth of *aggregated* free + paid financial/macro time-series in one standardized API; generous free-tier call volume (50k/day) versus most paid financial APIs; long institutional pedigree (ex-Quandl) among quant/hedge-fund users; strong Python/R tooling for research workflows.
- **Lags on:** Not a primary alt-data generator — depends on third-party publishers for alt-data depth and freshness; international/non-US equities coverage; real-time/intraday market data versus dedicated market-data vendors; per-dataset pricing opacity makes total cost-of-ownership hard to estimate up front.
- **Best-for:** Quant researchers and hedge funds needing a single standardized API/SDK to pull US equity fundamentals, macro series, and a marketplace of third-party alt-data feeds without negotiating dozens of individual vendor contracts.

## 8. Provenance
- https://ir.nasdaq.com/news-releases/news-release-details/nasdaq-acquires-quandl-advance-use-alternative-data — Nasdaq's 2018 Quandl acquisition announcement (accessed 2026-08-14)
- https://data.nasdaq.com/publishers/QDL — Nasdaq Data Link publisher/dataset marketplace page (accessed 2026-08-14)
- https://docs.data.nasdaq.com — official API docs (REST/time-series/tables), egress-blocked in this environment, relied on search-index summary (accessed 2026-08-14)
- https://help.data.nasdaq.com/article/568-how-much-does-nasdaq-data-link-data-cost-how-do-i-find-pricing — pricing lookup process and free/premium split (accessed 2026-08-14)
- https://github.com/nasdaq/data-link-r — official R SDK repository (accessed 2026-08-14)
- https://data.nasdaq.com/bundles/sharadar-core-us-data/pricing — Sharadar Core US Fundamentals bundle pricing page (accessed 2026-08-14)
- https://www.quantconnect.com/docs/v2/writing-algorithms/datasets/nasdaq/data-link — third-party integration doc corroborating API structure and rate limits (accessed 2026-08-14)
- https://tradingtoolshub.com/review/quandl/ — independent 2026 review noting rebrand history and use-case positioning (accessed 2026-08-14)
