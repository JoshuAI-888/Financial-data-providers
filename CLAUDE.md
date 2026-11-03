# CLAUDE.md

Guidance for Claude Code (and future contributors) working in this repository.

## What this repo is
Independent, vendor-neutral research on financial data providers, published as two
self-contained HTML pages:

- `financial_data_providers_landscape.html` (also `index.html`): the Provider Landscape.
- `idp_evaluation.html`: the Investment Data Platform (IDP) Evaluation, a guided
  Define → Evaluate → Decide model over 15 candidate vendors.

The evidence base is the Markdown fact-sheets in `provider-landscape/research/` and
`provider-landscape/idp-research/`. Read `provider-landscape/README.md` for method and scope.

## Layout
```
index.html, financial_data_providers_landscape.html, idp_evaluation.html   published pages
provider-landscape/          working copies of the pages, research-explorer.js, fact-sheets
provider-landscape/idp-research/   IDP fact-sheets, reqscores_*.json, reqnotes_*.md, _v2_updates.md
.github/workflows/pages.yml  GitHub Pages deploy (default branch)
```

## Conventions & invariants
- **Self-contained pages.** CSS, JS and data are inlined. No CDN links, external fonts or images.
  The only runtime fetch is `research-explorer.js` loading the Markdown fact-sheets.
- **Keep copies in sync.** `index.html` must equal `financial_data_providers_landscape.html`, and
  each root page must match its `provider-landscape/` copy except for the `research-explorer.js`
  path. Edit one, then propagate.
- **Evidence first.** Every claim in a page should trace to a fact-sheet with a dated source and a
  source type (vendor-authored vs independent). Update the fact-sheet, then the page.
- **Date everything.** Note the access date on new sources and re-stamp "as of" text when refreshing.
- **IDP scores stay provisional** (Stage-1 paper screen, evidence-capped) until a proof of value runs.

## Guardrails
- Not investment advice, a procurement recommendation, or affiliated with any provider named.
- Pricing is approximate and review scores are indicative; say so where they appear.

## Gotchas
- The managed cloud environment blocks egress to most vendor sites, so links can't be verified
  there. Check links on an open network.
