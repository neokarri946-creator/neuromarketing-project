"""
The Power of Suggestion — Interactive Experience
Based on Madrian & Shea (2001)

Run an HR department and watch how default settings
shape the financial futures of hundreds of employees.
"""

import random
import time


def show_intro():
    print("=" * 58)
    print("  THE POWER OF SUGGESTION")
    print("  Based on Madrian & Shea (2001)")
    print("=" * 58)
    print()
    print("  You're the new HR director at a 500-person company.")
    print("  Your job: design the retirement savings plan.")
    print()
    print("  You'll run THREE rounds, each with a different")
    print("  default setting. Watch what happens to participation")
    print("  and savings rates across your workforce.")
    print()
    print("  After each round, you'll see the results of your")
    print("  policy choice playing out across real employees.")
    print()
    input("  Press Enter to start your first year as HR director...\n")


def simulate_employees(n, default_enrolled, default_rate, default_fund):
    """Simulate employee behaviour given defaults."""
    employees = []
    for i in range(n):
        # Each employee has an 'inertia score' — how likely
        # they are to just accept whatever the default is
        inertia = random.gauss(0.75, 0.15)
        inertia = max(0.1, min(0.98, inertia))

        # Will they change the default?
        keeps_default = random.random() < inertia

        if keeps_default:
            enrolled = default_enrolled
            rate = default_rate
            fund = default_fund
        else:
            # Active choosers make their own decisions
            enrolled = random.random() < 0.60
            rate = random.choice([3, 5, 6, 8, 10, 12, 15])
            fund = random.choice(["Stocks", "Bonds", "Balanced", "Index"])

        employees.append({
            "enrolled": enrolled,
            "rate": rate,
            "fund": fund,
            "kept_default": keeps_default,
        })

    return employees


def show_results(employees, round_num, policy_name):
    enrolled = [e for e in employees if e["enrolled"]]
    not_enrolled = [e for e in employees if not e["enrolled"]]
    kept = [e for e in employees if e["kept_default"]]

    participation = len(enrolled) / len(employees) * 100
    default_pct = len(kept) / len(employees) * 100

    print(f"\n  {'=' * 50}")
    print(f"  YEAR {round_num} RESULTS — {policy_name}")
    print(f"  {'=' * 50}")

    # Participation bar
    bar_len = 40
    filled = int(participation / 100 * bar_len)
    bar = "█" * filled + "░" * (bar_len - filled)
    print(f"\n  Participation: [{bar}] {participation:.0f}%")
    print(f"  ({len(enrolled)} out of {len(employees)} employees)")

    # Contribution rates among enrolled
    if enrolled:
        rates = [e["rate"] for e in enrolled]
        avg_rate = sum(rates) / len(rates)
        print(f"\n  Average contribution rate: {avg_rate:.1f}%")

        # Fund distribution
        funds = {}
        for e in enrolled:
            funds[e["fund"]] = funds.get(e["fund"], 0) + 1
        print(f"  Investment fund choices:")
        for fund, count in sorted(funds.items(), key=lambda x: -x[1]):
            pct = count / len(enrolled) * 100
            print(f"    {fund:<12} {pct:5.1f}%")

    print(f"\n  Kept the default unchanged: {default_pct:.0f}%")

    return participation


def get_choice(prompt, options):
    while True:
        choice = input(f"  {prompt} ").strip().upper()
        for opt in options:
            if choice == opt[0] or choice == opt:
                return opt
        print(f"  Please choose: {' / '.join(options)}")


def main():
    show_intro()
    n = 500
    results = []

    # --- ROUND 1: OPT-IN (no default enrolment) ---
    print("-" * 58)
    print("\n  YEAR 1: TRADITIONAL OPT-IN PLAN")
    print()
    print("  Employees must actively fill out a form to enrol.")
    print("  No default enrolment. No default contribution rate.")
    print("  They choose everything from scratch — or do nothing.")
    print()
    input("  Press Enter to see how your workforce responds...\n")

    employees = simulate_employees(n, default_enrolled=False,
                                   default_rate=0, default_fund="None")
    p1 = show_results(employees, 1, "OPT-IN (No Defaults)")

    print()
    input("  Press Enter to continue to Year 2...\n")

    # --- ROUND 2: AUTO-ENROL with low default ---
    print("-" * 58)
    print("\n  YEAR 2: AUTOMATIC ENROLMENT (LOW DEFAULT)")
    print()
    print("  New policy: everyone is automatically enrolled.")
    print("  Default contribution: 3% of salary.")
    print("  Default fund: Money Market (safe, low returns).")
    print("  Employees can opt out or change settings any time.")
    print()
    input("  Press Enter to see the impact...\n")

    employees = simulate_employees(n, default_enrolled=True,
                                   default_rate=3, default_fund="Money Market")
    p2 = show_results(employees, 2, "AUTO-ENROL (3%, Money Market)")

    print()
    input("  Press Enter to continue to Year 3...\n")

    # --- ROUND 3: AUTO-ENROL with high default ---
    print("-" * 58)
    print("\n  YEAR 3: AUTOMATIC ENROLMENT (HIGH DEFAULT)")
    print()
    print("  Same auto-enrolment, but you change the defaults:")
    print("  Default contribution: 10% of salary.")
    print("  Default fund: Balanced (stocks + bonds).")
    print("  Employees can still opt out or change any time.")
    print()
    input("  Press Enter to see what happens...\n")

    employees = simulate_employees(n, default_enrolled=True,
                                   default_rate=10, default_fund="Balanced")
    p3 = show_results(employees, 3, "AUTO-ENROL (10%, Balanced)")

    # --- DEBRIEF ---
    print("\n" + "=" * 58)
    print("  DEBRIEF — WHAT YOU JUST WITNESSED")
    print("=" * 58)

    print(f"""
  Your three years as HR director:

    Year 1 (Opt-in):              {p1:5.0f}% participation
    Year 2 (Auto-enrol, 3%):      {p2:5.0f}% participation
    Year 3 (Auto-enrol, 10%):     {p3:5.0f}% participation

  THE SCIENCE:

  Madrian & Shea (2001) found exactly this pattern at a
  real company. When enrolment switched from opt-in to
  automatic, participation jumped from 49% to 86%.

  But here's the deeper finding: people didn't just stay
  enrolled — they kept WHATEVER defaults were set. The
  default contribution rate became the most common rate.
  The default fund became the most popular fund.

  Most employees never touched their settings. The default
  wasn't just a starting point — it became the decision.

  WHY THIS MATTERS:

  This is one of the most powerful findings in behavioural
  economics. The person who designs the default effectively
  makes the choice for most people. This principle now
  shapes policy worldwide — from pension design to organ
  donation, from app privacy settings to subscription plans.

  The lesson: if you want people to do something, make it
  the default. If you want them not to, make them opt in.
  The form matters more than the intention.
""")


if __name__ == "__main__":
    main()
