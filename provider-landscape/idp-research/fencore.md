# Fencore

## 1. Snapshot
- **Category:** Cloud-native, no-code enterprise data management (EDM) platform for the buy-side — Fencore DataHub masters reference, market and investment data, with reconciliation, migration and regulatory-reporting use cases.
- **Owner / parent:** Independent, privately held. Founded 2019, headquartered in Singapore; founding team drawn from established EDM/data-management backgrounds. Small but growing; not publicly traded.
- **HQ / footprint:** Singapore HQ servicing clients globally — one of very few genuine IDP/EDM peers actually headquartered in APAC, a differentiator for an APAC-based buyer needing in-region time-zone support.
- **Initial fit:** High as a data-management master (the layer that feeds Databricks); moderate overall because it is a data-management platform, not a book-of-record, and its Databricks-specific and AI capabilities are unconfirmed in public sources.
- **Positioning:** "No-code data management for the investment industry" — empower business users (not engineers) to build masters, reconcile and govern investment data through drag-and-drop, cloud-native tooling.
- **Recent developments:** As of 5 Nov 2026 the DataHub product page says governed data can be 'consumed via MCP, APIs, Python, FenWarehouse' and that the Cori assistant can use a Fencore internal model or a customer-configured provider (vendor, search-only); no MCP documentation, named customer, ANZ office, SOC 2 or published ISO 27001 certificate found; PitchBook puts headcount at ~10.

## 2. Investment-domain mastering
DataHub is built to manage reference, market and investment data and to build **masters** across a wide range of use cases — golden-copy construction, cross-referencing, data optimisation and migration. Security/instrument and issuer/entity mastering are core to the product's purpose. Explicit identifier-concordance breadth (ISIN/SEDOL/CUSIP/FIGI) and corporate-action mastering depth are plausible for an EDM of this class but are not itemised in public sources; confirm through RFI. Coverage is client-populated rather than vendor-supplied content.

## 3. Databricks & open architecture
Fencore is cloud-native with a stated focus on **interoperability** and API-based integration, and stores raw, historical and export snapshots. However, a Databricks-specific integration — Delta/Open Sharing, Unity Catalog interoperability, zero-copy access, governed bidirectional write-back — is **not evidenced** in public material. For a Databricks-first buyer this is an open, must-confirm question; treat as not established rather than assumed. Its no-code, API-forward design is architecturally sympathetic to a composed, open stack.

**Nov 2026 update:** the vendor site now positions DataHub as the 'operating layer' over Snowflake, Microsoft Fabric and Databricks, with Snowflake shown as a partner logo; no Delta Sharing, Unity Catalog, zero-copy, write-back or marketplace listing is described.

**5 Nov 2026 update:** the FenWarehouse page describes Snowflake as the default warehouse; Databricks remains positioning only, with no Databricks partner or marketplace listing and no Delta Sharing found (vendor pages, search-only).

## 4. IBOR & investment modelling
Fencore is a **data-management platform, not an investment book of record**. It stores automatic raw, historical and export snapshots (a form of point-in-time data retention) but does not claim an event-driven, bi-temporal position/accounting engine. Point-in-time reconstruction of *positions* would depend on an IBOR elsewhere in the stack; Fencore's role is mastering and reconciling the underlying data.

## 5. Data quality & investment operations
This is Fencore's clearest strength. DataHub ships full auditing, **data lineage from source to target**, out-of-the-box **four-eyes approval**, exception-management dashboards and automated snapshot storage — the operational-control surface an EDM buyer expects, delivered through a no-code UI aimed at business users rather than developers.

## 6. Public/private total portfolio
Fencore explicitly positions across **public and private markets** as a single data-management platform, which is relevant to a total-portfolio ambition. Depth of private-markets document ingestion, GP look-through and cash-flow handling is not detailed publicly; confirm through RFI.

## 7. AI & agent readiness
No AI/LLM or MCP/agent-interface capability is evidenced in public sources. The no-code transform layer is rules/UI-driven rather than model-driven on the current public evidence. Treat AI readiness as unproven pending vendor confirmation.

**Nov 2026 update:** the vendor site markets **Cori**, a governed in-product AI assistant that drafts dictionaries, pipelines and masters from natural language, with user review before changes apply. GA status, underlying LLM, buyer-own-LLM option and any MCP or agent interface are not stated (vendor marketing only).

