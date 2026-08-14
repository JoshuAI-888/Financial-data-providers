# LunarCrush

## 1. Snapshot
- **Owner/parent:** LunarCrush, Inc. — independent, VC-backed startup co-founded 2019 by Joe Vezzani (CEO) and Jon Farjo (CPO), based in Costa Mesa, California. Raised ~$5M total across rounds, including a Series A (July 2023) valuing the company at ~$30M; investors include Draper Associates, INCE Capital, Techstars, and MoonPay.
- **Coverage:** Social-intelligence platform originally crypto-native, now expanded to 4,000+ cryptocurrencies, 2,000+ stocks, plus NFTs and broader cultural/topic tracking — real-time social sentiment, creator/influencer metrics, and market-signal data via a single REST API.
- **Free tier:** Limited free/trial access exists (exact current cap not confirmed in available sources), but the primary self-serve model is **pay-as-you-go**: minimum $1/day buys 2,000 API credits, with additional credits at $0.0005 each; a 10% discount applies when paying with the platform's own token (LUNR).
- **Pricing model & ranges:** Usage-based/credit metered pricing (pay-as-you-go) at the low end, scaling to named "Builder" and "Scale" plan tiers for higher API limits, AI-agent capabilities, team seats, and support level; Enterprise tier available with custom SLAs via direct sales contact. Exact monthly dollar figures for Builder/Scale/Enterprise tiers were not confirmed in public sources — a research gap.

## 2. Coverage
Started as a crypto-only social-sentiment platform and has since extended the same engagement-tracking, sentiment-analysis, creator-ranking, Galaxy Score, and AltRank methodology to equities (2,000+ stocks) — an unusual cross-asset expansion among sentiment vendors (most stay purely equity or purely crypto). Also tracks NFTs and broader "cultural topics," positioning LunarCrush as a general social-intelligence layer rather than a narrowly finance-specific vendor. Social-source breadth spans major platforms (Twitter/X, Reddit, YouTube, TikTok, news, and other public social channels) aggregated into composite scores.

## 3. Datasets
- **Galaxy Score™:** composite social + market health metric comparing an asset's current social/market activity against its own historical baseline.
- **AltRank™:** relative-momentum ranking of every tracked asset against every other asset by combined social + market momentum (e.g., a stock at AltRank #1 has the strongest combined signal in the tracked universe).
- **Creator/influencer metrics:** rankings and engagement data on individual social-media accounts driving conversation about tracked assets.
- **Raw social engagement/sentiment feeds:** underlying mention volume, sentiment polarity, and engagement data feeding the composite scores, available via API for both crypto and (newer) equities.
- Real-time update cadence; API v4 (current generation) documented at lunarcrush.com/developers.

## 4. APIs & technical integration
- **API type:** Single REST/JSON API (v4) covering crypto, stocks, and topics; official developer hub with API overview, pricing, and SDK docs at lunarcrush.com/developers.
- **Auth:** API key, credit-metered per call under the pay-as-you-go model.
- **Formats:** JSON; official documentation and code examples via the developer portal.
- **MCP availability:** LunarCrush explicitly advertises **MCP support** ("API, MCP & SDK Documentation") — a notable differentiator, aligning it with Unusual Whales as one of the few providers in this landscape offering a documented MCP integration for AI-agent access.
- **Rate limits/delivery:** Credit-based consumption rather than fixed request-per-month caps; higher tiers (Builder/Scale) unlock greater throughput, AI-agent features, and enterprise SLAs.

## 5. Enabling technology
Real-time social-media crawling and NLP/engagement-scoring pipeline aggregating cross-platform social activity (Twitter/X, Reddit, YouTube, TikTok, news) into normalized composite metrics (Galaxy Score, AltRank). Applies the same scoring methodology across both crypto and equities, suggesting a generalized, asset-agnostic sentiment/momentum engine rather than asset-specific tooling. Recent product direction emphasizes AI-agent integration (MCP support, "AI agent capabilities" in pricing tiers) — positioning LunarCrush as infrastructure for AI-driven trading/research agents, not just a dashboard product.

## 6. Customer / user feedback
Reviewed favorably in crypto-focused outlets (CryptoAdventure, CryptoSlate, CryptoIndustry) as a leading social-intelligence platform for crypto traders, with the stocks expansion noted as a differentiating recent move. Positive notes: real-time data, broad social-platform aggregation, useful composite scores (Galaxy Score/AltRank) for quick asset screening, and growing AI-agent/API tooling. Common caveats in the review ecosystem for this type of tool: social-sentiment signals are noisy and best used as a screening/context layer rather than a standalone trading signal, and pricing transparency for higher tiers is limited without contacting sales. User base: retail and prosumer crypto traders primarily, with newer expansion into equity-focused retail/prosumer users and AI-agent/bot builders.

## 7. Edge & positioning
- **Leads on:** genuine crypto-social-sentiment pedigree (founded 2019, one of the original dedicated crypto-social platforms) now cross-applied to equities with the same proven methodology (Galaxy Score/AltRank); modern, credit-based self-serve pricing; explicit MCP/AI-agent support ahead of most peers.
- **Lags on:** pricing-tier transparency at the higher end (Builder/Scale/Enterprise dollar amounts not publicly clear), and depth/rigor versus institutional-grade equity-sentiment specialists (SMA, RavenPack) that offer patented methodologies and decades of validation research.
- **Best-for:** crypto traders and retail/prosumer investors wanting a unified, self-serve, API/MCP-accessible social-sentiment and momentum-ranking tool spanning both crypto and stocks — particularly attractive for AI-agent/bot builders given native MCP support.

## 8. Provenance
- https://lunarcrush.com/products/lunarcrush-api/ — official API product page (accessed 2026-08-14)
- https://lunarcrush.com/developers/api/overview — official developer hub, API/MCP/SDK docs (accessed 2026-08-14)
- https://lunarcrush.com/developers/api/pricing — official API pricing documentation (accessed 2026-08-14)
- https://lunarcrush.com/faq/how-much-does-lunarcrush-cost — official pricing FAQ (accessed 2026-08-14)
- https://lunarcrush.com/blog/social-signal-behind-every-stock-lunarcrush-equities/ — official blog on equities expansion (accessed 2026-08-14)
- https://app.dealroom.co/companies/lunarcrush — independent funding/investor profile (accessed 2026-08-14)
- https://cryptoadventure.com/lunarcrush-review-the-ultimate-social-intelligence-platform-for-crypto-traders/ — independent product review (accessed 2026-08-14)
- https://cryptoslate.com/companies/lunarcrush/ — independent company/research profile (accessed 2026-08-14)

**Note:** WebFetch to lunarcrush.com was egress-blocked in this environment; findings rely on the WebSearch index and cached/indexed content rather than direct page retrieval. Exact Builder/Scale/Enterprise dollar pricing was not confirmed and is flagged as a gap.
