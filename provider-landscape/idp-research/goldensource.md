# GoldenSource

## 1. Snapshot
- **Category:** Enterprise/reference data management (EDM/MDM) — security, entity, price and product mastering — with a new AI/data-intelligence layer (Scout).
- **Owner / parent:** Private, PE-backed. Acquired by mid-market PE firm Gemspring Capital in May 2022; new CEO James Corrigan appointed September 2024 to lead cloud/buy-side growth. Reported scale varies by source (~400–650 employees, ~$25–100m revenue estimates) — precise current figures not established from public sources.
- **HQ / footprint:** New York HQ (founded 1984 as Financial Technologies International). Five APAC offices including a dedicated Melbourne, Australia office (Level 31, 120 Collins St) plus Singapore, Hong Kong, Beijing and Mumbai — the most substantial ANZ/APAC physical footprint of the three vendors reviewed.
- **Initial fit:** High
- **Positioning:** Long-pedigree, cloud-agnostic security/entity master with a real Melbourne office and an MCP-based agentic layer (Scout) that is furthest along of the three vendors in explicitly naming MCP — but Scout is very recently launched (June 2026) and unproven at named-reference scale.

## 2. Investment-domain mastering
GoldenSource's core is security, entity/issuer and price/product mastering. Security Master unifies multi-source data (Bloomberg, LSEG, ICE, custodians, exchanges) into a centralised model with validation and governance; Entity Master consolidates legal-entity, client, account, product and issuer records, linking multiple identifiers and roles per entity (supporting KYC/AML/FATCA/MiFID II use cases). Each security/entity is stated to be "mastered once," with reference links back to vendor identifiers, embedded validation/lineage/workflow rules, and "plug-and-play" vendor connections. V10 (launched 2024, reaffirmed as the current architecture in 2026 material) is described as cloud-agnostic (AWS/Azure/GCP), microservices-based, with AI-supported documentation/search, automated pipelines, improved lineage/metadata extraction and new ESG connectors. Point-in-time/bitemporal history depth and business-user no-code extensibility are asserted but not independently itemised in public material.

## 3. Databricks & open architecture
GoldenSource has the most explicit, if dated, public open-architecture signal of the three: its 2022 Cloud Data Services launch states pre-configured vendor connections and toolkits let clients "transform and use data in their preferred warehouse, including Cloudera, Snowflake, Databricks and Google Cloud Platform" — a direct, named Databricks reference, though from 2022 and not confirmed as a current native Delta Sharing/Unity Catalog integration. A separate Snowflake-native onboarding app was also launched. AWS Marketplace listing exists for GoldenSource EDM in the cloud. No public evidence of a current Databricks Marketplace/Partner Connect listing or Delta Sharing/OpenSharing protocol support specifically was found — treat "Databricks-native" as **directionally credible but not confirmed current-state**, to be tested in RFP/PoV.

## 4. IBOR & investment modelling
GoldenSource IBOR (built on MAIA Technology, combined with the GoldenSource Nexus data warehouse) is marketed as a "real-time," event-based investment book of record that updates valuations as transactions and prices publish, giving PMs/allocators/risk managers intraday position and exposure visibility without time lag. This is a more explicit, dedicated IBOR capability claim than either NeoXam's general xBOR framing or Gresham's mastering-only positioning. Trade-date vs settlement-date handling and full point-in-time reconstruction mechanics are not detailed beyond the "responsive intra-day IBOR" description.

## 5. Data quality & investment operations
Reference-data mastering embeds validation, scrubbing and standardisation rules with lineage tracking as data is ingested. A fully managed SaaS option ("EDM Now") is offered with vendor monitoring, SLA-backed data quality and onboarding support explicitly aimed at firms with lean internal IT — directly relevant to this buyer's ~40-user internal-ops model. A pre-configured Bloomberg template (800+ standardised fields across equities and fixed income) ships ready-to-use, reducing onboarding effort. Exception workflow, four-eyes/override mechanics and reconciliation depth (position/transaction/cash/corporate-action) specific to GoldenSource are not itemised as thoroughly in public material as Gresham's Control Cloud, and should be probed directly in RFP.

## 6. Public/private total portfolio
Public-source evidence of a dedicated private-markets/GP-LP module (commitments, capital calls, distributions, NAV, look-through, document ingestion) comparable to NeoXam's private-markets IDP or Gresham's GP/LP messaging was **not found** for GoldenSource in this research — this is a **coverage gap** requiring direct RFP confirmation, not a confirmed absence.

