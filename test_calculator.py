"""Unit tests for the loan calculator."""

import pytest
from calculator import calculate_monthly_payment


# ── Correct calculations ─────────────────────────────────────────────────────

def test_standard_loan():
    # 10k principal, 5% rate, 10 years
    result = calculate_monthly_payment(10000, 5.0, 10)
    assert result == 106.07

def test_zero_interest_loan():
    # 12k principal, 0% rate, 1 year
    result = calculate_monthly_payment(12000, 0, 1)
    assert result == 1000.00

def test_small_loan():
    # 1k principal, 3% rate, 1 year
    result = calculate_monthly_payment(1000, 3.0, 1)
    assert result == 84.69


# ── Input validation ─────────────────────────────────────────────────────────

def test_negative_amount_raises():
    with pytest.raises(ValueError):
        calculate_monthly_payment(-10000, 5.0, 10)

def test_zero_years_raises():
    with pytest.raises(ValueError):
        calculate_monthly_payment(10000, 5.0, 0)

def test_negative_years_raises():
    with pytest.raises(ValueError):
        calculate_monthly_payment(10000, 5.0, -5)

def test_negative_rate_raises():
    with pytest.raises(ValueError):
        calculate_monthly_payment(10000, -5.0, 10)
