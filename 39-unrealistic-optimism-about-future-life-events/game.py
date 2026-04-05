"""
Unrealistic Optimism About Future Life Events — Interactive Experience
Based on Weinstein (1980)

Discover your own optimism bias by estimating your likelihood
of positive and negative life events compared to average.
"""

import random

EVENTS = [
    # (event, is_negative, base_rate_description)
    ("Developing heart disease before age 50", True,
     "About 1 in 20 people develop heart disease before 50."),
    ("Getting divorced (if you marry)", True,
     "Roughly 42% of marriages in the UK end in divorce."),
    ("Being made redundant at some point in your career", True,
     "About 1 in 3 workers experience redundancy."),
    ("Developing a serious mental health condition", True,
     "1 in 4 people experience a mental health problem each year."),
    ("Having a car accident in the next 10 years", True,
     "About 1 in 3 drivers will have an accident in a 10-year period."),
    ("Being a victim of a burglary", True,
     "About 2% of households are burgled each year in the UK."),
    ("Developing type 2 diabetes", True,
     "About 1 in 10 people will develop type 2 diabetes."),
    ("Owning your own home by age 40", False,
     "About 50% of under-40s own their home in the UK."),
    ("Earning above the national average salary", False,
     "By definition, about 50% earn above the median."),
    ("Living past age 80", False,
     "About 60% of people in the UK live to 80 or beyond."),
    ("Having a job you genuinely enjoy", False,
     "Surveys suggest about 40% of workers feel engaged at work."),
    ("Staying in good health into your 70s", False,
     "About 55% of people report good health at age 70."),
    ("Maintaining a close friendship for 20+ years", False,
     "About 50% of close friendships survive two decades."),
    ("Travelling to 10+ countries in your lifetime", False,
     "The average Brit visits about 7 countries in their lifetime."),
]


def show_intro():
    print("=" * 58)
    print("  UNREALISTIC OPTIMISM")
    print("  Based on Weinstein (1980)")
    print("=" * 58)
    print()
    print("  For each life event, you'll estimate YOUR chance")
    print("  compared to the AVERAGE person your age.")
    print()
    print("  Rate on this scale:")
    print()
    print("  -3 = Much LESS likely than average")
    print("  -2 = Moderately less likely")
    print("  -1 = Slightly less likely")
    print("   0 = About the same as average")
    print("  +1 = Slightly MORE likely than average")
    print("  +2 = Moderately more likely")
    print("  +3 = Much more likely than average")
    print()
    print("  Be honest — go with your gut feeling.")
    print()
    input("  Press Enter to begin...\n")


def get_rating():
    while True:
        try:
            val = int(input("  Your rating (-3 to +3): ").strip().replace("+", ""))
            if -3 <= val <= 3:
                return val
            print("  Please enter a number from -3 to +3.")
        except ValueError:
            print("  Please enter a number from -3 to +3.")


def run_events(events):
    results = []
    for i, (event, is_negative, base_rate) in enumerate(events, 1):
        print("-" * 58)
        if is_negative:
            print(f"\n  NEGATIVE EVENT #{i}")
        else:
            print(f"\n  POSITIVE EVENT #{i}")
        print(f"\n  \"{event}\"")
        print()
        print(f"  Compared to the average person your age,")
        print(f"  how likely is this to happen to YOU?")
        print()

        rating = get_rating()
        results.append({
            "event": event,
            "negative": is_negative,
            "rating": rating,
            "base_rate": base_rate,
        })
        print()

    return results


def show_bar(value, label="", width=7):
    """Show a visual bar for -3 to +3 range."""
    mid = width
    if value < 0:
        bar = " " * (mid + value) + "◄" + "█" * abs(value) + " " * mid
    elif value > 0:
        bar = " " * mid + "█" * value + "►" + " " * (mid - value)
    else:
        bar = " " * mid + "●" + " " * mid
    return f"  {label:<45} [{bar}] {value:+d}"


