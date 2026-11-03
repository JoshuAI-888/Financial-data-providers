# AlphaCert

## 1. Snapshot
- **Category:** Investment data management platform for asset managers and asset owners — modular data unification, reconciliation, performance and regulatory-reporting tooling built specifically for the buy-side.
- **Owner / parent:** AlphaCert Labs Limited, independent, privately held. Founded and headquartered in Auckland, New Zealand. Small firm (~26 staff, ~US$1.8m revenue as of late 2025) with staff across Oceania, Asia and Europe.
- **HQ / footprint:** Auckland, NZ — a genuine **ANZ home-market vendor**. Partnership with Refinitiv (LSEG) to serve NZ/Australian investment managers; trusted by a very large superannuation fund.
- **Initial fit:** Moderate as a **regional specialist** — strongest possible on APAC/ANZ support and local regulatory reporting — but with a small-vendor viability caveat and unconfirmed Databricks-native integration for a ~$35bn buyer.
- **Positioning:** "Simplify the complex world of investment data" — automate investment data operations, reduce operational cost and risk, and keep funds compliant with evolving (notably ANZ) regulation.
- **Recent developments:** Nov 2026 re-check: named clients on the vendor site include AustralianSuper, Nambawan Super and Milford, with ISG and IIS case studies; AI is marketing/roadmap only; no Databricks integration, MCP, funding or M&A found; the APRA SRS 550 reporting claim could not be verified.

## 2. Investment-domain mastering
At the core, AlphaCert **unifies, cleanses and transforms** data feeds from custodian banks, global and local market-data providers and internal teams into consistent investment data. It provides a data foundation (security/holdings/transaction data) rather than a full accounting master; identifier concordance and corporate-action mastering depth are not itemised publicly and should be confirmed. Strength is breadth of custodian/administrator feed integration ("plug-and-play data feeds across most global providers").

## 3. Databricks & open architecture
AlphaCert uses "industry-standard data architecture with **APIs** for seamless integration" and scalable cloud architecture. A Databricks-specific path — Delta/Open Sharing, Unity Catalog, zero-copy — is **not evidenced** publicly and is an open RFI question. The API-first, feed-integration design is architecturally compatible with delivering mastered data into a downstream analytical estate.

## 4. IBOR & investment modelling
AlphaCert is a **data-management, reconciliation and analytics** platform rather than an event-driven investment book of record. It supports performance and exposure analytics over reconciled data; bi-temporal point-in-time position reconstruction is not claimed and would depend on an IBOR elsewhere. Treat native IBOR as absent.

## 5. Data quality & investment operations
This is AlphaCert's core strength. A dedicated **Reconciliation Module** delivers comprehensive daily investment-data reconciliations (custodian vs. administrator vs. internal), and the platform targets DQ automation, exception handling and audit-ready outputs — squarely the operational-control problem an asset owner faces day to day.

## 6. Public/private total portfolio
AlphaCert serves multi-asset fund data for managers and asset owners. Explicit private-markets look-through / GP data handling is not detailed publicly; confirm depth through RFI. Total-portfolio breadth is moderate on current evidence.

## 7. AI & agent readiness
No AI/LLM or MCP/agent capability is evidenced in public sources. Treat AI/agent readiness as unproven.

**Nov 2026 update:** vendor articles (undated, 2026) describe AI-driven ESG insights on unstructured data using Microsoft Azure OpenAI and AI-agent exception alerts as a use case. There is no AI product, MCP server, buyer-own-LLM or permission-aware AI evidence — roadmap/marketing only.

## 8. Time-to-value, implementation, managed services & APAC support
**Strongest in the set on APAC/ANZ fit.** Auckland HQ, ANZ time-zone support, Refinitiv-partnered regional data, and claimed (not yet verified) regulatory-reporting support for **APRA SRS 550** (Australia) and **FMA QFU** (New Zealand) make it uniquely tuned to an ANZ institutional buyer's regulatory reality. Plug-and-play feeds support relatively fast onboarding within its focused scope.

**Nov 2026 update:** the vendor home page names AustralianSuper, Nambawan Super, Milford, ISG/Devon Funds, i-select, Clarity and Kernel Funds as clients, with case studies for ISG (client since 2019) and Implemented Investment Solutions. Vendor pages do not evidence APRA SRS 550 reporting; the ISG case study mentions QFU data use only in passing, so the regulatory-reporting claim above should be confirmed by RFI. Note: Milford is a named client, so AlphaCert may already be an incumbent for the buyer.

## 9. Commercials, TCO, exit & vendor viability
Likely competitive commercials for its focused scope (pricing not public). **Vendor viability is the dominant risk**: ~26 staff and ~US$1.8m revenue is very small for a ~$35bn manager's strategic platform — concentration, key-person and financial-durability risks require serious diligence, references and contractual protections (source-code escrow, exit assistance). Focused scope aids portability but exit terms are unconfirmed.

**Nov 2026 update:** directories (ZoomInfo, TheOrg) list 11–50 staff, revenue under US$5m and a single Auckland office; CEO Phil Pietersen also leads ClearPoint Ltd (key-person point for diligence). No investor or M&A found.

