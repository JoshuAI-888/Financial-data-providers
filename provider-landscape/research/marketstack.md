# Marketstack

## 1. Snapshot
- **Owner/parent:** APILayer (an API marketplace brand; part of the idalko/APILayer group). HQ associated with Austin, Texas, USA. Marketstack is one of APILayer's flagship financial APIs.
- Positioning one-liner: a low-cost, JSON-first REST API that makes real-time, intraday and historical stock-market data trivially easy to pull for developers and small apps.
- **Regions/markets covered:** Genuinely global equities by ticker — advertised at 125,000+ tickers across 70+ worldwide stock exchanges (US majors plus many international exchanges). Unlike US-only free tiers elsewhere, Marketstack's headline is multi-exchange breadth, though depth/quality is strongest on US names; coverage of specific home exchanges (e.g. NZX) should be verified per-symbol before relying on it.
- **Free tier:** Yes — Free plan gives ~100 API requests/month, end-of-day (EOD) data, and up to 12 months of history. No credit card required. Free tier is non-commercial and excludes real-time/intraday.
- **Pricing model & known ranges:** Subscription tiers by monthly request volume. Published ranges: Basic ~$9.99/mo (10,000 requests, intraday, longer history), Professional ~$49.99/mo (100,000 requests, real-time), Business ~$149.99/mo (500,000 requests). (Promotional pricing sometimes shows Basic near $8.99/mo.) Higher/custom enterprise plans on request.

## 2. Data-domain coverage
- **public equity:** yes — core product; EOD, intraday (1-min for Pro+), real-time (paid) across 70+ exchanges.
- **fundamentals:** limited — v2 adds tickers/exchanges/dividends/splits metadata; not a deep fundamentals provider.
- **forex / crypto:** not the focus of Marketstack itself (APILayer sells separate currency/crypto APIs).
- **macro / news / alt-data:** no.

## 3. Datasets
- End-of-day prices (OHLCV), intraday quotes (1/5/10/15/30/60-min intervals on paid tiers), real-time last-price (paid), plus dividends, stock splits, ticker and exchange reference/metadata.
- History depth: up to ~30+ years of EOD on higher tiers; free tier limited to ~12 months.
- Breadth: 125,000+ tickers, 70+ exchanges; sourced from multiple licensed upstream market-data vendors rather than direct exchange feeds.
- Real-time vs delayed vs EOD: EOD on all tiers; intraday and real-time gated to paid plans. No proprietary/exclusive datasets — it is an aggregator/reseller.

## 4. APIs & technical integration
- API type: REST (JSON) — simple GET endpoints (`/eod`, `/intraday`, `/tickers`, `/exchanges`, `/dividends`, `/splits`). v2 API is the current generation. No native WebSocket streaming.
- Auth: API access key passed as `access_key` query parameter.
- Formats: JSON (primary). Pagination via limit/offset.
- Rate limits/latency: enforced by monthly request quota per plan; per-second throughput scales with tier. Built on APILayer cloud infrastructure with ~99.9%+ advertised uptime and HTTPS/256-bit encryption (HTTPS on paid tiers).
- Delivery: pure API pull; no bulk flat-file/Snowflake/Databricks distribution. No official MCP (Claude/OpenAI) server.

## 5. Enabling technology
- Runs on APILayer's shared cloud API-gateway platform (same infrastructure powering their other APIs), giving elastic scaling and a consistent developer console/dashboard for keys and usage.
- Data-sourcing: aggregated from multiple high-authority, licensed market-data providers and normalized into one schema (not a direct-from-exchange feed).
- AI features: none specific. Reliability rests on cloud redundancy; being a reseller, freshness/accuracy depends on upstream vendors.

## 6. Customer / user feedback
- Marketstack is widely cited in "best free/cheap stock API" roundups (DEV.to, QuantPedia, blog comparisons) as an easy, affordable entry point; APILayer's marketplace lists it among their most-used APIs.
- Sentiment (triangulated across comparison blogs and third-party review pages such as FindMyMoat and ScoopReview): pros = very cheap, simple REST, broad exchange list, quick onboarding, generous history on paid tiers. Cons = free tier is tiny (100 calls/mo, EOD-only, no HTTPS historically), aggregated data so not tick-accurate for HFT, occasional gaps/lag on non-US symbols, support is marketplace-tier.
- Who uses it: indie developers, students, fintech prototypes, dashboards and screeners needing cheap global EOD/intraday rather than institutional-grade feeds.

## 7. Edge & positioning
- **Leads on:** price and simplicity — one of the cheapest ways to get multi-exchange EOD/intraday via a clean REST call; good for MVPs and side projects.
- **Lags on:** data depth, latency guarantees, streaming, and fundamentals; not suitable for latency-sensitive trading or as an institutional book-of-record. Aggregated sourcing means it's a convenience layer, not a primary market-data authority.
- **Best-for:** budget-conscious developers who want broad global tickers with minimal integration effort. The free tier exists but is too small for production; treat it as a trial.

## 8. Provenance
- https://marketstack.com/ — official product homepage (accessed 2026-08-11)
- https://marketstack.com/pricing — official pricing tiers (accessed 2026-08-11)
- https://marketstack.com/documentation — official API v1 docs (accessed 2026-08-11)
- https://docs.apilayer.com/marketstack/docs/marketstack-api-v2-v-2-0-0 — official v2 endpoint docs (accessed 2026-08-11)
- https://blog.apilayer.com/introducing-marketstack-v2-api/ — v2 feature/intraday details (accessed 2026-08-11)
- https://marketplace.apilayer.com/marketstack-api — APILayer marketplace listing (accessed 2026-08-11)
- https://www.findmymoat.com/tools/marketstack — independent review/pricing (accessed 2026-08-11)
- https://quantpedia.com/best-historical-market-data-providers/ — independent provider comparison (accessed 2026-08-11)
