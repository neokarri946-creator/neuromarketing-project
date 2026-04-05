"""
Thinking, Fast and Slow — Interactive Experience
Based on Kahneman (2011)

Feel the difference between your fast, intuitive System 1
and your slow, deliberate System 2.
"""

import time

PROBLEMS = [
    {
        "name": "The Bat and Ball",
        "setup": (
            "A bat and a ball cost £1.10 in total.\n"
            "The bat costs £1.00 more than the ball.\n"
            "How much does the ball cost?"
        ),
        "intuitive_trap": "10p",
        "correct": "5p",
        "explanation": (
            "Most people's gut says 10p — that's System 1 leaping to\n"
            "  an answer that 'feels' right. But if the ball is 10p and\n"
            "  the bat is £1.00 MORE, the bat would be £1.10, totalling\n"
            "  £1.20 — not £1.10. The real answer: the ball is 5p and\n"
            "  the bat is £1.05. System 2 catches this, but only if you\n"
            "  slow down enough to engage it."
        ),
        "accept": ["5", "5p", "0.05", "£0.05"],
    },
    {
        "name": "The Linda Problem",
        "setup": (
            "Linda is 31, single, outspoken, and very bright.\n"
            "She majored in philosophy. As a student she was deeply\n"
            "concerned with discrimination and social justice,\n"
            "and participated in anti-nuclear demonstrations.\n\n"
            "Which is MORE LIKELY?\n"
            "  A) Linda is a bank teller.\n"
            "  B) Linda is a bank teller AND active in the feminist movement."
        ),
        "intuitive_trap": "B",
        "correct": "A",
        "explanation": (
            "System 1 picks B because the story 'fits' — Linda sounds\n"
            "  like a feminist. But this is the conjunction fallacy.\n"
            "  The probability of TWO things both being true (bank teller\n"
            "  AND feminist) can never be higher than ONE of them alone\n"
            "  (bank teller). It's like asking: is it more likely to rain,\n"
            "  or to rain AND be a Tuesday? System 1 matches narratives;\n"
            "  System 2 follows logic."
        ),
        "accept": ["a", "A"],
    },
    {
        "name": "The Hospital Problem",
        "setup": (
            "A town has two hospitals. The large hospital has about\n"
            "45 births per day. The small one has about 15.\n\n"
            "On average, 50% of babies are boys. But the exact\n"
            "percentage varies day to day.\n\n"
            "Over a year, which hospital recorded more days where\n"
            "over 60% of babies born were boys?\n"
            "  A) The large hospital\n"
            "  B) The small hospital\n"
            "  C) About the same"
        ),
        "intuitive_trap": "C",
        "correct": "B",
        "explanation": (
            "System 1 says 'about the same' — both are hospitals,\n"
            "  both have the same average. But System 2 knows that\n"
            "  smaller samples vary more. Flip a coin 10 times and\n"
            "  getting 8 heads is common. Flip it 1000 times and\n"
            "  getting 800 heads is virtually impossible. The small\n"
            "  hospital, with fewer births, sees more extreme swings.\n"
            "  System 1 ignores sample size; System 2 accounts for it."
        ),
        "accept": ["b", "B"],
    },
    {
        "name": "Anchoring",
        "setup": (
            "Quick — DON'T calculate, just GUESS:\n\n"
            "  What is  8 × 7 × 6 × 5 × 4 × 3 × 2 × 1  ?\n\n"
            "Type your gut estimate (just a number):"
        ),
        "intuitive_trap": "around 2,000-5,000",
        "correct": "40,320",
        "explanation": (
            "The real answer is 40,320. Most people guess far too low\n"
            "  (typically 2,000-5,000). System 1 starts multiplying the\n"
            "  first few numbers (8×7=56, ×6=336...) then anchors on\n"
            "  that early impression and stops calculating. Kahneman\n"
            "  showed that reversing the order (1×2×3×...) produces\n"
            "  even lower guesses (~500) because the early anchor is\n"
            "  smaller. System 1 anchors and adjusts insufficiently."
        ),
        "accept": ["40320", "40,320"],
    },
    {
        "name": "Cognitive Ease",
        "setup": (
            "Read these two statements and pick which FEELS more true:\n\n"
            "  A) Woes unite foes.\n"
            "  B) Woes unite enemies.\n\n"
            "Which statement feels more believable?"
        ),
        "intuitive_trap": "A",
        "correct": "NEITHER — they say the same thing",
        "explanation": (
            "Both statements mean exactly the same thing. But most\n"
            "  people feel that 'Woes unite foes' is more true. Why?\n"
            "  Because it rhymes. System 1 uses cognitive ease — how\n"
            "  smoothly something is processed — as a signal of truth.\n"
            "  Rhyming phrases feel fluent, and fluency feels like\n"
            "  truth. This is why advertising slogans rhyme, and why\n"
            "  'If it doesn't fit, you must acquit' was so persuasive.\n"
            "  System 1 confuses 'easy to process' with 'likely true'."
        ),
        "accept": ["a", "A", "b", "B"],
    },
    {
        "name": "The Availability Heuristic",
        "setup": (
            "Which causes more deaths per year in the UK?\n\n"
            "  A) Shark attacks\n"
            "  B) Falling vending machines\n"
            "  C) They're about equal"
        ),
        "intuitive_trap": "A",
        "correct": "B",
        "explanation": (
            "Vending machines kill far more people than sharks do.\n"
            "  But System 1 judges frequency by how easily examples\n"
            "  come to mind — the 'availability heuristic'. Shark\n"
            "  attacks are vivid, dramatic, and heavily covered in\n"
            "  media. Vending machine deaths are mundane and rarely\n"
            "  reported. System 1 mistakes 'easy to recall' for\n"
            "  'happens often'. Marketers use this constantly —\n"
            "  dramatic testimonials feel more representative than\n"
            "  dry statistics, even when the statistics are more\n"
            "  accurate."
        ),
        "accept": ["b", "B"],
    },
]


