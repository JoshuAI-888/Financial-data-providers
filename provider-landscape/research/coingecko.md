# CoinGecko

## 1. Snapshot
- **Owner/parent:** Independent, privately held (Singapore-based); founded 2014 by Bobby Ong and TM Lee. No disclosed acquisition/parent company as of 2026.
- **Coverage:** 18,000+ coins, 20M+ tokens across 1,700+ CEX/DEX venues, 43M+ on-chain (DEX) tokens across 250+ blockchain networks, 3,000+ NFT collections across 20+ marketplaces.
- **Free tier:** Yes — "Demo" API plan, no credit card, ~30 calls/min (some sources cite up to 100 calls/min), 10,000 calls/month, 30 of 70+ endpoints exposed.
- **Pricing model & ranges:** Tiered SaaS + API subscription. Paid tiers reported as Analyst ~$129/mo, Lite ~$499/mo, Pro ~$999/mo (via API pricing page), with a separate Basic paid tier from ~$29–35/mo (300 calls/min, 100,000 calls/mo) adding WebSocket/webhook access; custom Enterprise above that. Pricing pages show variation between sources — treat listed dollar figures as indicative, confirm on coingecko.com/en/api/pricing.

## 2. Coverage
Broadest self-reported free-data asset universe of the five providers reviewed: 18,000+ coins and 20M+ tokens tracked across more centralized and decentralized exchanges (1,700+) than any peer here. Its GeckoTerminal on-chain arm separately covers 43M+ DEX-traded tokens across 250+ chains — positioned as one of the largest DEX/on-chain aggregation footprints in the market. NFT coverage (3,000+ collections, 20+ marketplaces including OpenSea, Blur, Magic Eden) is a differentiator versus CoinMarketCap and CryptoCompare. Coverage is global and multi-venue by design (aggregated CEX+DEX), not limited to US-listed assets.

## 3. Datasets
Real-time and historical spot prices, market cap, 24h volume, OHLCV candles; exchange-level order book/ticker data; derivatives (funding rates, open interest); DEX pool/liquidity and token-contract-level pricing (GeckoTerminal); NFT floor price/volume/metadata; "Public Companies" treasury holdings; trending/categories/market dominance indices; global market metrics. Historical depth varies by plan (deeper history gated to paid tiers).

## 4. APIs & technical integration
REST API (v3), 70+ endpoints total, 30 available on the free Demo key. Auth via API key in header or query param. Official and community SDKs exist in Python, Node.js, and other languages; extensive first-party documentation at docs.coingecko.com with a dedicated errors/rate-limits guide. WebSocket/webhook streaming introduced starting at the Basic paid plan (~$29/mo) for continuous price updates — free tier is polling/REST only. Separate dedicated API products exist for On-Chain DEX data (GeckoTerminal) and NFT data.

## 5. Enabling technology
Cloud-hosted REST infrastructure with tiered rate-limiting/gateway layer; own aggregation engine pulling from CEX and DEX order books plus on-chain sources to compute VWAP-style consolidated pricing. GeckoTerminal on-chain product indicates in-house blockchain-indexing infrastructure across 250+ networks rather than reliance on a single third-party indexer. No public disclosure of specific cloud vendor or index-methodology whitepaper found in this research pass.

## 6. Customer / user feedback
Generally positive: reviewers and developers cite ease of integration, strong documentation, and broad coverage "without high costs" relative to peers. Recurring complaints: response-time degradation during peak load, and a cost step-up between the free Demo tier and the first paid tier that some individual/hobbyist developers find steep. G2 reviews are broadly favorable; no major data-accuracy scandals surfaced in this research pass.

## 7. Edge & positioning
- **Leads on:** Broadest combined CEX+DEX+NFT asset coverage among the five; most generous free-tier call volume; strong developer experience/docs.
- **Lags on:** No regulated benchmark/index status (unlike CCData/CryptoCompare); less institutional-research depth than Messari; on-chain analytics (wallet cohorts, holder behavior) shallower than Glassnode.
- **Best-for:** General-purpose price/market-cap/volume data across the widest possible token and NFT universe, and DEX/on-chain token discovery, at low cost.

## 8. Provenance
- https://www.coingecko.com/en/api/pricing — official API pricing tiers (accessed 2026-08-14)
- https://docs.coingecko.com/v3.0.1/reference/endpoint-overview — endpoint count and structure (accessed 2026-08-14)
- https://www.coingecko.com/en/api/nft — NFT API coverage claims (accessed 2026-08-14)
- https://www.coingecko.com/en/api/dex — DEX/on-chain data coverage (accessed 2026-08-14)
- https://support.coingecko.com/hc/en-us/articles/23189120457497-What-is-the-rate-limit-for-the-paid-CoinGecko-API — paid rate limits (accessed 2026-08-14)
- https://www.g2.com/products/coingecko-api/reviews — user review sentiment (accessed 2026-08-14)
- https://docs.coingecko.com/docs/errors-and-rate-limits — API error/rate-limit documentation (accessed 2026-08-14)
