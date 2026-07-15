# Assumptions

## Data & coverage
- **A1.** FMP tier is **free/Basic**: US-listed only, EOD, ~5y annual statements, 250 calls/day.
  None of Milford's home exchanges are reachable; the universe is therefore US comparables.
- **A2.** Base/quote currency is **USD** at this tier (everything reachable is US-listed).
  NZD translation only becomes relevant on upgrade.
- **A3.** Fundamentals are **annual** (free tier). Half-yearly/quarterly APAC handling and
  point-in-time restatement history are *not* available until higher tiers / other sources.
- **A4.** Some endpoints (analyst estimates, price targets, ratings, insider/13F, transcripts)
  are **gated above free** — flagged `verify/gated` in `config.ENDPOINTS`; confirm on first
  live run and enable in the pipeline if your tier includes them.

## The demo dataset (this environment only)
- **A5.** This environment **blocks egress to financialmodelingprep.com**, so the committed
  report uses a **synthetic** dataset, clearly labelled `DEMO (synthetic)` on every widget.
- **A6.** Demo figures are **plausible, not real** — sector-appropriate magnitudes generated
  from per-ticker anchors with a seeded RNG. Prices use a **one-factor model**
  (`r = α + β·market + ε`) so realised betas ≈ anchor betas and correlations are structured.
  Do **not** cite demo numbers as fact; run `--live` for real values.

## Methodology choices
- **A7.** Metrics are **computed by us** from the statements, never ingested pre-baked, so a
  single consistent definition applies to every name (FMP's own ratios are a cross-check only).
- **A8.** **Tax rate** for NOPAT/ROIC is assumed **21%** flat (documented in `transform.py`);
  refine per-jurisdiction when precision matters.
- **A9.** **Risk statistics** use **weekly** returns over ~5y, annualised with ×52 / ×√52;
  live daily prices are downsampled to weekly to keep this consistent.
- **A10.** **Altman Z / Piotroski F** use standard formulas approximated from available
  free-tier fields; treat as screens, not audited scores.
- **A11.** **Factor z-scores** are cross-sectional over the current active universe — they are
  **relative**, not absolute, and shift as you filter companies.
- **A12.** PM **commentary is rule-based** (deterministic thresholds on the computed metrics),
  chosen over an LLM for reproducibility and auditability.

## Scope & governance
- **A13.** Book-of-record data (positions/NAV/performance/compliance) is **out of scope** (IBOR).
- **A14.** Output is **analytical tooling, not investment advice**, and **not for client-facing
  or decision-of-record** use (FMA boundary).
- **A15.** The provided API key is treated as **compromised** (shared in plain text) and should
  be **rotated**; it lives only in a git-ignored `.env`.

## Environment
- **A16.** Python **3.9+**; core pipeline needs **no third-party packages**. Playwright is
  optional (browser smoke test only).
- **A17.** Universe = **32 US names** across four themes; expandable via `config.UNIVERSE`.
  250/day ⇒ ~28–30 companies/day of full pulls, so large universes span multiple days (cache-backed).
