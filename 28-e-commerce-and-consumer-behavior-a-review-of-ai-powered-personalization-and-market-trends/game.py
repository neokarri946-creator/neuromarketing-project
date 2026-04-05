"""
E-commerce AI Personalization Manager — Interactive Experience
Based on the 2024 review of AI-powered personalization and market trends

Manage an e-commerce store: decide how much data to collect,
how transparent to be, and how aggressively to personalize.
Balance sales against customer trust.
"""

import random


def show_intro():
    print("=" * 60)
    print("  THE E-COMMERCE AI MANAGER")
    print("  Based on AI Personalization & Market Trends (2024)")
    print("=" * 60)
    print()
    print("  You run an online shop with 3 AI systems:")
    print("    1. Recommendation Engine — suggests products")
    print("    2. Dynamic Pricing — adjusts prices per customer")
    print("    3. Targeted Marketing — personalised ads & emails")
    print()
    print("  Each quarter, you'll configure these systems.")
    print("  Your choices affect SALES and TRUST.")
    print()
    print("  If trust drops too low, customers leave for good.")
    print("  If sales stay too low, your business fails.")
    print()
    print("  Survive 4 quarters and build a thriving store.")
    print()
    input("  Press Enter to start...\n")


QUARTERS = [
    {
        "title": "Q1 — DATA COLLECTION POLICY",
        "context": "You're setting up your data infrastructure.",
        "question": "How much customer data will you collect?",
        "options": [
            {
                "text": "Minimal — just purchase history and basic preferences",
                "data_quality": 30,
                "trust_mod": 10,
                "sales_mod": -5,
            },
            {
                "text": "Moderate — browsing, purchases, stated preferences with clear consent",
                "data_quality": 65,
                "trust_mod": 5,
                "sales_mod": 10,
            },
            {
                "text": "Maximum — track everything possible, bury consent in T&Cs",
                "data_quality": 90,
                "trust_mod": -15,
                "sales_mod": 15,
            },
        ],
    },
    {
        "title": "Q2 — RECOMMENDATION ENGINE",
        "context": "Your recommendation engine is live. Time to tune it.",
        "question": "How should recommendations work?",
        "options": [
            {
                "text": "Simple — 'Customers also bought...' with clear explanation",
                "data_quality": 0,
                "trust_mod": 8,
                "sales_mod": 10,
            },
            {
                "text": "Smart — deep pattern matching, explain reasoning when asked",
                "data_quality": 0,
                "trust_mod": 3,
                "sales_mod": 20,
            },
            {
                "text": "Aggressive — predict needs before they arise, no explanation",
                "data_quality": 0,
                "trust_mod": -12,
                "sales_mod": 25,
            },
        ],
    },
    {
        "title": "Q3 — DYNAMIC PRICING",
        "context": "You can now adjust prices per customer in real time.",
        "question": "How will you use dynamic pricing?",
        "options": [
            {
                "text": "Don't use it — same price for everyone, always",
                "data_quality": 0,
                "trust_mod": 10,
                "sales_mod": 0,
            },
            {
                "text": "Gentle — small discounts for hesitant buyers, transparent surge pricing",
                "data_quality": 0,
                "trust_mod": 2,
                "sales_mod": 15,
            },
            {
                "text": "Full optimisation — charge each person the maximum they'll pay",
                "data_quality": 0,
                "trust_mod": -20,
                "sales_mod": 25,
            },
        ],
    },
    {
        "title": "Q4 — TARGETED MARKETING",
        "context": "A journalist has written about 'creepy algorithms.' Customers are nervous.",
        "question": "How do you handle your marketing AI now?",
        "options": [
            {
                "text": "Pull back — reduce targeting, publish a transparency report",
                "data_quality": 0,
                "trust_mod": 18,
                "sales_mod": -10,
            },
            {
                "text": "Reframe — add 'Why am I seeing this?' buttons, keep targeting moderate",
                "data_quality": 0,
                "trust_mod": 12,
                "sales_mod": 5,
            },
            {
                "text": "Ignore it — double down on targeting, the controversy will pass",
                "data_quality": 0,
                "trust_mod": -18,
                "sales_mod": 10,
            },
        ],
    },
]


def show_bar(value, width=25, label=""):
    clamped = max(0, min(100, value))
    filled = int((clamped / 100) * width)
    bar = "█" * filled + "░" * (width - filled)
    return f"  {label:<12} [{bar}] {clamped}%"


