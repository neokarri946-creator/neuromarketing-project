"""
Defaults and Donation Decisions — Interactive Experience
Based on Johnson & Goldstein (2004)

Design organ donation systems for a fictional country and
watch how defaults dramatically shift participation rates.
"""

import random
import time


POPULATION = 1000
COUNTRY_NAME = "Valdonia"


def show_intro():
    print("=" * 58)
    print("  DEFAULTS AND DONATION DECISIONS")
    print("  Based on Johnson & Goldstein (2004)")
    print("=" * 58)
    print()
    print(f"  You've been appointed Health Minister of {COUNTRY_NAME},")
    print(f"  a country of {POPULATION:,} citizens.")
    print()
    print("  Your goal: design an organ donation system.")
    print("  You'll test THREE different policy designs and see")
    print("  how each one changes the donation rate.")
    print()
    print("  The citizens aren't for or against donation —")
    print("  most have no strong preference either way.")
    print("  What matters is HOW you ask the question.")
    print()
    input("  Press Enter to begin...\n")


def simulate_citizens(policy, effort_barrier, endorsement_effect, preference_strength):
    """
    Simulate citizen behaviour under a given policy.

    Each citizen has:
    - A slight lean toward or away from donation
    - Sensitivity to effort (most won't bother changing defaults)
    - Sensitivity to implied endorsement (default = recommended)
    """
    donors = 0
    reasons = {"effort": 0, "endorsement": 0, "preference": 0, "active": 0}

    for _ in range(POPULATION):
        # Each citizen's innate lean: slight normal distribution
        lean = random.gauss(0.05, 0.3)  # Slight positive lean toward donation
        has_strong_preference = abs(lean) > 0.5

        if policy == "opt-in":
            # Must actively check box to become donor
            if has_strong_preference and lean > 0:
                donors += 1
                reasons["active"] += 1
            elif random.random() < 0.08:
                # Small chance someone with mild preference makes the effort
                donors += 1
                reasons["effort"] += 1
            # Everyone else stays non-donor (default)

        elif policy == "opt-out":
            # Must actively check box to REMOVE donor status
            if has_strong_preference and lean < 0:
                # Strong objectors will opt out
                reasons["active"] += 1
            elif random.random() < 0.05:
                # Small chance someone mildly against makes the effort
                reasons["effort"] += 1
            else:
                donors += 1
                if not has_strong_preference:
                    if random.random() < 0.5:
                        reasons["endorsement"] += 1
                    else:
                        reasons["preference"] += 1

        elif policy == "mandated-choice":
            # Must actively choose — no default
            if lean > 0.1:
                donors += 1
                reasons["preference"] += 1
            elif lean > -0.1:
                # Ambivalent — slight lean toward "yes" due to social desirability
                if random.random() < 0.6:
                    donors += 1
                    reasons["endorsement"] += 1
            else:
                reasons["active"] += 1

    return donors, reasons


def show_results_animated(policy_name, donors, population):
    """Show donation rate building up with visual bar."""
    rate = donors / population * 100
    bar_width = 40

    print(f"\n  Policy: {policy_name}")
    print(f"  Processing {population:,} citizens", end="")

    # Animate counting up
    steps = 10
    for i in range(1, steps + 1):
        shown = int(rate * i / steps)
        filled = int(bar_width * shown / 100)
        empty = bar_width - filled
        bar = "█" * filled + "░" * empty
        print(f"\r  [{bar}] {shown}%  ({int(donors * i / steps):,}/{population:,})", end="")
        time.sleep(0.15)

    print(f"\r  [{('█' * int(bar_width * rate / 100)) + ('░' * (bar_width - int(bar_width * rate / 100)))}] "
          f"{rate:.1f}%  ({donors:,}/{population:,} donors)    ")
    return rate


