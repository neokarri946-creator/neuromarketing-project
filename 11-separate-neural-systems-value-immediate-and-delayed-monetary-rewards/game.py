"""
NOW vs LATER: The Hyperbolic Discounting Game
Based on: Separate Neural Systems Value Immediate and Delayed Monetary Rewards (2004) — McClure et al.

Two brain systems fight over every "now vs later" decision.
This game measures YOUR discount curve — how much future value
your impulsive brain throws away.
"""

import random
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def intro():
    clear()
    print("=" * 55)
    print("  NOW vs LATER: The Hyperbolic Discounting Game")
    print("=" * 55)
    print()
    print("Your brain has two systems fighting right now:")
    print()
    print("  LIMBIC SYSTEM  — wants rewards NOW, hates waiting")
    print("  PREFRONTAL CORTEX — can plan ahead, sees the bigger picture")
    print()
    print("You'll face 12 choices between money now and money later.")
    print("There are no wrong answers — just honest ones.")
    print("Go with your gut. Don't overthink it.")
    print()
    input("Press Enter to begin... ")

def run_game():
    intro()

    # Scenarios: (immediate_amount, delayed_amount, delay_description, delay_weeks)
    scenarios = [
        (10, 12, "1 week",    1),
        (20, 25, "2 weeks",   2),
        (50, 75, "1 month",   4),
        (15, 20, "3 days",    0.43),
        (100, 150, "3 months", 12),
        (30, 60, "6 months",  26),
        (5,  6,  "tomorrow",  0.14),
        (200, 350, "1 year",  52),
        (40, 50, "2 weeks",   2),
        (10, 30, "6 months",  26),
        (75, 100, "1 month",  4),
        (25, 80, "1 year",    52),
    ]

    random.shuffle(scenarios)
    choices = []
    now_count = 0
    later_count = 0

    for i, (now_amt, later_amt, delay_desc, delay_weeks) in enumerate(scenarios, 1):
        clear()
        print(f"  Choice {i} of 12")
        print("=" * 45)
        print()

        # Calculate the implied annual return
        if delay_weeks > 0:
            weekly_return = (later_amt / now_amt) ** (1 / delay_weeks) - 1
            annual_return = ((1 + weekly_return) ** 52 - 1) * 100
        else:
            annual_return = 0

        print(f"  [A]  £{now_amt} right now")
        print()
        print(f"  [B]  £{later_amt} in {delay_desc}")
        print()

        while True:
            choice = input("  Your choice (A/B): ").strip().upper()
            if choice in ("A", "B"):
                break
            print("  Please type A or B.")

        chose_now = (choice == "A")
        if chose_now:
            now_count += 1
        else:
            later_count += 1

        choices.append({
            "now": now_amt,
            "later": later_amt,
            "delay": delay_desc,
            "delay_weeks": delay_weeks,
            "chose_now": chose_now,
            "annual_return": annual_return,
        })

    # --- DEBRIEF ---
    clear()
    print("=" * 55)
    print("  YOUR RESULTS")
    print("=" * 55)
    print()
    print(f"  Chose NOW:   {now_count}/12 times")
    print(f"  Chose LATER: {later_count}/12 times")
    print()

    # Show their choices sorted by implied return they walked away from
    rejected_returns = [c for c in choices if c["chose_now"]]
    rejected_returns.sort(key=lambda c: c["annual_return"])

    if rejected_returns:
        print("-" * 55)
        print("  Returns you WALKED AWAY from by choosing 'now':")
        print("-" * 55)
        for c in rejected_returns:
            gain = c["later"] - c["now"]
            print(f"  £{c['now']} now over £{c['later']} in {c['delay']}"
                  f"  (+£{gain}, ~{c['annual_return']:.0f}% annual return)")
        print()

    # Categorise their discounting style
    if now_count <= 2:
        profile = "Patient Planner"
        desc = ("Your prefrontal cortex dominates. You're comfortable\n"
                "  waiting for better outcomes. Marketers would struggle\n"
                "  to rush you with urgency tactics.")
    elif now_count <= 5:
        profile = "Balanced Decider"
        desc = ("Your two systems are fairly matched. You can wait\n"
                "  when the payoff is big enough, but immediacy pulls\n"
                "  you when the gap is small.")
    elif now_count <= 9:
        profile = "Present-Biased"
        desc = ("Your limbic system has a strong voice. You'd rather\n"
                "  have less now than more later — 'buy now, pay later'\n"
                "  schemes and flash sales are designed for brains like yours.")
    else:
        profile = "Instant Gratification Seeker"
        desc = ("Your limbic system is firmly in charge. The pull of\n"
                "  'right now' overrides almost any future benefit.\n"
                "  Same-day delivery and impulse buy buttons were made\n"
                "  for you.")

    print(f"  Your profile: {profile}")
    print(f"  {desc}")

    print()
    print("=" * 55)
    print("  THE SCIENCE")
    print("=" * 55)
    print()
    print("  McClure et al. (2004) discovered that your brain")
    print("  literally has TWO separate systems competing:")
    print()
    print("  1. The LIMBIC system fires up when 'now' is an option.")
    print("     It wants immediate pleasure and discounts the future")
    print("     steeply — this is called HYPERBOLIC DISCOUNTING.")
    print()
    print("  2. The PREFRONTAL CORTEX evaluates both options more")
    print("     rationally, considering the actual value of waiting.")
    print()
    print("  The system with stronger activation WINS the choice.")
    print()
    print("  Marketers exploit this by making rewards feel immediate:")
    print("  instant downloads, same-day delivery, 'buy now pay later.'")
    print("  Each tactic tips the neural competition toward impulse.")
    print()
    input("Press Enter to exit... ")

if __name__ == "__main__":
    run_game()
