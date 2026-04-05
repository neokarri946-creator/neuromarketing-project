"""
A Behavior Model for Persuasive Design — Interactive Experience
Based on Fogg (2009)

Design a product launch by balancing Motivation, Ability, and Triggers.
See what happens when any element is missing.
"""

import random

# ── Scenarios ──────────────────────────────────────────────────────

SCENARIOS = [
    {
        "name": "Fitness App Launch",
        "goal": "Get users to complete their first workout",
        "audience": "Busy office workers who say they want to exercise",
        "base_motivation": 5,
        "base_ability": 3,
        "base_trigger": 2,
        "threshold": 18,
    },
    {
        "name": "Charity Donation Page",
        "goal": "Get visitors to donate after reading a story",
        "audience": "People who just read an emotional news article",
        "base_motivation": 7,
        "base_ability": 4,
        "base_trigger": 1,
        "threshold": 18,
    },
    {
        "name": "New Savings Feature in a Banking App",
        "goal": "Get users to set up automatic weekly savings",
        "audience": "Young adults who complain about not saving enough",
        "base_motivation": 4,
        "base_ability": 3,
        "base_trigger": 2,
        "threshold": 18,
    },
]

MOTIVATION_OPTIONS = [
    ("Show a testimonial video from a real user", 2),
    ("Offer a free trial month", 3),
    ("Display social proof ('12,000 people joined this week')", 2),
    ("Send a personalised message about their goals", 1),
    ("Do nothing for motivation", 0),
]

ABILITY_OPTIONS = [
    ("Reduce sign-up to just one tap (use existing account)", 3),
    ("Pre-fill all form fields with smart defaults", 2),
    ("Add a step-by-step guided tutorial", 2),
    ("Simplify the screen — remove all distractions", 1),
    ("Do nothing for ability", 0),
]

TRIGGER_OPTIONS = [
    ("Send a push notification at the perfect moment", 3),
    ("Place a big colourful button right after the story", 2),
    ("Add an email reminder the next morning", 2),
    ("Rely on the user remembering on their own", 0),
    ("Do nothing for triggers", 0),
]


def show_intro():
    print("=" * 58)
    print("  FOGG BEHAVIOUR MODEL: B = MAT")
    print("  Based on Fogg (2009)")
    print("=" * 58)
    print()
    print("  Behaviour happens when THREE things converge:")
    print()
    print("    M — Motivation  (do they WANT to?)")
    print("    A — Ability     (is it EASY enough?)")
    print("    T — Trigger     (is there a CUE to act NOW?)")
    print()
    print("  You'll design 3 product launches.")
    print("  For each, choose ONE strategy for M, A, and T.")
    print("  If ANY element is too weak, the launch fails.")
    print()
    input("  Press Enter to begin...\n")


def show_bar(value, max_val=10, label=""):
    filled = "#" * value
    empty = "." * (max_val - value)
    return f"  {label:<12} [{filled}{empty}] {value}/10"


def choose_option(category, options):
    print(f"\n  Choose a {category} strategy:")
    for i, (desc, _) in enumerate(options, 1):
        print(f"    {i}. {desc}")
    while True:
        try:
            choice = int(input(f"\n  Your choice (1-{len(options)}): "))
            if 1 <= choice <= len(options):
                desc, boost = options[choice - 1]
                print(f"  --> Selected: {desc}")
                return desc, boost
        except ValueError:
            pass
        print(f"  Please enter a number from 1 to {len(options)}.")