def run_policy(policy_name, policy_code, description):
    """Run one policy simulation."""
    print("\n" + "-" * 58)
    print(f"\n  POLICY: {policy_name}")
    print(f"  {description}")
    print()

    # Let player predict first
    while True:
        try:
            guess = float(input("  What donation rate do you predict? (0-100%): ").strip().replace("%", ""))
            if 0 <= guess <= 100:
                break
            print("  Enter a number between 0 and 100.")
        except ValueError:
            print("  Enter a number between 0 and 100.")

    donors, reasons = simulate_citizens(policy_code, 0, 0, 0)
    rate = show_results_animated(policy_name, donors, POPULATION)

    diff = abs(rate - guess)
    if diff < 5:
        print(f"  Your prediction: {guess:.0f}% — Very close!")
    elif diff < 15:
        print(f"  Your prediction: {guess:.0f}% — Not far off.")
    else:
        print(f"  Your prediction: {guess:.0f}% — Surprised?")

    return {"name": policy_name, "code": policy_code, "rate": rate,
            "donors": donors, "guess": guess, "reasons": reasons}


def debrief(results):
    print("\n" + "=" * 58)
    print("  DEBRIEF — THE POWER OF DEFAULTS")
    print("=" * 58)

    print("\n  YOUR THREE POLICIES COMPARED:")
    print()
    print(f"  {'Policy':<25} {'Predicted':>10} {'Actual':>10} {'Donors':>10}")
    print("  " + "-" * 55)
    for r in results:
        print(f"  {r['name']:<25} {r['guess']:>9.0f}% {r['rate']:>9.1f}% {r['donors']:>9,}")

    # Find the gap
    rates = {r["code"]: r["rate"] for r in results}
    opt_in = rates.get("opt-in", 0)
    opt_out = rates.get("opt-out", 0)
    gap = opt_out - opt_in

    print()
    print(f"  THE DEFAULT EFFECT: {gap:.0f} percentage points")
    print(f"  between opt-in and opt-out — same citizens,")
    print(f"  same attitudes, different default.")

    print()
    print("=" * 58)
    print("  REAL-WORLD DATA (Johnson & Goldstein, 2004)")
    print("=" * 58)
    print()
    print("  Opt-IN countries (must actively register):")
    print("    Denmark:     4.25%")
    print("    UK:         17.17%")
    print("    Germany:    12.00%")
    print("    Netherlands: 27.50%")
    print()
    print("  Opt-OUT countries (presumed consent):")
    print("    Austria:    99.98%")
    print("    France:     99.91%")
    print("    Belgium:    98.00%")
    print("    Sweden:     85.90%")
    print()
    print("  The difference is NOT about attitudes toward donation.")
    print("  Surveys show similar support across these countries.")
    print("  The difference is almost entirely about the DEFAULT.")

    print()
    print("=" * 58)
    print("  WHY DEFAULTS ARE SO POWERFUL")
    print("=" * 58)
    print()
    print("  Johnson & Goldstein identified three mechanisms:")
    print()
    print("  1. EFFORT — Any action, however small, reduces")
    print("     participation. Even ticking one box is enough")
    print("     to lose half your audience.")
    print()
    print("  2. IMPLIED ENDORSEMENT — People read the default")
    print("     as 'what's recommended' or 'what normal people")
    print("     do'. The default signals the socially approved")
    print("     option.")
    print()
    print("  3. CONSTRUCTED PREFERENCES — Most people don't have")
    print("     a strong opinion about organ donation until asked.")
    print("     When there's no strong preference, the default")
    print("     BECOMES the preference.")
    print()
    print("  FOR MARKETING & DESIGN:")
    print()
    print("  This is why pre-ticked newsletter boxes increase")
    print("  sign-ups. Why auto-enrolment transforms pension")
    print("  saving. Why app permission defaults shape behaviour.")
    print("  Why 'recommended plan' badges shift subscription")
    print("  choices. The person who sets the default holds")
    print("  enormous invisible power over the outcome.")
    print()


def main():
    show_intro()

    policies = [
        ("OPT-IN (Active Consent)", "opt-in",
         "Citizens must actively CHECK A BOX to become a donor.\n"
         "  If they do nothing, they are NOT a donor."),
        ("OPT-OUT (Presumed Consent)", "opt-out",
         "Citizens are AUTOMATICALLY registered as donors.\n"
         "  They must actively CHECK A BOX to remove themselves."),
        ("MANDATED CHOICE (Forced Decision)", "mandated-choice",
         "Citizens MUST choose yes or no — there is no default.\n"
         "  Neither option is pre-selected."),
    ]

    results = []
    for name, code, description in policies:
        result = run_policy(name, code, description)
        results.append(result)
        print()
        input("  Press Enter for the next policy...\n")

    debrief(results)


if __name__ == "__main__":
    main()
