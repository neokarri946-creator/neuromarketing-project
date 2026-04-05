"""
AI-Powered Personalization — Interactive Experience
Based on the 2025 study on consumer perceptions, trust, and purchase decisions

You ARE the recommendation algorithm. Dial personalization up or down
and find the sweet spot before crossing into creepy.
"""

import random

CUSTOMERS = [
    {"name": "Alex", "age": 28, "sensitivity": "low", "threshold": 7},
    {"name": "Jordan", "age": 45, "sensitivity": "medium", "threshold": 5},
    {"name": "Sam", "age": 33, "sensitivity": "high", "threshold": 3},
    {"name": "Taylor", "age": 22, "sensitivity": "low", "threshold": 8},
    {"name": "Morgan", "age": 55, "sensitivity": "high", "threshold": 4},
    {"name": "Casey", "age": 38, "sensitivity": "medium", "threshold": 6},
]

PERSONALIZATION_LEVELS = {
    1: {
        "label": "Generic",
        "desc": "Show bestsellers — same for everyone",
        "customer_reaction": "Meh. This could be anyone's homepage.",
    },
    2: {
        "label": "Category-based",
        "desc": "Recommend based on broad category they browsed",
        "customer_reaction": "Okay, at least it's in the right ballpark.",
    },
    3: {
        "label": "Purchase history",
        "desc": "Suggest items similar to what they've bought before",
        "customer_reaction": "Nice, this actually matches my taste.",
    },
    4: {
        "label": "Browsing patterns",
        "desc": "Use their click patterns and time spent on items",
        "customer_reaction": "Pretty spot-on. How did it know I liked that?",
    },
    5: {
        "label": "Cross-site tracking",
        "desc": "Use data from their activity on OTHER websites",
        "customer_reaction": "Wait... I was looking at this on a different site.",
    },
    6: {
        "label": "Inferred personal data",
        "desc": "Deduce their income, relationships, life events from patterns",
        "customer_reaction": "How does it know I just moved house? I never told them.",
    },
    7: {
        "label": "Predictive intimate",
        "desc": "Predict what they'll want before they know they want it",
        "customer_reaction": "This is unsettling. It's like it's reading my mind.",
    },
    8: {
        "label": "Deep surveillance",
        "desc": "Use location, messages, voice data — everything available",
        "customer_reaction": "This is way too much. I'm deleting this app.",
    },
}


def show_intro():
    print("=" * 60)
    print("  THE PERSONALIZATION ENGINE")
    print("  Based on AI Personalization & Consumer Trust (2025)")
    print("=" * 60)
    print()
    print("  You are an AI recommendation system.")
    print("  Customers are visiting your e-commerce platform.")
    print()
    print("  For each customer, you choose HOW PERSONALIZED")
    print("  your recommendations should be (level 1-8).")
    print()
    print("  Too generic = they ignore you.")
    print("  Too personal = they get creeped out and leave.")
    print()
    print("  Find the sweet spot for each customer.")
    print()
    input("  Press Enter to start...\n")


def calculate_response(level, customer):
    threshold = customer["threshold"]

    if level <= 1:
        trust = 40
        purchase_chance = 10
    elif level <= threshold:
        # In the sweet zone — trust and purchases climb
        progress = level / threshold
        trust = int(40 + progress * 50)
        purchase_chance = int(10 + progress * 60)
    elif level == threshold + 1:
        # Just past the line — slight discomfort
        trust = 55
        purchase_chance = 35
    else:
        # Deep into creepy territory
        overshoot = level - threshold
        trust = max(5, 55 - overshoot * 18)
        purchase_chance = max(2, 35 - overshoot * 15)

    # Add some noise
    trust = max(0, min(100, trust + random.randint(-5, 5)))
    purchase_chance = max(0, min(100, purchase_chance + random.randint(-5, 5)))

    return trust, purchase_chance


def show_bar(value, width=25):
    filled = int((value / 100) * width)
    return "█" * filled + "░" * (width - filled)


