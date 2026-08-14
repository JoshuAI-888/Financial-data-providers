# CryptoCompare (CCData / CoinDesk Data)

## 1. Snapshot
- **Owner/parent:** Founded 2014 in London by Charles Hayter; expanded its institutional data/index arm as CCData (regulated entity CC Data Limited). Acquired by CoinDesk in October 2024; CoinDesk itself is owned by Bullish (crypto exchange), which acquired CoinDesk in November 2023. Rebranded institutionally as "CoinDesk Data" in February 2025, with CryptoCompare retained as the retail-facing brand/site (300,000+ active users).
- **Coverage:** 300+ centralized and decentralized exchanges, 10,000+ cryptocurrencies, 260,000+ currency pairs / 300,000+ trading pairs (figures vary slightly by source and date).
- **Free tier:** Formerly yes; CoinDesk/CCData retired the self-serve free API tier around May 2026. All current paid plans require a sales conversation — no public self-serve signup as of this research.
- **Pricing model & ranges:** Historically self-serve commercial plans ran ~$80/mo (basic) to ~$200+/mo (advanced) across three commercial tiers; as of 2026 the self-serve pricing page has been removed and all commercial engagement is sales-led/custom-quoted.

## 2. Coverage
Mid-to-large coverage by exchange count (300+) and asset count (10,000+) — smaller than CoinGecko/CoinMarketCap's headline asset totals but with a specific emphasis on institutional-grade, benchmark-quality pricing rather than maximal long-tail token breadth. Its proprietary CCCAGG aggregate pricing methodology (24-hour volume-weighted, time-penalty, outlier-adjusted) covers 500+ liquid asset pairs specifically engineered for benchmark/index use rather than raw coverage maximization.

## 3. Datasets
Real-time and historical trade data, order-book data, block-explorer (on-chain) data, social data, and cryptocurrency indices; taxonomy/classification reports. CCCAGG proprietary aggregate reference pricing across 500+ pairs. As a regulated benchmark administrator, also produces investment-product reference indices, reference rates, contract settlement pricing, and fund-performance-measurement benchmarks — a regulated-index dataset none of the other four providers in this batch offer.

## 4. APIs & technical integration
REST API historically documented publicly (min-api-v2.cryptocompare.com), with community wrappers referenced on Postman and in third-party guides (Medium starter guide, StockAPIs parser docs). Commercial tier historically offered customizable endpoints/call limits, dedicated support, and SLAs, plus the ability to cache/save data locally for internal business use — an institutional licensing structure rather than a pure pay-as-you-go API. Following the CoinDesk/CCData integration and free-tier retirement, current technical access is understood to be arranged through direct sales engagement rather than public self-serve documentation; this research pass could not confirm the current public API doc URL is still live/self-serve.
- **Note:** WebFetch was not attempted against live product/pricing pages for this provider in this pass; findings rely on search-index summaries and news coverage of the pricing-page removal, so current self-serve API mechanics should be re-verified directly with CCData/CoinDesk Data before quoting to stakeholders.

## 5. Enabling technology
Distinguishing technical asset is CCCAGG, its proprietary volume-weighted aggregate pricing algorithm with outlier detection and time-penalty weighting, purpose-built for benchmark/index integrity rather than simple last-trade pass-through. As a UK FCA-authorised Benchmark Administrator (via CC Data Limited, authorised November 2021), its infrastructure and governance meet regulatory standards for use in financial instruments, fund performance measurement, and contract settlement pricing — a compliance/audit layer none of the other four crypto providers here carry.

## 6. Customer / user feedback
Long operating history (since 2014) and FCA regulatory status lend it credibility for institutional/regulated use cases (indices, benchmarks, fund NAV inputs) that pure market-data APIs cannot serve. Retail site retains a large user base (300,000+ active users cited at acquisition). Limited independent developer-review commentary surfaced in this pass (fewer G2/Reddit threads than CoinGecko/CoinMarketCap/Glassnode/Messari) — plausibly reflecting its more institutional/sales-led go-to-market versus the self-serve developer communities of its peers. The 2024–2026 ownership changes (CoinDesk acquisition, Bullish parent, free-tier retirement) are a relevant continuity/roadmap signal for evaluators.

## 7. Edge & positioning
- **Leads on:** Only provider of the five with formal UK FCA Benchmark Administrator status — usable for regulated reference rates, fund performance benchmarks, and contract settlement pricing.
- **Lags on:** No public self-serve free tier as of 2026 (retired); smaller public developer-community footprint; recent ownership churn (three changes of control since 2023–2024) creates roadmap/continuity uncertainty.
- **Best-for:** Institutional/regulated use cases needing audited, benchmark-grade reference pricing and indices (fund NAV, contract settlement) rather than exploratory or app-embedded price lookups.

## 8. Provenance
- https://www.coindesk.com/business/2024/10/16/coindesk-buys-crypto-data-provider-ccdata-and-cryptocompare — CoinDesk acquisition of CCData/CryptoCompare (accessed 2026-08-14)
- https://data.coindesk.com/press-releases/digital-asset-data-provider-cryptocompare-receives-fca-authorisation — FCA Benchmark Administrator authorisation (accessed 2026-08-14)
- https://www.ccdata.io/indices/regulatory — regulatory/benchmark product scope (accessed 2026-08-14)
- https://data.coindesk.com/press-releases/cryptocompare-adds-commercial-api-market-data-service-to-existing-free-service — commercial API service history (accessed 2026-08-14)
- https://www.spark.money/tools/crypto-api-pricing-comparison — free-tier retirement and pricing context (accessed 2026-08-14)
- https://medium.com/tales-from-the-crypto/a-complete-starter-guide-to-the-cryptocompare-api-29b4bb1ca25 — API structure and developer walkthrough (accessed 2026-08-14)
- https://masterthecrypto.com/cryptocompare/ — coverage figures (exchanges/pairs) (accessed 2026-08-14)
