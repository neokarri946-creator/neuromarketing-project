"""
Save More Tomorrow — Interactive Experience
Based on Thaler & Benartzi (2004)

Experience why saving from future raises feels painless
while saving from current income feels like a sacrifice.
"""

import random


def currency(amount):
    """Format a number as currency."""
    return f"£{amount:,.0f}"


def show_intro():
    print("=" * 58)
    print("  SAVE MORE TOMORROW")
    print("  Based on Thaler & Benartzi (2004)")
    print("=" * 58)
    print()
    print("  You've just started a new job earning £30,000/year.")
    print("  Over the next 6 years, you'll get annual pay rises.")
    print()
    print("  You'll play TWO careers side by side:")
    print()
    print("  CAREER A — Traditional saving")
    print("    Each year, you decide how much of your CURRENT")
    print("    income to redirect into savings.")
    print()
    print("  CAREER B — Save More Tomorrow")
    print("    Before you start, you commit to saving a portion")
    print("    of each FUTURE pay rise — not your current pay.")
    print()
    print("  At the end, we'll compare how each approach felt")
    print("  and what you actually saved.")
    print()
    input("  Press Enter to begin Career A...\n")


def get_savings_choice(prompt, max_amount):
    """Ask player how much they want to save."""
    while True:
        try:
            print(f"  {prompt}")
            raw = input("  Amount to save (£): ").strip().replace("£", "").replace(",", "")
            amount = int(float(raw))
            if 0 <= amount <= max_amount:
                return amount
            print(f"  Please enter an amount between £0 and {currency(max_amount)}.")
        except ValueError:
            print("  Please enter a number.")


def career_a_traditional(base_salary, raises):
    """Traditional saving: decide each year from current income."""
    print("\n" + "=" * 58)
    print("  CAREER A — TRADITIONAL SAVING")
    print("  (Decide each year how much to save from current pay)")
    print("=" * 58)

    salary = base_salary
    total_saved = 0
    yearly_spending = []
    yearly_saving = []

    for year, raise_pct in enumerate(raises, 1):
        if year > 1:
            old_salary = salary
            salary = int(salary * (1 + raise_pct))
            raise_amount = salary - old_salary
            print(f"\n  Year {year}: You got a {raise_pct*100:.0f}% raise! "
                  f"(+{currency(raise_amount)})")
        else:
            print(f"\n  Year {year}: Starting salary")

        print(f"  Annual salary: {currency(salary)}")
        monthly = salary / 12
        print(f"  Monthly take-home: {currency(monthly)}")
        print()

        save_amount = get_savings_choice(
            f"How much of your {currency(salary)}/year do you want to save?",
            salary
        )

        spending = salary - save_amount
        total_saved += save_amount
        yearly_spending.append(spending)
        yearly_saving.append(save_amount)

        save_pct = (save_amount / salary * 100) if salary > 0 else 0
        print(f"\n  You save {currency(save_amount)} ({save_pct:.1f}% of salary)")
        print(f"  You spend {currency(spending)} this year")
        print(f"  Running total saved: {currency(total_saved)}")

        if year > 1 and spending < yearly_spending[-2]:
            print("  ⚠ Your spending DROPPED — that's the loss aversion bite!")

    return total_saved, yearly_spending, yearly_saving


def career_b_smart(base_salary, raises):
    """SMarT saving: commit in advance to save from future raises."""
    print("\n" + "=" * 58)
    print("  CAREER B — SAVE MORE TOMORROW (SMarT)")
    print("  (Commit now to save from future raises)")
    print("=" * 58)

    salary = base_salary
    print(f"\n  Starting salary: {currency(salary)}")
    print(f"\n  Before your career begins, you'll decide what")
    print(f"  PERCENTAGE of each future pay rise goes to savings.")
    print(f"  This only affects the RAISE — never your current pay.")
    print()

    while True:
        try:
            pct_input = input("  What % of each future raise to save? (0-100): ").strip().replace("%", "")
            commit_pct = float(pct_input)
            if 0 <= commit_pct <= 100:
                break
            print("  Enter a number between 0 and 100.")
        except ValueError:
            print("  Enter a number between 0 and 100.")

    commit_pct /= 100
    print(f"\n  Locked in: {commit_pct*100:.0f}% of every future raise goes to savings.")
    print(f"  Your current {currency(salary)} spending is completely untouched.")
    input("\n  Press Enter to see your career unfold...\n")

    total_saved = 0
    base_spending = salary  # Year 1 spending = full salary (no saving yet)
    yearly_spending = [base_spending]
    yearly_saving = [0]
    current_annual_saving = 0

    print(f"  Year 1: Salary {currency(salary)}")
    print(f"  Savings: £0 (no raise yet — you keep everything)")
    print(f"  Spending: {currency(salary)}")

    for year, raise_pct in enumerate(raises[1:], 2):
        old_salary = salary
        salary = int(salary * (1 + raise_pct))
        raise_amount = salary - old_salary

        new_saving_from_raise = int(raise_amount * commit_pct)
        current_annual_saving += new_saving_from_raise
        spending = salary - current_annual_saving
        total_saved += current_annual_saving

        yearly_spending.append(spending)
        yearly_saving.append(current_annual_saving)

        save_pct = (current_annual_saving / salary * 100) if salary > 0 else 0

        print(f"\n  Year {year}: {raise_pct*100:.0f}% raise → +{currency(raise_amount)}")
        print(f"  Salary: {currency(salary)}")
        print(f"  Savings from raise: {currency(new_saving_from_raise)} "
              f"({commit_pct*100:.0f}% of raise)")
        print(f"  Total annual saving: {currency(current_annual_saving)} "
              f"({save_pct:.1f}% of salary)")
        print(f"  Spending: {currency(spending)}")

        if spending >= yearly_spending[-2]:
            print("  ✓ Spending went UP — you never felt a cut!")
        else:
            print("  (Spending dipped slightly — but only from the raise)")

    total_saved += 0  # Year 1 had no saving
    return total_saved, yearly_spending, yearly_saving


