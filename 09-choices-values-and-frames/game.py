"""
THE FRAMING EFFECT
==================
Based on: Choices, Values, and Frames (1984) — Kahneman & Tversky

The same facts, worded differently, lead to opposite choices.
This game presents you with identical scenarios in different
frames to see if your preferences flip.
"""

import random

def intro():
    print("=" * 50)
    print("  THE FRAMING EFFECT")
    print("  Same facts. Different words. Different choice?")
    print("=" * 50)
    print()
    print("You'll face several difficult decisions.")
    print("Choose the option that feels right to you.")
    print("Go with your gut — don't analyse too much.")
    print()
    input("Press Enter to begin...\n")

def get_choice():
    while True:
        c = input("  Your choice (A or B): ").strip().upper()
        if c in ('A', 'B'):
            return c
        print("  Please type A or B.")

# Each scenario has a GAIN frame and a LOSS frame.
# The options are mathematically identical across frames.
SCENARIOS = [
    {
        "name": "The Disease Outbreak",
        "context": "A dangerous disease is expected to kill 600 people.\nTwo emergency programmes have been proposed.",
        "gain_frame": {
            "intro": "Here are the programmes:",
            "a": "Programme A: 200 people will be saved",
            "b": "Programme B: 1/3 chance all 600 are saved, 2/3 chance nobody is saved",
        },
        "loss_frame": {
            "intro": "Here are the programmes:",
            "a": "Programme A: 400 people will die",
            "b": "Programme B: 1/3 chance nobody dies, 2/3 chance all 600 die",
        },
        "gain_predicted": "A",
        "loss_predicted": "B",
        "explanation": "These are the EXACT SAME outcomes.\n'200 saved out of 600' = '400 die out of 600'.\nBut the gain frame makes you cautious (save 200 for sure!)\nwhile the loss frame makes you gamble (maybe nobody has to die!).",
    },
    {
        "name": "The Factory Layoffs",
        "context": "Your company must restructure. 300 jobs are at risk.\nYou must choose a plan.",
        "gain_frame": {
            "intro": "The options are:",
            "a": "Plan A: 100 jobs will definitely be preserved",
            "b": "Plan B: 1/3 chance all 300 jobs are saved, 2/3 chance no jobs are saved",
        },
        "loss_frame": {
            "intro": "The options are:",
            "a": "Plan A: 200 jobs will definitely be lost",
            "b": "Plan B: 1/3 chance no jobs are lost, 2/3 chance all 300 jobs are lost",
        },
        "gain_predicted": "A",
        "loss_predicted": "B",
        "explanation": "'100 preserved out of 300' = '200 lost out of 300'.\nSame outcome, but 'jobs preserved' feels protective\nwhile 'jobs lost' feels devastating and pushes you to gamble.",
    },
    {
        "name": "The Investment Decision",
        "context": "You invested $6,000 across several stocks.\nThe market has been volatile. You must choose a strategy.",
        "gain_frame": {
            "intro": "Your options:",
            "a": "Strategy A: You will keep $2,000 of your investment",
            "b": "Strategy B: 1/3 chance of keeping all $6,000, 2/3 chance of keeping nothing",
        },
        "loss_frame": {
            "intro": "Your options:",
            "a": "Strategy A: You will lose $4,000 of your investment",
            "b": "Strategy B: 1/3 chance of losing nothing, 2/3 chance of losing all $6,000",
        },
        "gain_predicted": "A",
        "loss_predicted": "B",
        "explanation": "'Keep $2,000' = 'Lose $4,000' (from $6,000).\nWhen you read 'keep', you want to lock it in.\nWhen you read 'lose', you want to escape the pain.",
    },
    {
        "name": "The Medical Treatment",
        "context": "You've been diagnosed with a serious condition.\n1,000 patients have had this condition. You must choose a treatment.",
        "gain_frame": {
            "intro": "The treatments:",
            "a": "Treatment A: 500 patients survived after 5 years",
            "b": "Treatment B: 50% chance all 1,000 survive, 50% chance none survive",
        },
        "loss_frame": {
            "intro": "The treatments:",
            "a": "Treatment A: 500 patients died within 5 years",
            "b": "Treatment B: 50% chance nobody dies, 50% chance all 1,000 die",
        },
        "gain_predicted": "A",
        "loss_predicted": "B",
        "explanation": "'500 survived' = '500 died' (out of 1,000).\nDoctors know that framing survival vs mortality rates\nchanges patient decisions — even when the numbers are identical.",
    },
]

