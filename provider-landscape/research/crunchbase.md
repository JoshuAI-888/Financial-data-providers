# Crunchbase

## 1. Snapshot
- **Owner/parent:** Independent private company, Crunchbase Inc. — founded 2007 by Michael Arrington as a TechCrunch sister database; acquired by AOL in 2010 (via TechCrunch acquisition); spun out as an independent private company in September 2015 (backed by Emergence Capital, with AOL/Verizon retaining a minority stake).
- **Coverage:** 4M+ private and public companies globally; data sourced from a network of 4,000+ venture-firm partners plus 600,000+ community contributors, alongside Crunchbase's own editorial/research team; broadest at seed/early-stage US and global startup coverage, thinner on deep financials versus PitchBook.
- **Free tier:** No dedicated free API tier as of 2026 — the previously available free/low-cost "Basic" API key tier has been discontinued; free access is limited to the consumer-facing crunchbase.com website browsing, not the API.
- **Pricing model & ranges:** Consumer subscriptions: Pro ~$99/month (or ~$49/month, ~$588/year, billed annually) and Business ~$199/month (~$2,388/year) for CRM integrations/exports/SSO. **API access is gated separately** behind Enterprise/Applications licenses requiring a custom sales quote — third-party estimates put an API entry tier roughly in the $588–$1,188/year range at minimum, scaling to custom enterprise contracts with negotiated call-volume baselines and overage charges; rate limit is a flat 200 calls/minute across all endpoints regardless of plan.

## 2. Coverage
Company profiles (firmographics, industry tags, headcount signals), funding rounds (round-by-round detail, valuations where disclosed), investor profiles and portfolios, M&A/acquisition events, leadership/personnel changes, and news-mention aggregation. Global in scope but strongest for venture-backed startups, especially in the US; coverage of later-stage private financials and proprietary valuation modeling is comparatively shallow relative to PitchBook, and qualitative/strategic market analysis is thinner than CB Insights.

## 3. Datasets
Crunchbase Data / API v4.0 exposes 600+ endpoints spanning: company firmographics, funding-round history, investor/fund data, executives/people, acquisitions, IPOs, "AI insights" and predictive signals (including funding predictions), and news. Delivered via structured JSON entities (organizations, people, funding rounds, acquisitions, investors) with relationship links between them, enabling graph-style traversal of the startup/investor ecosystem.

## 4. APIs & technical integration
REST API (v4.0), documented at data.crunchbase.com, requiring an Enterprise or Applications license (sales-negotiated) — the old self-serve/free Basic API key path has been sunset as of 2026. Flat rate limit of 200 calls/minute across all endpoints with no plan-based tiering disclosed publicly. No official open-source SDK comparable to Nasdaq Data Link's Python/R packages; integration is via direct REST/JSON calls, with third-party wrapper libraries and scraping-adjacent tools (e.g., Piloterr, Nubela) filling gaps for users without enterprise API access. Crunchbase cites over 6 billion API calls annually across its client base, indicating substantial embedded usage in other platforms/tools despite the closed on-boarding process.

## 5. Enabling technology
A hybrid crowdsourced-plus-editorial data model: community contributors (600,000+) and venture-firm data-sharing partners (4,000+) submit and update company/funding records, supplemented by Crunchbase's own research/data team for verification and enrichment, plus increasingly AI-driven "insights" and funding-prediction models layered on top of the structured dataset (per Crunchbase's own API documentation on funding predictions). This crowdsourced-plus-verification model is structurally different from Nasdaq Data Link's marketplace-aggregation model, Similarweb's panel/ISP measurement model, or YipitData's proprietary scraping/transaction-panel model.

## 6. Customer / user feedback
Positioned by third-party comparison sites as the accessible, lower-cost entry point into private-company data relative to PitchBook (which is regarded as deeper on financials/analytics for PE/VC/M&A professionals) and CB Insights (regarded as stronger on strategic market/trend research for corporate innovation and consulting use cases). Reviews note Crunchbase's broader but shallower coverage is well-suited to quick funding lookups and startup-ecosystem exploration, but that VC/corp-dev/GTM teams needing coverage depth and data freshness often find its capabilities limited relative to paid competitors. The 2026 discontinuation of the free/Basic API tier is flagged by developer-community sources (dev.to, DataForB2B) as a notable access-model shift pushing smaller developers toward third-party scraping tools or Enterprise sales conversations.

## 7. Edge & positioning
- **Leads on:** Breadth of private-company/startup coverage (4M+ companies) at a lower consumer price point than PitchBook/CB Insights; API-native design with 600+ structured endpoints and graph-like entity relationships; high embedded usage (6B+ annual API calls) as infrastructure inside other tools.
- **Lags on:** Depth of financial/valuation data versus PitchBook; strategic market-trend analysis versus CB Insights; API accessibility — free/self-serve tier discontinued in 2026, now enterprise-sales-gated with an undisclosed, custom pricing structure and a flat, non-tiered 200 calls/minute rate limit.
- **Best-for:** Teams needing an API-native, broad-coverage private-company/funding-round dataset (company matching, funding-event triggers, investor mapping) as a complement to deeper deal-analytics platforms like PitchBook or research-oriented platforms like CB Insights, where budget favors Crunchbase's lower entry cost over enterprise-only rivals.

## 8. Provenance
- https://about.crunchbase.com/crunchbase-vs-cb-insights — Crunchbase's own comparison vs. CB Insights (accessed 2026-08-14)
- https://data.crunchbase.com/docs/welcome-to-crunchbase-data — official API/data documentation landing page, egress-blocked, relied on search-index summary (accessed 2026-08-14)
- https://pipeline.zoominfo.com/sales/crunchbase-api — third-party 2026 API review covering rate limits and licensing gates (accessed 2026-08-14)
- https://dev.to/agenthustler/crunchbase-api-in-2026-free-tier-gone-what-startup-data-hunters-do-now-1177 — developer-community note on 2026 free-tier discontinuation (accessed 2026-08-14)
- https://www.vendr.com/marketplace/crunchbase — third-party pricing aggregator for Pro/Business consumer tiers (accessed 2026-08-14)
- https://www.geekwire.com/2015/startup-database-crunchbase-to-reportedly-spin-out-as-standalone-company/ — 2015 AOL spin-out reporting (accessed 2026-08-14)
- https://otio.ai/blog/crunchbase-vs-pitchbook — third-party depth-of-coverage comparison vs. PitchBook (accessed 2026-08-14)
- https://en.wikipedia.org/wiki/Crunchbase — corroborating founding/ownership history, egress-blocked so relied on search-index summary (accessed 2026-08-14)
