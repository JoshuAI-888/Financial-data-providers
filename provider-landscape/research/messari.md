# Messari

## 1. Snapshot
- **Owner/parent:** Acquired by Blockworks in June 2026 for reportedly just over $10M — a steep discount to Messari's 2022 Series B valuation of ~$300M. Founded 2018 by Ryan Selkis (departed as CEO in 2024, preceding staff reductions and the eventual sale).
- **Coverage:** 40,000+ digital assets tracked for market/asset data; on-chain metrics across 50+ networks/protocols; research reports plus news aggregation from 500+ sources.
- **Free tier:** Yes — free API tier with 20 requests/minute and basic asset metrics/qualitative profiles; no bulk data or full research access.
- **Pricing model & ranges:** Tiered: Free → Pro ~$29/mo (full Pro research reports, on-chain metrics across 50+ networks, token unlocks, fundraising data, advanced screener, API access) → Enterprise (custom, sales-negotiated; adds full Token Unlocks API, intel-feed redistribution rights, Messari Copilot, per-seat licensing with bulk-seat discounts).

## 2. Coverage
Broad asset coverage (40,000+) comparable in scale to CoinGecko/CoinMarketCap for basic market data, but Messari's differentiator is layering qualitative/fundamental research and on-chain protocol metrics (50+ networks) on top — not pure price/volume aggregation. Coverage strength is concentrated in fundamentals: tokenomics, governance activity, protocol revenue, and fundraising/cap-table data, areas the pure market-data providers (CoinGecko, CoinMarketCap) do not cover at all.

## 3. Datasets
Asset & Market Data API: real-time/historical prices, market metrics, supply, ROI, ATH tracking, asset timeseries metrics. Qualitative/fundamental layer: asset profiles, protocol design writeups, tokenomics, governance activity. On-chain metrics for 200+ DeFi protocols. Token unlock schedules (vesting cliffs), fundraising/cap-table data (VC rounds, valuations), and curated news aggregation from 500+ sources. Enterprise-only: full Token Unlocks API and redistribution-licensed intel feed.

## 4. APIs & technical integration
REST API documented at docs.messari.io; core endpoints include List Assets, Get Asset Details, Get ROIs, Get ATHs, List Metrics, and Get Asset Timeseries Metric. Auth via `x-messari-api-key` header. Official Python client (messari/messari-python-api on GitHub); community clients also exist for PHP. Free tier capped at 20 req/min. Bulk data access (large historical/cross-asset pulls) is reserved for Pro and Enterprise plans rather than exposed via the free/basic REST tier.

## 5. Enabling technology
Combines automated on-chain/market data pipelines with a human research-analyst layer producing the qualitative reports — a hybrid data+editorial production model distinct from the purely automated pipelines of CoinGecko/CoinMarketCap/CryptoCompare. Post-acquisition, Messari's data/research stack is being folded into Blockworks' broader crypto-media and data infrastructure as part of an explicit market-consolidation strategy (Blockworks has stated intent to acquire competitors). No independent architecture disclosure found in this pass.

## 6. Customer / user feedback
Regarded as the premier platform for serious crypto fundamental research; reviewers cite protocol revenue data, token unlock schedules, governance tracking, and analyst reports as differentiators "free sources don't match," at roughly 4.4/5 in review aggregates. Primary criticism is cost/fit: seen as "too expensive and too focused on fundamentals" for retail technical traders, and not a substitute for a pure on-chain-flow tool (Glassnode) or a social-narrative tool. The 2024 CEO departure, subsequent layoffs, and 2026 fire-sale acquisition (down from a $300M valuation) are notable reputational/financial-stability signals for prospective enterprise buyers.

## 7. Edge & positioning
- **Leads on:** Fundamental/qualitative research depth (tokenomics, governance, protocol revenue), token-unlock and fundraising datasets unique among the five providers reviewed.
- **Lags on:** Recent corporate instability (CEO exit, layoffs, sub-scale acquisition price) raises platform-continuity risk; on-chain metric depth narrower than Glassnode; free-tier rate limit (20 req/min) is the most restrictive of the five.
- **Best-for:** Institutional/professional research teams needing qualitative fundamentals, tokenomics, and fundraising data layered onto market data — not high-throughput price feeds.

## 8. Provenance
- https://thedefiant.io/news/infrastructure/blockworks-acquires-messari-crypto-data-consolidation — acquisition terms and valuation context (accessed 2026-08-14)
- https://messari.io/pricing — official pricing tiers (accessed 2026-08-14)
- https://docs.messari.io/api-reference/endpoints/metrics/metrics-api — API endpoint documentation (accessed 2026-08-14)
- https://github.com/messari/messari-python-api — official Python client (accessed 2026-08-14)
- https://cryptoadventure.com/messari-review-2026-research-ai-tools-fundraising-data-and-api-access/ — coverage and product review (accessed 2026-08-14)
- https://coinmarketcap.com/academy/article/alternatives-to-messari-crypto-api-in-2026 — competitive positioning and free-tier limits (accessed 2026-08-14)
