"""
Do Defaults Save Lives? — Interactive Experience
Based on Johnson & Goldstein (2003)

Design default policies for multiple domains and witness
the raw power of default settings on human behaviour.
"""

import random


def show_intro():
    print("=" * 60)
    print("  THE DEFAULT EFFECT LAB")
    print("  Based on Johnson & Goldstein (2003)")
    print("=" * 60)
    print()
    print("  You are a policy designer for a small country.")
    print("  For each issue, you'll choose the DEFAULT setting")
    print("  that citizens start with.")
    print()
    print("  Citizens CAN always change their choice.")
    print("  But will they?")
    print()
    print("  Watch what happens when you control the default.")
    print()
    input("  Press Enter to begin...\n")


DOMAINS = [
    {
        "title": "ORGAN DONATION",
        "desc": "Should citizens be organ donors?",
        "opt_in": "Citizens must SIGN UP to be donors (opt-in)",
        "opt_out": "Citizens are donors unless they OPT OUT (opt-out)",
        "opt_in_rate": (12, 20),   # range of participation %
        "opt_out_rate": (86, 99),
        "real_data": (
            "REAL DATA from Johnson & Goldstein (2003):\n"
            "  Opt-in countries (Denmark, UK, Germany): 4-28% donors\n"
            "  Opt-out countries (Austria, France, Sweden): 86-100% donors\n"
            "  Same humans. Same freedom. Different default."
        ),
    },
    {
        "title": "RETIREMENT SAVINGS",
        "desc": "Should employees save part of their salary for retirement?",
        "opt_in": "Employees must ENROL to start saving (opt-in)",
        "opt_out": "Employees save automatically unless they STOP (opt-out)",
        "opt_in_rate": (30, 45),
        "opt_out_rate": (85, 95),
        "real_data": (
            "REAL DATA from Madrian & Shea (2001):\n"
            "  Opt-in enrollment: ~37% of employees saved\n"
            "  Opt-out enrollment: ~86% of employees saved\n"
            "  Most people wanted to save — they just never got around to it."
        ),
    },
    {
        "title": "GREEN ENERGY",
        "desc": "Should households use renewable energy (costs slightly more)?",
        "opt_in": "Households must REQUEST green energy (opt-in)",
        "opt_out": "Households get green energy unless they SWITCH (opt-out)",
        "opt_in_rate": (5, 15),
        "opt_out_rate": (80, 95),
        "real_data": (
            "REAL DATA from Pichert & Katsikopoulos (2008):\n"
            "  Opt-in green energy: ~7% chose it\n"
            "  Opt-out green energy: ~69% stayed with it\n"
            "  People say they care about the environment.\n"
            "  Defaults reveal whether they care enough to act."
        ),
    },
    {
        "title": "PRIVACY SETTINGS",
        "desc": "Should users share their data with third-party advertisers?",
        "opt_in": "Users must AGREE to share data (opt-in / privacy-friendly)",
        "opt_out": "Users share data unless they OPT OUT (opt-out / sharing default)",
        "opt_in_rate": (5, 15),
        "opt_out_rate": (70, 90),
        "real_data": (
            "REAL DATA from multiple studies:\n"
            "  When sharing is opt-in: ~10% agree to share\n"
            "  When sharing is opt-out: ~75% continue sharing\n"
            "  Same people, same preferences, wildly different outcomes.\n"
            "  This is why tech companies fight for opt-out defaults."
        ),
    },
    {
        "title": "FOOD PORTIONS",
        "desc": "A restaurant is setting its default meal size.",
        "opt_in": "Default is REGULAR size — pay more to upgrade (opt-in large)",
        "opt_out": "Default is LARGE size — ask to downsize (opt-out large)",
        "opt_in_rate": (15, 30),
        "opt_out_rate": (65, 85),
        "real_data": (
            "REAL DATA from Wisdom et al. (2016):\n"
            "  When healthier sides were the default, healthy choices\n"
            "  increased significantly even though swapping was free.\n"
            "  Defaults shape what and how much people eat."
        ),
    },
]


def show_bar(value, width=30):
    filled = int((value / 100) * width)
    return "█" * filled + "░" * (width - filled)


def simulate_population(rate_range, population=1000):
    """Simulate individual citizens making choices."""
    base_rate = random.uniform(rate_range[0], rate_range[1]) / 100
    count = 0
    for _ in range(population):
        if random.random() < base_rate:
            count += 1
    return round((count / population) * 100, 1)


