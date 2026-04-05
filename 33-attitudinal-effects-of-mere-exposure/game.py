"""
Attitudinal Effects of Mere Exposure — Interactive Experience
Based on Zajonc (1968)

You'll see unfamiliar symbols flash on screen at different
frequencies. Then you'll rate them — and discover that you
prefer the ones you saw most, without knowing why.
"""

import random
import time
import os


# Generate abstract "symbols" using text characters
SYMBOLS = [
    "  /\\  \n /  \\ \n/____\\",
    " ___ \n| O |\n|___|",
    "  *  \n * * \n  *  ",
    " ~~~ \n|   |\n ~~~ ",
    " <=> \n ||| \n <=> ",
    " {_} \n(   )\n {_} ",
    " /#\\ \n# # #\n \\#/ ",
    " |+| \n+   +\n |+| ",
]

SYMBOL_LABELS = ["Alpha", "Beta", "Gamma", "Delta",
                 "Epsilon", "Zeta", "Eta", "Theta"]


def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")


def show_intro():
    print("=" * 58)
    print("  MERE EXPOSURE EFFECT")
    print("  Based on Zajonc (1968)")
    print("=" * 58)
    print()
    print("  You're about to see a series of unfamiliar symbols")
    print("  flash on screen. Don't try to memorise them.")
    print("  Just watch casually — like background noise.")
    print()
    print("  Afterward, you'll rate how much you like each one.")
    print()
    print("  There are no right or wrong answers.")
    print("  Just go with your gut feeling.")
    print()
    input("  Press Enter to begin the exposure phase...\n")


def exposure_phase():
    """Show symbols with different frequencies."""
    # Assign each symbol a frequency tier
    indices = list(range(len(SYMBOLS)))
    random.shuffle(indices)

    # 2 symbols shown many times, 2 moderate, 2 few, 2 never
    frequencies = {}
    frequencies[indices[0]] = 12
    frequencies[indices[1]] = 10
    frequencies[indices[2]] = 5
    frequencies[indices[3]] = 4
    frequencies[indices[4]] = 1
    frequencies[indices[5]] = 1
    frequencies[indices[6]] = 0
    frequencies[indices[7]] = 0

    # Build the exposure sequence
    sequence = []
    for idx, count in frequencies.items():
        sequence.extend([idx] * count)
    random.shuffle(sequence)

    print("  EXPOSURE PHASE")
    print("  Symbols will flash on screen. Just watch.")
    print(f"  ({len(sequence)} flashes total)")
    print()
    input("  Press Enter when ready...\n")

    for i, idx in enumerate(sequence):
        clear_screen()
        print(f"\n  Flash {i + 1} of {len(sequence)}")
        print()
        for line in SYMBOLS[idx].split("\n"):
            print(f"       {line}")
        print()
        time.sleep(0.6)

    clear_screen()
    print("\n  Exposure phase complete!")
    print()

    return frequencies


def rating_phase(frequencies):
    """Ask the player to rate each symbol."""
    print("=" * 58)
    print("  RATING PHASE")
    print("=" * 58)
    print()
    print("  Now rate each symbol on how much you LIKE it.")
    print("  1 = dislike ... 7 = really like")
    print("  Go with your first instinct. No overthinking.")
    print()
    input("  Press Enter to begin rating...\n")

    # Show symbols in random order
    order = list(range(len(SYMBOLS)))
    random.shuffle(order)

    ratings = {}
    for idx in order:
        print(f"  Symbol: {SYMBOL_LABELS[idx]}")
        print()
        for line in SYMBOLS[idx].split("\n"):
            print(f"       {line}")
        print()

        while True:
            try:
                r = int(input("  Your rating (1-7): "))
                if 1 <= r <= 7:
                    ratings[idx] = r
                    break
                print("  Please enter 1-7.")
            except ValueError:
                print("  Please enter a number 1-7.")
        print()

    return ratings


def debrief(frequencies, ratings):
    print("\n" + "=" * 58)
    print("  DEBRIEF — THE MERE EXPOSURE EFFECT REVEALED")
    print("=" * 58)

    # Group symbols by exposure tier
    tiers = {"High (10-12x)": [], "Medium (4-5x)": [],
             "Low (1x)": [], "Never (0x)": []}

    for idx in range(len(SYMBOLS)):
        freq = frequencies.get(idx, 0)
        rating = ratings.get(idx, 0)
        if freq >= 10:
            tiers["High (10-12x)"].append(rating)
        elif freq >= 4:
            tiers["Medium (4-5x)"].append(rating)
        elif freq >= 1:
            tiers["Low (1x)"].append(rating)
        else:
            tiers["Never (0x)"].append(rating)

    print("\n  YOUR RATINGS BY EXPOSURE FREQUENCY:")
    print(f"  {'-' * 44}")

    tier_avgs = {}
    for tier_name, tier_ratings in tiers.items():
        if tier_ratings:
            avg = sum(tier_ratings) / len(tier_ratings)
            tier_avgs[tier_name] = avg
            bar = "█" * int(avg * 4) + "░" * (28 - int(avg * 4))
            print(f"  {tier_name:<16} [{bar}] {avg:.1f}/7")

    # Check if the effect appeared
    high_avg = tier_avgs.get("High (10-12x)", 0)
    never_avg = tier_avgs.get("Never (0x)", 0)

    print(f"\n  Individual results:")
    print(f"  {'-' * 44}")
    sorted_by_freq = sorted(range(len(SYMBOLS)),
                            key=lambda i: frequencies.get(i, 0),
                            reverse=True)
    for idx in sorted_by_freq:
        freq = frequencies.get(idx, 0)
        rating = ratings.get(idx, 0)
        bar = "★" * rating + "☆" * (7 - rating)
        print(f"  {SYMBOL_LABELS[idx]:<10} shown {freq:>2}x  rated {bar} {rating}/7")

    effect_present = high_avg > never_avg

    print(f"""
  THE SCIENCE:

  Zajonc (1968) found that simply seeing something more
  often makes people like it more — with NO conscious
  awareness that exposure is driving their preference.

  {"Your results showed the effect! You rated the most-seen" if effect_present else "Your results bucked the trend — but in Zajonc's studies,"}
  {"symbols higher than the ones you'd never seen before." if effect_present else "the effect appeared reliably across hundreds of participants."}
  {"You weren't told which symbols appeared more — yet" if effect_present else "Individual variation is normal, but the group pattern"}
  {"your gut feelings tracked the exposure frequency." if effect_present else "consistently favours the familiar."}

  WHY THIS MATTERS FOR MARKETING:

  This is why companies pay millions to put logos on sports
  shirts, run ads that say nothing persuasive, and ensure
  their brand appears everywhere — even in the background.

  You don't need to convince people your product is good.
  You just need them to see it. Repeatedly. The familiarity
  alone generates liking. Presence beats persuasion.

  Every billboard, product placement, and sponsored post
  is exploiting the mere exposure effect — shaping your
  preferences without a single argument being made.
""")


def main():
    show_intro()
    frequencies = exposure_phase()
    ratings = rating_phase(frequencies)
    debrief(frequencies, ratings)


if __name__ == "__main__":
    main()
