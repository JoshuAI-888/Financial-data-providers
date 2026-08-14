# CoinMarketCap

## 1. Snapshot
- **Owner/parent:** Owned by Binance (acquired CoinMarketCap in April 2020); operates as a semi-independent brand/subsidiary.
- **Coverage:** 51M+ tracked assets, 947+ exchanges, 72+ API endpoints, >1 billion API calls/month processed platform-wide.
- **Free tier:** Yes, two tiers — a keyless Public API (no signup, curated/limited endpoint subset) and a keyed Basic plan (free, ~10,000–15,000 call credits/month, 9 latest-market-data endpoints, no historical data, personal/non-commercial use only).
- **Pricing model & ranges:** Tiered subscription: Basic (free) → Hobbyist ~$29/mo (cheapest commercial-use tier) → Startup ~$348/mo → Standard ~$948/mo → Professional ~$3,588/mo → Enterprise ~$8,388/mo+ (custom above). A pay-per-call x402 route was also introduced at $0.01 USDC/call with no subscription.

## 2. Coverage
Largest raw "tracked assets" figure among the five (51M+, reflecting long-tail token listings including many low-liquidity/DEX-origin tokens) and 947+ exchange integrations — both figures larger than CoinGecko's headline numbers, though methodology for "tracked assets" is not independently verifiable. DEX coverage has matured recently with a dedicated DEX API suite (8 APIs across two rollout stages) spanning Ethereum, Solana, and BNB Chain for on-chain pricing, security signals, holders, and pair-level OHLCV. Global in scope; not exchange- or region-restricted the way FMP is to US equities.

## 3. Datasets
Cryptocurrency spot quotes, historical OHLCV, market cap/dominance/rankings, exchange volume and liquidity metrics, global aggregate market metrics, "community" trend/social data, and (new) DEX-specific datasets: token discovery, pricing, contract security flags, holder counts, and pair-level trade/OHLCV data. Standard API emphasizes token-level fundamentals aggregated across CEX+DEX; the DEX API is a separate, narrower on-chain-specific product line.

## 4. APIs & technical integration
REST API, 72+ endpoints, documented at coinmarketcap.com/api/documentation. Requires API key (`CMC_PRO_API_KEY` header) for the Basic+ keyed tiers; a separate keyless public endpoint subset exists for zero-friction prototyping. SDKs/wrappers exist community-side (GitHub: nsmle/cmc-api, cryptoscan-pro wrapper) rather than extensive official multi-language SDKs. Historical data access is explicitly gated — free Basic plan excludes it, a common commercial lever versus CoinGecko's more generous free historical access.

## 5. Enabling technology
Backed by Binance's infrastructure and capital following the 2020 acquisition; CMC operates its own price-aggregation methodology (volume-weighted across exchange feeds) and, more recently, on-chain indexing for its DEX API suite. No public architecture whitepaper found in this pass; positioning emphasizes very high request throughput (>1B calls/month) implying substantial caching/CDN investment.

## 6. Customer / user feedback
Widely described as "the world's most trusted source" for retail-facing crypto price data and ranked ahead of peers in some exchange-data-API comparisons. Known complaints cluster around the community/listings side of the business (bot-driven spam, scam-warning removal, slow moderation response) rather than the core market-data API itself. Some users report altcoin data being less reliable/consistent than for majors when cross-checked against other sources. No major API-specific outage or accuracy scandal surfaced in this pass.

## 7. Edge & positioning
- **Leads on:** Brand trust/name recognition as the default retail price reference; largest raw exchange (947+) and asset-count coverage; Binance-backed scale and uptime; mature DEX API suite.
- **Lags on:** Free tier is more restrictive than CoinGecko's (no historical data, personal-use-only license, smaller endpoint subset); no on-chain analytics depth (Glassnode) or research depth (Messari); no regulated-benchmark status (CCData).
- **Best-for:** High-volume, brand-trusted retail/consumer price and ranking data at scale, and teams already inside the Binance data ecosystem.

## 8. Provenance
- https://coinmarketcap.com/api/pricing/ — official plan tiers and pricing (accessed 2026-08-14)
- https://coinmarketcap.com/api/documentation/ — endpoint and API structure (accessed 2026-08-14)
- https://coinmarketcap.com/academy/article/dex-apis-soft-launch-unveiling-coinmarketcaps-first-dex-api-suite — DEX API launch and coverage (accessed 2026-08-14)
- https://costbench.com/software/blockchain-data-api/coinmarketcap-api/ — third-party pricing tier breakdown (accessed 2026-08-14)
- https://coinmarketcap.com/academy/article/best-free-crypto-api-in-2026-free-tier-comparison — free-tier limits comparison (accessed 2026-08-14)
- https://www.bitdegree.org/crypto/coinmarketcap-review — user review/reputation summary (accessed 2026-08-14)