def debrief(results_a, results_b, raises):
    total_a, spending_a, saving_a = results_a
    total_b, spending_b, saving_b = results_b

    print("\n" + "=" * 58)
    print("  DEBRIEF — COMPARING YOUR TWO CAREERS")
    print("=" * 58)

    print("\n  YEAR-BY-YEAR COMPARISON:")
    print(f"  {'Year':<6} {'Career A Saving':<20} {'Career B Saving':<20} {'Career A Spend':<18} {'Career B Spend':<18}")
    print("  " + "-" * 80)

    for i in range(len(spending_a)):
        yr = i + 1
        sa = currency(saving_a[i]) if i < len(saving_a) else "—"
        sb = currency(saving_b[i]) if i < len(saving_b) else "—"
        spa = currency(spending_a[i]) if i < len(spending_a) else "—"
        spb = currency(spending_b[i]) if i < len(spending_b) else "—"
        print(f"  {yr:<6} {sa:<20} {sb:<20} {spa:<18} {spb:<18}")

    print()
    print(f"  TOTAL SAVED (Career A — Traditional): {currency(total_a)}")
    print(f"  TOTAL SAVED (Career B — SMarT):       {currency(total_b)}")
    print()

    if total_b > total_a:
        print(f"  SMarT saved you {currency(total_b - total_a)} MORE!")
    elif total_a > total_b:
        print(f"  Traditional saved {currency(total_a - total_b)} more — but")
        print(f"  think about how each approach FELT.")
    else:
        print(f"  Both approaches saved the same amount.")

    # Check if spending ever dropped in each career
    a_drops = sum(1 for i in range(1, len(spending_a)) if spending_a[i] < spending_a[i-1])
    b_drops = sum(1 for i in range(1, len(spending_b)) if spending_b[i] < spending_b[i-1])

    print()
    print(f"  Times spending DROPPED (feels like a loss):")
    print(f"    Career A: {a_drops} times")
    print(f"    Career B: {b_drops} times")

    print()
    print("=" * 58)
    print("  THE SCIENCE")
    print("=" * 58)
    print()
    print("  Thaler & Benartzi's SMarT programme worked because")
    print("  it hacked three biases:")
    print()
    print("  1. LOSS AVERSION — Cutting current spending feels")
    print("     like a loss. Saving from a raise you haven't")
    print("     received yet doesn't feel like losing anything.")
    print()
    print("  2. INERTIA — Once enrolled, automatic escalation")
    print("     means you never have to decide again. The same")
    print("     laziness that prevented saving now locks it in.")
    print()
    print("  3. PRESENT BIAS — Committing your FUTURE self to")
    print("     save is easy. Committing your PRESENT self is hard.")
    print("     SMarT asks you when it's painless.")
    print()
    print("  In the real study, savings went from 3.5% to 13.6%")
    print("  in four years — nearly quadrupling — and 80% of")
    print("  participants stayed in the programme.")
    print()
    print("  The lesson: don't fight psychology. Redirect it.")
    print()


def main():
    base_salary = 30000
    raises = [0.0, 0.04, 0.05, 0.03, 0.06, 0.04]  # Year 1 = 0, then annual raises

    show_intro()
    results_a = career_a_traditional(base_salary, raises)

    print()
    input("  Now let's try Career B — Save More Tomorrow.\n  Press Enter to continue...\n")

    results_b = career_b_smart(base_salary, raises)
    debrief(results_a, results_b, raises)


if __name__ == "__main__":
    main()
