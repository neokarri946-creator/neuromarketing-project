"""
The Psychology of Luxury Consumption — Interactive Experience
Based on Dubois, Jung & Ordabayeva (2020)

Make luxury purchase decisions in different social scenarios.
Discover which psychological motive was driving each choice.
"""

import random

# ── Scenarios ──────────────────────────────────────────────────────

SCENARIOS = [
    {
        "situation": "You just got a big promotion. Nobody else knows yet.",
        "context": "private celebration",
        "options": [
            {
                "desc": "A hand-stitched Italian leather journal — beautiful, personal, no visible brand",
                "motive": "self-reward",
                "motive_label": "SELF-REWARD",
            },
            {
                "desc": "A Rolex Submariner — classic, recognisable, everyone will notice",
                "motive": "status",
                "motive_label": "STATUS SIGNALLING",
            },
            {
                "desc": "A limited-run artisan perfume — only 200 bottles made worldwide",
                "motive": "uniqueness",
                "motive_label": "UNIQUENESS-SEEKING",
            },
            {
                "desc": "The same designer briefcase your new director carries",
                "motive": "conformity",
                "motive_label": "ASPIRATIONAL CONFORMITY",
            },
        ],
    },
    {
        "situation": "You're attending a high-profile networking dinner with industry leaders.",
        "context": "public, high-status audience",
        "options": [
            {
                "desc": "A bespoke suit from a tailor nobody has heard of — superb quality, no label",
                "motive": "uniqueness",
                "motive_label": "UNIQUENESS-SEEKING",
            },
            {
                "desc": "A Tom Ford suit — the brand that says 'I've arrived'",
                "motive": "status",
                "motive_label": "STATUS SIGNALLING",
            },
            {
                "desc": "The exact same watch the keynote speaker is wearing",
                "motive": "conformity",
                "motive_label": "ASPIRATIONAL CONFORMITY",
            },
            {
                "desc": "Your favourite comfortable luxury knit — it just feels amazing on your skin",
                "motive": "self-reward",
                "motive_label": "SELF-REWARD",
            },
        ],
    },
    {
        "situation": "You've had a terrible week. You want to feel better.",
        "context": "emotional recovery, private",
        "options": [
            {
                "desc": "A luxury spa day — no photos, just pure indulgence for yourself",
                "motive": "self-reward",
                "motive_label": "SELF-REWARD",
            },
            {
                "desc": "A designer bag you can post on Instagram to show life is good",
                "motive": "status",
                "motive_label": "STATUS SIGNALLING",
            },
            {
                "desc": "A rare vintage wine that almost nobody else could find",
                "motive": "uniqueness",
                "motive_label": "UNIQUENESS-SEEKING",
            },
            {
                "desc": "The exact skincare set your favourite influencer swears by",
                "motive": "conformity",
                "motive_label": "ASPIRATIONAL CONFORMITY",
            },
        ],
    },
    {
        "situation": "You're buying a gift for yourself before starting at a new company.",
        "context": "identity transition, semi-public",
        "options": [
            {
                "desc": "A Montblanc pen — everyone in the office will recognise it",
                "motive": "status",
                "motive_label": "STATUS SIGNALLING",
            },
            {
                "desc": "The same laptop bag the CEO was photographed carrying",
                "motive": "conformity",
                "motive_label": "ASPIRATIONAL CONFORMITY",
            },
            {
                "desc": "A one-of-a-kind handmade notebook cover from a craft market",
                "motive": "uniqueness",
                "motive_label": "UNIQUENESS-SEEKING",
            },
            {
                "desc": "Premium noise-cancelling headphones — pure personal comfort",
                "motive": "self-reward",
                "motive_label": "SELF-REWARD",
            },
        ],
    },
    {
        "situation": "You're choosing what to wear to your 10-year school reunion.",
        "context": "social comparison, people from your past",
        "options": [
            {
                "desc": "A Gucci belt and designer shoes — unmistakably expensive",
                "motive": "status",
                "motive_label": "STATUS SIGNALLING",
            },
            {
                "desc": "A vintage designer piece nobody else could possibly own",
                "motive": "uniqueness",
                "motive_label": "UNIQUENESS-SEEKING",
            },
            {
                "desc": "Whatever the most successful person from your year would wear",
                "motive": "conformity",
                "motive_label": "ASPIRATIONAL CONFORMITY",
            },
            {
                "desc": "Your softest, most comfortable luxury outfit — you want to feel good",
                "motive": "self-reward",
                "motive_label": "SELF-REWARD",
            },
        ],
    },
]


