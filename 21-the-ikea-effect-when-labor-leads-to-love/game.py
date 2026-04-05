"""
The IKEA Effect — Interactive Experience
Based on Norton, Mochon & Ariely (2012)

Feel how building something yourself warps your sense of its value.
"""

import random
import time

# ── ASCII furniture parts ──────────────────────────────────────────

STEPS_SHELF = [
    ("Attach the LEFT side panel", "[|         ]"),
    ("Attach the RIGHT side panel", "[|         |]"),
    ("Slide in the BOTTOM shelf", "[|_________|]"),
    ("Slide in the MIDDLE shelf", "[|—————————|]"),
    ("Secure the BACK panel", "[|■■■■■■■■■|]"),
    ("Screw in the TOP", "[‾‾‾‾‾‾‾‾‾‾‾]"),
]

PREMADE_SHELF = """\
  [‾‾‾‾‾‾‾‾‾‾‾]
  [|■■■■■■■■■|]
  [|—————————|]
  [|_________|]"""

STEPS_LAMP = [
    ("Assemble the BASE", "  (_____)"),
    ("Attach the STEM", "  (_____)\\n    |"),
    ("Wire the SOCKET", "  (_____)\\n    |\\n    *"),
    ("Fit the SHADE", "   /---\\\\\\n  (_____)\\n    |\\n    *"),
    ("Screw in the BULB", "   /---\\\\\\n   | O |\\n  (_____)\\n    |"),
]

PREMADE_LAMP = """\
   /---\\
   | O |
  (_____)
    |"""

PROJECTS = [
    ("Bookshelf", STEPS_SHELF, PREMADE_SHELF),
    ("Desk Lamp", STEPS_LAMP, PREMADE_LAMP),
]


def show_intro():
    print("=" * 58)
    print("  THE IKEA EFFECT")
    print("  Based on Norton, Mochon & Ariely (2012)")
    print("=" * 58)
    print()
    print("  You'll BUILD one item step by step.")
    print("  Then you'll see an identical PREMADE version.")
    print("  Finally, you'll put a price on each one.")
    print()
    print("  Let's see if your labour changes your valuation.")
    print()
    input("  Press Enter to begin building...\n")


def build_item(name, steps):
    print("-" * 58)
    print(f"  PROJECT: Build a {name}")
    print("-" * 58)
    print()

    for i, (instruction, visual) in enumerate(steps, 1):
        print(f"  Step {i}/{len(steps)}: {instruction}")
        input("  [Press Enter to complete this step]")
        for line in visual.split("\\n"):
            print(f"    {line}")
        print()
        time.sleep(0.3)

    print("  *** Your build is COMPLETE! ***")
    print()
    return True


def get_valuation(label):
    while True:
        try:
            val = int(input(f"  How much would you pay for the {label}? £"))
            if val >= 0:
                return val
            print("  Please enter a positive number.")
        except ValueError:
            print("  Please enter a whole number (e.g. 25).")


def run_round(name, steps, premade_art):
    # Phase 1 — Build
    build_item(name, steps)

    # Phase 2 — Value your creation
    print("-" * 58)
    print(f"  VALUATION ROUND — {name.upper()}")
    print("-" * 58)
    print()
    print("  Here is the one YOU built:")
    for line in steps[-1][1].split("\\n"):
        print(f"    {line}")
    print()
    my_val = get_valuation(f"{name} you BUILT yourself")
    print()

    # Phase 3 — Value the premade
    print("  Now here is an IDENTICAL premade version")
    print("  (professionally assembled, same materials):")
    print()
    for line in premade_art.strip().split("\n"):
        print(f"  {line}")
    print()
    pre_val = get_valuation(f"PREMADE {name} (identical quality)")
    print()

    return my_val, pre_val


def debrief(results):
    print("\n" + "=" * 58)
    print("  DEBRIEF — THE IKEA EFFECT")
    print("=" * 58)

    total_self = 0
    total_pre = 0

    for name, my_val, pre_val in results:
        diff = my_val - pre_val
        pct = ((my_val - pre_val) / pre_val * 100) if pre_val > 0 else 0

        print(f"\n  {name}:")
        print(f"    Your build:  £{my_val}")
        print(f"    Premade:     £{pre_val}")

        if diff > 0:
            print(f"    --> You valued YOUR version £{diff} MORE ({pct:+.0f}%)")
        elif diff < 0:
            print(f"    --> You valued the premade £{abs(diff)} MORE ({pct:+.0f}%)")
        else:
            print(f"    --> Exactly the same valuation")

        total_self += my_val
        total_pre += pre_val

    overall_diff = total_self - total_pre
    print("\n" + "-" * 58)
    print(f"  TOTAL — Self-built: £{total_self}  |  Premade: £{total_pre}")
    if overall_diff > 0:
        print(f"  You valued your own work £{overall_diff} more overall.")
    elif overall_diff < 0:
        print(f"  You valued the premade versions £{abs(overall_diff)} more overall.")
    else:
        print(f"  Identical valuations — the effect didn't appear for you.")

    print("\n" + "=" * 58)
    print("  THE SCIENCE:")
    print()
    print("  Norton, Mochon & Ariely (2012) found that people valued")
    print("  items they assembled themselves about 63% MORE than")
    print("  identical items built by someone else — even when the")
    print("  self-made versions were objectively worse.")
    print()
    print("  The effect requires COMPLETION. Unfinished builds don't")
    print("  get the value boost. It's the feeling of 'I made this'")
    print("  that rewires your appraisal.")
    print()
    print("  This is why IKEA, Nike By You, Build-A-Bear, and meal")
    print("  kits all work: a little labour makes customers love")
    print("  the product more — and pay more for it.")
    print()
    if overall_diff > 0:
        print("  Your results fit the pattern — you overvalued what")
        print("  you built, just like the study participants did.")
    else:
        print("  Your results bucked the trend — but in lab studies,")
        print("  the majority of people consistently overvalue their")
        print("  own handiwork. Awareness of the bias may have helped")
        print("  you resist it here.")
    print()


def main():
    show_intro()

    results = []
    for name, steps, premade_art in PROJECTS:
        my_val, pre_val = run_round(name, steps, premade_art)
        results.append((name, my_val, pre_val))

    debrief(results)


if __name__ == "__main__":
    main()
