"""
Predictably Irrational — Interactive Experience
Based on Ariely (2008)

Experience the decoy effect first-hand: see how adding a
clearly inferior option changes which of two good options
you prefer.
"""

import random


def show_intro():
    print("=" * 58)
    print("  PREDICTABLY IRRATIONAL")
    print("  Based on Ariely (2008)")
    print("=" * 58)
    print()
    print("  You'll make a series of purchasing decisions.")
    print("  Some will have 2 options, some will have 3.")
    print()
    print("  Just go with your gut each time.")
    print("  At the end, we'll reveal what your brain did.")
    print()
    input("  Press Enter to start shopping...\n")


# Each scenario has: two real options and a decoy that makes option B look better
SCENARIOS = [
    {
        "name": "Magazine Subscription",
        "context": "You're subscribing to The Economist.",
        "option_a": {"label": "Digital only", "price": 59, "detail": "Full online access"},
        "option_b": {"label": "Print + Digital", "price": 125, "detail": "Print magazine + full online access"},
        "decoy":   {"label": "Print only", "price": 125, "detail": "Print magazine, no online access"},
        "decoy_helps": "B",
    },
    {
        "name": "Holiday Package",
        "context": "You're choosing between two holiday destinations.",
        "option_a": {"label": "Paris trip", "price": 800, "detail": "Flights + hotel + breakfast"},
        "option_b": {"label": "Rome trip", "price": 800, "detail": "Flights + hotel + breakfast"},
        "decoy":   {"label": "Rome trip (no breakfast)", "price": 800, "detail": "Flights + hotel only"},
        "decoy_helps": "B",
    },
    {
        "name": "Coffee Machine",
        "context": "You're buying a coffee machine for your kitchen.",
        "option_a": {"label": "Basic Brewer", "price": 49, "detail": "Drip coffee, 4-cup capacity"},
        "option_b": {"label": "Barista Pro", "price": 189, "detail": "Espresso, milk frother, 12-cup"},
        "decoy":   {"label": "Barista Lite", "price": 179, "detail": "Espresso only, no frother, 6-cup"},
        "decoy_helps": "B",
    },
    {
        "name": "Gym Membership",
        "context": "You're joining a gym.",
        "option_a": {"label": "Pay-per-visit", "price": 8, "detail": "No commitment, per session"},
        "option_b": {"label": "Annual unlimited", "price": 480, "detail": "All classes + pool + sauna"},
        "decoy":   {"label": "Annual gym-only", "price": 470, "detail": "Gym floor only, no classes/pool/sauna"},
        "decoy_helps": "B",
    },
]


def format_option(number, opt):
    return f"    {number}. {opt['label']} — {opt['detail']} (${opt['price']})"


def get_choice(max_val):
    while True:
        try:
            val = int(input(f"  Your choice (1-{max_val}): "))
            if 1 <= val <= max_val:
                return val
            print(f"  Enter 1 to {max_val}.")
        except ValueError:
            print(f"  Enter 1 to {max_val}.")


def run_scenario_pair(scenario):
    """Run the same scenario twice: once without decoy, once with."""

    results = {}

    # --- Round without decoy ---
    print("-" * 58)
    print(f"  {scenario['name'].upper()}")
    print(f"  {scenario['context']}")
    print("-" * 58)
    print()
    print(format_option(1, scenario["option_a"]))
    print(format_option(2, scenario["option_b"]))
    print()

    choice_no_decoy = get_choice(2)
    if choice_no_decoy == 1:
        results["without_decoy"] = "A"
        chosen_label = scenario["option_a"]["label"]
    else:
        results["without_decoy"] = "B"
        chosen_label = scenario["option_b"]["label"]

    print(f"  --> You chose: {chosen_label}")
    print()

    return results


