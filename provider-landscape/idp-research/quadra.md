# Quadra Platform

## 1. Snapshot
- **Category:** Emerging, open-standard investment data infrastructure — a vendor-neutral data layer that standardises portfolios, instruments, parties, transactions, pricing, valuations, benchmarks and performance on **FIBO** principles.
- **Owner / parent:** Quadra Platform (quadraplatform.com), an early-stage independent company. (Disambiguation: **not** the crypto OEMS at quadra.trade, nor Quadra Capital the fund manager.)
- **HQ / footprint:** Early-stage/small; limited public footprint. Positioned around open standards rather than a large installed base.
- **Initial fit:** Moderate and **watch-list / emerging** — conceptually the closest of any candidate to the buyer's own "open, inspectable, no proprietary re-platforming" architecture principle, but very early-stage and unproven at institutional scale.
- **Positioning:** "Make investment infrastructure open, inspectable, and independent of any single vendor" — a standards-based, vendor-neutral master rather than a proprietary black box.
- **Recent developments:** Nov 2026 re-check: vendor is Quadra Pty Ltd (Australia; ex-Cadis/Markit EDM/Matrix team), now marketing an 'AI-native', BSL 1.1 source-available model free for buy-side internal use and claiming Databricks/Snowflake/Fabric support; no customers, funding or MCP evidence.

## 2. Investment-domain mastering
Quadra's core claim is a standardised, conformed model spanning **portfolios, instruments, parties, transactions, pricing, valuations, benchmarks and performance**, with **security and issuer-entity resolution** and unification of positions/transactions/valuations into a single source of truth. It explicitly **reconciles data from Bloomberg, Refinitiv and custodians**. The FIBO-based ontology is a genuine differentiator for semantic consistency and regulator/counterparty alignment. Depth and production maturity are unproven; treat as promising but early.

## 3. Databricks & open architecture
Architecturally, Quadra is the **most philosophically aligned** candidate: open, inspectable, standards-based (FIBO), designed to be independent of any single vendor — the antithesis of proprietary lock-in. That said, a **specific** Databricks integration (Delta/Open Sharing, Unity Catalog, zero-copy, write-back) is not evidenced in public sources; the open model makes such integration plausible but must be confirmed. Score the *principle* favourably, the *proven integration* conservatively under evidence caps.

**Nov 2026 update:** the vendor's public sample repository README claims support for Snowflake, Databricks and Microsoft Fabric with DuckLake as the default lakehouse; the repo holds only a 20-table PostgreSQL DDL sample and the docs hub is login-gated, so Delta Sharing/Unity Catalog support is unverified (marketing claim).

## 4. IBOR & investment modelling
Quadra models valuations and performance over unified positions/transactions, but does **not** claim a bi-temporal, event-driven investment book of record. Point-in-time position reconstruction is not evidenced. Treat native IBOR as absent/unproven.

## 5. Data quality & investment operations
Reconciliation into a single source of truth (Bloomberg/Refinitiv/custodian) is a core function, implying validation and cross-source DQ. Detailed exception-management, four-eyes and tolerance mechanics are not itemised publicly; confirm through RFI.

## 6. Public/private total portfolio
The unified model spans instruments, parties and portfolios generically, which is favourable in principle for total-portfolio ambitions, but private-markets depth is unproven on public evidence.

## 7. AI & agent readiness
Not evidenced. A clean, semantically-typed FIBO model is *theoretically* well-suited to agent/LLM consumption, but no AI/MCP capability is documented; treat as unproven.

**Nov 2026 update:** Quadra now brands itself 'AI-native', claiming agentic pipeline builders, agent-assisted entity resolution and anomaly detection. No MCP server, demo, docs or customer evidence is public.

## 8. Time-to-value, implementation, managed services & APAC support
As an early-stage product, implementation track record, reference base and regional (APAC) support are unproven and are the dominant diligence risks. Time-to-value claims cannot be validated on public evidence.

## 9. Commercials, TCO, exit & vendor viability
The open, inspectable, standards-based design is **strongest on portability/exit** — the explicit anti-lock-in stance is a genuine architectural strength. However, **vendor viability is the dominant risk**: an early-stage company is a high-risk choice for a ~$35bn manager's strategic master, and would only be appropriate for a bounded PoV or a non-core role until proven.