## 7. AI & agent readiness — PREVIEW, NEWLY LAUNCHED
GoldenSource Scout launched 23 June 2026 as a "Trusted Contextual Data Layer," delivered as purpose-built agents (initial release: data investigation, exception management, lineage tracing) accessible via a chat interface and, notably, **an agent-building tool that explicitly uses the Model Context Protocol (MCP)** for cross-platform connectivity/automation. Scout runs on Amazon Bedrock and is stated to be "purpose-built to meet the rigorous requirements for data security, access controls and auditability that financial services firms demand." This is the most explicit MCP claim among the three vendors reviewed and directly relevant to G10. However: Scout is roughly two months old at the time of this assessment, positioned partly as a market-trust response (a cited InvestOps 2026 stat: 98% of firms worry poor data causes bad AI outputs), with no named production client, no independently verified model-independence statement, and no documented per-agent identity/entitlement or write-approval detail beyond the general Bedrock/audit framing — treat as **early-GA-or-preview**, not a mature, referenceable production capability.

## 8. Time-to-value, implementation, managed services & APAC support
Pre-built Bloomberg template (800+ fields), "plug-and-play" vendor connections, EDM Now managed SaaS, and dedicated GoldenSource Professional Services for setup/migration/integration/training/go-live all point to a config-over-code, accelerated-onboarding posture. APAC support is the strongest of the three vendors on paper: five APAC offices including a dedicated Melbourne, Australia office — though named ANZ client references were not found in this research and should be requested directly. 30–60 day PoV and 3–6 month foundation timelines are not established from public sources.

## 9. Commercials, TCO, exit & vendor viability
No public pricing, platform-vs-content separation, egress/API charges, or exit/data-portability terms were found. Vendor viability: mid-market PE-backed (Gemspring, since 2022) with a 2024 CEO change signalling a deliberate cloud/buy-side growth push; company-size estimates vary meaningfully across data sources (400–650 employees, $25–100m revenue), suggesting GoldenSource is smaller and less independently well-documented than NeoXam or the combined Gresham — a factor for viability due diligence, though a 40+ year operating history (since 1984) is a stability signal in the other direction.

## 10. Evidence, maturity & provisional scores

**Hard-gate read (G01–G22):**
- G01 (native equities/ETF/govvies/credit/FX/PE): PARTIAL — strong public-market coverage, PE module not evidenced
- G02 (security+entity+price mastering): PASS — core, long-standing capability
- G03 (intraday position/price, near-real-time txns): PASS — GoldenSource IBOR explicitly event-based/real-time
- G04 (5yr history + point-in-time): PARTIAL — lineage/metadata claimed, depth undocumented
- G05 (IDP-as-master, Databricks consumes): PARTIAL — Databricks named (2022) but currency unconfirmed
- G06 (open/native Databricks integration): PARTIAL — named integration exists, not confirmed current/native
- G07 (bidirectional API): PARTIAL — APIs referenced generally, write-back specifics undocumented
- G08 (business users extend model, no vendor code): UNKNOWN — asserted, not evidenced
- G09 (buyer can use own LLMs): UNKNOWN — Scout runs on Bedrock; model-choice flexibility undocumented
- G10 (permission-aware agent/MCP interface): PARTIAL — MCP explicitly named for Scout, but two months old, unreferenced
- G11 (field-level provenance/lineage/override/audit): PARTIAL — lineage/audit claimed for both EDM and Scout
- G12 (full export on exit): UNKNOWN — not established from public sources
- G13 (governable AI/LLM data-use rights): UNKNOWN — not established from public sources
- G14 (credible APAC + ANZ support): PASS — dedicated Melbourne office, 5 APAC offices (no named ANZ client found)
- G15 (30–60 day PoV): UNKNOWN — not established from public sources
- G16 (3–6 month production foundation): UNKNOWN — not established from public sources
- G17 (07:00 validated-portfolio SLA): UNKNOWN — not established from public sources
- G18 (internal ops retains exception/override control): PARTIAL — EDM Now managed-service framing implies shared control model
- G19 (institutional security architecture): PARTIAL — Bedrock/audit claims for Scout, general only for core EDM
- G20 (5-yr TCO transparency): UNKNOWN — no public pricing
- G21 (critical function not roadmap-dependent): PASS — mastering/IBOR shipping; only Scout is newly launched
- G22 (controlled write-back to downstream): UNKNOWN — not established from public sources

