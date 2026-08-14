# Gresham Opus EDM

## 1. Snapshot
- **Category:** Enterprise data management (EDM) / reference-data mastering with adjacent reconciliation (Control Cloud) heritage; two parallel EDM product lines under one owner.
- **Owner / parent:** Private. Gresham Technologies plc was taken private by US private-equity firm STG Partners for £146.7m in 2024 (delisted from LSE, ticker GHT) and merged with STG portfolio company Alveo; the combined entity trades as "Gresham." On 12 Jan 2026 Gresham (STG-backed) acquired S&P Global's Enterprise Data Management business in a carve-out; that platform — formerly Cadis, then Markit EDM, then IHS Markit EDM, then S&P Global EDM — was renamed **Opus EDM** on 30 Mar 2026. Opus EDM now sits alongside Gresham's pre-existing **Prime EDM** (ex-Alveo) under the same ownership. Reported combined headcount ~360; Opus EDM alone claims 150+ institutional clients and >$12tn AUM supported.
- **HQ / footprint:** London HQ (combined Gresham); APAC go-to-market strengthened by a newly appointed APAC Sales Director (2026); dedicated APAC office presence/depth beyond this appointment not established from public sources.
- **Initial fit:** Moderate
- **Positioning:** Deep, long-pedigree EDM/reconciliation heritage now split across two co-owned platforms (Opus EDM and Prime EDM) mid-integration — capability breadth is real, but the buyer must resolve which product line, and how much post-acquisition roadmap uncertainty, they are underwriting.

## 2. Investment-domain mastering
Opus EDM (ex-S&P Global EDM) masters market, reference, private-markets and ESG data at scale for 150+ institutions; Prime EDM independently masters reference data "across all asset classes and operational domains within a fully normalised, extensible data model," ingesting and harmonising exchange, vendor (Bloomberg, Refinitiv/LSEG) and internal-system data into a common model with lineage/change-history tracking. Prime EDM's product/account master is delivered as a "configurable, reusable template with flexible data schema supporting multiple hierarchies" — a genuine business-configurable model rather than pure vendor-coded. Identifier concordance (ISIN/SEDOL/CUSIP/FIGI) is implied by "reference data mastering" claims but not itemised per-scheme in public material. **Critical open question for this RFP:** which of the two products — Opus or Prime — is the actual RFP subject, since their data models, extensibility mechanics and golden-record/survivorship logic are not confirmed to be identical.

## 3. Databricks & open architecture
Prime EDM explicitly states delivery of mastered data to downstream systems via "UI, REST API, R, Python and Apache Spark" — Spark-native delivery is a meaningful, if indirect, open-architecture signal for a Databricks estate (Spark is Databricks' native engine), though no explicit Delta Sharing/OpenSharing/Unity Catalog integration or Databricks partner listing was found for either Opus or Prime. Data-as-a-Service (DaaS) is offered under Prime EDM. Egress/duplication posture and replicate-vs-share-in-place approach are not established from public sources for either product line.

## 4. IBOR & investment modelling
Neither Opus EDM nor Prime EDM is positioned in public material as a dedicated IBOR engine — Gresham/Opus is fundamentally a reference/market-data mastering and reconciliation business, not a books-of-record system. Event-driven vs overnight-snapshot processing, trade-date/settlement-date handling and point-in-time position reconstruction for IBOR purposes are not established from public sources — this domain is **not a core capability** of either platform as evidenced, and should be treated as a gap unless the vendor demonstrates otherwise in RFP response.

## 5. Data quality & investment operations
This is Gresham's traditional strength. The Control Cloud reconciliation line (100+ active clients, "gold standard" positioning per vendor/press coverage) integrates positions, transactions, cash, collateral/margin, failed trades, securities lending and corporate actions in one workflow, with patented intelligent-workflow matching, a web interface for daily oversight, and a documented API for automated record extraction/update. Exception workflows include four-eyes approval, entitlements control over who can edit account/product setup, investigation history, escalations and audit trails. Prime EDM separately automates validation/reconciliation of pricing and reference data with exception management. A managed-service option ("EDM as a Service") exists. Specific SLA commitments (e.g., a 07:00 validated-portfolio time) are not established from public sources.

## 6. Public/private total portfolio
Gresham publishes specific private-markets messaging: EDM gives GPs and LPs "a single master record across funds, geographies and structures," reflecting direct private-markets client implementation experience. Opus EDM's asset coverage explicitly includes "private markets" data alongside market/reference/ESG. Commitment/capital-call/distribution/NAV modelling detail, look-through mechanics and private-document ingestion/extraction tooling (comparable to NeoXam's IDP or GoldenSource Scout) are not established from public sources — private-markets support appears to be data-mastering-level rather than a dedicated GP/LP operational module.