def run_domain(domain, domain_num, total):
    print(f"\n{'─' * 60}")
    print(f"  POLICY {domain_num}/{total}: {domain['title']}")
    print(f"{'─' * 60}")
    print(f"\n  {domain['desc']}\n")
    print(f"    1. {domain['opt_in']}")
    print(f"    2. {domain['opt_out']}")

    while True:
        try:
            choice = int(input("\n  Set the default (1 or 2): "))
            if choice in (1, 2):
                break
            print("  Pick 1 or 2.")
        except ValueError:
            print("  Pick 1 or 2.")

    is_opt_out = (choice == 2)

    print("\n  Simulating 1,000 citizens making their choice...")
    print("  (Remember: everyone CAN change the default freely)")
    print()

    if is_opt_out:
        rate = simulate_population(domain["opt_out_rate"])
        label = "participated/stayed in"
    else:
        rate = simulate_population(domain["opt_in_rate"])
        label = "signed up"

    bar = show_bar(rate)
    print(f"  Result: [{bar}] {rate}% {label}")
    print()

    # Now show what the OTHER default would have done
    print("  What if you'd chosen the OTHER default?")
    if is_opt_out:
        alt_rate = simulate_population(domain["opt_in_rate"])
        alt_label = "would have signed up"
    else:
        alt_rate = simulate_population(domain["opt_out_rate"])
        alt_label = "would have stayed in"

    alt_bar = show_bar(alt_rate)
    print(f"  Result: [{alt_bar}] {alt_rate}% {alt_label}")

    diff = abs(rate - alt_rate)
    print(f"\n  Difference: {diff:.1f} percentage points.")
    print(f"  Same people. Same freedom. Different default.")

    return {
        "domain": domain["title"],
        "chose_opt_out": is_opt_out,
        "rate": rate,
        "alt_rate": alt_rate,
        "diff": diff,
        "real_data": domain["real_data"],
    }


def debrief(results):
    print("\n" + "=" * 60)
    print("  YOUR POLICY REPORT")
    print("=" * 60)

    total_diff = 0
    print("\n  DOMAIN-BY-DOMAIN RESULTS:\n")
    for r in results:
        default_type = "opt-out" if r["chose_opt_out"] else "opt-in"
        print(f"  {r['domain']}")
        print(f"    Default: {default_type} | Result: {r['rate']}% | "
              f"Alternative: {r['alt_rate']}% | Gap: {r['diff']:.1f}pp")
        total_diff += r["diff"]

    avg_diff = total_diff / len(results)
    print(f"\n  Average default effect: {avg_diff:.1f} percentage points")
    print(f"  That's how much the default alone shifted behaviour —")
    print(f"  with ZERO change to people's options or freedom.")

    print("\n" + "=" * 60)
    print("  REAL-WORLD EVIDENCE")
    print("=" * 60)
    for r in results:
        print(f"\n  {r['domain']}:")
        print(f"  {r['real_data']}")

    print("\n" + "=" * 60)
    print("  THE SCIENCE")
    print("=" * 60)
    print()
    print("  Johnson & Goldstein (2003) showed that defaults are")
    print("  one of the most powerful forces in decision-making.")
    print()
    print("  WHY do people stick with defaults?")
    print()
    print("    1. EFFORT — changing requires action, and action")
    print("       requires energy most people won't spend")
    print()
    print("    2. IMPLIED RECOMMENDATION — 'if that's the default,")
    print("       it must be the right/normal choice'")
    print()
    print("    3. LOSS AVERSION — switching away from the default")
    print("       feels like giving something up")
    print()
    print("  THE ETHICAL QUESTION:")
    print()
    print("  If most people keep whatever default you set, then")
    print("  setting the default IS making the choice for them.")
    print()
    print("  This means defaults carry moral weight:")
    print("    • Opt-out organ donation saves thousands of lives")
    print("    • Opt-out data sharing profits companies at the")
    print("      expense of privacy")
    print("    • Opt-out retirement saving secures people's futures")
    print()
    print("  The default is never 'neutral.' Whoever sets it")
    print("  is shaping the outcome — whether they admit it or not.")
    print()

    opt_out_count = sum(1 for r in results if r["chose_opt_out"])
    if opt_out_count >= 4:
        print("  You mostly chose opt-out defaults — maximising")
        print("  participation. That's powerful, but with power")
        print("  comes the responsibility to set defaults that")
        print("  genuinely serve people's interests.")
    elif opt_out_count <= 1:
        print("  You mostly chose opt-in defaults — respecting")
        print("  active choice. Noble, but you saw the cost:")
        print("  many people who WOULD have benefited simply")
        print("  never got around to signing up.")
    else:
        print("  You mixed opt-in and opt-out defaults — perhaps")
        print("  using opt-out where it benefits people (saving,")
        print("  donation) and opt-in where it protects them")
        print("  (privacy). That's thoughtful design.")
    print()


def main():
    show_intro()

    results = []
    for i, domain in enumerate(DOMAINS, 1):
        result = run_domain(domain, i, len(DOMAINS))
        results.append(result)

    debrief(results)


if __name__ == "__main__":
    main()
