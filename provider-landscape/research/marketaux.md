# Marketaux

## 1. Snapshot
- **Owner/parent:** Marketaux (independent, small team; Australia-based). Positioning: an affordable, developer-friendly **financial** news API that returns headlines already linked to the tickers/entities they concern, each with a sentiment score — "stock, crypto and forex news + sentiment."
- **Regions/language coverage:** Global markets — **80+ exchanges/markets, 30+ languages, ~5,000 sources**, tracking **200,000+ entities**. Good international/non-English breadth for a low-cost finance API.
- **Free tier:** **YES (a genuine free/low-cost pick).** ~100 requests/day, no credit card required; enough to build and test. Paid plans add volume, more history and extra filters.
- **Pricing model & ranges (published):** Freemium. Higher paid tier ("Professional") around **$166/mo billed annually (~$199/mo monthly)** for ~50,000 requests/day, 100 articles/request, full metadata, Market Stats API and full entity/source access. ~20% discount (2 months free) on annual billing; smaller intermediate tiers exist.

## 2. Data-domain coverage
- **Financial news:** Core — stock, ETF, index, crypto and forex news across 80+ markets.
- **General news:** Secondary — general/business articles surface where they mention tracked entities.
- **Press releases/newswires:** Not a dedicated newswire; PR appears via indexed sources.
- **Historical archive:** Yes, but history depth gated by plan (longer look-back on higher tiers).
- **Sentiment/analytics:** Yes — per-entity `sentiment_score` (-1 to +1), `match_score`, and per-highlight sentiment scored on the exact text span where the entity appears.
- **Entity tagging:** Yes — resolves stock/crypto/forex symbols and returns the exact sentences (highlights) each entity is mentioned in; Market Stats API aggregates entity sentiment.

## 3. Datasets
- Sources: ~5,000 financial/news outlets; 200,000+ tracked entities across 80+ global markets.
- History depth: recent by default on free/low tiers; extended archive on paid.
- Update latency: near-real-time ("instant news access" on Professional); free tier has some delay/limits.
- Metadata: entity symbols + names, per-entity and per-highlight sentiment, match score, source, published date, snippet, image, industry/country filters.

## 4. APIs & technical integration
- **API type:** REST/JSON.
- **Auth:** API key (`api_token` query parameter).
- **Formats:** JSON responses; rich filter params (symbols, entity types, countries, industries, languages, sentiment thresholds, date ranges).
- **Rate limits:** ~100 req/day free; up to ~50,000 req/day on Professional.
- **Delivery:** HTTP API only — no managed S3/Snowflake/Databricks share or streaming feed.
- **MCP server:** No official MCP server.

## 5. Enabling technology
- Entity-resolution engine mapping article text to stock/crypto/forex symbols, plus a sentiment model scoring both whole-article and per-highlight spans (-1..+1). Filtering/aggregation layer (Market Stats API) computes rolling entity sentiment. Lightweight, finance-focused NLP rather than a heavy analytics stack.

## 6. Customer / user feedback
- **Ratings:** Positive but low-volume — favourable coverage on Product Hunt and API-directory/comparison sites (FreeAPIHub, publicapis.io); repeatedly cited among the best affordable finance-sentiment APIs.
- **Pros:** Cheap, reliable, easy to integrate; news pre-linked to tickers with usable sentiment; broad market/language coverage for the price; usable free tier.
- **Cons:** Small independent vendor (support/SLA weaker than enterprise players); source pool (~5k) smaller than premium feeds; history and rate limits gated behind paid tiers; no streaming/bulk delivery.
- **User segments:** Indie fintech developers, retail-trading dashboards, research/alerting tools, budget quant prototyping.

## 7. Edge & positioning
- **Leads on:** price-to-value for **finance-tagged** news + sentiment — you get ticker linkage and sentiment where NewsAPI/Mediastack give none.
- **Lags on:** enterprise-grade breadth, latency guarantees, delivery options and support versus RavenPack/Bigdata or Benzinga.
- **Best for:** startups and researchers who need affordable, entity-tagged financial news with sentiment; the practical low-cost alternative to institutional analytics vendors.

## 8. Provenance
- https://www.marketaux.com/ — official product overview (accessed 2026-08-11)
- https://www.marketaux.com/pricing — official pricing/tiers (accessed 2026-08-11)
- https://www.marketaux.com/documentation — official API documentation (accessed 2026-08-11)
- https://www.producthunt.com/products/marketaux — independent product listing/reviews (accessed 2026-08-11)
- https://freeapihub.com/apis/marketaux — independent free-tier/sentiment summary (accessed 2026-08-11)
- https://adanos.org/insights/blog/best-financial-news-sentiment-apis-2026/ — independent sentiment-API comparison (accessed 2026-08-11)
