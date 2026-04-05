"""
Judgment Under Uncertainty: Heuristics and Biases — Interactive Experience
Based on Tversky & Kahneman (1974)

Experience the three classic heuristic traps firsthand:
representativeness, availability, and anchoring.
"""

import random
import time


def show_intro():
    print("=" * 60)
    print("  HEURISTICS & BIASES LAB")
    print("  Based on Tversky & Kahneman (1974)")
    print("=" * 60)
    print()
    print("  You'll face a series of judgment tasks.")
    print("  Answer each one with your gut feeling.")
    print("  Be honest — don't try to outsmart the test.")
    print()
    print("  Afterward, we'll reveal the traps your brain")
    print("  fell into — the same ones everyone falls into.")
    print()
    input("  Press Enter to begin...\n")


def get_int(prompt, low=None, high=None):
    while True:
        try:
            val = int(input(prompt))
            if low is not None and val < low:
                print(f"  Please enter a number of at least {low}.")
                continue
            if high is not None and val > high:
                print(f"  Please enter a number no higher than {high}.")
                continue
            return val
        except ValueError:
            print("  Please enter a whole number.")


def get_choice(prompt, options):
    while True:
        answer = input(prompt).strip().upper()
        if answer in options:
            return answer
        print(f"  Please enter one of: {', '.join(options)}")


# ─── REPRESENTATIVENESS HEURISTIC ───────────────────────────

def representativeness_test():
    print("\n" + "─" * 60)
    print("  SECTION 1: PROFILE JUDGMENT")
    print("─" * 60)

    print("""
  Linda is 31 years old, single, outspoken, and very bright.
  She studied philosophy at university. As a student, she was
  deeply concerned with issues of discrimination and social
  justice, and participated in anti-nuclear demonstrations.
""")

    print("  Which is MORE PROBABLE?")
    print()
    print("    A. Linda is a bank teller.")
    print("    B. Linda is a bank teller AND active in the")
    print("       feminist movement.")
    print()

    answer = get_choice("  Your answer (A or B): ", ["A", "B"])

    print()
    print("  ---")

    # Second representativeness problem
    print("""
  Tom is a quiet man who wears glasses, loves puzzles, and
  spends his evenings reading technical manuals. He is shy
  and rarely socialises.
""")
    print("  Which is more likely to be Tom's profession?")
    print()
    print("    A. Librarian")
    print("    B. Salesperson")
    print()
    answer2 = get_choice("  Your answer (A or B): ", ["A", "B"])

    return answer, answer2


# ─── AVAILABILITY HEURISTIC ─────────────────────────────────

def availability_test():
    print("\n" + "─" * 60)
    print("  SECTION 2: FREQUENCY ESTIMATES")
    print("─" * 60)

    print("""
  In a typical year in a developed country, which causes
  MORE deaths?
""")
    pairs = [
        {
            "a": "Shark attacks",
            "b": "Falling coconuts",
            "correct": "B",
            "fact": "Coconuts kill ~150 people/year globally vs ~10 for sharks.\n"
                    "  But shark attacks make the news; falling coconuts don't.",
        },
        {
            "a": "Plane crashes",
            "b": "Car accidents",
            "correct": "B",
            "fact": "Car accidents kill tens of thousands more per year.\n"
                    "  But a single plane crash dominates news for days.",
        },
        {
            "a": "Terrorism",
            "b": "Falling down stairs",
            "correct": "B",
            "fact": "Stair falls kill thousands annually in the UK alone.\n"
                    "  But terrorism receives vastly more media coverage.",
        },
    ]

    answers = []
    for i, pair in enumerate(pairs, 1):
        print(f"  Question {i}:")
        print(f"    A. {pair['a']}")
        print(f"    B. {pair['b']}")
        ans = get_choice("  Your answer (A or B): ", ["A", "B"])
        answers.append((ans, pair))
        print()

    return answers


# ─── ANCHORING HEURISTIC ────────────────────────────────────

def anchoring_test():
    print("\n" + "─" * 60)
    print("  SECTION 3: QUICK ESTIMATES")
    print("─" * 60)

    # Generate a random anchor (high or low)
    high_anchor = random.choice([True, False])

    if high_anchor:
        anchor = 65
        print(f"""
  The percentage of African countries in the United Nations...
  Is it MORE or LESS than {anchor}%?
""")
    else:
        anchor = 10
        print(f"""
  The percentage of African countries in the United Nations...
  Is it MORE or LESS than {anchor}%?
""")

    get_choice("  More or Less? (M or L): ", ["M", "L"])

    print()
    estimate1 = get_int("  Now give your actual estimate (0-100%): ", 0, 100)

    # Second anchoring problem
    print()
    print("  Quick! You have 5 seconds to ESTIMATE this product:")
    print()
    if high_anchor:
        print("    8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = ?")
        order = "descending"
    else:
        print("    1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 = ?")
        order = "ascending"

    print()
    print("  Don't calculate — just estimate fast!")
    estimate2 = get_int("  Your estimate: ", 0)

    return high_anchor, anchor, estimate1, estimate2, order


# ─── DEBRIEF ────────────────────────────────────────────────