def run_scenario_with_decoy(scenario):
    """Run with the decoy present."""
    print("-" * 58)
    print(f"  {scenario['name'].upper()} (different presentation)")
    print(f"  {scenario['context']}")
    print("-" * 58)
    print()

    # Shuffle the order but track positions
    options = [
        ("A", scenario["option_a"]),
        ("B", scenario["option_b"]),
        ("D", scenario["decoy"]),
    ]
    random.shuffle(options)

    position_map = {}
    for i, (tag, opt) in enumerate(options, 1):
        print(format_option(i, opt))
        position_map[i] = tag
    print()

    choice = get_choice(3)
    tag = position_map[choice]

    if tag == "A":
        chosen_label = scenario["option_a"]["label"]
        result = "A"
    elif tag == "B":
        chosen_label = scenario["option_b"]["label"]
        result = "B"
    else:
        chosen_label = scenario["decoy"]["label"]
        result = "D"

    print(f"  --> You chose: {chosen_label}")
    print()

    return result


def debrief(results):
    print("\n" + "=" * 58)
    print("  DEBRIEF — THE DECOY EFFECT IN ACTION")
    print("=" * 58)

    decoy_worked = 0
    total_scenarios = len(results)

    for scenario_name, data in results.items():
        without = data["without"]
        with_d = data["with"]
        decoy_target = data["decoy_helps"]

        print(f"\n  {scenario_name}")
        print(f"    Without decoy: chose option {without}")
        print(f"    With decoy:    chose option {with_d}")

        if without != decoy_target and with_d == decoy_target:
            print(f"    >> DECOY EFFECT! The dummy option pulled you toward {decoy_target}.")
            decoy_worked += 1
        elif with_d == "D":
            print(f"    >> You chose the decoy itself — that's unusual!")
        elif without == with_d:
            print(f"    >> Same choice both times — you weren't swayed.")
        elif without == decoy_target and with_d != decoy_target:
            print(f"    >> You moved AWAY from the decoy's target — contrarian!")
        else:
            print(f"    >> Your preference shifted, though not in the typical pattern.")

    print("\n" + "=" * 58)
    pct = (decoy_worked / total_scenarios) * 100 if total_scenarios > 0 else 0
    print(f"  DECOY SUCCESS RATE: {decoy_worked}/{total_scenarios} ({pct:.0f}%)")
    print("=" * 58)

    print()
    print("  THE SCIENCE:")
    print()
    print("  Ariely showed that adding a clearly inferior option (the")
    print("  'decoy') changes how people choose between the other two.")
    print()
    print("  Example from his most famous experiment:")
    print("    A. Digital only — $59")
    print("    B. Print + Digital — $125")
    print("    C. Print only — $125  (the decoy)")
    print()
    print("  Nobody picks C. But its PRESENCE makes B look like a")
    print("  bargain ('I get digital FREE!'). Without C, most people")
    print("  picked A. With C, most switched to B.")
    print()
    print("  WHY? Because our brains struggle with absolute value.")
    print("  We evaluate options RELATIVE to each other. The decoy")
    print("  gives your brain an easy comparison that makes the")
    print("  target option look obviously superior.")
    print()
    print("  WHERE YOU SEE THIS:")
    print()
    print("  - Subscription tiers (basic / pro / enterprise)")
    print("  - 'Was $99, now $59' — the old price is the decoy")
    print("  - Small / Medium / Large drinks — medium is often the decoy")
    print("  - Estate agents showing a bad house before the one they")
    print("    actually want to sell you")
    print()
    print("  Your irrationality isn't random. It's predictable.")
    print("  And that makes it exploitable.")
    print()


def main():
    show_intro()

    selected = random.sample(SCENARIOS, min(3, len(SCENARIOS)))
    all_results = {}

    # Phase 1: All scenarios WITHOUT decoys
    print("=" * 58)
    print("  PHASE 1: Initial Choices")
    print("=" * 58)
    print()

    without_results = {}
    for scenario in selected:
        result = run_scenario_pair(scenario)
        without_results[scenario["name"]] = result["without_decoy"]

    input("  Press Enter for Phase 2...\n")

    # Phase 2: Same scenarios WITH decoys
    print("=" * 58)
    print("  PHASE 2: Choose Again (slightly different options)")
    print("=" * 58)
    print()
    print("  You'll see the same scenarios with a new option added.")
    print("  Just pick whichever appeals to you most.")
    print()

    for scenario in selected:
        with_result = run_scenario_with_decoy(scenario)
        all_results[scenario["name"]] = {
            "without": without_results[scenario["name"]],
            "with": with_result,
            "decoy_helps": scenario["decoy_helps"],
        }

    debrief(all_results)


if __name__ == "__main__":
    main()