def run_scenario(scenario):
    print("\n" + "-" * 58)
    print(f"  SCENARIO: {scenario['name']}")
    print(f"  Goal: {scenario['goal']}")
    print(f"  Audience: {scenario['audience']}")
    print("-" * 58)

    print(f"\n  Starting levels (before your design choices):")
    print(show_bar(scenario["base_motivation"], label="Motivation"))
    print(show_bar(scenario["base_ability"], label="Ability"))
    print(show_bar(scenario["base_trigger"], label="Trigger"))

    m_desc, m_boost = choose_option("MOTIVATION", MOTIVATION_OPTIONS)
    a_desc, a_boost = choose_option("ABILITY", ABILITY_OPTIONS)
    t_desc, t_boost = choose_option("TRIGGER", TRIGGER_OPTIONS)

    final_m = min(scenario["base_motivation"] + m_boost, 10)
    final_a = min(scenario["base_ability"] + a_boost, 10)
    final_t = min(scenario["base_trigger"] + t_boost, 10)

    score = final_m + final_a + final_t
    # Any element below 4 = automatic failure (the Fogg principle)
    weak_element = None
    if final_m < 4:
        weak_element = "MOTIVATION"
    elif final_a < 4:
        weak_element = "ABILITY"
    elif final_t < 4:
        weak_element = "TRIGGER"

    success = score >= scenario["threshold"] and weak_element is None

    print(f"\n  === RESULTS ===")
    print(show_bar(final_m, label="Motivation"))
    print(show_bar(final_a, label="Ability"))
    print(show_bar(final_t, label="Trigger"))
    print(f"\n  Combined score: {score}/{scenario['threshold']} needed")

    if success:
        print("  OUTCOME: SUCCESS — Users took action!")
    elif weak_element:
        print(f"  OUTCOME: FAILURE — {weak_element} was too low.")
        print(f"  Even though other elements were decent, the weak")
        print(f"  {weak_element} blocked the behaviour entirely.")
    else:
        print("  OUTCOME: FAILURE — Overall signal too weak.")
        print("  No single element was catastrophically low, but the")
        print("  combined force wasn't enough to push past the threshold.")

    return {
        "name": scenario["name"],
        "m": final_m,
        "a": final_a,
        "t": final_t,
        "score": score,
        "success": success,
        "weak": weak_element,
        "choices": (m_desc, a_desc, t_desc),
    }


def debrief(results):
    print("\n" + "=" * 58)
    print("  DEBRIEF — THE FOGG BEHAVIOUR MODEL")
    print("=" * 58)

    wins = sum(1 for r in results if r["success"])
    print(f"\n  You succeeded in {wins}/{len(results)} launches.")

    for r in results:
        status = "SUCCESS" if r["success"] else "FAILED"
        print(f"\n  {r['name']}: {status}")
        print(f"    M={r['m']}  A={r['a']}  T={r['t']}")
        if r["weak"]:
            print(f"    Bottleneck: {r['weak']}")

    print("\n" + "=" * 58)
    print("  THE SCIENCE:")
    print()
    print("  BJ Fogg (2009) showed that behaviour = M x A x T.")
    print("  All three must be present AT THE SAME MOMENT.")
    print()
    print("  Key insight: if ANY one element is near zero,")
    print("  the behaviour won't happen — no matter how strong")
    print("  the other two are.")
    print()
    print("  This is why:")
    print("  - Motivated people don't act if it's too hard (low A)")
    print("  - Easy actions get ignored without a prompt (low T)")
    print("  - Great UX fails if nobody cares (low M)")
    print()
    print("  Smart designers DIAGNOSE which element is weakest,")
    print("  then fix THAT one — rather than blindly boosting all.")
    print()
    print("  Amazon's 1-click buy = maximise Ability.")
    print("  Push notifications = provide Triggers.")
    print("  Emotional storytelling = boost Motivation.")
    print()

    if wins == len(results):
        print("  You nailed all three — you've got a designer's eye")
        print("  for balancing the behaviour equation.")
    elif wins == 0:
        print("  None succeeded — which perfectly demonstrates the")
        print("  model: it only takes one weak element to block action.")
    else:
        print("  A mixed result — look at what differed between your")
        print("  successes and failures. That's the diagnostic power")
        print("  of B = MAT in action.")
    print()


def main():
    show_intro()

    results = []
    for scenario in SCENARIOS:
        result = run_scenario(scenario)
        results.append(result)

    debrief(results)


if __name__ == "__main__":
    main()
