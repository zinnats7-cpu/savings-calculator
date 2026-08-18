"""
Compound Interest / Savings Calculator
Author: [Your Name]

Calculates and visualizes how savings grow over time with monthly
contributions and compound interest.
"""

import matplotlib.pyplot as plt


def calculate_growth(starting_amount, monthly_contribution, annual_rate, years):
    """
    Calculates the account balance for every month, given:
    - starting_amount: how much money you start with
    - monthly_contribution: how much you add each month
    - annual_rate: the yearly interest rate, as a percentage (e.g. 5 for 5%)
    - years: how many years to project

    Returns a list of balances, one for each month (including month 0,
    the starting point).
    """
    # Interest rates are usually given per YEAR, but we're compounding
    # every MONTH, so we convert the annual rate into a monthly rate.
    # Example: 6% annual becomes 0.5% per month (6 / 12), then we turn
    # the percentage into a decimal by dividing by 100.
    monthly_rate = annual_rate / 100 / 12

    total_months = years * 12

    balance = starting_amount
    balances = [balance]  # month 0 = starting amount, before anything happens

    for month in range(1, total_months + 1):
        # Each month: the existing balance earns interest, THEN we add
        # this month's contribution.
        balance = balance * (1 + monthly_rate) + monthly_contribution
        balances.append(balance)

    return balances


def get_positive_number(prompt, allow_zero=True):
    """
    Asks the user for a number and keeps asking until they give a valid one.
    This is called a "loop until valid input" pattern — very common in
    beginner programs. `while True` means "loop forever" until we hit a
    `return`, which breaks out of the loop.
    """
    while True:
        raw_text = input(prompt)
        try:
            value = float(raw_text)
        except ValueError:
            # This runs if float() couldn't convert the text to a number
            print("  -> Please enter a valid number (e.g. 1000 or 250.50).")
            continue

        if value < 0:
            print("  -> Please enter a number that isn't negative.")
        elif value == 0 and not allow_zero:
            print("  -> Please enter a number greater than zero.")
        else:
            return value


def get_user_inputs():
    """Collects all four inputs needed for the calculation."""
    print("=== Compound Interest / Savings Calculator ===\n")
    starting_amount = get_positive_number("Starting amount ($): ")
    monthly_contribution = get_positive_number("Monthly contribution ($): ")
    annual_rate = get_positive_number("Annual interest rate (%, e.g. 5 for 5%): ")
    years = int(get_positive_number("Number of years: ", allow_zero=False))
    return starting_amount, monthly_contribution, annual_rate, years


def plot_growth(balances, save_path="savings_growth.png"):
    """
    Turns the list of monthly balances into a line chart.
    `balances` has one entry per month, so we convert the month index
    into a "years" value (month / 12) for a nicer x-axis.
    """
    months = list(range(len(balances)))
    years_axis = [m / 12 for m in months]

    plt.figure(figsize=(10, 6))
    plt.plot(years_axis, balances, color="#2E86AB", linewidth=2)
    plt.fill_between(years_axis, balances, color="#2E86AB", alpha=0.1)

    plt.title("Savings Growth Over Time", fontsize=14, fontweight="bold")
    plt.xlabel("Years")
    plt.ylabel("Balance ($)")
    plt.grid(True, alpha=0.3)

    # Format the y-axis as dollars with commas (e.g. $10,000 not 10000)
    ax = plt.gca()
    ax.yaxis.set_major_formatter(lambda x, pos: f"${x:,.0f}")

    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    print(f"\nChart saved to '{save_path}'")
    plt.show()


def print_summary(balances, starting_amount, monthly_contribution, years):
    """Prints a plain-text summary of the results before showing the chart."""
    total_contributed = starting_amount + monthly_contribution * years * 12
    final_balance = balances[-1]
    interest_earned = final_balance - total_contributed

    print(f"\n--- Results after {years} year(s) ---")
    print(f"Total contributed:  ${total_contributed:,.2f}")
    print(f"Interest earned:    ${interest_earned:,.2f}")
    print(f"Final balance:      ${final_balance:,.2f}")


def main():
    starting_amount, monthly_contribution, annual_rate, years = get_user_inputs()

    balances = calculate_growth(
        starting_amount, monthly_contribution, annual_rate, years
    )

    print_summary(balances, starting_amount, monthly_contribution, years)
    plot_growth(balances)


if __name__ == "__main__":
    main()