def show_intro():
    print("=" * 58)
    print("  THE PSYCHOLOGY OF LUXURY CONSUMPTION")
    print("  Based on Dubois, Jung & Ordabayeva (2020)")
    print("=" * 58)
    print()
    print("  You'll face 5 social situations.")
    print("  In each, choose the luxury option that appeals")
    print("  to you most — go with your gut.")
    print()
    print("  Afterward, we'll reveal the hidden psychological")
    print("  motive behind each of your choices.")
    print()
    input("  Press Enter to begin...\n")


def run_scenario(scenario, num):
    print("-" * 58)
    print(f"  SCENARIO {num}")
    print(f"  {scenario['situation']}")
    print(f"  (Context: {scenario['context']})")
    print("-" * 58)

    options = scenario["options"][:]
    random.shuffle(options)

    print()
    for i, opt in enumerate(options, 1):
        print(f"    {i}. {opt['desc']}")

    while True:
        try:
            choice = int(input(f"\n  Your choice (1-{len(options)}): "))
            if 1 <= choice <= len(options):
                chosen = options[choice - 1]
                break
        except ValueError:
            pass
        print(f"  Enter a number from 1 to {len(options)}.")

    print(f"\n  --> {chosen['desc']}")
    return chosen["motive"], chosen["motive_label"]


def debrief(choices):
    print("\n" + "=" * 58)
    print("  DEBRIEF — YOUR LUXURY MOTIVE PROFILE")
    print("=" * 58)

    motive_counts = {"status": 0, "self-reward": 0, "uniqueness": 0, "conformity": 0}
    motive_labels = {
        "status": "STATUS SIGNALLING",
        "self-reward": "SELF-REWARD",
        "uniqueness": "UNIQUENESS-SEEKING",
        "conformity": "ASPIRATIONAL CONFORMITY",
    }
    motive_descriptions = {
        "status": "Using luxury to communicate wealth and rank to others",
        "self-reward": "Treating yourself — luxury as private pleasure",
        "uniqueness": "Seeking rare items to stand out from the crowd",
        "conformity": "Buying what admired groups buy, to belong",
    }

    for i, (motive, label) in enumerate(choices, 1):
        motive_counts[motive] += 1
        print(f"\n  Scenario {i}: Your motive was {label}")

    print("\n" + "-" * 58)
    print("  YOUR MOTIVE BREAKDOWN:")

    sorted_motives = sorted(motive_counts.items(), key=lambda x: -x[1])
    for motive, count in sorted_motives:
        bar = "#" * (count * 4) + "." * ((5 - count) * 4)
        print(f"    {motive_labels[motive]:<28} [{bar}] {count}/5")

    dominant = sorted_motives[0]
    print(f"\n  Your dominant motive: {motive_labels[dominant[0]]}")
    print(f"  ({motive_descriptions[dominant[0]]})")

    if sorted_motives[0][1] == sorted_motives[1][1]:
        print(f"\n  (Tied with: {motive_labels[sorted_motives[1][0]]})")

    print("\n" + "=" * 58)
    print("  THE SCIENCE:")
    print()
    print("  Dubois, Jung & Ordabayeva (2020) found that luxury")
    print("  consumption isn't just about showing off. There are")
    print("  FOUR distinct psychological motives:")
    print()
    print("  1. STATUS SIGNALLING — 'Look how successful I am'")
    print("  2. SELF-REWARD — 'I deserve this, just for me'")
    print("  3. UNIQUENESS — 'Nobody else has this'")
    print("  4. CONFORMITY — 'I want to be part of THAT group'")
    print()
    print("  These shift based on:")
    print("  - Context (public vs private)")
    print("  - Emotion (celebration vs stress)")
    print("  - Culture (collectivist vs individualist)")
    print("  - Personality (narcissism, need for uniqueness)")
    print()
    print("  Smart luxury brands identify WHICH motive their")
    print("  customer segment is driven by and design the entire")
    print("  experience around it — not just the product.")
    print()
    print("  Loud logos serve status. Quiet craftsmanship serves")
    print("  self-reward. Limited editions serve uniqueness.")
    print("  Celebrity endorsements serve conformity.")
    print()


def main():
    show_intro()

    choices = []
    for i, scenario in enumerate(SCENARIOS, 1):
        motive, label = run_scenario(scenario, i)
        choices.append((motive, label))
        print()

    debrief(choices)


if __name__ == "__main__":
    main()
