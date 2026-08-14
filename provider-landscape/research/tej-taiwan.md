# TEJ / Taiwan Economic Journal

## 1. Snapshot
- **Owner/parent:** Taiwan Economic Journal Co., Ltd. — independent Taiwanese company, founded April 1990; the largest local financial/economic database provider in Taiwan.
- **Coverage:** Primary depth in Taiwan equities (TWSE and TPEx-listed), financials and fundamentals; API also extends to Japan, Korea, China and Hong Kong market data for cross-Asia fundamental analysis.
- **Free tier:** No public free tier for production data; API access requires account registration and an API key. (Academic/campus-licensed access is common via university library subscriptions, which is effectively "free" to end users at subscribing institutions.)
- **Pricing model & ranges:** Not publicly published — commercial pricing is quote/registration-based (contact TEJ directly); academic institutions typically access via site-licensed subscriptions through university libraries.

## 2. Coverage
TEJ's core and best-known coverage is Taiwan-listed equities and related instruments, sourced directly from TWSE (Taiwan Stock Exchange) and TPEx (Taipei Exchange): daily stock prices, institutional investor (foreign/investment trust/dealer) trading flows, margin trading and short-selling data, monthly revenue disclosures, audited financial statements, cash-flow detail, and TEJ-derived financial ratios. Its API additionally provides fundamental-analysis data for Japan, Korea, China and Hong Kong, positioning TEJ as a Taiwan-anchored but broader-Northeast-Asia fundamental data source — though the non-Taiwan coverage is less differentiated/authoritative than its home-market data.

## 3. Datasets
TEJ's differentiated strength is depth and history in Taiwan corporate fundamentals and market microstructure data: audited financials, monthly sales disclosures, corporate-governance/event-driven data, and derived valuation/risk ratios built specifically for Taiwan GAAP/regulatory disclosure norms — content that global vendors typically source secondhand or with a lag. It is described as Taiwan's largest and most comprehensive financial/economic database, with long, consistent historical series supporting quantitative backtesting and academic research (100+ published academic papers cited as using TEJ data).

## 4. APIs & technical integration
The TEJ API (documented at a public "TEJAPI User Guide," tejtw.github.io) supports REST API access as well as native bindings for Python, R and .NET, enabling direct database integration for quantitative/statistical workflows. Access requires registering a TEJ account and applying for an API key. This is a comparatively modern, developer-friendly integration model (public docs, familiar languages, key-based REST access) relative to some other regional/legacy vendors in this set. No public evidence of an MCP server.

## 5. Enabling technology
Public materials emphasize TEJ's role as a data curator/normalizer for Taiwan's fragmented local disclosure sources (TWSE/TPEx filings, monthly revenue announcements, audited statements) into consistent, analysis-ready datasets and derived ratios — i.e., its "enabling technology" value is data standardization and normalization of local regulatory disclosures rather than published AI/ML or entity-resolution infrastructure. No specific AI/LLM feature disclosures were found.

## 6. Customer / user feedback
TEJ is described in available sources as having "excellent data quality and professional standards" and being "highly regarded in the field of financial databases in Taiwan," with strong endorsement via extensive academic citation (100+ international journal papers using TEJ data) — a meaningful proxy for data-quality trust among quantitative researchers. No structured commercial customer-review base (G2/Capterra) was found; feedback triangulation here rests primarily on reputation/citation evidence rather than direct user reviews, and is skewed toward the academic/quant-research segment rather than commercial asset-management users.

## 7. Edge & positioning
- **Leads on:** Authoritative, deep, long-history Taiwan equity fundamentals and market microstructure data (institutional flows, margin/short data, monthly revenue, audited financials) sourced and normalized specifically for local TWSE/TPEx disclosure conventions; strong academic credibility/citation record; modern, well-documented REST API with Python/R/.NET support.
- **Lags on:** Non-Taiwan coverage (Japan/Korea/China/HK) is a secondary extension, not comparable in depth to Taiwan-specific data or to global vendors' coverage of those markets; no public pricing transparency; limited brand recognition and review presence outside Taiwan/academic circles.
- **Best-for:** Quantitative researchers, academic finance departments, and asset managers/analysts needing granular, long-history Taiwan-listed company fundamentals, ownership/flow data and derived financial ratios for backtesting or fundamental analysis, especially where global vendors' Taiwan coverage is comparatively shallow.

## 8. Provenance
- https://www.tejwin.com/en/about/ — TEJ company background and history (accessed 2026-08-14)
- https://www.tejwin.com/en/solution/taiwan-stock-data/ — Taiwan Stock Data Solutions overview (accessed 2026-08-14)
- https://www.tejwin.com/en/insight/stock-api/ — TEJ stock API guide/explainer (accessed 2026-08-14)
- https://tejtw.github.io/EN-TEJAPI/ — TEJAPI public user guide (accessed 2026-08-14)
- https://tejtw.github.io/EN-TEJAPI/tutorial/restapi/ — TEJAPI REST API documentation (accessed 2026-08-14)
- https://www.linkedin.com/company/taiwan-economic-journal-co-ltd- — TEJ LinkedIn company profile (accessed 2026-08-14)
- https://www.crunchbase.com/organization/taiwan-economic-journal-tej — TEJ Crunchbase company profile (accessed 2026-08-14)
- Note: WebFetch to tejwin.com was blocked by the sandbox's egress proxy; findings rely on WebSearch index snippets rather than direct page fetches.
