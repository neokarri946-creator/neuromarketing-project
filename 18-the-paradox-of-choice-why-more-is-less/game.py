"""
The Paradox of Choice — Interactive Experience
Based on Schwartz (2004)

Feel the difference between choosing from a few options
versus drowning in possibilities.
"""

import random
import time

COLOURS = [
    "Midnight Black", "Arctic White", "Ocean Blue", "Forest Green",
    "Crimson Red", "Sunset Orange", "Lavender Purple", "Dusty Rose",
    "Slate Grey", "Champagne Gold", "Electric Teal", "Burnt Sienna",
    "Ivory Cream", "Cobalt Blue", "Sage Green", "Terracotta",
    "Charcoal", "Blush Pink", "Navy", "Olive Drab",
    "Plum", "Copper", "Sand", "Steel Blue",
    "Mint", "Coral", "Graphite", "Mocha",
    "Pearl", "Jade",
]

SMALL_SET_SIZE = 3
LARGE_SET_SIZE = 30


def show_intro():
    print("=" * 58)
    print("  THE PARADOX OF CHOICE")
    print("  Based on Schwartz (2004)")
    print("=" * 58)
    print()
    print("  You're buying a new phone case.")
    print("  You'll choose TWICE — once from a small selection,")
    print("  once from a huge one.")
    print()
    print("  Pay attention to how each experience FEELS.")
    print()
    input("  Press Enter to begin...\n")


def get_number(prompt, min_val, max_val):
    while True:
        try:
            val = int(input(f"  {prompt}: "))
            if min_val <= val <= max_val:
                return val
            print(f"  Enter a number from {min_val} to {max_val}.")
        except ValueError:
            print(f"  Enter a number from {min_val} to {max_val}.")


def get_rating(prompt):
    while True:
        try:
            print(f"  (1 = lowest ... 10 = highest)")
            val = int(input(f"  {prompt}: "))
            if 1 <= val <= 10:
                return val
            print("  Enter a number from 1 to 10.")
        except ValueError:
            print("  Enter a number from 1 to 10.")


def display_options(options):
    for i, opt in enumerate(options, 1):
        print(f"    {i:>2}. {opt}")
    print()


def run_choice_round(options, round_name):
    print("-" * 58)
    print(f"  {round_name}")
    print(f"  Choose a colour for your new phone case.")
    print(f"  Options available: {len(options)}")
    print("-" * 58)
    print()
    display_options(options)

    start_time = time.time()
    choice = get_number("Enter the number of your choice", 1, len(options))
    elapsed = time.time() - start_time

    chosen = options[choice - 1]
    print(f"\n  You chose: {chosen}  (took {elapsed:.1f} seconds)")
    print()

    difficulty = get_rating("How DIFFICULT was it to decide?")
    print()
    confidence = get_rating("How CONFIDENT are you in your choice?")
    print()
    satisfaction = get_rating("How SATISFIED are you with your choice?")
    print()
    regret = get_rating("How much do you WONDER if another option was better?")
    print()

    return {
        "round": round_name,
        "num_options": len(options),
        "chosen": chosen,
        "time": elapsed,
        "difficulty": difficulty,
        "confidence": confidence,
        "satisfaction": satisfaction,
        "regret": regret,
    }


def show_bar(value, max_val=10, label=""):
    filled = "█" * value
    empty = "░" * (max_val - value)
    return f"  {label:<14} [{filled}{empty}] {value}/10"