def show_intro():
    print("=" * 58)
    print("  THINKING, FAST AND SLOW")
    print("  Based on Kahneman (2011)")
    print("=" * 58)
    print()
    print("  Your brain has two modes:")
    print()
    print("  SYSTEM 1 — Fast, automatic, intuitive")
    print("  SYSTEM 2 — Slow, deliberate, analytical")
    print()
    print("  You'll face 6 problems. For each one, answer with")
    print("  your GUT INSTINCT first. Don't overthink it.")
    print()
    print("  Then we'll see where System 1 led you astray")
    print("  — and where System 2 could have saved you.")
    print()
    input("  Press Enter to begin...\n")


def run_trial(problem):
    print("-" * 58)
    print(f"\n  {problem['name'].upper()}")
    print()
    print(f"  {problem['setup']}")
    print()

    start = time.time()
    answer = input("  Your answer: ").strip()
    elapsed = time.time() - start

    is_correct = answer.lower().replace("£", "").replace(" ", "") in [
        a.lower().replace("£", "").replace(" ", "") for a in problem["accept"]
    ]

    speed_label = "FAST" if elapsed < 10 else "SLOW"

    print()
    if is_correct and problem["name"] != "Cognitive Ease":
        print("  ✓ CORRECT — System 2 caught this one!")
    elif problem["name"] == "Cognitive Ease":
        print(f"  You picked: {answer}")
        print(f"  Correct answer: {problem['correct']}")
    else:
        print(f"  ✗ The intuitive trap strikes.")
        print(f"  Your answer: {answer}")
        print(f"  Correct answer: {problem['correct']}")

    print()
    print(f"  Response time: {elapsed:.1f}s ({speed_label})")
    print(f"\n  WHY THIS HAPPENS:")
    print(f"  {problem['explanation']}")
    print()
    input("  Press Enter for next problem...\n")

    return {
        "name": problem["name"],
        "correct": is_correct if problem["name"] != "Cognitive Ease" else None,
        "elapsed": elapsed,
        "speed": speed_label,
    }


def debrief(results):
    print("\n" + "=" * 58)
    print("  DEBRIEF — YOUR SYSTEM 1 vs SYSTEM 2 SCORECARD")
    print("=" * 58)

    scoreable = [r for r in results if r["correct"] is not None]
    system1_wins = sum(1 for r in scoreable if not r["correct"])
    system2_wins = sum(1 for r in scoreable if r["correct"])
    avg_time = sum(r["elapsed"] for r in results) / len(results)

    print()
    print(f"  Problems where System 1 tricked you: {system1_wins}/{len(scoreable)}")
    print(f"  Problems where System 2 saved you:   {system2_wins}/{len(scoreable)}")
    print(f"  Average response time: {avg_time:.1f}s")
    print()

    print("  YOUR RESULTS:")
    for r in results:
        if r["correct"] is None:
            tag = "DEMO"
        elif r["correct"]:
            tag = "System 2 ✓"
        else:
            tag = "System 1 trap ✗"
        print(f"    {r['name']:<30} {r['elapsed']:>5.1f}s  {tag}")

    print()
    print("=" * 58)
    print("  THE BIG PICTURE")
    print("=" * 58)
    print()
    print("  Kahneman's key insight: System 1 runs the show.")
    print("  It handles 95%+ of daily decisions — quickly,")
    print("  efficiently, and usually well enough.")
    print()
    print("  But it has blind spots. It anchors on first")
    print("  impressions. It confuses fluency with truth.")
    print("  It ignores base rates. It matches narratives")
    print("  instead of following logic.")
    print()
    print("  Marketers design for System 1 — simple messages,")
    print("  familiar brands, emotional appeals, round prices.")
    print("  The problems you just faced are the same traps")
    print("  that make advertising, pricing, and persuasion work.")
    print()
    print("  The defence? Knowing WHEN to slow down and let")
    print("  System 2 take the wheel. Not always — just when")
    print("  the stakes are high and the answer feels too easy.")
    print()


def main():
    show_intro()
    results = []
    for problem in PROBLEMS:
        result = run_trial(problem)
        results.append(result)
    debrief(results)


if __name__ == "__main__":
    main()