**5 Nov 2026 update:** the DataHub product page now states governed data can be 'consumed via MCP, APIs, Python, FenWarehouse' and supports 'external AI and agents'; Cori uses allow-listed tools, inherits user permissions, and runs on 'a Fencore internal model' or a provider the customer configures. No MCP technical documentation, identity-propagation (e.g. Entra ID) design, tool-call audit or AI data-use/no-training terms were found publicly. An external consultant's shortlisting (Sep 2026) reports a vendor-run demo of an external LLM querying DataHub through MCP with entitlement enforcement; that is demo evidence, not public, and should be re-tested in a proof of value. Status: vendor marketing (capped 2.0).

## 8. Time-to-value, implementation, managed services & APAC support
The **no-code, business-user** model is the time-to-value pitch — configuration by data operations staff rather than an engineering project. Singapore HQ gives genuine **APAC time-zone coverage and regional support**, a material advantage over EMEA/US-centric incumbents for an APAC buyer. As a young vendor, reference depth and large-scale implementation track record are the key diligence risks.

**Nov 2026 update:** the 2024 brochure lists teams in Singapore and the UK with 'additional market coverage in Hong Kong and Australia'; New Zealand is not mentioned and no named ANZ client or partner was located.

## 9. Commercials, TCO, exit & vendor viability
SaaS/subscription commercial model; specific pricing is not public. As a **2019 startup**, vendor viability, financial durability and reference base are the dominant risks for a ~$35bn institutional buyer and would need careful diligence (financials, client references, escrow/exit terms). Cloud-native, API-based design is favourable for portability, but exit terms are unconfirmed.

**Nov 2026 update:** ISO 27001 certification is claimed on the solution page (certificate not seen); NCC Group is the named escrow provider (May 2023). CB Insights shows only a convertible note and accelerator investors; no 2024–26 funding round or headcount was located.

**5 Nov 2026 update:** PitchBook lists ~10 employees and a single seed round (~USD 373k; Tenity, Engine); the legal entity is FENCORE PTE. LTD. (UEN 201900822Z, registered 2019-01-07, ACRA mirror) with a one-employee UK subsidiary (incorporated 2023). Fencore joined the EDM Council (undated); its partner Empaxis was acquired by Communify Fincentric (Oct 2025). No analyst coverage, awards or 2024–26 funding round found. Viability and key-person risk remain the dominant diligence item for any multi-year commitment.

## 10. Evidence, maturity & provisional scores
Evidence class is largely **vendor-authored / directory listings** (Fencore site, The Wealth Mosaic, fintech directories) — no independent analyst coverage or public customer reviews were found, so scores are **evidence-capped** and conservative. Hard gates: data-ops/lineage/four-eyes read as partial-to-pass on the strength of the product description; Databricks-open-sharing, native IBOR, AI/agent and vendor-scale gates read as **unknown or fail** on current public evidence. Provisional domain read: strong on data quality/operations and self-service, moderate on mastering and total-portfolio breadth, weak/unproven on Databricks-native integration, IBOR, AI and vendor viability. **Stage-1 paper screen — not a selection of record.** In-sandbox egress is restricted, so figures are triangulated from the search index and flagged as open RFI items.

**Hard-gate read:**
- G01 native equities/ETF/govvies/credit/FX/PE: PARTIAL
- G02 security+entity+price mastering: PASS — security/entity mastering is the core DataHub product (Nov 2026)
- G03 intraday position/price + near-real-time txns: PARTIAL
- G04 5yr history + point-in-time: PASS
- G05 IDP-as-master while Databricks consumes: UNKNOWN
- G06 open/native Databricks integration: FAIL
- G07 bidirectional API: UNKNOWN
- G08 business users extend model w/o vendor coding: PASS — no-code configuration by business users is the core proposition (Nov 2026)
- G09 buyer can use own LLMs: PARTIAL — vendor page says customer-configured model providers are supported; terms unpublished (5 Nov 2026)
- G10 permission-aware MCP/agent interface: PARTIAL — vendor page states MCP consumption with inherited permissions; no technical documentation (5 Nov 2026)
- G11 field-level provenance/lineage/override/audit: PASS — source-to-target lineage, four-eyes and audit documented (Nov 2026)
- G12 full export on exit: UNKNOWN
- G13 AI/LLM data-use rights governable: UNKNOWN — no published AI data-use terms (Nov 2026)
- G14 credible APAC+ANZ support: PARTIAL — Singapore HQ with Australia market coverage; no named ANZ client (Nov 2026)
- G15 30–60 day PoV: UNKNOWN
- G16 3–6 month production foundation: PARTIAL
- G17 07: UNKNOWN
- G18 internal ops retains exception/override control: PASS — four-eyes and override workflows run by client operations (Nov 2026)
- G19 institutional security architecture: PARTIAL — ISO 27001 claimed; SOC 2 not evidenced (Nov 2026)
- G20 5-yr TCO transparency: FAIL
- G21 critical function not roadmap-dependent: PARTIAL — core EDM shipping; AI assistant status unstated (Nov 2026)
- G22 controlled write-back to downstream systems: PARTIAL

