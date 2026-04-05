"""
The Consumer Behavior of Luxury Goods — Interactive Experience
Based on Dhaliwal et al. (2020)

Run a luxury brand and make strategic decisions about exclusivity,
heritage, and sustainability. See how different consumer segments react.
"""

import random

SEGMENTS = {
    "Status Seekers": {
        "desc": "Want luxury to signal wealth and social position",
        "weights": {"exclusivity": 3, "heritage": 1, "sustainability": -1, "digital": 1},
    },
    "Uniqueness Hunters": {
        "desc": "Want to stand out and express individuality",
        "weights": {"exclusivity": 2, "heritage": 0, "sustainability": 1, "digital": -1},
    },
    "Heritage Purists": {
        "desc": "Value craftsmanship, tradition, and brand story",
        "weights": {"exclusivity": 1, "heritage": 3, "sustainability": 0, "digital": -2},
    },
    "Conscious Luxurists": {
        "desc": "Want premium quality with ethical responsibility",
        "weights": {"exclusivity": 0, "heritage": 1, "sustainability": 3, "digital": 1},
    },
    "Digital Natives": {
        "desc": "Discover and buy luxury primarily through social media",
        "weights": {"exclusivity": -1, "heritage": 0, "sustainability": 1, "digital": 3},
    },
}

SCENARIOS = [
    {
        "title": "YEAR 1 — DISTRIBUTION STRATEGY",
        "question": "How widely should your products be available?",
        "options": [
            ("Open flagship stores in every major city and sell online globally", {"exclusivity": -2, "digital": 2}),
            ("Keep only 5 boutiques worldwide — invite-only online access", {"exclusivity": 3, "digital": -1}),
            ("Selective retailers plus a curated online experience", {"exclusivity": 1, "digital": 1}),
        ],
    },
    {
        "title": "YEAR 2 — PRODUCT IDENTITY",
        "question": "What story does your brand tell?",
        "options": [
            ("Lean into 100-year heritage — handmade, traditional methods only", {"heritage": 3, "sustainability": 0}),
            ("Reinvent with bold modern designs — break from the past", {"heritage": -2, "sustainability": 0}),
            ("Honour the craft tradition but reinterpret it for modern tastes", {"heritage": 1, "sustainability": 1}),
        ],
    },
    {
        "title": "YEAR 3 — SUSTAINABILITY MOVE",
        "question": "Your competitors are making sustainability pledges. What do you do?",
        "options": [
            ("Launch a fully sustainable line — recycled materials, carbon neutral", {"sustainability": 3, "exclusivity": -1}),
            ("Ignore it — true luxury is about rare materials and indulgence", {"sustainability": -2, "exclusivity": 1}),
            ("Integrate sustainability quietly — better sourcing, no greenwashing", {"sustainability": 2, "exclusivity": 0}),
        ],
    },
    {
        "title": "YEAR 4 — SOCIAL MEDIA DILEMMA",
        "question": "A massive influencer wants to promote your brand to 20 million followers.",
        "options": [
            ("Partner enthusiastically — massive exposure is always good", {"digital": 3, "exclusivity": -2}),
            ("Decline — your brand doesn't need influencers, it needs mystique", {"digital": -2, "exclusivity": 2}),
            ("Collaborate on a limited exclusive piece — controlled exposure", {"digital": 1, "exclusivity": 1}),
        ],
    },
    {
        "title": "YEAR 5 — PRICING CRISIS",
        "question": "A recession hits. Sales are slipping. What's your move?",
        "options": [
            ("Launch a more affordable 'diffusion' line to capture volume", {"exclusivity": -3, "digital": 1}),
            ("Raise prices and cut production — become even more exclusive", {"exclusivity": 3, "heritage": 1}),
            ("Hold prices steady but add more value — better packaging, service", {"exclusivity": 0, "heritage": 1}),
        ],
    },
]


def show_intro():
    print("=" * 60)
    print("  THE LUXURY BRAND SIMULATOR")
    print("  Based on Dhaliwal et al. (2020)")
    print("=" * 60)
    print()
    print("  You're the CEO of a luxury fashion house.")
    print("  Over 5 years, you'll face strategic decisions about:")
    print()
    print("    • Exclusivity vs Accessibility")
    print("    • Heritage vs Innovation")
    print("    • Sustainability vs Tradition")
    print("    • Digital presence vs Mystique")
    print()
    print("  Five consumer segments are watching.")
    print("  Each cares about different things.")
    print("  Your choices will attract some and alienate others.")
    print()
    input("  Press Enter to begin...\n")