## 10. Evidence, maturity & provisional scores
Evidence class is largely **vendor-authored plus directory/partner references** (AlphaCert site, Refinitiv/CFOtech partnership coverage, business directories); no independent analyst or broad review-site coverage was found, so scores are **evidence-capped** and conservative. Hard gates: reconciliation/data-ops and ANZ regulatory-reporting gates read pass-to-partial; native IBOR, Databricks-open-sharing, AI/agent and **vendor-scale/viability** gates read fail/unknown. Provisional domain read: strong on data quality/reconciliation and (qualitatively) APAC support and regional governance; weak on IBOR, Databricks-native integration, AI and vendor viability. **Stage-1 paper screen — not a selection of record.** In-sandbox egress is restricted; figures are triangulated from the search index and flagged as open RFI items.

**Hard-gate read:**
- G01 native equities/ETF/govvies/credit/FX/PE: PARTIAL
- G02 security+entity+price mastering: PARTIAL — investment data management with ODS/RDS; golden-record mechanics not itemised (Nov 2026)
- G03 intraday position/price + near-real-time txns: FAIL — daily provider-file batch model evidenced; no intraday (Nov 2026)
- G04 5yr history + point-in-time: UNKNOWN — history held; point-in-time model not evidenced (Nov 2026)
- G05 IDP-as-master while Databricks consumes: UNKNOWN
- G06 open/native Databricks integration: FAIL
- G07 bidirectional API: UNKNOWN
- G08 business users extend model w/o vendor coding: PARTIAL
- G09 buyer can use own LLMs: UNKNOWN — no AI product (Nov 2026)
- G10 permission-aware MCP/agent interface: FAIL — no MCP/agent interface (Nov 2026)
- G11 field-level provenance/lineage/override/audit: PARTIAL — audit-ready reconciliation; field-level lineage not detailed (Nov 2026)
- G12 full export on exit: UNKNOWN
- G13 AI/LLM data-use rights governable: UNKNOWN — no published AI data-use terms (Nov 2026)
- G14 credible APAC+ANZ support: PASS — Auckland HQ; AustralianSuper, Nambawan, Milford and other ANZ clients named (Nov 2026)
- G15 30–60 day PoV: UNKNOWN
- G16 3–6 month production foundation: PARTIAL
- G17 07: UNKNOWN — no SLA evidence (Nov 2026)
- G18 internal ops retains exception/override control: PARTIAL
- G19 institutional security architecture: PARTIAL
- G20 5-yr TCO transparency: FAIL
- G21 critical function not roadmap-dependent: PARTIAL — core reconciliation/data platform mature; AI roadmap only (Nov 2026)
- G22 controlled write-back to downstream systems: UNKNOWN

**Evidence re-checked 2026-11-03 (v3 refresh).** Scores remain provisional (Stage-1 paper screen) until a proof of value runs; see `_v3_updates.md`.

## 11. Sources
- AlphaCert — company site: https://alphacert.com/ (accessed 2026-08-15)
- AlphaCert — investment data management platform: https://alphacert.com/investment-data-management (accessed 2026-08-15)
- AlphaCert — why AlphaCert: https://alphacert.com/why-alphacert (accessed 2026-08-15)
- AlphaCert — simplifying daily investment data reconciliations: https://alphacert.com/insights/simplifying-investment-data-reconciliations (accessed 2026-08-15)
- CFOtech NZ — AlphaCert & Refinitiv partnership: https://cfotech.co.nz/story/alphacert-refinitiv-bring-data-to-better-investment-decisions (accessed 2026-08-15)
- Capterra NZ — AlphaCert pricing/reviews/features: https://www.capterra.co.nz/software/192616/alphacert (accessed 2026-08-15)
- https://alphacert.com/customer-stories/transforming-data-management-for-investment-operations-with-isg — ISG customer story (AlphaCert; accessed 2026-11-03) [vendor · Named customer case study · undated · opened]
- https://alphacert.com/customer-stories/better-cashflow-management-for-iis-with-a-data-platform-for-growth — IIS customer story (AlphaCert; accessed 2026-11-03) [vendor · Named customer case study · undated · opened]
- https://alphacert.com/insights/quick-wins-scalable-growth-ai-ready-investment-data — Quick Wins. Scalable Growth. AI-Ready Investment Data. (AlphaCert; accessed 2026-11-03) [vendor · Vendor marketing · undated · opened]
- https://alphacert.com/insights/the-ai-impact-within-the-investment-management-industry — The AI impact within the investment management industry (AlphaCert (author S. Huppert); accessed 2026-11-03) [vendor · Vendor marketing · undated · opened]
- https://alphacert.com/insights/reflections-from-investops-europe-2026-on-t1-investment-data-and-modular-architecture — Reflections from InvestOps Europe 2026 (AlphaCert; accessed 2026-11-03) [vendor · Vendor marketing · 2026-09 · opened]
- https://zoominfo.com/c/alphacert-labs-ltd/372942869 — AlphaCert Labs (ZoomInfo; accessed 2026-11-03) [independent · Independent research · undated · opened]
- https://theorg.com/org/alphacert/org-chart/phil-pietersen — Phil Pietersen (TheOrg; accessed 2026-11-03) [independent · Independent research · undated · opened]
- https://alphacert.com/insights — AlphaCert insights index (incl. IDT Summit Sydney 2025, Macro Trends in Australian Investment Management) (AlphaCert; accessed 2026-11-03) [vendor · Vendor marketing · undated · opened]
- https://www.trustradius.com/products/alphacert/details — AlphaCert on TrustRadius (TrustRadius; accessed 2026-11-03) [independent · Independent research · undated · search-only]