**Evidence re-checked 2026-11-03 (v3 refresh).** Scores remain provisional (Stage-1 paper screen) until a proof of value runs; see `_v3_updates.md`.

## 11. Sources
- Fencore — company site & DataHub product: https://www.fencore.co/ (accessed 2026-08-15)
- Fencore — solution overview: https://fencore.co/solution/ (accessed 2026-08-15)
- The Wealth Mosaic — Fencore DataHub profile: https://www.thewealthmosaic.com/vendors/fencore/fencore-datahub/ (accessed 2026-08-15)
- Fintech News Singapore — Fencore directory listing: https://fintechnews.sg/list-fintech-startup-singapore-fintech-companies-directory/fintech/fencore/ (accessed 2026-08-15)
- CB Insights — Fencore company profile: https://www.cbinsights.com/company/fencore (accessed 2026-08-15)
- Crunchbase — Fencore profile: https://www.crunchbase.com/organization/fencore (accessed 2026-08-15)
- https://www.fencore.co/about/ — Fencore about (Fencore; accessed 2026-11-03) [vendor · Vendor marketing · undated · opened]
- https://imas.org.sg/fintech-directory/marketing/9Rnv8_Fencore%20Main%20Brochure%202024.pdf — Fencore Main Brochure 2024 (Fencore via IMAS fintech directory; accessed 2026-11-03) [vendor · Vendor marketing · 2024 · opened]
- https://www.fencore.co/company — Fencore company/team (Fencore; accessed 2026-11-03) [vendor · Vendor marketing · undated · opened]
- https://app-escode-prod-79.azurewebsites.net/resources/fencore-partners-with-escode-to-provide-operational-resilience/ — Fencore Partners with Escode to Provide Operational Resilience (Escode (NCC Group); accessed 2026-11-03) [vendor · News · 2023-05-01 · opened]
- https://www.cbinsights.com/company/fencore/customers — Fencore customers (CB Insights; accessed 2026-11-03) [independent · Independent research · undated · opened]
- https://investopsasia.wbresearch.com/sponsors/fencore — Fencore - InvestOps Asia sponsor (WBR; accessed 2026-11-03) [vendor · Vendor marketing · undated · opened]
- https://www.fencore.co/products/datahub/full — DataHub product page (MCP consumption, Cori, 75+ integrations) (Fencore; accessed 2026-11-05) [vendor · Vendor marketing · undated · search-only]
- https://www.fencore.co/products/fenwarehouse — FenWarehouse (Snowflake default) (Fencore; accessed 2026-11-05) [vendor · Vendor marketing · undated · search-only]
- https://pitchbook.com/profiles/company/493732-81 — Fencore company profile (~10 employees, seed funding) (PitchBook; accessed 2026-11-05) [independent · Independent research · undated · search-only]
- https://www.acrawatch.sg/company/fencore-pte-ltd — FENCORE PTE. LTD. registration (AcraWatch, ACRA mirror; accessed 2026-11-05) [independent · Official filings · undated · search-only]
- https://corpsignals.uk/companies/uk/fencore-uk-ltd-15096324.html — Fencore UK Ltd (Companies House mirror; accessed 2026-11-05) [independent · Official filings · undated · search-only]
- https://edmcouncil.org/announcement/edm-council-welcomes-fencore-as-its-newest-member/ — EDM Council welcomes Fencore (EDM Council; accessed 2026-11-05) [independent · News · undated · search-only]
- https://www.businesswire.com/news/home/20251016273143/en — Communify Fincentric acquires Empaxis (Business Wire; accessed 2026-11-05) [vendor · News · 2025-10-16 · search-only]
