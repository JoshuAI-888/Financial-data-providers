"""
Generate docs/GLOSSARY.md and docs/DATA_DICTIONARY.md from the code so they never
drift from the implementation. Run:  python docs/gen_reference.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fmp_milford.glossary import METRIC_GLOSSARY, INSIGHT_EXPLAINERS
from fmp_milford.config import ENDPOINTS, PULL_ENDPOINTS, UNIVERSE, SETTINGS, BENCHMARK

DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)))

# Grouping for readability
GROUPS = [
    ("Profitability", ["gross_margin", "ebitda_margin", "operating_margin", "net_margin", "roe", "roa", "roic", "roce"]),
    ("Growth", ["revenue_cagr", "eps_cagr", "fcf_cagr"]),
    ("Liquidity", ["current_ratio", "quick_ratio", "interest_coverage"]),
    ("Leverage", ["net_debt_ebitda", "debt_to_equity", "gearing"]),
    ("Efficiency & cash conversion", ["asset_turnover", "cash_conversion_cycle", "fcf_conversion", "ocf_ebitda", "capex_sales"]),
    ("Valuation", ["pe", "ev_ebitda", "ev_sales", "pb", "p_fcf", "fcf_yield", "dividend_yield", "peg"]),
    ("Per share", ["eps", "bvps", "dps", "cfps"]),
    ("Quality scores", ["altman_z", "piotroski_f", "dupont_roe"]),
    ("Risk (price-based)", ["total_return", "ann_return", "ann_vol", "downside_vol", "beta", "max_drawdown", "momentum_12m", "sharpe"]),
    ("Factors", ["value", "quality", "growth", "momentum", "composite"]),
]


def gen_glossary():
    L = ["# Metric Glossary",
         "",
         "> Auto-generated from `fmp_milford/glossary.py` (the single source of truth, also",
         "> surfaced in the app as hover tooltips and the calculation modal). For each metric:",
         "> **meaning**, what **good** looks like, what you're **targeting**, and the **alpha / trade** angle.",
         ""]
    for title, keys in GROUPS:
        L.append(f"## {title}\n")
        for k in keys:
            g = METRIC_GLOSSARY.get(k)
            if not g:
                continue
            L.append(f"### {g['label']}  (`{k}`)")
            L.append(f"- **Meaning:** {g['meaning']}")
            L.append(f"- **What good looks like:** {g['good']}")
            L.append(f"- **What we're targeting:** {g['target']}")
            L.append(f"- **Alpha / what it trades:** {g['alpha']}")
            L.append("")
    L.append("## Widget-level intent\n")
    L.append("Each dashboard widget also carries an *intent / good / target / alpha* explainer:\n")
    for iid, e in INSIGHT_EXPLAINERS.items():
        L.append(f"- **`{iid}`** — {e['intent']} _Alpha:_ {e['alpha']}")
    L.append("")
    with open(os.path.join(DOCS, "GLOSSARY.md"), "w") as f:
        f.write("\n".join(L))


NORMALIZED = [
    ("ticker", "str", "—", "profile", "Exchange symbol / join key"),
    ("name", "str", "—", "profile.companyName", "Legal/common name"),
    ("sector", "str", "—", "config UNIVERSE (theme)", "Milford theme bucket"),
    ("industry", "str", "—", "profile.industry", "FMP industry label"),
    ("currency", "str", "—", "profile.currency", "Reporting/trading currency (USD on free tier)"),
    ("price", "float", "$", "profile.price", "Latest EOD price"),
    ("shares_out", "float", "count", "profile.sharesOutstanding", "Shares outstanding"),
    ("market_cap", "float", "$m", "profile.marketCap", "Market capitalisation"),
    ("beta", "float", "—", "profile.beta", "Vendor beta (we also compute our own)"),
    ("years", "list[int]", "—", "statements", "Fiscal years available (<=5 on free tier)"),
    ("income[y]", "dict", "$m", "income-statement", "revenue, gross_profit, operating_income, ebitda, dep_amort, interest_expense, net_income, shares, eps"),
    ("balance[y]", "dict", "$m", "balance-sheet-statement", "total_assets, current_assets, cash, inventory, receivables, total_liabilities, current_liabilities, total_debt, total_equity, retained_earnings, payables"),
    ("cash_flow[y]", "dict", "$m", "cash-flow-statement", "operating_cf, capex, free_cash_flow, dividends_paid, buybacks"),
    ("dividend_per_share", "float", "$", "dividends", "TTM dividend per share"),
    ("dividend_yield", "float", "%", "derived", "dps / price"),
    ("prices", "dict", "$", "historical-price-eod/full", "{start, freq='W', closes:[...]} weekly EOD closes"),
    ("fmp_scores", "dict", "—", "financial-scores", "Vendor Altman Z / Piotroski (cross-check)"),
    ("source", "str", "—", "—", "'FMP /stable/' or 'DEMO (synthetic)'"),
    ("retrieved", "iso ts", "—", "—", "Extraction timestamp (provenance)"),
]


def gen_data_dictionary():
    L = ["# Data Dictionary", "",
         "> Auto-generated from `fmp_milford/config.py` + the normalized record shape. Covers",
         "> (1) FMP endpoints used, (2) the canonical company record, (3) computed metric outputs.",
         "",
         f"**Universe:** {sum(len(v) for v in UNIVERSE.values())} US-listed names across "
         f"{len(UNIVERSE)} themes. **Benchmark:** {BENCHMARK}. **Daily call budget:** "
         f"{SETTINGS['daily_call_budget']}. **History:** ~{SETTINGS['price_years']}y (free tier).",
         "",
         "## 1. FMP endpoints (stable API)", "",
         "| key | path | params | free tier? | feeds |",
         "|---|---|---|---|---|"]
    for k, spec in ENDPOINTS.items():
        params = ", ".join(f"{a}={b}" for a, b in spec.get("params", {}).items()) or "symbol"
        free = "✓ free" if spec.get("free") else "verify/gated"
        L.append(f"| `{k}` | `/{spec['path']}` | {params} | {free} | {spec.get('feeds','')} |")
    L.append("")
    L.append(f"Per-company pull uses: {', '.join('`'+e+'`' for e in PULL_ENDPOINTS)} "
             f"(~{len(PULL_ENDPOINTS)} calls/company → ~{SETTINGS['daily_call_budget']//len(PULL_ENDPOINTS)} companies/day on free tier).")
    L.append("")
    L.append("## 2. Canonical company record (normalized; demo and live share this shape)")
    L.append("")
    L.append("| field | type | unit | source | notes |")
    L.append("|---|---|---|---|---|")
    for f, t, u, s, n in NORMALIZED:
        L.append(f"| `{f}` | {t} | {u} | {s} | {n} |")
    L.append("")
    L.append("## 3. Computed metric outputs")
    L.append("")
    L.append("Each metric is a dict `{value, formula, inputs, steps, unit, good}` (see `transform.py`). "
             "Plain-language meaning/target/alpha for every one is in [GLOSSARY.md](GLOSSARY.md). Keys:")
    L.append("")
    L.append(", ".join(f"`{k}`" for k in METRIC_GLOSSARY))
    L.append("")
    with open(os.path.join(DOCS, "DATA_DICTIONARY.md"), "w") as f:
        f.write("\n".join(L))


if __name__ == "__main__":
    gen_glossary()
    gen_data_dictionary()
    print("wrote docs/GLOSSARY.md and docs/DATA_DICTIONARY.md")
