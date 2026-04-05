"""
Unskilled and Unaware of It — Interactive Experience
Based on Kruger & Dunning (1999)

Take a quiz on an obscure topic, estimate how well you did,
then see the truth. Most people overestimate — and the less
they know, the more they overestimate.
"""

import random


def show_intro():
    print("=" * 58)
    print("  THE DUNNING-KRUGER EFFECT")
    print("  Based on Kruger & Dunning (1999)")
    print("=" * 58)
    print()
    print("  You're about to take a 15-question quiz on a topic")
    print("  you probably know very little about: world flags,")
    print("  obscure geography, and unusual science facts.")
    print()
    print("  After each section of 5 questions, you'll estimate")
    print("  how many you got RIGHT — before seeing the answers.")
    print()
    print("  At the end, we'll compare your estimates to your")
    print("  actual performance. The gap reveals something")
    print("  fascinating about how the human mind works.")
    print()
    input("  Press Enter to begin...\n")


# Questions organised by section
SECTIONS = [
    {
        "name": "WORLD FLAGS & GEOGRAPHY",
        "questions": [
            {
                "q": "What country's flag is entirely green with no other\n  colours, symbols, or markings?",
                "options": ["A) Saudi Arabia", "B) Libya (1977-2011)",
                            "C) Bangladesh", "D) Nigeria"],
                "answer": "B",
                "explanation": "Libya's flag from 1977-2011 was a plain green rectangle — the only national flag in history with just one colour and no design.",
            },
            {
                "q": "Which country has the most time zones?",
                "options": ["A) Russia", "B) United States",
                            "C) France", "D) China"],
                "answer": "C",
                "explanation": "France has 12 time zones (due to overseas territories), beating Russia's 11.",
            },
            {
                "q": "What is the only country whose flag is not rectangular\n  or square?",
                "options": ["A) Switzerland", "B) Vatican City",
                            "C) Nepal", "D) Bhutan"],
                "answer": "C",
                "explanation": "Nepal's flag is made of two stacked triangles — the only non-quadrilateral national flag.",
            },
            {
                "q": "Which African country was formerly known as Abyssinia?",
                "options": ["A) Somalia", "B) Eritrea",
                            "C) Ethiopia", "D) Sudan"],
                "answer": "C",
                "explanation": "Ethiopia was historically known as Abyssinia until the 20th century.",
            },
            {
                "q": "What is the smallest country in mainland Africa?",
                "options": ["A) Eswatini", "B) The Gambia",
                            "C) Djibouti", "D) Lesotho"],
                "answer": "B",
                "explanation": "The Gambia (11,295 km2) is the smallest country on mainland Africa.",
            },
        ],
    },
    {
        "name": "UNUSUAL SCIENCE",
        "questions": [
            {
                "q": "What percentage of the universe's total matter is\n  made up of ordinary (visible) matter?",
                "options": ["A) About 50%", "B) About 27%",
                            "C) About 5%", "D) About 15%"],
                "answer": "C",
                "explanation": "Only about 5% of the universe is ordinary matter. ~27% is dark matter and ~68% is dark energy.",
            },
            {
                "q": "How long does it take for light from the Sun to\n  reach Earth?",
                "options": ["A) About 8 seconds", "B) About 8 minutes",
                            "C) About 80 minutes", "D) About 1 minute"],
                "answer": "B",
                "explanation": "Light from the Sun takes approximately 8 minutes and 20 seconds to reach Earth.",
            },
            {
                "q": "What is the most abundant gas in Earth's atmosphere?",
                "options": ["A) Oxygen", "B) Carbon dioxide",
                            "C) Nitrogen", "D) Hydrogen"],
                "answer": "C",
                "explanation": "Nitrogen makes up about 78% of Earth's atmosphere. Oxygen is second at about 21%.",
            },
            {
                "q": "Which planet in our solar system has the shortest\n  day (fastest rotation)?",
                "options": ["A) Mercury", "B) Mars",
                            "C) Jupiter", "D) Saturn"],
                "answer": "C",
                "explanation": "Jupiter rotates in about 9 hours 56 minutes — the fastest of any planet in our solar system.",
            },
            {
                "q": "What is the hardest natural substance on Earth?",
                "options": ["A) Titanium", "B) Quartz",
                            "C) Diamond", "D) Corundum"],
                "answer": "C",
                "explanation": "Diamond is the hardest natural substance, scoring 10 on the Mohs hardness scale.",
            },
        ],
    },
    {
        "name": "HISTORY & LANGUAGE",
        "questions": [
            {
                "q": "Which language has the most native speakers worldwide?",
                "options": ["A) English", "B) Spanish",
                            "C) Hindi", "D) Mandarin Chinese"],
                "answer": "D",
                "explanation": "Mandarin Chinese has roughly 920 million native speakers, more than any other language.",
            },
            {
                "q": "In what year did the Berlin Wall fall?",
                "options": ["A) 1987", "B) 1989",
                            "C) 1991", "D) 1985"],
                "answer": "B",
                "explanation": "The Berlin Wall fell on 9 November 1989.",
            },
            {
                "q": "What was the shortest war in recorded history?",
                "options": ["A) Six Day War (Israel-Arab)",
                            "B) Falklands War (UK-Argentina)",
                            "C) Anglo-Zanzibar War",
                            "D) Football War (El Salvador-Honduras)"],
                "answer": "C",
                "explanation": "The Anglo-Zanzibar War of 1896 lasted between 38 and 45 minutes.",
            },
            {
                "q": "Which ancient civilisation invented the concept of\n  zero as a number?",
                "options": ["A) Ancient Greece", "B) Ancient Egypt",
                            "C) Ancient India", "D) Ancient China"],
                "answer": "C",
                "explanation": "The concept of zero as a number (not just a placeholder) was developed in ancient India, notably by Brahmagupta in 628 CE.",
            },
            {
                "q": "What does the word 'gymnasium' literally mean in\n  its original Greek?",
                "options": ["A) Place of strength",
                            "B) Place to exercise naked",
                            "C) House of athletes",
                            "D) Hall of competition"],
                "answer": "B",
                "explanation": "From Greek 'gymnos' meaning naked — ancient Greeks exercised without clothes.",
            },
        ],
    },
]


