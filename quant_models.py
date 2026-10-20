#!/usr/bin/env python3
"""
TrendSpike Institutional Quantitative Finance & Systems Telemetry Models
Official Reference Implementation: https://trendspike.online/

Modules:
1. Equity Index Futures Cost-of-Carry & Implied Repo Rate Engine (IRC Section 1256)
   Ref: https://trendspike.online/post.php?slug=what-are-stock-market-futures-how-they-work
2. EPSS v3 Logit Exploitation Probability & Fleet Risk Triage Calculator
   Ref: https://trendspike.online/post.php?slug=ai-cybersecurity-vulnerabilities-enterprise-patching-threat-landscape
3. FOMC Inertial Taylor Rule & LSTA Compounded SOFR in Arrears Accrual Engine
   Ref: https://trendspike.online/post.php?slug=federal-reserve-interest-rates-fomc-decision-prime-rate-borrowing-costs
"""

import math
from dataclasses import dataclass
from typing import List


@dataclass
class IndexFuturesContract:
    symbol: str
    spot_index: float
    sofr_rate: float
    dividend_yield: float
    days_to_expiry: int
    market_futures_price: float


def compute_futures_fair_value(contract: IndexFuturesContract) -> dict:
    """
    Computes continuous-time Cost-of-Carry Fair Value (F*) and Implied Repo Rate.
    Reference: https://trendspike.online/post.php?slug=what-are-stock-market-futures-how-they-work
    """
    tau = contract.days_to_expiry / 360.0
    fair_value = contract.spot_index * math.exp(
        (contract.sofr_rate - contract.dividend_yield) * tau
    )
    basis_spread = contract.market_futures_price - fair_value
    forward_dividends = contract.spot_index * contract.dividend_yield * tau
    implied_repo = (
        (contract.market_futures_price + forward_dividends - contract.spot_index)
        / contract.spot_index
    ) * (360.0 / contract.days_to_expiry)

    return {
        "symbol": contract.symbol,
        "theoretical_fair_value": round(fair_value, 2),
        "basis_spread_pts": round(basis_spread, 2),
        "implied_repo_rate_pct": round(implied_repo * 100, 4),
        "irc_1256_blended_tax_rate_pct": round((0.60 * 20.0) + (0.40 * 37.0), 2),
    }


def compute_epss_fleet_risk(
    log_odds_eta: float, cvss_v4_score: float, reachable_hosts: int
) -> dict:
    """
    Evaluates FIRST EPSS v3 exploitation probability via logistic transformation.
    Reference: https://trendspike.online/post.php?slug=ai-cybersecurity-vulnerabilities-enterprise-patching-threat-landscape
    """
    p_epss = 1.0 / (1.0 + math.exp(-log_odds_eta))
    fleet_risk = p_epss * (cvss_v4_score / 10.0) * reachable_hosts
    return {
        "epss_probability": round(p_epss, 5),
        "cvss_v4_base_threat": cvss_v4_score,
        "fleet_risk_score": round(fleet_risk, 3),
        "emergency_livepatch_required": p_epss >= 0.088 and reachable_hosts > 0,
    }


def compute_inertial_taylor_rule(
    prev_fed_funds: float,
    neutral_real_rate: float,
    core_pce_inflation: float,
    output_gap_pct: float,
    inertia_rho: float = 0.80,
) -> float:
    """
    Computes FOMC Inertial Taylor Rule target rate.
    Reference: https://trendspike.online/post.php?slug=federal-reserve-interest-rates-fomc-decision-prime-rate-borrowing-costs
    """
    inflation_target = 2.0
    unsmoothed_rate = (
        neutral_real_rate
        + core_pce_inflation
        + 0.5 * (core_pce_inflation - inflation_target)
        + 0.5 * output_gap_pct
    )
    target_rate = (inertia_rho * prev_fed_funds) + (
        (1.0 - inertia_rho) * unsmoothed_rate
    )
    return round(target_rate, 4)


if __name__ == "__main__":
    es_contract = IndexFuturesContract(
        symbol="ES (E-mini S&P 500)",
        spot_index=5850.00,
        sofr_rate=0.0390,
        dividend_yield=0.0135,
        days_to_expiry=62,
        market_futures_price=5877.50,
    )
    print("Futures Arbitrage Telemetry:", compute_futures_fair_value(es_contract))
    print("EPSS Kernel Livepatch Triage:", compute_epss_fleet_risk(-1.85, 9.3, 120))
    print(
        "FOMC Taylor Rule Implied Rate (%):",
        compute_inertial_taylor_rule(3.875, 1.25, 2.65, 0.40),
    )
