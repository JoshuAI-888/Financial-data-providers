# Requirement-level rationale — Cluster B (DQ / Total Portfolio / Coverage)

**Buyer context:** institutional multi-asset manager, Databricks strategic platform. Stage-1 paper screen — no PoV run, so scores are evidence-capped (roadmap ≤1.0, sales ≤2.0, docs ≤3.0, demo ≤3.5, named-customer ≤4.0, sla ≤4.5). Most cells land ≤3.0.

**Method / caveat:** Scores derive first from the existing fact-sheets and `_v2_updates.md`, then targeted WebSearch to fill gaps. WebFetch was not relied on (egress). All cited URLs are **format-valid, search-sourced — not individually machine-fetched**. Material new claims (LUSID quote tolerances/bitemporal, NeoXam DataHub bi-temporal as-at/as-of, Rimes 5.5M daily checks, MSCI TPM cash-flows) triangulated across ≥2 sources where possible. "Unknown" scored 0.5–1.0, never auto-fail.

---

## Data quality & investment operations

**DQ-01 Tolerance-based price validation.** FINBOURNE leads with documented LUSID quote-store tolerance checks per portfolio plus outlier controls (support.lusid.com). NeoXam (Aro configurable tolerances on ISIN/qty/amount) and Gresham (Prime EDM pricing validation + Control Cloud heritage) tie at 3.0. Rimes now credible (5.5M daily validation checks at ingestion) but tolerance mechanic not itemised → 2.5. MSCI weakest (1.5) — validation exists but scoped to private documents, not public prices. Aladdin scale-implied only (2.0, sales).

**DQ-02 Stale/missing-price detection.** Same leaders — FINBOURNE outlier control, NeoXam outlier/cross-source detection, Gresham automated pricing validation (all 3.0). GoldenSource / FactSet / SimCorp / Arcesium mid-band (2.5) on ingestion completeness checks. MSCI 1.5 (private scope), Aladdin 2.0 (not established).

**DQ-03 Exception workflow with automated resolution.** Strongest, most concrete band: Gresham Control Cloud (patented workflow matching, escalation, audit), NeoXam Aro (routing/escalation), Arcesium (any-vs-any recon + AI loan-notice cutting hours→minutes), FINBOURNE+Taskize — all 3.0. SimCorp / MSCI / GoldenSource 2.5. Rimes SLA-backed but vendor-side (2.5). FactSet / Aladdin 2.0 (depth not established).

**DQ-04 Four-eyes / internal override control.** Gresham is the clear leader (3.0) — explicit four-eyes approval, edit entitlements, investigation history, audit trail documented in Control Cloud. FINBOURNE 2.5 (bitemporal audit + entitlements; explicit maker-checker unconfirmed). Managed-service vendors are penalised where exception handling defaults to the vendor and buyer override authority is unclear: Rimes 1.0, Aladdin/FactSet 1.5. Others 2.0.

## Public/private total portfolio

**TP-01 Private-market document ingestion & extraction.** MSCI PADP leads (3.0) — AI extraction vs 1,500+ rules, 97% automation, human-in-loop, plus Vantager. Arcesium ties (3.0, demo) on the named/quantified loan-notice extraction across 15+ counterparties. NeoXam 3.0 (AI IDP for private-markets docs, GA/reference maturity unclear). Aladdin 2.0 (eFront/Preqin data, extraction not specifically evidenced). Rimes/GoldenSource have no capability located (0.5).

**TP-02 Capital-call / distribution / waterfall modelling.** Aladdin/eFront leads (3.5, named-customer) — full lifecycle commitments/calls/distributions/NAV/waterfall, the industry standard, Mirae reference. MSCI 3.0 (TPM audit-ready cash-flows + commitment forecasting). FINBOURNE 2.0 (fund accounting/NAV native, waterfall not itemised), NeoXam/SimCorp 2.0. FactSet/GoldenSource/Rimes bottom (0.5–1.0).

**TP-03 Total-portfolio look-through exposure.** MSCI (3.0, TPM public/private look-through risk) and Aladdin (3.5, whole-portfolio at scale, named super-fund refs) lead decisively. Everyone else 1.0–2.0 — unified models exist but explicit look-through is not evidenced.

**TP-04 Public + private on one unified model.** Aladdin 3.5 (whole-portfolio + eFront, named refs). MSCI / FINBOURNE 3.0 (explicit unified public+private model). Arcesium / NeoXam / SimCorp 2.5. Gresham 2.0 (data-level). FactSet / GoldenSource 1.0 — not established.

## Data coverage, currency & history

**CUR-01 5-year point-in-time history depth.** FINBOURNE (bitemporal reconstruction) and SimCorp (IBOR point-in-time native) lead at 3.0. NeoXam 2.5 (bi-temporal as-of reconstruction now evidenced), FactSet 2.5 (20+ yr estimates), Aladdin 2.5. Others 2.0 — lineage/change-history claimed, explicit point-in-time depth undocumented.

**CUR-02 Asset-class breadth (equities/FI/credit/FX/PE).** Aladdin 3.5 (public multi-asset + eFront private, proven at scale). Rimes / Gresham / FactSet / SimCorp 3.0 (broad public breadth; native PE the common gap). FINBOURNE 2.0 — model can represent all classes but content is client-populated, not vendor-supplied. MSCI 2.5 (risk-model breadth + PE, no security master).

**CUR-03 Market-aware SLA / data currency (multi-market close).** SLA-backed managed-service vendors lead: SimCorp (24/6 follow-the-sun, 3.0), Rimes (SLA-backed managed data services, 3.0), GoldenSource (EDM Now, 2.5), FactSet (global DaaS, 2.5). MSCI weakest (1.5, Crux/Snowflake delivery). Explicit multi-market-close granularity is nowhere fully itemised — probe in PoV.

**CUR-04 Timestamp / bitemporal field model.** Two clear leaders at 3.0: FINBOURNE (native effectiveAt/asAt business+system timestamps) and NeoXam (DataHub bi-temporal as-at/as-of with timestamped audit logs — the notable upgrade this pass). SimCorp / Aladdin 2.0 (point-in-time native, explicit bitemporal taxonomy not detailed). Rimes / MSCI have no bitemporal field model located (1.0).

---

### Cross-cutting reads
- **Price-validation / DQ operations** genuinely lead: Gresham (four-eyes + reconciliation heritage), FINBOURNE (documented tolerance + bitemporal), NeoXam (Aro + hundreds of controls).
- **Private markets** genuinely lead: MSCI (document extraction + total-portfolio) and BlackRock/Aladdin (eFront lifecycle + waterfall + named ANZ refs); Arcesium/NeoXam strong on document ingestion specifically.
- **Coverage & currency**: Aladdin broadest asset breadth; SimCorp/Rimes strongest SLA currency; FINBOURNE + NeoXam strongest bitemporal field model.
- **Unproven / thin for this cluster**: Rimes and GoldenSource on private markets (no capability located); MSCI on public DQ price-validation; FactSet on total-portfolio public+private. All are paper-screen reads pending PoV.
