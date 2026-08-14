# IRESS

## 1. Snapshot
- **Owner/parent:** IRESS Limited — independent, publicly listed on the Australian Securities Exchange (ASX: IRE); not owned by a bank or exchange group.
- **Coverage:** Primarily ANZ (Australia/New Zealand), UK (incl. UK Lending), South Africa, and Canada; segments reported as Financial Markets-APAC, Wealth Management-ANZ, UK, UK Lending, South Africa and Canada. Fund coverage extends to UK, Australia, New Zealand, Singapore, Canada and South Africa.
- **Free tier:** No public free tier; retail-facing products (e.g. IRESS Investor/htmlIRESS) carry small monthly fees that are often rebated against brokerage commissions.
- **Pricing model & ranges:** Per-seat/per-product monthly subscriptions plus market-data royalty pass-through. Retail examples: IRESSTrader (webIRESS) ~A$88/month (GST incl.), IRESS Investor (htmlIRESS) ~A$15/month, IRESS ViewPoint ~A$342.82/month (raised from ~A$187 in Nov 2023), netIRESS priced on application. Institutional/enterprise trading and wealth platform pricing is quote-based, not published.

## 2. Coverage
IRESS's core footprint is the ANZ, UK, South Africa and Canada markets where it holds strong incumbent positions in trading and wealth-management software; it is not a global multi-asset data vendor in the Bloomberg/Refinitiv sense. Its data products span equities, derivatives, fixed income access and managed-fund data (asset allocation, pricing, distributions, performance, fees, fund security information) across the markets it serves, plus consolidated global market news feeds sourced from third-party vendors distributed through its terminals. Depth is strongest in local-market trading infrastructure (order routing, portfolio and compliance tooling) rather than broad cross-asset historical depth outside its home regions.

## 3. Datasets
IRESS's differentiated asset is less "proprietary content" and more integrated trading/wealth infrastructure: real-time exchange feeds (ASX, NZX, LSE, JSE and others it connects to), managed-fund/unit-trust data, adviser/wealth-management datasets (portfolio, CRM, compliance), and mortgage/lending data in the UK (via its UK Lending business, e.g. Mortgage Sourcing/Criteria data). It is best understood as a trading-and-advice-workflow platform with embedded market data rather than a standalone reference-data content house.

## 4. APIs & technical integration
IRESS offers "Web Services" (public-facing IRESS Central Web Servers, or self-hosted "Web Services 4" for better performance/security) documented via a Programmer's Guide, plus a Desktop COM API (IRESS Server API Type Library) for the Windows-based netIRESS terminal. FIX-protocol-style server sessions (IOSPlus, IPS, FIXPlus) support order/trade-related connectivity. "IRESS Open" is the umbrella for third-party/partner integrations (200+ integrations, 300+ data feeds claimed), with sample code and documentation partly hosted on GitHub (github.com/iress) and the IRESS Community forum. No public evidence of an MCP server or LLM-native integration layer.

## 5. Enabling technology
IRESS runs a mix of legacy Windows desktop terminals (netIRESS) alongside modern web/API layers (webIRESS, Web Services 4) — reflecting a decades-old platform (est. 1993) undergoing incremental modernization rather than a cloud-native rebuild. No public disclosure of AI/LLM features, entity-resolution technology, or a modern data-ops/streaming architecture comparable to newer entrants; public materials emphasize platform breadth (trading + wealth + compliance + market data) over data-science tooling.

## 6. Customer / user feedback
Public review volume is thin relative to global peers; most available commentary is from brokerage/platform forums (e.g. Whirlpool forums on Australian retail platforms) rather than structured review sites. Analyst commentary (e.g. Porter's Five Forces-style write-ups) frames IRESS as holding "a strong position in wealth management and trading software in Australia, the UK and South Africa but facing margin and growth pressure from global pricing competition and evolving client needs" — i.e., entrenched but increasingly squeezed by cheaper/newer alternatives. Retail users have flagged fee increases (e.g. ViewPoint's ~83% subscription hike in Nov 2023) as a pain point. Segments served: retail brokers/platforms, wealth advisers, institutional trading desks, and lenders (UK).

## 7. Edge & positioning
- **Leads on:** Deep incumbency and workflow lock-in in ANZ/UK/South Africa wealth and trading software; integrated order management + compliance + portfolio tooling in one stack; local exchange connectivity and adviser ecosystem relationships.
- **Lags on:** Global multi-asset coverage and content depth (no meaningful presence outside its core geographies); modern API/cloud-native design is partial (legacy desktop core still central); minimal public AI/analytics innovation; pricing is opaque and has drawn criticism for step-increases.
- **Best-for:** Brokers, wealth advisers and buy-side/sell-side trading desks operating specifically in Australia, New Zealand, the UK or South Africa who need integrated trading + portfolio + compliance workflow rather than standalone global market data.

## 8. Provenance
- https://www.iress.com/software/trading-and-market-data/market-data/ — IRESS market data product page (accessed 2026-08-14)
- https://www.iress.com/software/trading-and-market-data/institutional-trading/market-data-institutional/ — institutional market data segment page (accessed 2026-08-14)
- https://www.iress.com/software/trading-and-market-data/market-data-south-africa/ — South Africa market data offering (accessed 2026-08-14)
- https://portersfiveforce.com/blogs/competitors/iress — competitive-landscape analysis of IRESS (accessed 2026-08-14)
- https://webservices4.iress.com.au/Documentation/Guide.aspx — Web Services 4 Programmer's Guide (accessed 2026-08-14)
- https://community.iress.com/t5/Xplan-Integrations/What-is-Iress-Open-Understanding-our-integration-tool-types-and/ta-p/27257 — IRESS Open integration overview (accessed 2026-08-14)
- https://github.com/iress — IRESS public developer/GitHub presence (accessed 2026-08-14)
- https://www.ausiex.com.au/private/Products/News.aspx?id=AUSIEXannouncement194 — IRESS subscription price-increase notice (accessed 2026-08-14)
- Note: WebFetch to iress.com and other live pages was blocked by the sandbox's egress proxy; findings rely on the search index's cached snippets of these URLs, not direct page fetches.
