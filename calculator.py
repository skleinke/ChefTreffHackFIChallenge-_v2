"""
Loan Calculator v1.0 – Banking Hackathon Edition

Currently supports:
  - Monthly payment calculation

"""

import math


# ── Core Calculation ─────────────────────────────────────────────────────────


def calculate_monthly_payment(principal, annual_interest_rate, years):
    """Calculate the monthly payment for a loan.

    Formula: M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1 ]

    Args:
        principal:            Total loan amount (must be >= 0)
        annual_interest_rate: Annual interest rate in % (must be >= 0)
        years:                Loan duration in years (must be > 0)

    Returns:
        Monthly payment rounded to 2 decimal places
    """
    if principal < 0 or annual_interest_rate < 0 or years <= 0:
        raise ValueError("Invalid input: principal and annual_interest_rate must be non-negative, and years must be greater than zero.")

    n = years * 12

    if annual_interest_rate == 0:
        return round(principal / n, 2)

    i = (annual_interest_rate / 100) / 12

    numerator = i * (1 + i) ** n
    denominator = (1 + i) ** n - 1
    monthly_payment = principal * (numerator / denominator)

    return round(monthly_payment, 2)


# ── CLI ──────────────────────────────────────────────────────────────────────


def main():
    print("\n🏦 LOAN CALCULATOR v1.0\n")

    while True:
        print("  [1] Calculate monthly payment")
        print("  [2] Calculate loan term (not yet implemented)")
        print("  [q] Quit\n")

        choice = input("Choice: ").strip().lower()

        if choice == "1":
            try:
                amount = float(input("  Loan amount (€): "))
                years = float(input("  Duration (years): "))
                rate = float(input("  Annual interest rate (%): "))

                monthly_payment = calculate_monthly_payment(amount, rate, years)

                total_payment = monthly_payment * (years * 12)
                total_interest = total_payment - amount

                print(f"\n  Monthly payment: € {monthly_payment:,.2f}")
                print(f"  Total payment:   € {total_payment:,.2f}")
                print(f"  Total interest:  € {total_interest:,.2f}\n")

            except (ValueError, TypeError) as e:
                print(f"\n  ⚠ Error: {e}\n")

        elif choice == "2":
            print("\n  ⚠ Not yet implemented. See BUSINESS_REQUIREMENT.md\n")

        elif choice == "q":
            print("Goodbye! 👋\n")
            break

        else:
            print("\n  ⚠ Invalid choice.\n")


if __name__ == "__main__":
    main()
