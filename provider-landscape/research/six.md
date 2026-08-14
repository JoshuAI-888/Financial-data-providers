# SIX Group / SIX Financial Information

## 1. Snapshot
- **Owner/parent:** SIX Group AG — owned by its user banks (a consortium of ~120 Swiss and international financial institutions); operates the Swiss and Spanish stock exchanges (SIX Swiss Exchange, BME) and the SIX Financial Information data division (formerly Telekurs, renamed from "SIX Telekurs" in 2012).
- **Coverage:** Global reference, pricing and corporate-actions data with strong European/Swiss depth; offices in 23 countries; sourced from 1,500+ trading venues and contributors.
- **Free tier:** No public free tier; SIX offers a "request a free demo" for its APIs but data access is licensed/subscription-based.
- **Pricing model & ranges:** Enterprise licensing by instrument coverage, delivery method and use-case (display vs. redistribution vs. internal use); no public price list — quote-based via sales contact. Delivery-method tiers (file feed, Bulk API, Web API) suggest differentiated pricing by volume/latency need.

## 2. Coverage
SIX Financial Information's flagship reference-data product (Valordata Feed, VDF) covers reference/descriptive data and corporate actions on roughly 20 million financial instruments (some materials cite up to 23 million with pricing), drawing from 1,500+ trading venues globally — giving it very broad cross-asset, cross-market reference-data breadth rather than deep proprietary market-by-market analytics. Evaluated/fair-value pricing extends to fixed income, floating rate notes, money-market instruments, MBS/ABS, OTC derivatives and green/ESG-labelled securities, supplemented by US municipal-securities data added from Moody's Analytics and Mergent. Swiss home-market depth (SIX Swiss Exchange listings, Swiss indices) is a particular strength given SIX's exchange-operator role.

## 3. Datasets
Core proprietary holdings: Valordata Feed (reference & descriptive data + corporate actions across ~20M instruments), Evaluated Pricing (independent fair-value pricing for hard-to-price fixed income/derivatives/structured products), and Swiss Indices (SIX operates the official Swiss market indices, e.g. SMI). It positions itself as an independent, exchange-grade source of record for instrument identifiers, corporate actions and reference data — a category where accuracy/completeness (not breadth of alternative datasets) is the value proposition.

## 4. APIs & technical integration
Multiple delivery layers: (1) SIX Web API — REST/JSON interface aimed at asset managers, wealth managers, online brokers and software integrators; (2) SIX Bulk API — high-throughput feed for populating databases, secured via mTLS certificate authentication; (3) File-based delivery — Valordata Feed natively in EDIFACT (ISO-based), convertible to XML (VDF2XML) or fixed-record-length (DOC converter), with cash-flow/event data also available in ISO15022 (SWIFT MT564) format; (4) Display/desktop and cloud-based solutions. SIX adheres to ISO standards (dates, times, countries, currencies) for integration consistency. No public evidence of an MCP server; API design (REST/JSON, mTLS) is modern relative to legacy EDIFACT-era peers.

## 5. Enabling technology
SIX's technical differentiation is standards-compliance and format interoperability (ISO15022/SWIFT MT564, ISO country/currency/date standards) layered over a legacy EDIFACT-native reference-data core, now exposed through modern REST/JSON and Bulk APIs with certificate-based security. No public disclosure of AI/LLM-specific features or automated entity-resolution technology; the emphasis in public materials is data governance/standardization and multi-format delivery rather than data-science tooling.

## 6. Customer / user feedback
Independent customer-review coverage is sparse (SIX Financial Information is enterprise/B2B and does not appear on consumer review sites). Trade press (Finextra, A-Team Insight/A-Team Group) coverage over the years documents steady expansion of evaluated-pricing instrument coverage (green bonds, ABS/MBS, US munis via Moody's/Mergent partnership) as a recurring investment theme, suggesting active content roadmap execution. Caution: search results also surfaced an unrelated "Six Group Trust" — a fraudulent brokerage impersonating the SIX brand, flagged by scam-review sites; this is a distinct, unaffiliated scam entity and not evidence about the real SIX Group's service quality.

## 7. Edge & positioning
- **Leads on:** Breadth and neutrality of reference/corporate-actions data (~20M instruments, 1,500+ venues); Swiss/European home-market authority as the exchange operator itself; strong evaluated-pricing franchise for hard-to-value fixed income and structured products; ISO/SWIFT-standard interoperability.
- **Lags on:** Brand visibility and API modernity relative to Bloomberg/Refinitiv/S&P; legacy EDIFACT format still the native VDF format (retrofitted with XML/JSON wrappers); thin independent customer-review presence makes third-party validation hard to triangulate; less known for analytics, estimates, or research content than reference/pricing data.
- **Best-for:** Custodians, fund administrators, wealth managers and back-office/middle-office operations needing authoritative, standards-compliant instrument reference data, corporate actions and independent fair-value pricing — especially for European/Swiss and hard-to-price fixed income instruments.

## 8. Provenance
- https://www.six-group.com/en/products-services/financial-information/reference-pricing-data/reference-data.html — reference data solutions overview (accessed 2026-08-14)
- https://www.six-group.com/en/products-services/financial-information/market-reference-data.html — market & reference data provider overview (accessed 2026-08-14)
- https://www.six-group.com/en/products-services/financial-information/delivery-methods.html — data feeds & desktop delivery methods (accessed 2026-08-14)
- https://www.six-group.com/en/products-services/financial-information/delivery-methods/api/web.html — SIX Web API description (accessed 2026-08-14)
- https://www.six-group.com/en/products-services/financial-information/delivery-methods/api/bulk.html — SIX Bulk API, mTLS auth (accessed 2026-08-14)
- https://www.six-group.com/en/products-services/financial-information/delivery-methods/files/vdf.html — Valordata Feed formats (EDIFACT/XML/DOC) (accessed 2026-08-14)
- https://www.finextra.com/pressarticle/35991/six-telekurs-expands-evaluated-pricing-business — evaluated pricing expansion coverage (accessed 2026-08-14)
- https://a-teaminsight.com/blog/six-telekurs-adds-data-from-moodys-analytics-and-mergent-for-us-municipal-securities/?brand=ati — US muni data partnership (accessed 2026-08-14)
- Note: WebFetch to six-group.com and en.wikipedia.org was blocked by the sandbox's egress proxy; findings rely on WebSearch index snippets rather than direct page fetches.
