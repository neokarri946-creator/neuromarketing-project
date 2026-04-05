"""
We Buy What We Wanna Be — Interactive Experience
Based on Xi et al. (2022)

Build your ideal self-profile, then pick brands.
See how your choices mirror who you WANT to be.
"""

import random

# ── Identity Dimensions ────────────────────────────────────────────

TRAITS = [
    {
        "name": "Adventurous vs Comfortable",
        "low": "I prefer comfort, routine, and familiarity",
        "high": "I crave adventure, risk, and new experiences",
    },
    {
        "name": "Minimalist vs Expressive",
        "low": "I prefer simple, understated, clean style",
        "high": "I prefer bold, colourful, expressive style",
    },
    {
        "name": "Independent vs Social",
        "low": "I value independence and going my own way",
        "high": "I value connection, community, and belonging",
    },
    {
        "name": "Practical vs Aspirational",
        "low": "I value practicality and getting things done",
        "high": "I value ambition, vision, and dreaming big",
    },
    {
        "name": "Rebellious vs Traditional",
        "low": "I respect tradition, heritage, and proven quality",
        "high": "I like breaking rules and challenging the norm",
    },
]

# ── Brand Choice Scenarios ─────────────────────────────────────────

BRAND_SCENARIOS = [
    {
        "category": "Smartphone",
        "options": [
            {
                "brand": "Apple iPhone",
                "image": "Sleek, aspirational, creative, premium",
                "profile": {"adventurous": 5, "expressive": 4, "social": 6, "aspirational": 8, "rebellious": 5},
            },
            {
                "brand": "Samsung Galaxy",
                "image": "Innovative, tech-forward, feature-rich, versatile",
                "profile": {"adventurous": 6, "expressive": 5, "social": 5, "aspirational": 6, "rebellious": 4},
            },
            {
                "brand": "Fairphone",
                "image": "Ethical, sustainable, understated, independent-minded",
                "profile": {"adventurous": 4, "expressive": 2, "social": 3, "aspirational": 3, "rebellious": 7},
            },
            {
                "brand": "Nothing Phone",
                "image": "Bold, design-obsessed, counter-culture, statement piece",
                "profile": {"adventurous": 8, "expressive": 9, "social": 4, "aspirational": 6, "rebellious": 9},
            },
        ],
    },
    {
        "category": "Clothing Brand",
        "options": [
            {
                "brand": "Patagonia",
                "image": "Outdoorsy, ethical, adventurous, rugged simplicity",
                "profile": {"adventurous": 9, "expressive": 3, "social": 5, "aspirational": 4, "rebellious": 6},
            },
            {
                "brand": "Zara",
                "image": "Trendy, social, affordable fashion, in-the-moment",
                "profile": {"adventurous": 4, "expressive": 6, "social": 8, "aspirational": 5, "rebellious": 3},
            },
            {
                "brand": "Uniqlo",
                "image": "Minimal, practical, understated quality, no-fuss",
                "profile": {"adventurous": 3, "expressive": 1, "social": 4, "aspirational": 3, "rebellious": 2},
            },
            {
                "brand": "Vivienne Westwood",
                "image": "Punk, rebellious, bold, politically charged fashion",
                "profile": {"adventurous": 7, "expressive": 10, "social": 5, "aspirational": 6, "rebellious": 10},
            },
        ],
    },
    {
        "category": "Car",
        "options": [
            {
                "brand": "Tesla",
                "image": "Futuristic, ambitious, tech-savvy, visionary",
                "profile": {"adventurous": 7, "expressive": 5, "social": 5, "aspirational": 9, "rebellious": 7},
            },
            {
                "brand": "Volvo",
                "image": "Safe, reliable, family-oriented, Scandinavian calm",
                "profile": {"adventurous": 3, "expressive": 2, "social": 6, "aspirational": 4, "rebellious": 2},
            },
            {
                "brand": "Jeep",
                "image": "Rugged, adventurous, free-spirited, off-the-beaten-path",
                "profile": {"adventurous": 10, "expressive": 5, "social": 4, "aspirational": 5, "rebellious": 6},
            },
            {
                "brand": "BMW",
                "image": "Ambitious, status-driven, performance, success",
                "profile": {"adventurous": 5, "expressive": 6, "social": 7, "aspirational": 9, "rebellious": 3},
            },
        ],
    },
    {
        "category": "Coffee Shop",
        "options": [
            {
                "brand": "Starbucks",
                "image": "Social, familiar, community, mainstream comfort",
                "profile": {"adventurous": 3, "expressive": 4, "social": 8, "aspirational": 5, "rebellious": 2},
            },
            {
                "brand": "A local independent roaster",
                "image": "Unique, anti-corporate, craft-focused, connoisseur",
                "profile": {"adventurous": 6, "expressive": 5, "social": 4, "aspirational": 4, "rebellious": 8},
            },
            {
                "brand": "Nespresso",
                "image": "Sleek, premium, efficient, George Clooney sophistication",
                "profile": {"adventurous": 3, "expressive": 5, "social": 5, "aspirational": 8, "rebellious": 3},
            },
            {
                "brand": "Costa",
                "image": "Reliable, no-nonsense, practical, everyday ritual",
                "profile": {"adventurous": 2, "expressive": 2, "social": 6, "aspirational": 3, "rebellious": 2},
            },
        ],
    },
    {
        "category": "Headphones",
        "options": [
            {
                "brand": "Sony WH-1000XM5",
                "image": "Tech-forward, practical excellence, understated quality",
                "profile": {"adventurous": 4, "expressive": 3, "social": 4, "aspirational": 5, "rebellious": 3},
            },
            {
                "brand": "Beats by Dre",
                "image": "Bold, street culture, expressive, status symbol",
                "profile": {"adventurous": 5, "expressive": 8, "social": 8, "aspirational": 6, "rebellious": 5},
            },
            {
                "brand": "Bose QuietComfort",
                "image": "Comfort-first, premium calm, mature, refined",
                "profile": {"adventurous": 2, "expressive": 2, "social": 5, "aspirational": 5, "rebellious": 2},
            },
            {
                "brand": "Marshall Major",
                "image": "Rock-and-roll heritage, retro, rebellious, music purist",
                "profile": {"adventurous": 6, "expressive": 7, "social": 4, "aspirational": 4, "rebellious": 8},
            },
        ],
    },
]

