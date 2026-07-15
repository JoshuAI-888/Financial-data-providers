"""
Unit tests for the metric engine on a hand-checked fixture company.
Run: python -m pytest tests/ -q   (or: python tests/test_transform.py)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fmp_milford import transform as T


def _fixture():
    # Two years so YoY / Piotroski work. Round numbers for easy hand-check.
    years = [2023, 2024]
    inc = {
        2023: dict(revenue=1000, gross_profit=500, operating_income=200, ebitda=250,
                   dep_amort=50, interest_expense=20, net_income=120, shares=100, eps=1.20),
        2024: dict(revenue=1200, gross_profit=640, operating_income=260, ebitda=320,
                   dep_amort=60, interest_expense=20, net_income=150, shares=100, eps=1.50),
    }
    bal = {
        2023: dict(total_assets=2000, current_assets=800, cash=200, inventory=150, receivables=180,
                   total_liabilities=1200, current_liabilities=400, total_debt=700, total_equity=800,
                   retained_earnings=500, payables=120),
        2024: dict(total_assets=2200, current_assets=900, cash=300, inventory=160, receivables=190,
                   total_liabilities=1250, current_liabilities=420, total_debt=720, total_equity=950,
                   retained_earnings=560, payables=130),
    }
    cf = {
        2023: dict(operating_cf=180, capex=60, free_cash_flow=120, dividends_paid=-30, buybacks=-10),
        2024: dict(operating_cf=210, capex=80, free_cash_flow=130, dividends_paid=-30, buybacks=-10),
    }
    return dict(ticker="TST", name="Test Co", sector="Healthcare", industry="x", currency="USD",
                price=30.0, shares_out=100, market_cap=3000, beta=1.0, years=years,
                income=inc, balance=bal, cash_flow=cf, dividend_per_share=0.3, dividend_yield=1.0,
                prices={"start": "2020-01-03", "freq": "W", "closes": [10, 11, 12]},
                fmp_scores={}, source="TEST", retrieved="t")


def approx(a, b, tol=1e-6):
    return a is not None and abs(a - b) <= tol


def test_margins_and_valuation():
    m = T.company_metrics(_fixture())
    assert approx(m["net_margin"]["value"], 150 / 1200)          # 12.5%
    assert approx(m["gross_margin"]["value"], 640 / 1200)
    assert approx(m["ev_ebitda"]["value"], (3000 + (720 - 300)) / 320)
    assert approx(m["pe"]["value"], 3000 / 150)                  # 20x
    assert approx(m["fcf_yield"]["value"], 130 / 3000)


def test_roic_and_cash_conversion():
    m = T.company_metrics(_fixture())
    nopat = 260 * (1 - 0.21)
    invested = 720 + 950 - 300
    assert approx(m["roic"]["value"], nopat / invested)
    assert approx(m["fcf_conversion"]["value"], 130 / 150)       # ~86.7%


def test_dupont_identity_equals_roe():
    m = T.company_metrics(_fixture())
    # DuPont product should reconstruct ROE (both use average equity/assets)
    assert approx(m["dupont_roe"]["value"], m["roe"]["value"], tol=1e-6)


def test_leverage_and_liquidity():
    m = T.company_metrics(_fixture())
    assert approx(m["net_debt_ebitda"]["value"], (720 - 300) / 320)
    assert approx(m["current_ratio"]["value"], 900 / 420)
    assert approx(m["quick_ratio"]["value"], (900 - 160) / 420)


def test_every_metric_has_formula():
    m = T.company_metrics(_fixture())
    for k, c in m.items():
        assert c.get("formula"), f"{k} missing formula"


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn(); print("ok:", fn.__name__)
    print(f"\n{len(fns)} tests passed.")