def debrief(rep_answers, avail_answers, anchor_data):
    linda_answer, tom_answer = rep_answers
    high_anchor, anchor, un_estimate, mult_estimate, order = anchor_data

    print("\n" + "=" * 60)
    print("  RESULTS — YOUR HEURISTIC PROFILE")
    print("=" * 60)

    # Representativeness
    print("\n  --- REPRESENTATIVENESS ---")
    print()
    if linda_answer == "B":
        print("  THE LINDA PROBLEM: You chose B (bank teller AND feminist).")
        print("  That's the trap! 85% of people choose B.")
        print()
        print("  But it's LOGICALLY IMPOSSIBLE for B to be more likely")
        print("  than A. 'Bank teller AND feminist' is a SUBSET of")
        print("  'bank teller' — so it can never be more probable.")
        print()
        print("  Your brain matched Linda's description to a 'feminist'")
        print("  prototype and ignored basic probability. That's the")
        print("  REPRESENTATIVENESS heuristic at work.")
    else:
        print("  THE LINDA PROBLEM: You chose A. That's correct!")
        print("  Most people (85%) choose B, falling for the trap.")
        print("  'Bank teller AND feminist' can never be more probable")
        print("  than 'bank teller' alone — it's a subset.")
        print("  You resisted the representativeness heuristic here.")

    print()
    if tom_answer == "A":
        print("  THE TOM PROBLEM: You chose Librarian.")
        print("  Tom 'feels' like a librarian — he matches the stereotype.")
        print("  But there are roughly 10x more salespeople than librarians.")
        print("  Base rates matter, but representativeness overrides them.")
    else:
        print("  THE TOM PROBLEM: You chose Salesperson — good thinking!")
        print("  Most people say Librarian because Tom 'fits the type.'")
        print("  But salespeople vastly outnumber librarians, so pure")
        print("  probability favours salesperson despite the description.")

    # Availability
    print("\n  --- AVAILABILITY ---")
    correct_avail = 0
    for ans, pair in avail_answers:
        is_correct = ans == pair["correct"]
        if is_correct:
            correct_avail += 1
        symbol = "CORRECT" if is_correct else "WRONG"
        print(f"\n  {pair['a']} vs {pair['b']}: You said {'A' if ans == 'A' else 'B'} — {symbol}")
        if not is_correct:
            print(f"  {pair['fact']}")

    if correct_avail <= 1:
        print("\n  The AVAILABILITY heuristic got you: dramatic, memorable")
        print("  events feel more common because examples flood your mind.")
        print("  The news warps your sense of what's actually dangerous.")
    else:
        print("\n  You beat the availability bias on most of these!")
        print("  Most people overestimate dramatic causes of death because")
        print("  vivid examples come to mind easily.")

    # Anchoring
    print("\n  --- ANCHORING ---")
    print(f"\n  Your anchor was {anchor}% ({'high' if high_anchor else 'low'}).")
    print(f"  Your UN estimate: {un_estimate}%")
    print(f"  The actual answer: ~28% of UN members are African countries.")
    print()
    if high_anchor and un_estimate > 35:
        print("  The HIGH anchor pulled your estimate UP — classic anchoring.")
    elif not high_anchor and un_estimate < 22:
        print("  The LOW anchor pulled your estimate DOWN — classic anchoring.")
    else:
        print("  You resisted the anchor somewhat — but in Kahneman's")
        print("  experiments, even experts are pulled toward the anchor.")

    print(f"\n  The multiplication estimate:")
    print(f"  You saw the {order} sequence and guessed {mult_estimate:,}.")
    print(f"  The actual answer: 40,320.")
    print()
    print(f"  Kahneman found that people shown 8x7x6x5... estimated")
    print(f"  ~2,250 on average, while those shown 1x2x3x4... estimated")
    print(f"  ~512. The first few numbers ANCHOR the estimate.")

    # Final summary
    print("\n" + "=" * 60)
    print("  THE SCIENCE")
    print("=" * 60)
    print()
    print("  Tversky & Kahneman (1974) showed that human judgment")
    print("  under uncertainty relies on THREE mental shortcuts:")
    print()
    print("  1. REPRESENTATIVENESS — judging by how well something")
    print("     matches a stereotype, ignoring base rates")
    print()
    print("  2. AVAILABILITY — estimating frequency by how easily")
    print("     examples come to mind (vivid = 'common')")
    print()
    print("  3. ANCHORING — starting from an arbitrary number and")
    print("     adjusting too little from it")
    print()
    print("  These aren't flaws in YOUR thinking — they're built")
    print("  into ALL human cognition. Marketers use them daily:")
    print()
    print("  • High 'was' prices ANCHOR you to see discounts as bigger")
    print("  • Memorable ads make brands feel more popular (availability)")
    print("  • Packaging that 'looks premium' beats actual quality")
    print("    (representativeness)")
    print()
    print("  Knowing these biases exist doesn't make you immune —")
    print("  but it does help you notice when they're pulling your")
    print("  judgments in predictable directions.")
    print()


def main():
    show_intro()

    rep_answers = representativeness_test()
    avail_answers = availability_test()
    anchor_data = anchoring_test()

    debrief(rep_answers, avail_answers, anchor_data)


if __name__ == "__main__":
    main()
