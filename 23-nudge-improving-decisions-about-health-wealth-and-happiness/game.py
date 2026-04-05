"""
Nudge: Choice Architecture — Interactive Experience
Based on Thaler & Sunstein (2008)

Design environments as a choice architect and watch how
small changes dramatically shift people's decisions.
"""

import random

# ── Environments ───────────────────────────────────────────────────

ENVIRONMENTS = [
    {
        "name": "School Cafeteria",
        "goal": "Increase healthy food choices among students",
        "baseline": 23,  # % choosing healthy option without nudge
        "nudges": [
            {
                "desc": "Put healthy food at eye level, junk food on bottom shelf",
                "type": "Placement / Default visibility",
                "effect": 31,
            },
            {
                "desc": "Label healthy items with a green 'POPULAR PICK' sticker",
                "type": "Social norm + framing",
                "effect": 27,
            },
            {
                "desc": "Make the healthy meal the default combo, with junk as add-on",
                "type": "Default option",
                "effect": 38,
            },
            {
                "desc": "Put up a poster saying 'Eat healthy!'",
                "type": "Information / lecture",
                "effect": 4,
            },
        ],
    },
    {
        "name": "Website Subscription Page",
        "goal": "Get more users to choose the annual plan (better value)",
        "baseline": 18,
        "nudges": [
            {
                "desc": "Pre-select the annual plan as the default",
                "type": "Default option",
                "effect": 34,
            },
            {
                "desc": "Show 'MOST POPULAR' badge on annual plan",
                "type": "Social proof",
                "effect": 22,
            },
            {
                "desc": "Frame it as 'Save £60/year' instead of '£5/month less'",
                "type": "Framing",
                "effect": 18,
            },
            {
                "desc": "Add a detailed comparison table of all plans",
                "type": "More information",
                "effect": 7,
            },
        ],
    },
    {
        "name": "Organ Donor Registration Form",
        "goal": "Increase organ donor sign-ups",
        "baseline": 15,
        "nudges": [
            {
                "desc": "Make organ donation the DEFAULT (opt-out instead of opt-in)",
                "type": "Default option",
                "effect": 62,
            },
            {
                "desc": "Add a message: '89% of people in your area are donors'",
                "type": "Social norm",
                "effect": 24,
            },
            {
                "desc": "Simplify the form to just one tick box",
                "type": "Simplification",
                "effect": 19,
            },
            {
                "desc": "Include a paragraph explaining why donation matters",
                "type": "Rational persuasion",
                "effect": 5,
            },
        ],
    },
]


def show_intro():
    print("=" * 58)
    print("  NUDGE: CHOICE ARCHITECTURE")
    print("  Based on Thaler & Sunstein (2008)")
    print("=" * 58)
    print()
    print("  You are a CHOICE ARCHITECT.")
    print()
    print("  Your job: design environments that guide people")
    print("  toward better decisions — WITHOUT removing options.")
    print()
    print("  For each scenario, pick ONE nudge.")
    print("  See how much it shifts behaviour compared to")
    print("  doing nothing.")
    print()
    input("  Press Enter to start designing...\n")


