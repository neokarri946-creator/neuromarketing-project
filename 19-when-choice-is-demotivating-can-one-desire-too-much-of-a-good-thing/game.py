"""
When Choice Is Demotivating — Interactive Experience
Based on Iyengar & Lepper (2000) — The Jam Study

Experience the difference between choosing from 6 vs 24 options
and see how choice overload affects your willingness to commit.
"""

import random
import time

JAM_FLAVOURS = [
    "Strawberry", "Blueberry", "Raspberry", "Apricot", "Blackberry",
    "Peach", "Fig", "Plum", "Cherry", "Mango",
    "Passion Fruit", "Guava", "Lemon Curd", "Blood Orange", "Cranberry",
    "Gooseberry", "Damson", "Rhubarb & Ginger", "Quince", "Boysenberry",
    "Elderflower", "Seville Marmalade", "Lingonberry", "Yuzu",
]


def show_intro():
    print("=" * 58)
    print("  THE JAM STUDY")
    print("  Based on Iyengar & Lepper (2000)")
    print("=" * 58)
    print()
    print("  Welcome to the Gourmet Jam Tasting Booth!")
    print()
    print("  You'll visit the booth TWICE:")
    print("    Round 1: A small selection of jams")
    print("    Round 2: The full range")
    print()
    print("  At the end, you can buy one jar (or walk away).")
    print("  Pay attention to how each round FEELS.")
    print()
    input("  Press Enter to approach the booth...\n")


def get_rating(prompt):
    while True:
        try:
            val = int(input(f"  {prompt} (1-10): "))
            if 1 <= val <= 10:
                return val
            print("  Enter a number from 1 to 10.")
        except ValueError:
            print("  Enter a number from 1 to 10.")


def display_jams(jams):
    cols = 2
    for i in range(0, len(jams), cols):
        row_items = []
        for j in range(cols):
            idx = i + j
            if idx < len(jams):
                row_items.append(f"  {idx + 1:>2}. {jams[idx]:<22}")
        print("".join(row_items))
    print()


def run_round(jams, round_label):
    print("-" * 58)
    print(f"  {round_label}")
    print(f"  The booth has {len(jams)} jams on display:")
    print("-" * 58)
    print()
    display_jams(jams)

    start = time.time()

    # Let them browse
    print("  Take a moment to read through the options...")
    print()

    # Ask if they want to buy
    while True:
        decision = input("  Would you like to BUY a jar, or WALK away? ").strip().upper()
        if decision in ("BUY", "B"):
            bought = True
            break
        elif decision in ("WALK", "W"):
            bought = False
            break
        print("  Type BUY or WALK.")

    chosen = None
    if bought:
        while True:
            try:
                pick = int(input(f"  Which one? Enter the number (1-{len(jams)}): "))
                if 1 <= pick <= len(jams):
                    chosen = jams[pick - 1]
                    break
                print(f"  Enter a number from 1 to {len(jams)}.")
            except ValueError:
                print(f"  Enter a number from 1 to {len(jams)}.")

    elapsed = time.time() - start
    print()

    if chosen:
        print(f"  You bought: {chosen}!")
    else:
        print("  You walked away without buying.")

    print()
    enjoyment = get_rating("How much did you ENJOY browsing?")
    difficulty = get_rating("How DIFFICULT was the decision?")
    overwhelm = get_rating("How OVERWHELMED did you feel?")
    print()

    if chosen:
        confidence = get_rating("How CONFIDENT are you that you picked the best one?")
    else:
        confidence = None

    print()

    return {
        "round": round_label,
        "num_options": len(jams),
        "bought": bought,
        "chosen": chosen,
        "time": elapsed,
        "enjoyment": enjoyment,
        "difficulty": difficulty,
        "overwhelm": overwhelm,
        "confidence": confidence,
    }


def show_bar(value, max_val=10, label=""):
    if value is None:
        return f"  {label:<14} [----N/A---]"
    filled = "█" * value
    empty = "░" * (max_val - value)
    return f"  {label:<14} [{filled}{empty}] {value}/10"


def debrief(small, large):
    print("\n" + "=" * 58)
    print("  DEBRIEF — YOUR JAM STUDY RESULTS")
    print("=" * 58)

    for result in [small, large]:
        tag = "SMALL" if result["num_options"] <= 6 else "LARGE"
        bought_str = result["chosen"] if result["chosen"] else "Walked away"
        print(f"\n  {tag} DISPLAY ({result['num_options']} jams)")
        print(f"  Decision: {bought_str}")
        print(f"  Time: {result['time']:.1f}s")
        print(show_bar(result["enjoyment"], label="Enjoyment"))
        print(show_bar(result["difficulty"], label="Difficulty"))
        print(show_bar(result["overwhelm"], label="Overwhelm"))
        print(show_bar(result["confidence"], label="Confidence"))

    print("\n" + "-" * 58)
    print("  COMPARING YOUR ROUNDS")
    print("-" * 58)

    # Check the classic effect
    classic_effect = False
    if small["bought"] and not large["bought"]:
        print("\n  You bought from the small display but walked away")
        print("  from the large one — exactly what happened in the study!")
        classic_effect = True
    elif not small["bought"] and large["bought"]:
        print("\n  Interestingly, you bought from the LARGE display but")
        print("  not the small one — the opposite of the typical finding.")
    elif small["bought"] and large["bought"]:
        print("\n  You bought from both — you're a decisive shopper!")
    else:
        print("\n  You walked away from both — a tough customer!")

    diff_difficulty = large["difficulty"] - small["difficulty"]
    diff_overwhelm = large["overwhelm"] - small["overwhelm"]

    if diff_difficulty > 0:
        print(f"  Difficulty jumped by {diff_difficulty} point(s) with more options.")
    if diff_overwhelm > 0:
        print(f"  Overwhelm jumped by {diff_overwhelm} point(s) with more options.")

    print("\n" + "=" * 58)
    print("  THE SCIENCE")
    print("=" * 58)
    print()
    print("  In the real study at a gourmet food store:")
    print()
    print("  DISPLAY      STOPPED    BOUGHT")
    print("  24 jams       60%        3%")
    print("   6 jams       40%       30%")
    print()
    print("  The large display ATTRACTED more people — but was")
    print("  10x WORSE at converting interest into a purchase.")
    print()
    print("  WHY?")
    print("  - Too many options create decision paralysis")
    print("  - You can't meaningfully compare 24 things")
    print("  - Walking away feels easier than risking a bad pick")
    print("  - Regret looms larger: 'What if another was better?'")
    print()
    print("  WHY THIS MATTERS FOR MARKETING:")
    print()
    print("  - Attention is not the same as action")
    print("  - Curated ranges convert better than vast catalogues")
    print("  - Netflix shows you ~40 titles, not its full 15,000+")
    print("  - 'Featured' and 'Top Picks' exist to cut through overload")
    print("  - The sweet spot: enough variety to feel free,")
    print("    not so much that you freeze")
    print()


def main():
    show_intro()

    all_jams = JAM_FLAVOURS[:]
    random.shuffle(all_jams)

    small_selection = all_jams[:6]
    large_selection = all_jams[:]

    small_result = run_round(small_selection, "ROUND 1: SMALL DISPLAY")
    input("  Press Enter to visit the booth again...\n")
    large_result = run_round(large_selection, "ROUND 2: FULL RANGE")

    debrief(small_result, large_result)


if __name__ == "__main__":
    main()
