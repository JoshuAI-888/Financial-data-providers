# Financial Data Providers

Independent, vendor-neutral research on financial market-data and intelligence providers, and a
guided evaluation of Investment Data Platforms (IDP), for an institutional multi-asset manager with a
Databricks-centred data strategy.

Both deliverables are **single HTML pages** with their CSS, JS and data inlined (light/dark aware), so
no build step is needed. The one exception is the in-page research library, which loads
`provider-landscape/research-explorer.js` and the Markdown fact-sheets beside it, so serve the repo
(for example via GitHub Pages) rather than opening a lone file if you want that panel to work.

> Not investment advice, a procurement recommendation, or affiliated with any provider named.

## The deliverables

| Page | What it is |
|---|---|
| [`financial_data_providers_landscape.html`](financial_data_providers_landscape.html) (also served as [`index.html`](index.html)) | **Provider Landscape.** 93 providers across public equity, private markets, fixed income & credit, indexes, ratings, ESG, risk and alternative data: cross-asset capability map, per-provider deep-dives, "who leads and why" by asset class, technical-integration comparison, customer-feedback synthesis, an Extended Universe of 76 further sources, and an Earnings Calls & Transcripts lens. |
| [`idp_evaluation.html`](idp_evaluation.html) | **IDP Evaluation (v2 guided decision system).** Works forward from strategy (outcomes, current/target maturity, ownership and sourcing model, architecture principles, risk tolerance) and derives vendor weightings from those answers. Live ranking with a "Why this score?" panel and typed, dated citations; sensitivity analysis; 15 × 12 capability map; hard-gate grid (G01–G22); vendor deep-dives; PoV and templates toolkit. |

## IDP Evaluation at a glance

A **Stage-1 paper screen** of 15 candidates from public sources, evidence-capped and flagged as
provisional, organised **Define → Evaluate → Decide**.

| Segment | Candidates |
|---|---|
| Core IDP / EDM | Rimes · FINBOURNE · Arcesium · NeoXam · Gresham Opus EDM · GoldenSource · Fencore · AlphaCert |
| Strategic data & content layers | FactSet · MSCI |
| Broad operating-platform counterfactuals | SimCorp One · BlackRock Aladdin · State Street Alpha Data Platform |
| Emerging / open-standard challengers | Quadra (watch-list) |
| Build accelerators & systems integrators | Exafluence |

IDP vendor facts were last refreshed on **3 November 2026** (v3: all 15 vendors; Databricks
integration, AI/MCP status, ownership, APAC/ANZ support, commercial model). The 93-provider
landscape is as of 10 August 2026. Treat both as point-in-time and re-verify before any
shortlisting decision. IDP scores are provisional until a proof of value runs.

**Refreshing:** see [REFRESH.md](REFRESH.md). Research notes are the source of truth, then
requirement scores, then pages. The pages are rebuilt by `provider-landscape/tools/build_pages.py`;
don't hand-edit the HTML.

## Repository layout

```
index.html                               published landing page (Provider Landscape)
financial_data_providers_landscape.html  Provider Landscape
idp_evaluation.html                      IDP Evaluation
provider-landscape/
  README.md                              full landscape write-up: coverage, findings, method
  research/                              per-provider fact-sheets (8 sections + dated sources)
  idp-research/                          IDP vendor fact-sheets, best-practice notes,
                                         requirement scores (reqscores_*.json, reqnotes_*.md)
                                         vendors.json, and the refresh audit trails
                                         (_v2_updates.md Aug 2026, _v3_updates.md Nov 2026)
  tools/build_pages.py                   rebuilds all pages from notes + scores (--check for CI)
  tools/build_register.py                writes source_register.csv (every cited URL)
  tools/check_links.py                   link checker (open network only) -> link_check.csv
  tools/smoke_test.py                    Playwright browser check (no console errors)
  source_register.csv, link_check.csv    source register and latest link-check results
  research-explorer.js                   research explorer script
  *.html                                 working copies of the two pages
.github/workflows/pages.yml              GitHub Pages deploy
.github/workflows/link-check.yml         pages-in-sync check + link check (PRs, monthly)
REFRESH.md                               how to refresh the research and pages
```

## Evidence base

Every page is assembled from the fact-sheets in `provider-landscape/research/` and
`provider-landscape/idp-research/`, which together record roughly **1,000+ unique source URLs** with
dates and source types (vendor-authored vs independent). See
[`provider-landscape/README.md`](provider-landscape/README.md) for the full method and limitations.
In short: pricing is approximate (enterprise vendors rarely publish list prices), review scores are
indicative, and some sources were search-sourced rather than individually fetched.

## Publishing

`.github/workflows/pages.yml` deploys the three root HTML pages and `provider-landscape/` to GitHub
Pages on every push to the default branch that touches them, or on manual dispatch.

When you edit a page, keep the root file and its `provider-landscape/` copy in sync. They differ
only in the relative path to `research-explorer.js`.
