# Dun & Bradstreet (D&B)

## 1. Snapshot
- Owner/parent: taken private by **Clearlake Capital** in August 2025 for ~$7.7B (incl. debt); previously NYSE-listed (DNB). HQ **Jacksonville, Florida, USA**; founded **1841** as The Mercantile Agency, New York City. Positioning: the incumbent global business-decisioning data & analytics utility, anchored by the **D-U-N-S Number**.
- **Regions/markets covered:** global — 255+ countries and territories; strongest in North America and the UK, with deep presence in Europe, India and China.
- **Free tier:** No (a free D-U-N-S Number lookup/registration exists, but the data products are paid). Limited free "iUpdate"/D-U-N-S self-service.
- Pricing model & known ranges: subscription/enterprise licensing, largely quote-based and opaque. Known figures: **D&B Hoovers from ~$10,000/yr** (bundles $25k-$50k+); **D&B Credit Insights Plus ~$149/mo**. Direct+ API priced per volume/entitlement (not publicly disclosed).

## 2. Data-domain coverage
- Company reference/firmographics: core strength — 500M-600M+ business records with the D-U-N-S identifier.
- Beneficial ownership: corporate linkage (parent/subsidiary/branch/global-ultimate) is best-in-class; UBO/compliance data available.
- KYC/identity: KYC/AML-ready compliance data and third-party risk products.
- Sanctions/PEP/adverse-media: available via compliance/third-party-risk suite (Risk Analytics / Compliance).
- Private-company sourcing: partial — B2B sales intelligence via D&B Hoovers.
- Credit/risk scores: core strength — Paydex, Failure/Delinquency scores, financial-stress and viability ratings.

## 3. Datasets
- 500M+ (per DUNS lookup) to 600M+ business records; corporate-family linkage across global ultimates. 255+ countries/territories. History depth spans decades of trade-payment and credit observations. Proprietary **D-U-N-S nine-digit ID** is the anchoring entity key and de-facto industry standard. Sourcing: trade references, public registries, partner data, direct investigation, and the D&B Data Cloud master database. ISO 27001 certified; GDPR/CCPA compliant.

## 4. APIs & technical integration
- Primary developer surface: **D&B Direct+**, a RESTful API platform (match/enrich/monitor/stream) authenticated via **OAuth 2.0** access tokens; JSON responses. Connect API matches input records to a D&B entity for enrichment. Also bulk/batch data delivery, monitoring/notification feeds, and data-block entitlements. Snowflake/marketplace and file-based delivery available for enterprise. No public MCP server known. Both batch and real-time supported.

## 5. Enabling technology
- Entity resolution and match-grade confidence scoring against the DUNS master; corporate-hierarchy/linkage graph; analytics/predictive scores (failure, delinquency, viability); master-data-management tooling; compliance/third-party-risk screening; data-quality and monitoring operations across the Data Cloud.

## 6. Customer / user feedback
- G2: Dun & Bradstreet products ~**4.3/5 across ~1,553 reviews**; **D&B Hoovers ~4.1/5 (~781 reviews)**. Pros: comprehensive firmographics, best-in-class corporate hierarchy, accurate/authoritative credit reports; risk & finance teams rate it highly. Cons: opaque pricing, aggressive auto-renewal terms, stale/aging contact records, steep learning curve ("complicated"), and no real-time buying signals. User segments: credit/risk, procurement/supply, compliance/third-party-risk, master data, and B2B sales/marketing.

## 7. Edge & positioning
- Leads on breadth of firmographics, universal DUNS identifier, corporate linkage and commercial credit scoring — the default backbone for supplier/customer master data and credit-risk decisioning. Lags on freshness of contact data, intent/real-time signals, pricing transparency and UX. Best-for: enterprise credit-risk, supplier/third-party-risk and B2B master-data enrichment at global scale.

## 8. Provenance
- https://www.dnb.com/en-us/products/dnb-direct-plus.html — Direct+ API product page (accessed 2026-08-11)
- https://www.dnb.com/en-us/smb/duns/duns-lookup.html — DUNS number & 500M+ businesses (accessed 2026-08-11)
- https://www.g2.com/products/dun-bradstreet-d-b-hoovers/reviews — G2 D&B Hoovers ratings (accessed 2026-08-11)
- https://tomba.io/blog/dun-bradstreet-pricing-reviews-pros-and-cons — pricing and pros/cons (accessed 2026-08-11)
- https://syncgtm.com/blog/dun-bradstreet-review — independent enterprise-data review (accessed 2026-08-11)
- https://lseg.com/en/data-analytics/products/workspace/updates/d-u-n-s-numbers-are-now-integrated-into-lseg-workspace — DUNS as industry identifier (accessed 2026-08-11)
- https://www.postman.com/api-evangelist/dun-bradstreet/overview — Direct+ API collection/auth (accessed 2026-08-11)