def run_game():
    intro()

    # Present scenarios in pairs — gain frame first for some, loss frame first for others
    # Shuffle the order and which frame comes first
    order = list(range(len(SCENARIOS)))
    random.shuffle(order)

    results = []

    round_num = 1
    for idx in order:
        s = SCENARIOS[idx]

        # Randomly choose which frame to show
        # (we only show ONE frame per scenario to avoid the player catching on)
        if random.random() < 0.5:
            frame = "gain"
            shown = s["gain_frame"]
            predicted = s["gain_predicted"]
        else:
            frame = "loss"
            shown = s["loss_frame"]
            predicted = s["loss_predicted"]

        print(f"  --- SCENARIO {round_num} of {len(SCENARIOS)}: {s['name']} ---")
        print()
        for line in s["context"].split("\n"):
            print(f"  {line}")
        print()
        print(f"  {shown['intro']}")
        print(f"  A: {shown['a']}")
        print(f"  B: {shown['b']}")
        print()

        choice = get_choice()
        results.append({
            "scenario": s,
            "frame": frame,
            "choice": choice,
            "predicted": predicted,
            "matched": choice == predicted,
        })
        round_num += 1
        print()

    # Now show one head-to-head comparison
    print("=" * 50)
    print("  BONUS ROUND: SAME SCENARIO, BOTH FRAMES")
    print("=" * 50)
    print()
    print("  Now I'll show you the SAME situation twice,")
    print("  worded differently. Answer each honestly.")
    print()

    bonus = SCENARIOS[0]  # The classic Asian Disease problem

    # Gain frame
    print(f"  VERSION 1:")
    print(f"  {bonus['context']}")
    print()
    print(f"  A: {bonus['gain_frame']['a']}")
    print(f"  B: {bonus['gain_frame']['b']}")
    print()
    gain_choice = get_choice()
    print()

    # Loss frame
    print(f"  VERSION 2:")
    print(f"  {bonus['context']}")
    print()
    print(f"  A: {bonus['loss_frame']['a']}")
    print(f"  B: {bonus['loss_frame']['b']}")
    print()
    loss_choice = get_choice()
    print()

    # === DEBRIEF ===
    print("=" * 50)
    print("  RESULTS: HOW FRAMING SHAPED YOUR CHOICES")
    print("=" * 50)
    print()

    matched = sum(1 for r in results if r["matched"])
    print(f"  Main rounds: {matched} of {len(results)} choices matched")
    print(f"  the predicted framing effect pattern.")
    print()

    for r in results:
        s = r["scenario"]
        print(f"  {s['name']} ({r['frame'].upper()} frame)")
        print(f"  You chose: {r['choice']}  |  Predicted: {r['predicted']}")
        tag = "MATCHED" if r["matched"] else "BUCKED THE TREND"
        print(f"  [{tag}]")
        print()

    # Bonus round reveal
    print("-" * 50)
    print("  BONUS ROUND REVEAL:")
    print("-" * 50)
    print()
    if gain_choice != loss_choice:
        print("  YOUR PREFERENCES FLIPPED!")
        print()
        print(f"  Gain frame: you chose {gain_choice}")
        print(f"  Loss frame: you chose {loss_choice}")
        print()
        print("  The two versions describe IDENTICAL outcomes.")
        print("  But different words triggered different feelings,")
        print("  which triggered different choices.")
    else:
        print(f"  You chose {gain_choice} both times — consistent!")
        print("  You resisted the framing effect here. That's")
        print("  uncommon. Most people's choices flip when the")
        print("  wording changes from gains to losses.")

    print()
    for line in bonus["explanation"].split("\n"):
        print(f"  {line}")

    print()
    print("  THE SCIENCE:")
    print("  Kahneman & Tversky (1984) showed that preferences")
    print("  are not fixed — they are CONSTRUCTED by how options")
    print("  are presented. The frame is not decoration. It is")
    print("  part of the decision.")
    print()
    print("  Marketers, politicians, and doctors use this daily:")
    print("  '90% fat-free' vs '10% fat' — same product,")
    print("  different frame, different sales. Whoever controls")
    print("  the frame controls the choice.")
    print()

if __name__ == "__main__":
    run_game()
