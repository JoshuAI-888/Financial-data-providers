# IDP Evaluation — v3.1 Shortlist Check (Nov 2026)

**As of:** 2026-11-05. **Previous refresh:** `_v3_updates.md` (2026-11-03).

## What this update does
- Adds a **Shortlist check (v3.1)** tab to the IDP Evaluation (Decide group). It compares three
  inputs: the buyer's strategic-rationale paper (Apr 2026), its use-case register and selection
  criteria (vReviewed), and an external consultant's IDP shortlisting deliverable (30 Sep 2026,
  nine platforms screened, five demonstrated, one preferred platform progressed to POC).
- Introduces `alignment_v3_1.json` as the source of truth for that tab: scope decisions, gates
  A01–A14, 13 weighted domains, per-vendor ratings with their basis, 38 triaged use cases,
  31 concerns and questions, and sources. `tools/build_pages.py` renders it and **computes** the
  weighted scores and the use-case demand cross-check. Nothing on the tab is typed by hand.
- Records new public evidence (5 Nov 2026) in the fact-sheets and makes two Fencore requirement
  score changes (below).

## Method
- **Criteria alignment.** The buyer's 44 selection dimensions (34 rated HIGH) were mapped to
  13 domains with a 100-point budget. Items every credible vendor should meet anyway (security
  assurance, tenant isolation, no-training, residency, entitlements for machine consumers, exit,
  resilience, viability floor) became pass/fail gates. Three gaps that none of the inputs scored
  were added: Income Fund instrument coverage, CRIMS + Apex NZ ingestion, and Bloomberg licensing.
- **Re-score.** The consultant's demo ratings were translated as Strong 3.5, Good 2.5, Limited 1.5
  (demo cap 3.5); desktop answers are vendor written responses (≤2.5). Domains the consultant did
  not assess (Databricks, TCO, viability) use this repo's v3 public-evidence domain scores. D4
  (instrument coverage) and D5 (calculation support) are unassessed for all vendors.
- **Validation.** Three research agents checked the consultant's vendor claims and the buyer's
  context against official and independent sources. Page fetches were blocked in the research
  environment, so almost all new sources are **search-only**; each is tagged.

## Results (computed by the build)
| Weight set | NeoXam | Fencore | FINBOURNE | EXF | Rimes |
|---|---|---|---|---|---|
| v3.1 proposed | 2.39 | 2.64 | 2.17 | 2.10 | **2.77** |
| Equal | 2.14 | 2.50 | 2.14 | 2.09 | **2.64** |
| Consultant lens (implied) | 2.28 | **3.17** | 2.06 | 2.17 | 2.83 |

The top two swap with the weight set; gaps under ~0.25 are inside the evidence noise; 16% of the
v3.1 weight is unassessed for every vendor.

## Score and gate changes (requirement level)
| Vendor | Item | Old → New | Evidence | Domain effect |
|---|---|---|---|---|
| Fencore | AI-01 | 1.0 → 1.5 | Vendor product page states governed data 'consumed via MCP, APIs, Python, FenWarehouse' (vendor marketing, search-only, 5 Nov 2026). No MCP documentation. | AI domain 0.5 → 1.0 |
| Fencore | AI-02 | 0.5 → 1.0 | Vendor page: Cori runs on a Fencore internal model or a customer-configured provider. | (as above) |
| Fencore | G09 | UNKNOWN → PARTIAL | As AI-02. | — |
| Fencore | G10 | FAIL → PARTIAL | As AI-01; permission inheritance stated, not documented. | — |

**Not used to change public scores:** the consultant's vendor-run demo results (e.g. Fencore's MCP
demo with entitlement enforcement). They are non-public evidence. They appear only on the v3.1
tab, labelled as demo ratings.

## Fact-sheet updates (dated 5 Nov 2026)
- **fencore.md:** MCP and model-choice statements; Snowflake default (FenWarehouse); headcount
  ~10 (PitchBook), single seed round, legal entities, EDM Council membership, Empaxis acquisition;
  no named customers, SOC 2 or published ISO 27001 certificate found.
- **neoxam.md:** the public NeoXam–Apex link is Maitland (South Africa, 2024). No public evidence
  of live Apex AU/NZ or Charles River production integration.
- **rimes.md:** JANA, NGS Super and Rest as ANZ references; Delta Sharing partnership is for
  managed data services, not documented for Matrix itself.
- **statestreet-alpha.md:** Charles River IBOR and Data Management Service; overlap and
  concentration question for a Charles River IBOR buyer.

## Withheld on purpose
- Indicative commercial figures that vendors gave privately.
- Internal stakeholder names, and identifying detail of the buyer, beyond what the repo already holds.

## Main concerns raised (full list on the tab)
- The shortlist rests on qualitative ratings without published weights.
- Calculations and Income Fund instrument coverage, the core of the rationale paper, were not assessed.
- No vendor showed live Charles River + Apex NZ integration.
- The preferred vendor carries vendor-viability risk (~10 staff, seed funding, no named customers in public sources).
- The screening universe omitted an existing supplier (AlphaCert) and has inconsistent drop reasons (ICS ATHENA, Arcesium).
- The rationale paper needs corrections: Databricks start-up times, the claim that a pre-built connector avoids Bloomberg licensing, which system is the OMS, and a one-sided TCO comparison.

Scores remain a **Stage-1 paper screen, provisional until a proof of value runs.**

## Link fixes (2026-11-05, after the PR link check)
The PR link check (GitHub Actions, open network) found 7 new dead links. Each was replaced with a current source for the same claim:
- FMC Act s 227: the NZLII mirror is replaced by the consolidated Act on legislation.govt.nz.
- IPP 12 / s 11: the OPC knowledge-base item is replaced by the OPC 'disclosing personal information outside NZ' decision tree.
- IAF MD 26: the Issue 1 copy is replaced by the IAF MD 26:2023 (Issue 2) copy hosted by SAC Singapore.
- Anthropic remote MCP: the support article is replaced by 'Get started with custom connectors using remote MCP'.
- APRA CPS 230: a PDF link containing spaces is replaced by the APRA Handbook page.
- Pre-existing citations (link rot, not part of v3.1):
  - Xignite 12B requests/day: the GlobeNewswire link is replaced by the Mondo Visione relay of the same release.
  - Crunchbase API: a third-party review is replaced by Crunchbase's official API docs.

Replacement URLs come from search results; they are confirmed by the next CI link check, not in the sandbox.
