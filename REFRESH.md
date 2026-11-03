# Refreshing the IDP Evaluation and Provider Landscape

How to keep every vendor claim current and the pages consistent. The short version:
**research notes are the source of truth → requirement scores → pages**, and the pages are
rebuilt by script, never hand-edited.

```
provider-landscape/idp-research/<vendor>.md     fact-sheets (narrative, hard gates, dated + typed sources)
provider-landscape/idp-research/reqscores_*.json requirement scores (48 requirements × 15 vendors)
provider-landscape/idp-research/vendors.json     vendor order, segment, risk penalties, "as of" dates
            │
            ▼  python3 provider-landscape/tools/build_pages.py
provider-landscape/idp_evaluation.html  ─┬─▶  idp_evaluation.html (root copy)
provider-landscape/financial_data_providers_landscape.html ─┬─▶ financial_data_providers_landscape.html
                                                            └─▶ index.html
```

## 1. Cadence

| Type | When | Scope |
|---|---|---|
| **Full refresh** | Quarterly (Feb, May, Aug, Nov) | All 15 IDP vendors across the five gap areas below, plus anything material since the last refresh. New audit log `idp-research/_vN_updates.md`. Link check of the whole register. |
| **Quick update** | Within a week of a big event | Only the vendor(s) affected. Triggers: acquisition, ownership or CEO change; a GA launch or withdrawal of a scored capability (MCP server, Databricks integration, agents); a named ANZ client win or go-live; published pricing. Append a dated entry to the current audit log. |

The five gap areas (from the Aug 2026 audit, `_v2_updates.md`):
1. Databricks & open architecture (Delta Sharing, Unity Catalog, Marketplace, zero-copy, write-back)
2. AI / agents / MCP (GA vs preview vs roadmap, buyer-own-LLM, permission-aware access)
3. Ownership / corporate changes
4. APAC / ANZ support (offices, named Australia/NZ clients)
5. Pricing / commercial model

## 2. Research (one vendor at a time)

Gather sources one vendor per researcher (in Claude Code: one Sonnet subagent per vendor, using
the brief in `idp-research/_research_brief.md`). Each researcher writes findings; nothing goes
into the notes or scores until reviewed.

Rules for every source:
- **Dated.** Publication date (YYYY-MM-DD, or YYYY-MM / "undated") and the access date.
- **Typed.** `vendor` (vendor site, vendor press release, vendor-paid PR wire, partner
  announcement) or `independent` (trade press, analyst, customer, regulator, filings), plus an
  evidence type: Official release note · Official docs · Vendor marketing · Named customer case
  study · News · Independent research · Official filings · Platform-standards docs.
- **Access recorded.** `opened` if the page was actually fetched and read; `search-only` if it was
  only seen in search results.
- Only cite URLs actually seen. Skip SEO/AI-generated aggregator blogs.
- "No new evidence located (as of <date>)" is a valid finding — write it rather than padding.

Source line format in a fact-sheet's `## 11. Sources` section (the build reads the tag):

```
- https://example.com/release — Title (Publisher; accessed 2026-11-03) [independent · News · 2026-10-27 · opened]
```

Older lines without a tag (`- URL — description (accessed 2026-08-14)`) are still accepted; the
August notes state those were search-sourced and not individually fetched.

## 3. Review, then update the notes

A reviewer (in Claude Code: Opus) reads every finding before it changes anything:
- **Fact-sheet text**: add a dated `**<Mon YYYY> update:**` paragraph to the relevant section, and
  correct stale sentences in place (say what changed in the audit log).
- **Snapshot**: update `- **Recent developments:**` (one dated sentence; shown on the vendor card).
- **Hard gates** (`## 10.` list `- G01 …: PASS|PARTIAL|FAIL|UNKNOWN — reason`): change only with
  evidence, and add the date to the reason.
- **Sources**: append the new tagged lines.

## 4. Score changes

Requirement scores live only in `reqscores_*.json` (fields `s, ev, rel, cite, url, type, note`).
Domain scores are **computed** (mean of the domain's four requirements, rounded to 0.5) — never
type them anywhere.

- Every score change is reviewed before it goes into the JSON, and listed in the audit log with
  old → new and the evidence.
- Evidence caps (enforced by the build): roadmap ≤1.0, sales/marketing ≤2.0, docs ≤3.0,
  demo ≤3.5, named-customer production reference ≤4.0, SLA ≤4.5, proof of value ≤5.0.
- **IDP scores stay provisional until a proof of value runs.** No score above 4.0 without a PoV.
- Don't upgrade on press-release adjectives; "available to clients" with no GA label is docs at most.

## 5. Rebuild and check

```bash
python3 provider-landscape/tools/build_pages.py          # rewrite pages from notes + scores
python3 provider-landscape/tools/build_pages.py --check  # CI: fails if a page is stale
python3 provider-landscape/tools/build_register.py       # refresh source_register.csv
python3 provider-landscape/tools/check_links.py          # OPEN NETWORK ONLY -> link_check.csv
python3 provider-landscape/tools/build_register.py       # merge link results into the register
```

- Bump `idp_as_of` in `vendors.json` on a full refresh (it re-stamps the page). `landscape_as_of`
  only moves when the 93-provider landscape itself is refreshed.
- The **Pages and link check** GitHub Actions workflow runs `build_pages.py --check` and the link
  check on every PR that touches `provider-landscape/`, monthly, and on demand. The Claude Code
  cloud sandbox blocks vendor sites, so run the link check there, or locally, never in the sandbox.
- Treat `dead` (404/410/DNS) as must-fix: replace with an archived or current URL, or remove the
  claim. `blocked` (403/429 bot walls) usually means alive — spot-check in a browser.
- Open the rebuilt `idp_evaluation.html` in a browser and confirm no console errors
  (`python3 provider-landscape/tools/smoke_test.py`, needs `pip install playwright`).

## 6. Audit log and PR

- Write `idp-research/_vN_updates.md` next to `_v2_updates.md`: window searched, per-vendor
  findings by gap, every score and gate change (old → new, evidence), corrections to earlier
  claims, and open questions for RFI.
- Open a PR for review. Never push to the default branch.

## Guardrails
- Stage-1 paper screen from public sources — not investment advice, not a selection of record.
- Don't store API keys or credentials anywhere in the repo or outputs.