def run_customer(customer, round_num, total):
    print(f"\n{'─' * 60}")
    print(f"  CUSTOMER {round_num}/{total}: {customer['name']}, age {customer['age']}")
    print(f"  Privacy sensitivity: {customer['sensitivity'].upper()}")
    print(f"{'─' * 60}")

    print("\n  PERSONALIZATION LEVELS:")
    for lvl in range(1, 9):
        info = PERSONALIZATION_LEVELS[lvl]
        print(f"    {lvl}. {info['label']:<22} — {info['desc']}")

    while True:
        try:
            choice = int(input(f"\n  Set personalization level (1-8): "))
            if 1 <= choice <= 8:
                break
            print("  Pick a level from 1 to 8.")
        except ValueError:
            print("  Pick a level from 1 to 8.")

    level_info = PERSONALIZATION_LEVELS[choice]
    trust, purchase = calculate_response(choice, customer)

    print(f"\n  You chose: Level {choice} — {level_info['label']}")
    print(f"  \"{level_info['customer_reaction']}\"")
    print()
    print(f"  Trust:     [{show_bar(trust)}] {trust}%")
    print(f"  Purchase:  [{show_bar(purchase)}] {purchase}%")

    bought = random.randint(1, 100) <= purchase
    if bought:
        print(f"\n  >> {customer['name']} BOUGHT something!")
    else:
        print(f"\n  >> {customer['name']} left without buying.")

    if choice > customer["threshold"] + 1:
        print(f"  >> {customer['name']} also unsubscribed from emails.")

    return {
        "name": customer["name"],
        "sensitivity": customer["sensitivity"],
        "threshold": customer["threshold"],
        "level_chosen": choice,
        "trust": trust,
        "purchase_pct": purchase,
        "bought": bought,
        "was_creepy": choice > customer["threshold"],
    }


def debrief(results):
    print("\n" + "=" * 60)
    print("  YOUR PERFORMANCE REPORT")
    print("=" * 60)

    total_bought = sum(1 for r in results if r["bought"])
    total_creeped = sum(1 for r in results if r["was_creepy"])
    avg_trust = sum(r["trust"] for r in results) / len(results)

    print(f"\n  Customers served:    {len(results)}")
    print(f"  Purchases made:      {total_bought}/{len(results)}")
    print(f"  Creeped out:         {total_creeped}/{len(results)}")
    print(f"  Average trust:       {avg_trust:.0f}%")

    print("\n  CUSTOMER-BY-CUSTOMER:")
    for r in results:
        status = "BOUGHT" if r["bought"] else "passed"
        creep = " (CREEPY)" if r["was_creepy"] else ""
        sweet = r["threshold"]
        print(f"    {r['name']:<8} Level {r['level_chosen']} chosen | "
              f"Sweet spot was ~{sweet} | Trust {r['trust']}% | {status}{creep}")

    print("\n" + "=" * 60)
    print("  THE SCIENCE")
    print("=" * 60)
    print()
    print("  This 2025 study found that AI personalization and")
    print("  purchase likelihood form an INVERTED U-SHAPE:")
    print()
    print("  Purchase")
    print("  Intent")
    print("    ^")
    print("    |      .-~~~-.")
    print("    |    /         \\")
    print("    |   /           \\")
    print("    |  /     SWEET   \\")
    print("    | /      SPOT     \\")
    print("    |/                  \\___")
    print("    +------------------------>")
    print("    Generic    |    Creepy")
    print("          Personalization")
    print()
    print("  KEY FINDINGS:")
    print("  • Trust is the GATEWAY — personalization only boosts")
    print("    sales when consumers trust the system")
    print("  • Over-personalization triggers a 'creepiness effect'")
    print("    that DESTROYS trust — worse than no personalization")
    print("  • Different people have different thresholds — privacy-")
    print("    sensitive people hit the creep wall much sooner")
    print("  • Transparency helps: 'We suggest this because you")
    print("    bought X' feels less creepy than silent inference")
    print()
    if total_creeped == 0 and total_bought >= 4:
        print("  You nailed the sweet spot — high trust, good sales,")
        print("  no creepiness. That's the optimal strategy.")
    elif total_creeped >= 3:
        print("  You pushed too hard — the creepiness effect kicked in.")
        print("  More data doesn't always mean better outcomes.")
    else:
        print("  You found the balance is tricky — each customer has")
        print("  a different comfort zone, and the cost of overshooting")
        print("  is much higher than the cost of undershooting.")
    print()


def main():
    show_intro()

    selected = random.sample(CUSTOMERS, 5)
    results = []

    for i, customer in enumerate(selected, 1):
        result = run_customer(customer, i, len(selected))
        results.append(result)

    debrief(results)


if __name__ == "__main__":
    main()