TRAIT_KEYS = ["adventurous", "expressive", "social", "aspirational", "rebellious"]


def show_intro():
    print("=" * 58)
    print("  WE BUY WHAT WE WANNA BE")
    print("  Based on Xi et al. (2022)")
    print("=" * 58)
    print()
    print("  PHASE 1: Build your IDEAL SELF profile.")
    print("  PHASE 2: Choose brands across 5 categories.")
    print("  PHASE 3: See how closely your brand picks")
    print("           matched the person you WANT to be.")
    print()
    input("  Press Enter to begin...\n")


def build_self_profile():
    print("-" * 58)
    print("  PHASE 1: YOUR IDEAL SELF")
    print("  Who do you WANT to be? (Not who you are now —")
    print("  who you aspire to become.)")
    print("-" * 58)

    profile = {}
    for i, trait in enumerate(TRAITS):
        print(f"\n  {trait['name']}:")
        print(f"    1-3 = {trait['low']}")
        print(f"    8-10 = {trait['high']}")
        print(f"    4-7 = somewhere in between")

        while True:
            try:
                val = int(input(f"  Your ideal self (1-10): "))
                if 1 <= val <= 10:
                    profile[TRAIT_KEYS[i]] = val
                    break
                print("  Enter a number from 1 to 10.")
            except ValueError:
                print("  Enter a number from 1 to 10.")

    return profile