def run_scenario(scenario, brand_scores):
    print("\n" + "-" * 60)
    print(f"  {scenario['title']}")
    print("-" * 60)
    print(f"\n  {scenario['question']}\n")

    for i, (desc, _) in enumerate(scenario["options"], 1):
        print(f"    {i}. {desc}")

    while True:
        try:
            choice = int(input("\n  Your choice (1/2/3): "))
            if 1 <= choice <= 3:
                break
            print("  Pick 1, 2, or 3.")
        except ValueError:
            print("  Pick 1, 2, or 3.")

    _, effects = scenario["options"][choice - 1]
    for key, val in effects.items():
        brand_scores[key] = brand_scores.get(key, 0) + val

    print(f"\n  Decision locked in.")
    return brand_scores


def calculate_segment_loyalty(brand_scores):
    results = {}
    for seg_name, seg_data in SEGMENTS.items():
        score = 50  # baseline
        for dimension, weight in seg_data["weights"].items():
            score += brand_scores.get(dimension, 0) * weight * 4
        score += random.randint(-5, 5)  # market noise
        score = max(5, min(100, score))
        results[seg_name] = score
    return results


def show_bar(value, width=30):
    filled = int((value / 100) * width)
    return "█" * filled + "░" * (width - filled)


def debrief(brand_scores, segment_results):
    print("\n" + "=" * 60)
    print("  5-YEAR BRAND REPORT")
    print("=" * 60)

    print("\n  YOUR BRAND PROFILE:")
    for dim in ["exclusivity", "heritage", "sustainability", "digital"]:
        val = brand_scores.get(dim, 0)
        label = dim.capitalize()
        if val > 2:
            strength = "Strong"
        elif val > 0:
            strength = "Moderate"
        elif val == 0:
            strength = "Neutral"
        elif val > -2:
            strength = "Weak"
        else:
            strength = "Neglected"
        print(f"    {label:<16} {val:>+3}  ({strength})")

    print("\n  CONSUMER SEGMENT LOYALTY:")
    for seg_name, loyalty in sorted(segment_results.items(), key=lambda x: -x[1]):
        bar = show_bar(loyalty)
        print(f"\n    {seg_name}")
        print(f"    {SEGMENTS[seg_name]['desc']}")
        print(f"    [{bar}] {loyalty}%")

    top_seg = max(segment_results, key=segment_results.get)
    bottom_seg = min(segment_results, key=segment_results.get)
    avg = sum(segment_results.values()) / len(segment_results)

    print(f"\n  Strongest following: {top_seg} ({segment_results[top_seg]}%)")
    print(f"  Weakest following:   {bottom_seg} ({segment_results[bottom_seg]}%)")
    print(f"  Average loyalty:     {avg:.0f}%")

    print("\n" + "=" * 60)
    print("  THE SCIENCE")
    print("=" * 60)
    print()
    print("  Dhaliwal et al. (2020) found that luxury consumption is")
    print("  driven by THREE interacting forces:")
    print()
    print("    1. PERSONAL — self-esteem, uniqueness, pleasure")
    print("    2. SOCIAL  — reference groups, culture, status display")
    print("    3. BRAND   — heritage, exclusivity, craftsmanship")
    print()
    print("  No single factor explains luxury buying alone.")
    print("  The segments you just served each weigh these differently.")
    print()
    print("  The key tensions you navigated are real:")
    print("    • Going digital boosts reach but can kill exclusivity")
    print("    • Heritage builds trust but can feel outdated")
    print("    • Sustainability attracts new buyers but may clash")
    print("      with traditional luxury's emphasis on rare materials")
    print()
    print("  There's no single 'right' strategy — the best luxury")
    print("  brands find a coherent identity that serves their core")
    print("  segment while carefully managing the trade-offs.")
    print()
    if avg >= 60:
        print("  Your brand built a solid following overall — you managed")
        print("  the trade-offs well.")
    elif avg >= 40:
        print("  Your brand had a mixed reception — some segments loved")
        print("  you while others felt neglected. That's the luxury dilemma.")
    else:
        print("  Your brand struggled — trying to please everyone in luxury")
        print("  often means pleasing no one. Focus is essential.")
    print()


def main():
    show_intro()
    brand_scores = {"exclusivity": 0, "heritage": 0, "sustainability": 0, "digital": 0}

    for scenario in SCENARIOS:
        brand_scores = run_scenario(scenario, brand_scores)

    segment_results = calculate_segment_loyalty(brand_scores)
    debrief(brand_scores, segment_results)


if __name__ == "__main__":
    main()