## 7. AI & agent readiness — ROADMAP
Opus EDM is marketed as an "AI-Ready EDM Platform," and Gresham states it plans to incorporate AI into **both** Opus and Prime EDM in 2026 — this is explicitly a roadmap commitment, not a shipped capability. No public evidence of MCP or equivalent agent-tool interfaces, per-agent identity/entitlements, provenance/citation mechanics, model independence, or write-approval controls was found for either platform. This domain must be scored at roadmap level.

## 8. Time-to-value, implementation, managed services & APAC support
Prime EDM cites "plug-and-play" connections to major vendors including Bloomberg; managed EDM-as-a-Service and DaaS options exist to reduce internal FTE burden. Post-acquisition, Gresham states existing Opus (ex-S&P) and Prime clients face "little immediate change," with both roadmaps, teams and delivery models continuing unchanged for now — reducing near-term disruption risk but leaving medium-term convergence/consolidation plans unstated. APAC support consists of a 2026 APAC Sales Director hire; no dedicated ANZ office, named ANZ client reference, or APAC delivery-team depth was found in public sources — this is a **material gap** relative to NeoXam and GoldenSource for this buyer's APAC-based requirement. 30–60 day PoV and 3–6 month foundation timelines are not established from public sources.

## 9. Commercials, TCO, exit & vendor viability
No public pricing, platform-vs-content separation, or exit/data-portability terms for Opus or Prime EDM were found. Vendor viability carries real post-acquisition integration risk: Gresham has undergone a take-private (2024), an Alveo merger, and an S&P Global EDM carve-out acquisition (Jan 2026) in under two years, all under STG Partners ownership — this is an actively consolidating platform with two overlapping EDM products and an unstated long-term convergence plan, which a buyer should treat as elevated roadmap-execution risk pending clarity.

## 10. Evidence, maturity & provisional scores

**Hard-gate read (G01–G22):**
- G01 (native equities/ETF/govvies/credit/FX/PE): PARTIAL — broad reference-data coverage, PE explicitly named for Opus
- G02 (security+entity+price mastering): PASS — long-standing core capability, both products
- G03 (intraday position/price, near-real-time txns): FAIL — not an IBOR/positions platform, no evidence
- G04 (5yr history + point-in-time): PARTIAL — lineage/change-history claimed, depth undocumented
- G05 (IDP-as-master, Databricks consumes): PARTIAL — Spark-native delivery cited, no explicit Databricks integration
- G06 (open/native Databricks integration): PARTIAL — Apache Spark delivery is a proxy signal, not confirmed native integration
- G07 (bidirectional API): PASS — REST API for automated extraction/update documented (Control Cloud)
- G08 (business users extend model, no vendor code): PARTIAL — configurable template model cited for Prime EDM
- G09 (buyer can use own LLMs): UNKNOWN — AI roadmap-stage only
- G10 (permission-aware agent/MCP interface): FAIL — no AI/agent product shipped, 2026 roadmap only
- G11 (field-level provenance/lineage/override/audit): PASS — lineage, four-eyes, audit trails documented
- G12 (full export on exit): UNKNOWN — not established from public sources
- G13 (governable AI/LLM data-use rights): UNKNOWN — not established from public sources
- G14 (credible APAC + ANZ support): FAIL — sales-director hire only, no ANZ office/reference found
- G15 (30–60 day PoV): UNKNOWN — not established from public sources
- G16 (3–6 month production foundation): UNKNOWN — not established from public sources
- G17 (07:00 validated-portfolio SLA): UNKNOWN — not established from public sources
- G18 (internal ops retains exception/override control): PASS — four-eyes, entitlements, escalation documented
- G19 (institutional security architecture): UNKNOWN — not established from public sources
- G20 (5-yr TCO transparency): UNKNOWN — no public pricing
- G21 (critical function not roadmap-dependent): PARTIAL — reconciliation/mastering shipping; AI and Databricks-native are roadmap
- G22 (controlled write-back to downstream): PASS — documented API-driven downstream update with workflow controls

