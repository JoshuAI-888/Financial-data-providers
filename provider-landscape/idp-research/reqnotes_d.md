# Requirement Scoring Rationale — Cluster D (Time-to-Value, Commercials/TCO/Exit, Viability)

Stage-1 paper screen, 10 IDP vendors, for an institutional multi-asset manager whose strategic
platform is **Databricks** and home region is **APAC/ANZ**. Scores 0.0–5.0 (0.5 steps) = evidenced
fit for THIS buyer, evidence-capped (roadmap≤1.0, sales≤2.0, docs≤3.0, demo≤3.5, named-customer≤4.0,
sla≤4.5, pov≤5.0). No PoV run in a paper screen, so most cells sit ≤3.0/≤3.5; named ANZ/comparable
references reach 3.5. Pricing is undisclosed across the field (only FactSet has third-party
estimates), so TCO-01/TCO-02 are capped low with evidence "sales". Grounded in the existing
fact-sheets + `_v2_updates.md`; two targeted web searches confirmed FINBOURNE's 30-day LUSID free
evaluation and open OpenAPI SDKs (format-valid, search-sourced, not machine-fetched).

## Time to value & implementation

**TTV-01 Dataset onboarding speed (days not months).** No vendor publishes day-level onboarding
metrics, so this is inference from delivery model. Leaders (2.5): GoldenSource (pre-built Bloomberg
template, 800+ fields), FactSet (Databricks Marketplace Delta Sharing = near-instant dataset
access), Arcesium (Aquata hundreds of connectors), FINBOURNE (self-service CSV/API load). Mid (2.0):
Rimes, NeoXam, Gresham, MSCI. Laggards (1.0): SimCorp One and Aladdin — onboarding to a full data
model/operating platform is measured in months (6–18mo for Aladdin), the opposite of this
requirement.

**TTV-02 Pre-built connector library.** Strongest (3.0): Rimes (1,000+ data partners / ~2,500
datasets), Arcesium (explicit "hundreds of connectors"), FactSet (own catalogue + Marketplace).
Mid (2.5): Gresham, GoldenSource, SimCorp (Infomediary/partner ecosystem), Aladdin (extensive but
proprietary). Lower (2.0): NeoXam and MSCI (count not published / MSCI content only).

**TTV-03 Low implementation FTE / PS dependency.** Managed-service and config-over-code models score
higher for lowering *internal* FTE: Rimes, GoldenSource (EDM Now for lean IT), FactSet (2.5). Mid
(2.0): FINBOURNE, NeoXam, Gresham (DaaS/EDM-as-a-Service), MSCI. Heavy professional-services /
programme dependency pulls Arcesium (1.5), SimCorp (1.5) and Aladdin (1.0) down.

**TTV-04 30–60 day PoV feasibility.** FINBOURNE leads (2.5) — a **published 30-day free LUSID
evaluation** is the only concrete PoV-enabling artifact found. GoldenSource/FactSet/MSCI (2.0) are
plausible via templates / Marketplace+MCP / PADP document pilot but with no formal PoV programme.
Rimes/Arcesium/NeoXam/Gresham (1.5) have no documented path. SimCorp and Aladdin (1.0) explicitly
fail — programmes are months, not weeks.

## Commercials, TCO & exit

**TCO-01 Pricing transparency.** Undisclosed across the field → capped low. **FactSet is the sole
exception (2.0)**: third-party procurement aggregators (Vendr, Costbench) publish per-user estimate
ranges (~$4k–$50k+/user/yr) — indicative, not official list price. Aladdin (1.0) has informal
third-party AUM-bps estimates. All others 0.5 (contact-for-quote). FINBOURNE nudged to 1.0 for a
published free-trial-then-subscription model.

**TCO-02 Predictable AUM-scalable 5-year TCO.** Same pricing blackout. FactSet (2.0) has an
estimable per-user subscription (but not AUM-scaled). Aladdin (1.0) is genuinely AUM-scalable (bps
of AUM) but opaque and can balloon with AUM growth. FINBOURNE/MSCI (1.0) name a subscription model
without figures. Others 0.5. Note: Arcesium's subscription-plus-consulting model is *less*
predictable, not more.

**TCO-03 Full data export on exit (raw+mastered+history+rules+audit).** Mostly UNKNOWN — a genuine
RFP-stage gap. **FINBOURNE leads (2.5)**: open OpenAPI SDKs (public GitHub) + CSV/Excel export +
bi-temporal history queryable via API (full rules/audit export still unconfirmed). Gresham (2.0)
documents API record extraction with lineage/audit. NeoXam/GoldenSource (1.5) expose extraction
APIs but no exit terms. Content licensors (Rimes, FactSet, MSCI, 1.0) are constrained by licence —
you cannot retain the vendor's content on exit. **Aladdin lowest (0.5)** — Snowflake-embedded
derived data = high exit-lock; migrating off Aladdin plausibly means migrating off Snowflake too.