def choose_brands(self_profile):
    print("\n" + "-" * 58)
    print("  PHASE 2: BRAND CHOICES")
    print("  Pick the brand that appeals to you most in each")
    print("  category. Go with your gut — don't overthink.")
    print("-" * 58)

    choices = []
    for scenario in BRAND_SCENARIOS:
        print(f"\n  Category: {scenario['category']}")
        options = scenario["options"][:]
        random.shuffle(options)

        for i, opt in enumerate(options, 1):
            print(f"    {i}. {opt['brand']} — {opt['image']}")

        while True:
            try:
                choice = int(input(f"\n  Your pick (1-{len(options)}): "))
                if 1 <= choice <= len(options):
                    chosen = options[choice - 1]
                    break
            except ValueError:
                pass
            print(f"  Enter a number from 1 to {len(options)}.")

        # Calculate congruity score
        match_score = 0
        max_possible = 0
        for key in TRAIT_KEYS:
            diff = abs(self_profile[key] - chosen["profile"][key])
            match_score += (10 - diff)
            max_possible += 10

        congruity = match_score / max_possible * 100

        choices.append({
            "category": scenario["category"],
            "brand": chosen["brand"],
            "image": chosen["image"],
            "profile": chosen["profile"],
            "congruity": congruity,
        })

    return choices


def debrief(self_profile, choices):
    print("\n" + "=" * 58)
    print("  PHASE 3: THE REVEAL")
    print("=" * 58)

    print("\n  Your IDEAL SELF profile:")
    for i, key in enumerate(TRAIT_KEYS):
        bar = "#" * self_profile[key] + "." * (10 - self_profile[key])
        label = TRAITS[i]["name"].split(" vs ")[0] + "/" + TRAITS[i]["name"].split(" vs ")[1]
        print(f"    {label:<30} [{bar}] {self_profile[key]}/10")

    total_congruity = 0
    print("\n  Your brand choices vs your ideal self:")
    print()

    for c in choices:
        total_congruity += c["congruity"]
        match_str = f"{c['congruity']:.0f}%"
        if c["congruity"] >= 75:
            verdict = "STRONG MATCH"
        elif c["congruity"] >= 55:
            verdict = "Moderate match"
        else:
            verdict = "Weak match"

        print(f"  {c['category']}: {c['brand']}")
        print(f"    Brand image: {c['image']}")
        print(f"    Self-congruity: {match_str} — {verdict}")
        print()

    avg_congruity = total_congruity / len(choices)
    print("-" * 58)
    print(f"  AVERAGE SELF-CONGRUITY: {avg_congruity:.0f}%")
    print("-" * 58)

    if avg_congruity >= 70:
        print("\n  Your brand choices strongly mirrored your ideal self.")
        print("  You're buying who you WANT TO BE.")
    elif avg_congruity >= 55:
        print("\n  A moderate match — your ideal self influenced your")
        print("  choices, but other factors (price, habit) also played a role.")
    else:
        print("\n  A weaker match — you may have been choosing on")
        print("  practical grounds rather than identity this time.")

    print("\n" + "=" * 58)
    print("  THE SCIENCE:")
    print()
    print("  Xi et al. (2022) found that consumers consistently")
    print("  choose brands that match their IDEAL SELF — the person")
    print("  they aspire to be — not their actual self.")
    print()
    print("  Three types of value drive the choice:")
    print("  - FUNCTIONAL value (does it work well?)")
    print("  - EMOTIONAL value (does it feel right?)")
    print("  - SOCIAL value (does it look good to others?)")
    print()
    print("  But the KEY MEDIATOR is SELF-CONGRUITY:")
    print("  'Does this brand reflect who I want to become?'")
    print()
    print("  This is why brand storytelling, lifestyle imagery,")
    print("  and aspirational ambassadors beat spec sheets.")
    print("  People don't buy the best product — they buy the")
    print("  product that best reflects their ideal identity.")
    print()
    print("  Emotional and social value predicted purchases MORE")
    print("  strongly than functional value. Feeling right matters")
    print("  more than working right.")
    print()
    if avg_congruity >= 65:
        print("  Your choices demonstrate this perfectly — you")
        print("  consistently gravitated toward brands that matched")
        print("  the identity you built in Phase 1.")
    else:
        print("  Your choices were less identity-driven today,")
        print("  but in large-scale studies, the pattern holds:")
        print("  we buy what we wanna be.")
    print()


def main():
    show_intro()
    self_profile = build_self_profile()
    choices = choose_brands(self_profile)
    debrief(self_profile, choices)


if __name__ == "__main__":
    main()