def debrief(small_result, large_result):
    print("\n" + "=" * 58)
    print("  DEBRIEF — SMALL vs LARGE CHOICE SET")
    print("=" * 58)

    print(f"\n  SMALL SET ({small_result['num_options']} options) — chose: {small_result['chosen']}")
    print(f"  Decision time: {small_result['time']:.1f}s")
    print(show_bar(small_result["difficulty"], label="Difficulty"))
    print(show_bar(small_result["confidence"], label="Confidence"))
    print(show_bar(small_result["satisfaction"], label="Satisfaction"))
    print(show_bar(small_result["regret"], label="Regret"))

    print(f"\n  LARGE SET ({large_result['num_options']} options) — chose: {large_result['chosen']}")
    print(f"  Decision time: {large_result['time']:.1f}s")
    print(show_bar(large_result["difficulty"], label="Difficulty"))
    print(show_bar(large_result["confidence"], label="Confidence"))
    print(show_bar(large_result["satisfaction"], label="Satisfaction"))
    print(show_bar(large_result["regret"], label="Regret"))

    print("\n" + "-" * 58)
    print("  WHAT CHANGED?")
    print("-" * 58)

    comparisons = [
        ("Difficulty", large_result["difficulty"] - small_result["difficulty"],
         "higher", "easier"),
        ("Confidence", large_result["confidence"] - small_result["confidence"],
         "higher", "lower"),
        ("Satisfaction", large_result["satisfaction"] - small_result["satisfaction"],
         "higher", "lower"),
        ("Regret", large_result["regret"] - small_result["regret"],
         "more", "less"),
    ]

    paradox_score = 0
    for name, diff, more_word, less_word in comparisons:
        if name in ("Difficulty", "Regret"):
            if diff > 0:
                paradox_score += 1
        elif name in ("Confidence", "Satisfaction"):
            if diff < 0:
                paradox_score += 1

        if diff > 0:
            print(f"  {name}: {more_word} with large set (+{diff})")
        elif diff < 0:
            print(f"  {name}: {less_word} with large set ({diff})")
        else:
            print(f"  {name}: same in both rounds")

    time_diff = large_result["time"] - small_result["time"]
    if time_diff > 1:
        print(f"  Time: {time_diff:.1f}s slower with more options")
        paradox_score += 1
    elif time_diff < -1:
        print(f"  Time: {abs(time_diff):.1f}s faster with more options")
    else:
        print(f"  Time: roughly the same")

    print("\n" + "=" * 58)
    print("  THE SCIENCE")
    print("=" * 58)
    print()

    if paradox_score >= 3:
        print("  You experienced the paradox of choice strongly!")
        print("  More options made things harder, not better.")
    elif paradox_score >= 1:
        print("  You showed some signs of the paradox.")
    else:
        print("  You seemed untroubled by the extra options —")
        print("  you may be a natural 'satisficer' (someone who")
        print("  picks the first good-enough option, rather than")
        print("  exhaustively searching for the best).")

    print()
    print("  Schwartz (2004) showed that more choice leads to:")
    print()
    print("  1. DECISION PARALYSIS — harder to choose at all")
    print("  2. OPPORTUNITY COST — you imagine what you're missing")
    print("  3. INFLATED EXPECTATIONS — with so many options,")
    print("     anything less than perfect feels like failure")
    print("  4. SELF-BLAME — 'with all those options, I should")
    print("     have found the perfect one'")
    print()
    print("  WHY THIS MATTERS FOR MARKETING:")
    print()
    print("  - Apple offers ~4 phone models, not 40")
    print("  - Trader Joe's stocks 4,000 items vs 30,000 at rivals")
    print("  - 'Editor's Pick' and 'Best Seller' labels cut through noise")
    print("  - Recommendation algorithms exist to REDUCE choice")
    print()
    print("  Sometimes the best way to sell more is to offer less.")
    print()


def main():
    show_intro()

    small_set = random.sample(COLOURS[:10], SMALL_SET_SIZE)
    large_set = COLOURS[:]
    random.shuffle(large_set)

    small_result = run_choice_round(small_set, "ROUND 1: SMALL SELECTION")
    input("  Press Enter for Round 2...\n")
    large_result = run_choice_round(large_set, "ROUND 2: HUGE SELECTION")

    debrief(small_result, large_result)


if __name__ == "__main__":
    main()