def run_section(section):
    """Run one section of 5 questions, then ask for estimate."""
    print(f"\n{'=' * 58}")
    print(f"  SECTION: {section['name']}")
    print(f"{'=' * 58}")
    print()

    answers = []
    questions = section["questions"]

    for i, q in enumerate(questions, 1):
        print(f"  Question {i}/5:")
        print(f"  {q['q']}")
        print()
        for opt in q["options"]:
            print(f"    {opt}")
        print()

        while True:
            choice = input("  Your answer (A/B/C/D): ").strip().upper()
            if choice in ("A", "B", "C", "D"):
                correct = choice == q["answer"]
                answers.append(correct)
                break
            print("  Please enter A, B, C, or D.")
        print()

    # Ask for estimate BEFORE revealing answers
    print(f"  {'-' * 48}")
    print(f"  You've finished this section.")
    print(f"  Before I show you the answers...")
    print()

    while True:
        try:
            estimate = int(input("  How many out of 5 do you think you got right? "))
            if 0 <= estimate <= 5:
                break
            print("  Enter a number from 0 to 5.")
        except ValueError:
            print("  Enter a number from 0 to 5.")

    actual = sum(answers)

    # Now reveal answers
    print(f"\n  ANSWERS:")
    print(f"  {'-' * 48}")
    for i, q in enumerate(questions):
        status = "CORRECT" if answers[i] else "WRONG"
        marker = "+" if answers[i] else "x"
        print(f"  [{marker}] Q{i+1}: {q['answer']} — {q['explanation']}")
    print()
    print(f"  Your estimate: {estimate}/5")
    print(f"  Actual score:  {actual}/5")

    gap = estimate - actual
    if gap > 0:
        print(f"  Overestimated by {gap}")
    elif gap < 0:
        print(f"  Underestimated by {abs(gap)}")
    else:
        print(f"  Spot on!")

    return {"estimate": estimate, "actual": actual}