def run_quarter(quarter, trust, sales, data_quality):
    print(f"\n{'─' * 60}")
    print(f"  {quarter['title']}")
    print(f"{'─' * 60}")
    print(f"\n  {quarter['context']}")
    print()
    print(show_bar(trust, label="Trust"))
    print(show_bar(sales, label="Sales"))
    print(f"\n  {quarter['question']}\n")

    for i, opt in enumerate(quarter["options"], 1):
        print(f"    {i}. {opt['text']}")

    while True:
        try:
            choice = int(input(f"\n  Your choice (1/2/3): "))
            if 1 <= choice <= 3:
                break
            print("  Pick 1, 2, or 3.")
        except ValueError:
            print("  Pick 1, 2, or 3.")

    opt = quarter["options"][choice - 1]

    # Data quality affects how well personalization works
    if opt["data_quality"] > 0:
        data_quality = opt["data_quality"]

    # Poor data quality reduces sales benefit and can hurt trust
    quality_factor = data_quality / 100 if data_quality > 0 else 0.5
    effective_sales = int(opt["sales_mod"] * (0.5 + 0.5 * quality_factor))

    trust += opt["trust_mod"] + random.randint(-3, 3)
    sales += effective_sales + random.randint(-3, 3)

    trust = max(0, min(100, trust))
    sales = max(0, min(100, sales))

    print(f"\n  Decision made.")
    print(show_bar(trust, label="Trust"))
    print(show_bar(sales, label="Sales"))

    if trust < 20:
        print("\n  WARNING: Trust is critically low!")
        print("  Customers are actively telling friends to avoid your store.")
    elif trust < 40:
        print("\n  CAUTION: Trust is falling. Customers are getting uneasy.")

    return trust, sales, data_quality, choice


def debrief(trust, sales, data_quality, choices):
    print("\n" + "=" * 60)
    print("  ANNUAL PERFORMANCE REVIEW")
    print("=" * 60)

    print(f"\n  Final Trust:        {trust}%")
    print(f"  Final Sales:        {sales}%")
    print(f"  Data Quality:       {data_quality}%")

    # Calculate overall health
    health = (trust * 0.6 + sales * 0.4)  # trust weighted more heavily long-term

    print(f"\n  Business Health:    {health:.0f}%")

    if health >= 70:
        print("\n  VERDICT: Thriving.")
        print("  Your store has strong sales AND customer loyalty.")
        print("  Sustainable long-term growth ahead.")
    elif health >= 50:
        print("\n  VERDICT: Surviving.")
        print("  Decent numbers, but cracks are showing.")
        print("  One more trust hit could spiral into decline.")
    elif health >= 30:
        print("\n  VERDICT: Struggling.")
        print("  Either customers don't trust you or sales are weak.")
        print("  Major course correction needed.")
    else:
        print("\n  VERDICT: Failing.")
        print("  Your store is bleeding customers and credibility.")
        print("  The AI systems did more harm than good.")

    print("\n" + "=" * 60)
    print("  THE SCIENCE")
    print("=" * 60)
    print()
    print("  This 2024 review found that AI personalization in")
    print("  e-commerce works through three channels:")
    print()
    print("    1. RECOMMENDATION ENGINES — suggest products")
    print("    2. DYNAMIC PRICING — adjust prices per person")
    print("    3. TARGETED MARKETING — personalised ads/emails")
    print()
    print("  But effectiveness depends on THREE conditions:")
    print()
    print("    • DATA QUALITY — bad data = bad recommendations")
    print("      = eroded trust (worse than no personalization)")
    print()
    print("    • ALGORITHM TRANSPARENCY — 'Why this suggestion?'")
    print("      builds trust. Silent inference breeds suspicion.")
    print()
    print("    • PRIVACY BALANCE — collecting more data improves")
    print("      accuracy but risks crossing the line into")
    print("      surveillance that drives customers away.")
    print()
    print("  The review warned that as regulations like the EU")
    print("  AI Act tighten, companies that built trust-first")
    print("  personalization will thrive — while those that")
    print("  maximised extraction will scramble to comply.")
    print()
    print("  The game you just played reflects this: aggressive")
    print("  tactics boost short-term sales but erode the trust")
    print("  that sustains long-term business health.")
    print()


def main():
    show_intro()

    trust = 60
    sales = 40
    data_quality = 0
    choices = []

    for quarter in QUARTERS:
        trust, sales, data_quality, choice = run_quarter(
            quarter, trust, sales, data_quality
        )
        choices.append(choice)

    debrief(trust, sales, data_quality, choices)


if __name__ == "__main__":
    main()