**TCO-04 Usable without vendor proprietary runtime.** Best fit for a Databricks buyer. **Rimes and
FactSet lead (3.0)** — Delta Sharing (Rimes) / Delta Sharing + LLM-agnostic MCP (FactSet) deliver
data into the buyer's *own* Databricks runtime. Gresham (2.5, Spark/Python/REST delivery),
GoldenSource (2.5, cloud-agnostic warehouse delivery incl. a 2022 Databricks reference), MSCI (2.5,
Parquet/CSV via Crux — open formats but not Databricks-native), FINBOURNE (2.5, open APIs/SDKs but
mastering runs in LUSID). Arcesium (1.5) is a proprietary estate with MCP access. SimCorp and
Aladdin (1.0) are proprietary front-to-back runtimes — integration-via-extraction only.

## Vendor viability, roadmap, support & references

**VIA-01 APAC / ANZ support & named references.** The single most differentiating requirement for
this buyer. **SimCorp (3.5, Ardea + Challenger/Fidante, APAC MD)**, **NeoXam (3.5, Sydney+Melbourne
offices + Platinum AM)** and **Aladdin (3.5, AustralianSuper + Aware Super)** lead on named ANZ
production references — though Aladdin's are super-fund scale, not mid-manager. Rimes (3.0, new Rest
2026 win) and FactSet (3.0, 20+yr ANZ presence, 70+ staff) are strong. GoldenSource (2.5, Melbourne
office but no named ANZ client). MSCI (2.0, Sydney + ANZ lead, no named IDP client), FINBOURNE (2.0,
ANZ sales hire 2025 only). Weakest: Arcesium (1.5, HK office Jan 2026, no ANZ) and Gresham (1.5,
sales-director hire only).

**VIA-02 Roadmap execution track record.** Public-company disciplined shippers lead (3.0): FactSet,
MSCI, Aladdin, Arcesium (Opterra→Aquata AI→Limina). Mid (2.5): Rimes (Delta Sharing shipped on
time), FINBOURNE, GoldenSource, SimCorp (Agent Launchpad rolling GA). Laggards: NeoXam (2.0 —
Agents production slipped to 2027) and Gresham (1.5 — mid-integration, two-product convergence
unproven).

**VIA-03 Financial viability & ownership stability.** Top (3.0): FactSet ($2.45bn ASV, public),
MSCI ($2.98bn run-rate, public), SimCorp (Deutsche Börse-owned), BlackRock/Aladdin (world's largest
AM), Arcesium (D.E.Shaw/JPM, $6tn serviced), NeoXam (Eurazeo majority — though repeated PE churn).
Mid (2.5): Rimes (strong scale but two PE changes since 2020), FINBOURNE (Series B, >£100m,
smaller), GoldenSource (Gemspring, 40yr history, variably reported scale). Lowest: Gresham (2.0 —
three M&A moves in two years, active integration risk).

**VIA-04 Comparable-customer reference availability.** For a mid-size multi-asset manager, the most
directly comparable named references are **NeoXam (3.5, Platinum AM)** and **SimCorp (3.5, Ardea
~A$18bn)**. FINBOURNE (3.0, Baillie Gifford/LSEG), Rimes (3.0, 60 of top-100 AMs), Arcesium (3.0,
Neuberger Berman), FactSet (3.0, broad buy-side but content-layer), Aladdin (3.0, but super-fund
scale-mismatch). MSCI (2.5, asset-owner base, ANZ ref unclear). Gresham/GoldenSource (2.0 — client
counts cited but no named comparable production reference surfaced).

## Cross-vendor read (this cluster)

- **Time-to-value leaders:** FINBOURNE (only published PoV/free-trial + open export), then
  FactSet/GoldenSource/Arcesium on onboarding accelerators. SimCorp and Aladdin are structurally
  slow (months-to-year programmes).
- **TCO/exit transparency:** universally weak. FactSet is the only pricing-transparent name (third-
  party estimates). For *exit/runtime independence*, Rimes and FactSet (Delta Sharing) and FINBOURNE
  (open SDKs) lead; Aladdin is the clear exit-lock risk (Snowflake-embedded).
- **APAC/ANZ + viability:** SimCorp, NeoXam and Aladdin have the strongest named ANZ references;
  FactSet and MSCI bring the strongest balance sheets. Gresham and Arcesium are the weakest on ANZ.
- **Undisclosed/unproven:** pricing (all but FactSet), exit terms (all — RFP-stage gap), 30–60 day
  PoV (all but FINBOURNE), and NeoXam's AI roadmap (production 2027) remain the biggest open
  questions to close in diligence.