def debrief(results):
    neg_results = [r for r in results if r["negative"]]
    pos_results = [r for r in results if not r["negative"]]

    neg_avg = sum(r["rating"] for r in neg_results) / len(neg_results) if neg_results else 0
    pos_avg = sum(r["rating"] for r in pos_results) / len(pos_results) if pos_results else 0

    # Count optimistic responses
    optimistic_neg = sum(1 for r in neg_results if r["rating"] < 0)  # think bad less likely
    optimistic_pos = sum(1 for r in pos_results if r["rating"] > 0)  # think good more likely
    total_optimistic = optimistic_neg + optimistic_pos
    total_events = len(results)

    print("\n" + "=" * 58)
    print("  DEBRIEF — YOUR OPTIMISM PROFILE")
    print("=" * 58)

    print("\n  YOUR RATINGS:")
    print()
    print("  NEGATIVE EVENTS (bad things):")
    for r in neg_results:
        direction = "← less likely" if r["rating"] < 0 else ("→ more likely" if r["rating"] > 0 else "= average")
        marker = " ★" if r["rating"] < 0 else ""
        print(f"    {r['event'][:42]:<44} {r['rating']:+d} {direction}{marker}")
    print(f"\n    Average rating: {neg_avg:+.1f}")
    if neg_avg < 0:
        print("    ↑ You think bad things are LESS likely for you (optimistic)")
    elif neg_avg > 0:
        print("    ↑ You think bad things are MORE likely for you (pessimistic)")
    else:
        print("    ↑ You rated yourself as average")

    print()
    print("  POSITIVE EVENTS (good things):")
    for r in pos_results:
        direction = "← less likely" if r["rating"] < 0 else ("→ more likely" if r["rating"] > 0 else "= average")
        marker = " ★" if r["rating"] > 0 else ""
        print(f"    {r['event'][:42]:<44} {r['rating']:+d} {direction}{marker}")
    print(f"\n    Average rating: {pos_avg:+.1f}")
    if pos_avg > 0:
        print("    ↑ You think good things are MORE likely for you (optimistic)")
    elif pos_avg < 0:
        print("    ↑ You think good things are LESS likely for you (pessimistic)")
    else:
        print("    ↑ You rated yourself as average")

    print()
    print(f"  OPTIMISM SCORE: {total_optimistic}/{total_events} responses")
    print(f"  showed optimistic bias (★ marked above)")

    # The impossibility argument
    print()
    print("=" * 58)
    print("  THE STATISTICAL IMPOSSIBILITY")
    print("=" * 58)
    print()
    print("  Here's the problem:")
    print()
    print("  If EVERYONE rates themselves as less likely than")
    print("  average to get divorced, have an accident, or get")
    print("  ill... and MORE likely than average to own a home,")
    print("  earn well, and live long...")
    print()
    print("  ...then MOST PEOPLE ARE WRONG.")
    print()
    print("  By definition, roughly half of people must be above")
    print("  average and half below. We can't all be special.")
    print()

    # Show the real base rates
    print("  THE REAL BASE RATES:")
    print()
    for r in results:
        print(f"    {r['event'][:42]}")
        print(f"    Reality: {r['base_rate']}")
        print()

    print("=" * 58)
    print("  WHAT WEINSTEIN FOUND")
    print("=" * 58)
    print()
    print("  In 1980, Weinstein showed that optimism bias is:")
    print()
    print("  • UNIVERSAL — the vast majority of people show it")
    print("  • SYSTEMATIC — strongest for events we feel we can")
    print("    control, and for events we haven't experienced")
    print("  • RESISTANT TO CORRECTION — even showing people")
    print("    the base rates barely budges their estimates")
    print()
    print("  WHY THIS MATTERS FOR MARKETING:")
    print()
    print("  • Fear-based ads often fail because people think")
    print("    'that won't happen to ME'")
    print("  • Aspirational marketing works because people")
    print("    already believe good outcomes are coming their way")
    print("  • Insurance is chronically under-bought because")
    print("    people underestimate personal risk")
    print("  • Making risk feel PERSONAL ('1 in 3 people in")
    print("    this room') works better than abstract statistics")
    print()


def main():
    show_intro()

    # Select a balanced subset
    neg_events = [e for e in EVENTS if e[1]]
    pos_events = [e for e in EVENTS if not e[1]]
    selected = random.sample(neg_events, min(4, len(neg_events))) + \
               random.sample(pos_events, min(4, len(pos_events)))
    random.shuffle(selected)

    results = run_events(selected)
    debrief(results)


if __name__ == "__main__":
    main()
