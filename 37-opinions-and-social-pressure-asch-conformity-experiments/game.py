"""
Asch Conformity Experiment — Interactive Experience
Based on Asch (1955)

Experience the pull of social conformity when a group
gives an obviously wrong answer. Will you trust your eyes?
"""

import random
import time


NUM_ROUNDS = 12
CONFORMITY_ROUNDS = [2, 3, 5, 6, 8, 9, 10, 11]  # 8 of 12 are pressure rounds
FAKE_NAMES = [
    "Participant A", "Participant B", "Participant C",
    "Participant D", "Participant E",
]


def generate_lines():
    """Create a standard line and three comparison lines."""
    standard = random.randint(40, 80)
    correct_idx = random.randint(0, 2)
    comparisons = []
    for i in range(3):
        if i == correct_idx:
            comparisons.append(standard)
        else:
            offset = random.choice([-20, -15, -12, 12, 15, 20])
            comparisons.append(standard + offset)
    return standard, comparisons, correct_idx


def draw_line(length, label, max_len=80):
    """Draw a horizontal line with ASCII."""
    bar = "█" * (length // 2)
    return f"    {label}: {bar} ({length}mm)"


def show_intro():
    print("=" * 58)
    print("  THE ASCH CONFORMITY EXPERIMENT")
    print("  Based on Asch (1955)")
    print("=" * 58)
    print()
    print("  You're in a room with 5 other participants.")
    print("  (They're actually all in on the experiment.)")
    print()
    print("  Each round, you'll see a STANDARD line and three")
    print("  COMPARISON lines (A, B, C). One comparison clearly")
    print("  matches the standard.")
    print()
    print("  The other 'participants' will answer before you.")
    print("  Sometimes they'll all give the WRONG answer.")
    print()
    print("  Your job: pick the line that matches the standard.")
    print("  Trust your eyes... if you can.")
    print()
    input("  Press Enter to begin...\n")


def run_round(round_num, is_pressure):
    standard, comparisons, correct_idx = generate_lines()
    labels = ["A", "B", "C"]

    print("-" * 58)
    print(f"\n  ROUND {round_num}")
    print()
    print("  STANDARD LINE:")
    print(draw_line(standard, "S"))
    print()
    print("  COMPARISON LINES:")
    for i, (comp, label) in enumerate(zip(comparisons, labels)):
        print(draw_line(comp, label))
    print()

    # Generate fake participant answers
    if is_pressure:
        # All confederates pick the SAME wrong answer
        wrong_options = [i for i in range(3) if i != correct_idx]
        wrong_idx = random.choice(wrong_options)
        fake_answer = labels[wrong_idx]
        print("  Other participants' answers:")
        for name in FAKE_NAMES:
            time.sleep(0.4)
            print(f"    {name}: {fake_answer}")
        print()
    else:
        # Confederates answer correctly (to maintain illusion)
        print("  Other participants' answers:")
        for name in FAKE_NAMES:
            time.sleep(0.3)
            print(f"    {name}: {labels[correct_idx]}")
        print()

    # Get player's answer
    while True:
        answer = input("  YOUR ANSWER (A, B, or C): ").strip().upper()
        if answer in labels:
            break
        print("  Please type A, B, or C.")

    player_idx = labels.index(answer)
    player_correct = player_idx == correct_idx

    if is_pressure:
        conformed = answer == fake_answer
    else:
        conformed = False

    # Brief feedback
    if player_correct:
        print("  ✓ Correct.")
    else:
        print(f"  ✗ The correct answer was {labels[correct_idx]}.")

    if is_pressure and conformed:
        print("  (You matched the group's wrong answer.)")

    print()
    return {
        "round": round_num,
        "pressure": is_pressure,
        "correct": player_correct,
        "conformed": conformed,
    }


def debrief(results):
    pressure_rounds = [r for r in results if r["pressure"]]
    control_rounds = [r for r in results if not r["pressure"]]

    conformity_count = sum(1 for r in pressure_rounds if r["conformed"])
    pressure_correct = sum(1 for r in pressure_rounds if r["correct"])
    control_correct = sum(1 for r in control_rounds if r["correct"])

    conformity_rate = (conformity_count / len(pressure_rounds) * 100) if pressure_rounds else 0
    ever_conformed = conformity_count > 0

    print("\n" + "=" * 58)
    print("  DEBRIEF — YOUR CONFORMITY PROFILE")
    print("=" * 58)
    print()
    print(f"  PRESSURE ROUNDS (group gave wrong answer): {len(pressure_rounds)}")
    print(f"  Times you went with the group:  {conformity_count}/{len(pressure_rounds)}")
    print(f"  Your conformity rate:           {conformity_rate:.0f}%")
    print()
    print(f"  CONTROL ROUNDS (group gave right answer):  {len(control_rounds)}")
    print(f"  Times you got it right:         {control_correct}/{len(control_rounds)}")
    print()

    # Visual conformity bar
    print("  YOUR CONFORMITY ACROSS ROUNDS:")
    for r in results:
        if r["pressure"]:
            if r["conformed"]:
                tag = "██ CONFORMED"
            elif r["correct"]:
                tag = "░░ Resisted (correct)"
            else:
                tag = "▒▒ Wrong (but not conforming)"
        else:
            tag = "·· Control round"
        print(f"    Round {r['round']:>2}: {tag}")

    print()
    print("=" * 58)
    print("  WHAT ASCH FOUND")
    print("=" * 58)
    print()
    print("  In the original 1955 experiments:")
    print()
    print("  • 75% of participants conformed AT LEAST ONCE")
    print("  • Overall conformity rate: ~37% on pressure trials")
    print("  • Error rate without pressure: less than 1%")
    print()

    if ever_conformed:
        print(f"  You conformed {conformity_count} time(s). You're in the majority")
        print("  — most people do. Asch found three reasons:")
        print()
        print("  1. Distortion of PERCEPTION — you start to genuinely")
        print("     see it the group's way")
        print("  2. Distortion of JUDGMENT — you think 'they must know")
        print("     something I don't'")
        print("  3. Distortion of ACTION — you KNOW they're wrong but")
        print("     go along to avoid standing out")
    else:
        print("  You never conformed — only about 25% of Asch's")
        print("  participants managed that. But notice: even if you")
        print("  answered correctly, did you HESITATE? That pause is")
        print("  the conformity pressure working on you.")

    print()
    print("  WHY THIS MATTERS FOR MARKETING:")
    print()
    print("  Social proof (reviews, 'bestseller' labels, '10,000")
    print("  people bought this') creates the same pressure.")
    print("  When everyone seems to agree, System 1 screams")
    print("  'go with the group' — even if the evidence of")
    print("  your own experience says otherwise.")
    print()
    print("  One dissenter breaks the spell. That's why a few")
    print("  honest negative reviews actually INCREASE trust.")
    print()


def main():
    show_intro()
    results = []

    for round_num in range(1, NUM_ROUNDS + 1):
        is_pressure = round_num in CONFORMITY_ROUNDS
        result = run_round(round_num, is_pressure)
        results.append(result)

    debrief(results)


if __name__ == "__main__":
    main()
