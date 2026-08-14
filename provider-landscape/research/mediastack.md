# mediastack

## 1. Snapshot
- **Owner/parent:** apilayer (a Vue Storefront / APILayer-branded API marketplace product); mediastack is one of several APIs sold through the apilayer.com marketplace, alongside sister products like Currencylayer and Weatherstack. Not a dedicated financial-data company.
- **Coverage:** General/global news aggregator — 7,500+ sources across 50+ countries in 13 languages (Arabic, German, English, Spanish, French, Hebrew, Italian, Dutch, Norwegian, Portuguese, Russian, Swedish, Chinese). Not finance-specific: no ticker/entity tagging or sentiment scoring out of the box.
- **Free tier:** Yes — free plan allows up to 500 requests/month, HTTP only (no HTTPS on free tier), and explicitly **forbids commercial use** (must upgrade once a project generates revenue or goes live commercially).
- **Pricing model & ranges:** Simple tiered SaaS subscription. Basic ~$24.99/mo (10,000 req/mo), Professional ~$99.99/mo (50,000 req/mo), Premium ~$249.99/mo (250,000 req/mo, HTTPS, historical data). Entry paid tier reported as low as ~$9.99/mo in some listings; exact tier names/limits vary slightly by source and change periodically — treat as approximate.

## 2. Coverage
General/global news and blog aggregation (not finance-specialist). Broad geographic and source count (7,500+ outlets, 50+ countries) but a narrow language set (13) versus larger competitors (NewsData.io lists 206 countries/85,000+ sources; NewsAPI.org lists 80,000+ sources). No dedicated financial-markets, crypto, or forex vertical — coverage is topical (general/business/entertainment/sports/etc. categories) rather than entity/ticker-driven. No political-trades, options, or social-sentiment data — pure news headline/article aggregation.

## 3. Datasets
Single core dataset: live and historical news/blog articles returned via one `/news` endpoint, filterable by keyword, date/timeframe, country, language, source, and category. Each article record includes title, description/snippet, author, source, URL, image, category, language, country, and published date/time — a raw news-headline feed, **not** entity-tagged or sentiment-scored (no ticker linkage, no NLP sentiment field). Historical archive available but gated to higher/premium tiers. Indexing latency is reported as within ~5 minutes of publication for major sources.

## 4. APIs & technical integration
- **API type:** REST/JSON, single `news` endpoint with rich query parameters.
- **Auth:** API key via query parameter (`access_key`).
- **Formats:** JSON only; official code samples in PHP, Python, jQuery, Go, Ruby via the apilayer documentation portal.
- **Rate limits:** Tier-dependent (500/mo free up to 250,000/mo Premium); free tier restricted to HTTP (no SSL/HTTPS) — a notable limitation for production use.
- **Delivery:** Simple HTTP polling only; no streaming, no bulk/S3 delivery, no webhook push.
- **MCP availability:** No official MCP server found.

## 5. Enabling technology
Lightweight news aggregation/crawling infrastructure shared across the APILayer marketplace family (same architecture pattern as Currencylayer, Weatherstack, etc.) — essentially a metadata/crawl aggregation layer with no proprietary NLP, entity-resolution, or sentiment-scoring technology. Positioned as a "no-frills" utility API rather than an analytics platform.

## 6. Customer / user feedback
Consistently described in third-party comparisons (dataresearchtools.com, cloro.dev, apitube.io) as one of the cheapest, easiest-to-integrate general news APIs, good for basic prototyping and non-critical use cases. Recurring criticisms: source/language breadth is smaller than rivals (NewsData.io, NewsAPI.org, GNews), the free tier's HTTP-only restriction and low 500 req/month cap are impractical for anything beyond testing, and it lacks the financial entity-tagging/sentiment features that finance-specific competitors (Marketaux, Benzinga) provide. User base is largely indie developers and small SaaS builders prototyping news-display features rather than institutional or buy-side users.

## 7. Edge & positioning
- **Leads on:** price and simplicity for basic, non-financial news-headline aggregation; easy onboarding with no upfront commercial commitment.
- **Lags on:** financial specialization (no ticker/entity tagging, no sentiment scoring, no political/options/social data), language/source breadth versus larger general-news APIs, and production-readiness of the free tier (HTTP-only, low cap, no commercial use).
- **Best-for:** hobbyist/prototype projects needing a cheap, generic global news feed; not a fit for financial-sentiment or entity-level research — Marketaux, Benzinga, or RavenPack cover that ground instead.

## 8. Provenance
- https://mediastack.com/pricing — official pricing tiers and limits (accessed 2026-08-14)
- https://mediastack.com/documentation — official API documentation overview (accessed 2026-08-14)
- https://docs.apilayer.com/mediastack/docs/api-documentation — APILayer technical API docs (accessed 2026-08-14)
- https://github.com/apilayer/mediastack — official GitHub README, endpoint/feature summary (accessed 2026-08-14)
- https://dataresearchtools.com/best-news-apis-comparison/ — independent comparison vs NewsAPI/GDELT (accessed 2026-08-14)
- https://apitube.io/blog/post/news-api-pricing-breakdown-2026 — independent pricing/cost breakdown (accessed 2026-08-14)
- https://www.g2.com/products/mediastack/competitors/alternatives — independent competitor/alternatives listing (accessed 2026-08-14)

**Note:** WebFetch to mediastack.com was egress-blocked in this environment; findings rely on the WebSearch index and third-party comparison sites rather than direct page retrieval.