**Provisional 0–5 scores (evidence-capped; no PoV performed, ceiling 4, 4 only with named production reference):**
- Domain 1 (Investment data mastering): 3.0 (evidence: official docs)
- Domain 2 (Databricks & open architecture): 2.0 (evidence: official docs — named but dated Databricks claim)
- Domain 3 (Time to value & implementation): 2.5 (evidence: official docs — Bloomberg template, managed SaaS)
- Domain 4 (Data quality & investment operations): 2.5 (evidence: official docs, less exception-workflow detail than Gresham)
- Domain 5 (Public/private total portfolio): 0.5 (evidence: absence of evidence — no PE module found)
- Domain 6 (IBOR & investment modelling): 3.0 (evidence: official docs — explicit event-based IBOR claim)
- Domain 7 (AI & agent readiness): 1.5 (evidence: official docs/preview — MCP named but two months old, unreferenced)
- Domain 8 (Data coverage/currency/history): 2.5 (evidence: official docs)
- Domain 9 (Integration & user self-service): 2.0 (evidence: official docs — APIs general, plug-and-play connectors)
- Domain 10 (Governance/security/data rights): 2.0 (evidence: official docs — Bedrock/audit claims for Scout only)
- Domain 11 (Commercials/TCO/exit): 1.0 (evidence: sales — no public terms)
- Domain 12 (Vendor viability/roadmap/support): 2.5 (evidence: official docs — 40-yr history offset by smaller/uncertain scale, no named production reference for Scout)

**Overall read:** GoldenSource leads on APAC/ANZ physical footprint (a dedicated Melbourne office), an explicit event-based IBOR claim, and the most direct MCP reference of the three vendors via Scout. It lags on private-markets/PE-specific tooling (no evidence found) and on AI-readiness maturity in practice — Scout is barely two months old with no named production reference. Biggest risk: buying ahead of proof on Scout's MCP/agent claims, and a comparatively thin, variably-reported company scale versus NeoXam and the combined Gresham.

## 11. Sources
- https://www.thegoldensource.com/reference-data/ — reference data / security & entity mastering overview (accessed 2026-08-14)
- https://www.thegoldensource.com/goldensource-scout/ — Scout AI platform overview (accessed 2026-08-14)
- https://www.thegoldensource.com/goldensource-unveils-next-generation-ai-powered-data-intelligence-platform-for-financial-services/ — Scout launch detail, MCP, Bedrock, agent types (accessed 2026-08-14)
- https://www.businesswire.com/news/home/20260623321268/en/GoldenSource-Unveils-Next-Generation-AI-Powered-Data-Intelligence-Platform-for-Financial-Services — independent confirmation of Scout launch date/details (accessed 2026-08-14)
- https://a-teaminsight.com/blog/goldensource-scout-launched-to-close-data-trust-gap-using-ai/?brand=ati — independent coverage, InvestOps 2026 trust-gap stat (accessed 2026-08-14)
- https://www.thegoldensource.com/goldensource-introduces-version-10-of-data-management-platform/ — V10 cloud-agnostic architecture, AI/lineage features (accessed 2026-08-14)
- https://www.thegoldensource.com/security-master-module/ — Security Master module detail (accessed 2026-08-14)
- https://www.thegoldensource.com/goldensource-launches-new-real-time-investment-book-of-record/ — GoldenSource IBOR launch, MAIA/Nexus (accessed 2026-08-14)
- https://www.thegoldensource.com/goldensource-launches-cloud-data-services-data-lakes-warehouses/ — Databricks/Snowflake/Cloudera cloud data services (accessed 2026-08-14)
- https://aws.amazon.com/marketplace/pp/prodview-6zypovnf6jadc — AWS Marketplace listing, cloud deployment (accessed 2026-08-14)
- https://www.thegoldensource.com/data-onboarding-getting-your-entity-master-right/ — Entity Master identifiers/hierarchies (accessed 2026-08-14)
- https://www.thegoldensource.com/contact-us/melbourne-office/ — dedicated Melbourne, Australia office (accessed 2026-08-14)
- https://a-teaminsight.com/blog/goldensource-opens-singapore-office-hires-new-apac-sales-director/?brand=rti — Singapore office, APAC footprint history (accessed 2026-08-14)
- https://www.prnewswire.com/news-releases/gemspring-capital-acquires-goldensource-301548498.html — Gemspring Capital acquisition, ownership (accessed 2026-08-14)
- https://en.wikipedia.org/wiki/GoldenSource — company founding history, leadership change (accessed 2026-08-14)
