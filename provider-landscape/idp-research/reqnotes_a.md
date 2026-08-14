# Requirement rationale — cluster A (mastering / Databricks / IBOR)

Stage-1 paper screen, 10 IDP vendors. No PoV run, so most scores cap at docs (≤3.0); a
handful reach 3.5 on a named comparable production reference (named-customer cap 4.0).
Grounded in the per-vendor fact-sheets and `_v2_updates.md`; current-status claims verified
by WebSearch (URLs format-valid, snippet-sourced, not machine-fetched).

## Mastering

**MSTR-01 Security/instrument golden master.** Six vendors are genuine golden-record masters
at docs level (GoldenSource, NeoXam, Gresham/Opus, SimCorp, Aladdin, plus Rimes/FINBOURNE/
Arcesium). FactSet is concordance-grade (crosswalk to its own IDs, not survivorship merge) →
2.0. MSCI has no security master (GICS classification only) → 1.0. Biggest unknown:
point-in-time/bitemporal depth of the master is asserted, not itemised, almost everywhere.

**MSTR-02 Entity & issuer-hierarchy master.** GoldenSource Entity Master (legal-entity/issuer,
multi-identifier/role, KYC/AML) and Gresham Prime EDM ("multiple hierarchies" template) are the
clearest → 3.0. FactSet has a real Entity Master but content-side. Most others document an
entity store without itemising issuer-hierarchy mechanics → 2.5. MSCI 1.0. Unknown: depth of
issuer-parent/subsidiary hierarchy modelling.

**MSTR-03 Identifier concordance (ISIN/SEDOL/CUSIP/FIGI).** Strongest evidence: FactSet
(Symbology API + Concordance Service, explicit standard-scheme cross-map with confidence),
NeoXam (explicit ISIN/CUSIP/SEDOL/ticker concordance), GoldenSource (multi-ID links to vendor
IDs) → 3.0. Others plausible but not itemised → 2.0–2.5. MSCI 1.0. Near-universal gap: **FIGI
specifically is almost never named** — flag for RFP.

**MSTR-04 Corporate-action mastering.** SimCorp and Aladdin strongest (native CA processing at
scale) → 3.0; Gresham Control Cloud integrates CA in reconciliation; Rimes/GoldenSource/FactSet
carry CA as data → 2.5. MSCI none → 0.5. Unknown: dedicated CA-mastering mechanics (voluntary
elections, entitlement calc) are itemised nowhere in public sources.

## Databricks & open architecture

**DBX-01 Delta Sharing / Open Sharing into Databricks.** Two clear leaders: **Rimes** (native
Delta Sharing partnership, Nov 2025, "without replication") and **FactSet** (datasets live on
Databricks Marketplace, Delta Sharing-based by architecture) → 3.0. Arcesium's Databricks tie is
the **MCP Marketplace (agent access), not data sharing** → 1.5. Everyone else 0.5–1.5:
NeoXam/MSCI Snowflake-centric, SimCorp roadmap ("Snowflake→Databricks"), Aladdin Snowflake-based
Data Cloud (duplication risk), GoldenSource named Databricks in 2022 (dated), Gresham Spark-only.

**DBX-02 Unity Catalog governance interop.** Nobody documents UC interop explicitly. Rimes and
FactSet inherit it (Delta Sharing is built into Unity Catalog; Marketplace is UC-governed) →
2.5. All others 0.5–1.5. Biggest unknown across the field — UC lineage/permission propagation
must be proven in PoV, not assumed.

**DBX-03 Zero-copy / no-replication.** Rimes explicit ("connect without replication") → 3.0;
FactSet share-in-place via Marketplace/Delta Sharing → 2.5 (vs Databricks-hosted read-replica
needs PoV). All others rely on extraction/ETL (SimCorp, Aladdin, MSCI, Gresham) → ≤1.0–1.5.

**DBX-04 Governed bidirectional write-back.** Weakly evidenced everywhere; note this is scored as
generic governed write-back, not Databricks-native. FINBOURNE Luminesce (read+write) and Gresham
Control Cloud (API extract/update with four-eyes/entitlements) are strongest → 2.5; Arcesium MCP
"transformation workloads" → 2.0. Databricks-native, governed write-back is unproven for all —
the single biggest open question in the Databricks domain.

## IBOR & investment modelling

**IBOR-01 Event-driven near-real-time book of record.** FINBOURNE (bi-temporal near-real-time,
named IBOR customer Baillie Gifford) and SimCorp (native real-time IBOR, ANZ refs Ardea/
Challenger) reach 3.5. Arcesium UBOR (unified IBOR/ABOR) and GoldenSource (explicit event-based
IBOR) and Aladdin (real-time position record) → 3.0. NeoXam 2.5, FactSet 2.0 (LiquidityBook,
newly acquired). Rimes/Gresham/MSCI are not book-of-record engines → 0.5.

**IBOR-02 / IBOR-03 Bi-temporal PIT reconstruction / correction history.** **FINBOURNE is the
definitional leader** — full bi-temporal AsAt history, rewind timelines, prior-known-state
preserved through corrections (named IBOR customer) → 3.5 both. SimCorp native PIT → 3.0.
Arcesium bi-temporal claimed in RFI but not publicly corroborated → 2.5/2.0. Gresham brings
lineage/investigation-history/audit (correction axis) → 2.5 on IBOR-03. Aladdin plausible at
scale, unconfirmed. Rimes/MSCI out of scope. Biggest unknown: only FINBOURNE and SimCorp make
genuine bi-temporal reconstruction claims; others assert lineage, not as-was position rebuild.

**IBOR-04 Intraday position/price.** SimCorp and Aladdin reach 3.5 on named large ANZ refs
(Ardea; Aware Super). GoldenSource explicit intraday exposure as prices publish → 3.0. NeoXam/
Arcesium/FINBOURNE claim near-real-time intraday but without SLA itemisation → 2.5. FactSet 2.0
(LiquidityBook). Rimes (EOD), Gresham (no positions), MSCI (analytics over supplied positions)
→ 0.5.

## Cross-cutting caveats
- Evidence ceiling: almost all scores are docs-capped (3.0); 3.5s rest on named production
  references (FINBOURNE/Baillie Gifford; SimCorp/Ardea; Aladdin/Aware Super), not on this
  buyer's own PoV.
- Recurring unknowns for RFP: FIGI concordance specifically; Unity Catalog lineage propagation;
  governed Databricks-native write-back; SLA-grade intraday/event mechanics; point-in-time depth
  outside FINBOURNE/SimCorp.