def main():
    show_intro()

    all_results = []
    for section in SECTIONS:
        result = run_section(section)
        all_results.append(result)
        print()
        input("  Press Enter to continue...\n")

    # --- OVERALL DEBRIEF ---
    total_estimate = sum(r["estimate"] for r in all_results)
    total_actual = sum(r["actual"] for r in all_results)
    total_gap = total_estimate - total_actual

    print("=" * 58)
    print("  DEBRIEF — THE DUNNING-KRUGER EFFECT")
    print("=" * 58)

    print(f"\n  YOUR OVERALL RESULTS:")
    print(f"  {'-' * 44}")

    for i, (section, result) in enumerate(zip(SECTIONS, all_results)):
        name = section["name"]
        est = result["estimate"]
        act = result["actual"]
        gap = est - act
        gap_str = f"+{gap}" if gap > 0 else str(gap) if gap < 0 else "0"
        print(f"  {name:<28} Est: {est}  Actual: {act}  Gap: {gap_str}")

    print(f"  {'-' * 44}")
    gap_str = f"+{total_gap}" if total_gap > 0 else str(total_gap)
    print(f"  {'TOTAL':<28} Est: {total_estimate}  Actual: {total_actual}  Gap: {gap_str}")

    # Visual comparison
    print(f"\n  ESTIMATE vs REALITY:")
    est_bar = "█" * total_estimate + "░" * (15 - total_estimate)
    act_bar = "█" * total_actual + "░" * (15 - total_actual)
    print(f"  You thought: [{est_bar}] {total_estimate}/15")
    print(f"  You scored:  [{act_bar}] {total_actual}/15")

    # Interpretation
    pct_actual = total_actual / 15 * 100

    if total_gap > 3:
        effect = "strong"
        desc = (
            "You significantly overestimated your performance.\n"
            "  This is the classic Dunning-Kruger pattern: the less\n"
            "  you knew, the harder it was to judge what you didn't know."
        )
    elif total_gap > 0:
        effect = "mild"
        desc = (
            "You slightly overestimated — a mild version of the\n"
            "  effect. Most people show at least some overconfidence\n"
            "  on unfamiliar topics."
        )
    elif total_gap == 0:
        effect = "absent"
        desc = (
            "Your estimate was spot on! This is uncommon — most\n"
            "  people show at least a small gap. You may have strong\n"
            "  metacognitive awareness (knowing what you don't know)."
        )
    else:
        effect = "reversed"
        desc = (
            "You underestimated your performance — the pattern\n"
            "  Kruger & Dunning found in TOP performers. People who\n"
            "  know more tend to assume others know just as much,\n"
            "  leading them to underrate themselves."
        )

    print(f"""
  YOUR PATTERN: {effect.upper()} Dunning-Kruger effect

  {desc}

  THE SCIENCE:

  Kruger & Dunning (1999) found that people who scored in
  the bottom 25% on tests of logic, grammar, and humour
  estimated they performed near the 62nd percentile.

  The cruel twist: the skills you need to GET the right
  answers are the SAME skills you need to KNOW your answers
  are wrong. Incompetence robs you of the ability to
  recognise your own incompetence.

  Meanwhile, top performers slightly underestimated —
  they assumed the questions were equally easy for everyone.

  WHY THIS MATTERS:

  - Overconfident consumers skip research and make poor
    purchases, then rate products badly (blaming the product)
  - Expert consumers underestimate their knowledge and
    hesitate to buy premium products they'd benefit from
  - Product reviews are skewed: the least informed reviewers
    are often the most confident in their judgements
  - Financial decisions suffer most: people who understand
    investing least are most certain they can beat the market

  The antidote? Gaining even a little real knowledge makes
  people dramatically better at judging what they don't know.
""")


if __name__ == "__main__":
    main()