**Nov 2026 update:** the company is Quadra Pty Ltd, an Australian entity built by the team behind Cadis, Markit EDM and Matrix IDM (about page). Licensing is Business Source License 1.1: free for buy-side institutions' internal production use, commercial licence for service providers and resellers, converting to Apache 2.0 after ten years. Revenue comes from consulting/managed-service and consortium tiers; no price list. It is not the London crypto-trading Quadra profiled on CB Insights (that source has been removed).

## 10. Evidence, maturity & provisional scores
Evidence class is **vendor-authored only** (Quadra site) with corroborating context on FIBO from independent sources — no independent customer evidence, so scores are **heavily evidence-capped**. Hard gates: open-architecture/portability read favourably in principle; native IBOR, AI/agent, Databricks-specific integration, and especially **vendor-scale/viability and production-reference** gates read fail/unknown. Provisional domain read: distinctive on open architecture and portability *as a principle*, moderate on mastering *as a design*, weak/unproven on IBOR, AI, delivery track record and viability. **Stage-1 paper screen — emerging/watch, not a selection of record.** Appropriate as a bounded PoV or watch-list entry, not a core screen finalist, until institutional references exist. In-sandbox egress is restricted; figures triangulated from the search index and flagged as open items.

**Hard-gate read:**
- G01 native equities/ETF/govvies/credit/FX/PE: PARTIAL
- G02 security+entity+price mastering: PARTIAL — mastering is a model design; no production evidence (Nov 2026)
- G03 intraday position/price + near-real-time txns: PARTIAL
- G04 5yr history + point-in-time: UNKNOWN
- G05 IDP-as-master while Databricks consumes: PARTIAL
- G06 open/native Databricks integration: UNKNOWN — Databricks support claimed in README only (Nov 2026)
- G07 bidirectional API: UNKNOWN
- G08 business users extend model w/o vendor coding: PARTIAL
- G09 buyer can use own LLMs: UNKNOWN — no AI product documented (Nov 2026)
- G10 permission-aware MCP/agent interface: FAIL — no MCP/agent interface (Nov 2026)
- G11 field-level provenance/lineage/override/audit: PARTIAL — cell-level lineage claimed (Nov 2026)
- G12 full export on exit: PARTIAL — source-available model aids exit; full platform not public (Nov 2026)
- G13 AI/LLM data-use rights governable: UNKNOWN — no AI data-use terms (Nov 2026)
- G14 credible APAC+ANZ support: PARTIAL — Australian legal entity; no staff, offices or clients published (Nov 2026)
- G15 30–60 day PoV: FAIL
- G16 3–6 month production foundation: FAIL
- G17 07: UNKNOWN
- G18 internal ops retains exception/override control: PARTIAL
- G19 institutional security architecture: UNKNOWN — no security certifications published (Nov 2026)
- G20 5-yr TCO transparency: PARTIAL — licence terms published; no price list (Nov 2026)
- G21 critical function not roadmap-dependent: FAIL
- G22 controlled write-back to downstream systems: UNKNOWN

**Evidence re-checked 2026-11-03 (v3 refresh).** Scores remain provisional (Stage-1 paper screen) until a proof of value runs; see `_v3_updates.md`.

## 11. Sources
- Quadra Platform — company site: https://www.quadraplatform.com/ (accessed 2026-08-15)
- Quadra — open standards demo/overview: https://demo.quadraplatform.com/ (accessed 2026-08-15)
- EDM Council — FIBO (Financial Industry Business Ontology): https://spec.edmcouncil.org/fibo/ (accessed 2026-08-15)
- EDM Council — FIBO framework overview: https://edmcouncil.org/frameworks/industry-models/fibo/ (accessed 2026-08-15)
- https://www.quadraplatform.com/product.html — Product (Quadra; accessed 2026-11-03) [vendor · Official docs · undated · opened]
- https://www.quadraplatform.com/about.html — About (Quadra; accessed 2026-11-03) [vendor · Vendor marketing · undated · opened]
- https://github.com/quadra-platform/data-model-sample — quadra-platform/data-model-sample (Quadra (GitHub); accessed 2026-11-03) [vendor · Official docs · undated · opened]
- https://www.quadraplatform.com/privacy.html — Privacy Policy (Quadra; accessed 2026-11-03) [vendor · Official docs · 2026-04-07 · opened]
