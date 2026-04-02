"""Unit tests for the loan calculator."""

import pytest
from calculator import calculate_monthly_payment


# ── Correct calculations ─────────────────────────────────────────────────────

def test_standard_loan():
    result = calculate_monthly_payment(25000, 60, 5.0)
    assert result["monthly_payment"] == 471.78

def test_small_loan():
    result = calculate_monthly_payment(1000, 12, 3.0)
    assert result["monthly_payment"] == 84.69

def test_large_loan():
    result = calculate_monthly_payment(500000, 360, 4.0)
    assert result["monthly_payment"] == 2387.08

def test_total_interest_is_positive():
    result = calculate_monthly_payment(10000, 24, 5.0)
    assert result["total_interest"] > 0

def test_total_payment_exceeds_loan():
    result = calculate_monthly_payment(10000, 24, 5.0)
    assert result["total_payment"] > 10000


# ── Input validation ─────────────────────────────────────────────────────────

def test_negative_amount_raises():
    with pytest.raises(ValueError):
        calculate_monthly_payment(-10000, 60, 5.0)

def test_zero_duration_raises():
    with pytest.raises(ValueError):
        calculate_monthly_payment(10000, 0, 5.0)

def test_negative_rate_raises():
    with pytest.raises(ValueError):
        calculate_monthly_payment(10000, 60, -5.0)


# ── TODO (v2.0): Add tests for calculate_loan_term ──────────────────────────
# Expected test cases from BUSINESS_REQUIREMENT.md:
#   - €25,000 / €500/month / 5%  → 56 months
#   - €10,000 / €2,000/month / 3% → 6 months
#   - €25,000 / €50/month / 5%   → Error (payment too low)