def run_environment(env):
    print("-" * 58)
    print(f"  ENVIRONMENT: {env['name']}")
    print(f"  Goal: {env['goal']}")
    print(f"  Current rate (no nudge): {env['baseline']}%")
    print("-" * 58)

    print("\n  Choose your nudge:")
    shuffled = env["nudges"][:]
    random.shuffle(shuffled)
    for i, nudge in enumerate(shuffled, 1):
        print(f"    {i}. {nudge['desc']}")

    while True:
        try:
            choice = int(input(f"\n  Your choice (1-{len(shuffled)}): "))
            if 1 <= choice <= len(shuffled):
                chosen = shuffled[choice - 1]
                break
        except ValueError:
            pass
        print(f"  Enter a number from 1 to {len(shuffled)}.")

    new_rate = min(env["baseline"] + chosen["effect"], 97)
    lift = chosen["effect"]

    print(f"\n  You chose: {chosen['desc']}")
    print(f"  Nudge type: {chosen['type']}")
    print()
    print(f"  BEFORE nudge: {env['baseline']}%")

    # Animated bar
    bar_before = "#" * (env["baseline"] // 3) + "." * ((100 - env["baseline"]) // 3)
    bar_after = "#" * (new_rate // 3) + "." * ((100 - new_rate) // 3)
    print(f"    [{bar_before}]")
    print(f"  AFTER nudge:  {new_rate}%")
    print(f"    [{bar_after}]")
    print(f"\n  Lift: +{lift} percentage points")

    if lift >= 30:
        print("  MASSIVE shift — this nudge fundamentally changed")
        print("  the decision landscape.")
    elif lift >= 15:
        print("  Strong shift — a small design change moved a lot")
        print("  of people without anyone being forced.")
    elif lift >= 10:
        print("  Moderate shift — noticeable but there's a stronger")
        print("  nudge you could have used.")
    else:
        print("  Weak shift — giving people information rarely changes")
        print("  behaviour as much as changing the environment does.")

    # Show what would have been best
    best = max(env["nudges"], key=lambda n: n["effect"])
    if chosen != best:
        print(f"\n  The strongest option was: '{best['desc']}'")
        print(f"  ({best['type']} — would have added +{best['effect']}pp)")

    return {
        "name": env["name"],
        "baseline": env["baseline"],
        "chosen_desc": chosen["desc"],
        "chosen_type": chosen["type"],
        "lift": lift,
        "new_rate": new_rate,
        "best_possible": best["effect"],
    }


def debrief(results):
    print("\n" + "=" * 58)
    print("  DEBRIEF — NUDGE THEORY IN ACTION")
    print("=" * 58)

    total_lift = sum(r["lift"] for r in results)
    max_possible = sum(r["best_possible"] for r in results)

    for r in results:
        print(f"\n  {r['name']}:")
        print(f"    {r['baseline']}% --> {r['new_rate']}%  (+{r['lift']}pp)")
        print(f"    Nudge type: {r['chosen_type']}")

    print(f"\n  Your total lift: +{total_lift}pp")
    print(f"  Maximum possible: +{max_possible}pp")

    # Find which nudge types they chose
    types_used = [r["chosen_type"] for r in results]

    print("\n" + "=" * 58)
    print("  THE SCIENCE:")
    print()
    print("  Thaler & Sunstein (2008) showed that CHOICE ARCHITECTURE")
    print("  — how options are presented — shapes decisions far more")
    print("  than information or rational argument.")
    print()
    print("  The most powerful nudges:")
    print()
    print("  1. DEFAULTS — what happens if you do nothing?")
    print("     (Opt-out organ donation: 15% --> 85%+ in Europe)")
    print()
    print("  2. SOCIAL NORMS — what are others doing?")
    print("     ('75% of guests reused towels' beats eco-lectures)")
    print()
    print("  3. FRAMING — how is the same info described?")
    print("     ('90% survival' vs '10% mortality' changes consent)")
    print()
    print("  4. SIMPLIFICATION — remove friction, not options")
    print("     (Auto-enrolment boosted US pension savings 49%-->86%)")
    print()
    print("  Notice: INFORMATION ALONE was always the weakest nudge.")
    print("  Telling people what's good for them rarely works.")
    print("  Changing the environment they decide IN always does.")
    print()

    if total_lift >= max_possible * 0.8:
        print("  You chose powerfully — you have strong instincts")
        print("  for choice architecture.")
    else:
        print("  Look at the pattern: the strongest nudges changed")
        print("  the STRUCTURE of the choice, not the information")
        print("  around it. That's the core lesson of nudge theory.")
    print()


def main():
    show_intro()

    results = []
    for env in ENVIRONMENTS:
        result = run_environment(env)
        results.append(result)
        print()

    debrief(results)


if __name__ == "__main__":
    main()