**Provisional 0–5 scores (evidence-capped; no PoV performed, ceiling 4, 4 only with named production reference):**
- Domain 1 (Investment data mastering): 3.0 (evidence: official docs)
- Domain 2 (Databricks & open architecture): 1.5 (evidence: official docs — Spark delivery only, no Databricks-native proof)
- Domain 3 (Time to value & implementation): 2.0 (evidence: sales)
- Domain 4 (Data quality & investment operations): 3.5 (evidence: official docs, strong reconciliation heritage)
- Domain 5 (Public/private total portfolio): 2.0 (evidence: sales — data-level only, no GP/LP operational module evidenced)
- Domain 6 (IBOR & investment modelling): 0.5 (evidence: absence of evidence — not a core capability)
- Domain 7 (AI & agent readiness): 1.0 (evidence: roadmap — 2026 AI-enablement commitment only)
- Domain 8 (Data coverage/currency/history): 2.5 (evidence: official docs)
- Domain 9 (Integration & user self-service): 2.5 (evidence: official docs — API/Spark delivery documented)
- Domain 10 (Governance/security/data rights): 2.0 (evidence: sales)
- Domain 11 (Commercials/TCO/exit): 1.0 (evidence: sales — no public terms)
- Domain 12 (Vendor viability/roadmap/support): 1.5 (evidence: sales — active M&A integration risk, thin APAC presence)

**Overall read:** Gresham leads on reconciliation/control-room heritage and data-lineage/audit rigour, and Opus EDM's private-markets and ESG data coverage is credible on paper. It lags badly on IBOR/positions modelling (not a core capability), AI/agent maturity (2026 roadmap only) and APAC/ANZ presence (a sales hire, not an office or reference). Biggest risk: buying into an unresolved two-product (Opus vs Prime) architecture mid-post-acquisition-integration under a PE owner that has made three major corporate moves in under two years.

## 11. Sources
- https://www.greshamtech.com/press-releases/gresham-announces-acquisition-of-sp-globals-enterprise-data-management-business — S&P Global EDM acquisition announcement (accessed 2026-08-14)
- https://www.greshamtech.com/press-releases/gresham-renames-acquired-sp-global-edm-platform-as-opus-edm — Opus EDM rename, product lineage, client/AUM scale (accessed 2026-08-14)
- https://www.greshamtech.com/products/opus-edm — Opus EDM product page, AI-ready positioning, asset-class coverage (accessed 2026-08-14)
- https://www.greshamtech.com/products/prime-edm — Prime EDM product page, data model, Spark/API delivery (accessed 2026-08-14)
- https://www.greshamtech.com/products/prime-edm/data-as-a-service — Prime EDM DaaS managed-service offering (accessed 2026-08-14)
- https://www.greshamtech.com/products/control-cloud/investment-management — Control Cloud reconciliation, workflow, client scale (accessed 2026-08-14)
- https://www.greshamtech.com/press-releases/cloud-control-investment-management-launch — Control Cloud API and web-interface launch (accessed 2026-08-14)
- https://www.greshamtech.com/blog/managing-private-asset-data-complexity-how-edm-supports-gps-and-lps — private-markets GP/LP data mastering claims (accessed 2026-08-14)
- https://a-teaminsight.com/blog/bigger-is-better-says-gresham-ceo-after-acquisition-of-sp-globals-edm-business/ — independent coverage, integration commentary (accessed 2026-08-14)
- https://cfotech.co.uk/story/stg-folds-s-p-edm-into-gresham-carves-out-thinkfolio — carve-out structure, STG ownership context (accessed 2026-08-14)
- https://www.proactiveinvestors.co.uk/companies/news/1044850/gresham-technologies-accepts-offer-from-us-private-equity-firm-stg-partners-1044850.html — 2024 take-private by STG Partners (accessed 2026-08-14)
- https://www.pehub.com/stg-partners-agrees-to-take-gresham-technologies-private-in-a-147m-deal/ — take-private deal terms (accessed 2026-08-14)
- https://a-teaminsight.com/blog/alveo-and-gresham-merge-to-offer-data-services-at-significant-scale/ — Gresham/Alveo merger, combined entity (accessed 2026-08-14)
- https://pitchbook.com/profiles/company/62280-91 — combined Gresham employee/scale figures (accessed 2026-08-14)
