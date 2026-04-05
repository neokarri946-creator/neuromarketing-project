"""
A Theory of Cognitive Dissonance — Interactive Experience
Based on Festinger (1957)

Feel how your mind quietly rewrites your beliefs to match
your behaviour — the engine behind cognitive dissonance.
"""

import random

SCENARIOS = [
    {
        "topic": "Healthy Eating",
        "belief_question": "How important is eating healthy to you?",
        "action_prompt": (
            "A friend invites you to an all-you-can-eat fast food challenge\n"
            "  for a charity livestream. It would be fun and for a good cause,\n"
            "  but the food is pure junk.\n"
            "  Do you JOIN the challenge or SKIP it?"
        ),
        "conflicting_choice": "JOIN",
        "consistent_choice": "SKIP",
        "reask": "Now, thinking about it again — how important is eating healthy to you?",
        "rationalizations": [
            "It's just one day — it won't really affect my health.",
            "The charity cause is more important than one meal.",
            "Life's about balance. Being too strict is unhealthy too.",
            "Fast food occasionally is fine. I'm not that rigid about it.",
        ],
    },
    {
        "topic": "Environmental Responsibility",
        "belief_question": "How important is reducing your carbon footprint?",
        "action_prompt": (
            "You've been offered a dream holiday — but it requires two\n"
            "  long-haul flights with a huge carbon footprint.\n"
            "  Do you BOOK the trip or DECLINE?"
        ),
        "conflicting_choice": "BOOK",
        "consistent_choice": "DECLINE",
        "reask": "Now, rethinking — how important is reducing your carbon footprint?",
        "rationalizations": [
            "One flight won't make a difference in the grand scheme.",
            "I offset my carbon in other ways, so this balances out.",
            "Travel broadens the mind — that's valuable too.",
            "The airline flies whether I'm on it or not.",
        ],
    },
    {
        "topic": "Saving Money",
        "belief_question": "How important is saving money and being financially careful?",
        "action_prompt": (
            "You spot a luxury jacket that costs three times your budget.\n"
            "  It looks incredible on you and it's the last one in your size.\n"
            "  Do you BUY it or LEAVE it?"
        ),
        "conflicting_choice": "BUY",
        "consistent_choice": "LEAVE",
        "reask": "Now, reflecting — how important is saving money and being financially careful?",
        "rationalizations": [
            "Quality items last longer, so it's actually an investment.",
            "You can't take money with you — enjoy life.",
            "I'll cut back next month to make up for it.",
            "Treating yourself occasionally is part of a healthy mindset.",
        ],
    },
    {
        "topic": "Honesty",
        "belief_question": "How important is being completely honest with people?",
        "action_prompt": (
            "Your friend shows you a creative project they've worked on for\n"
            "  months. Honestly, it's not great. They ask what you think.\n"
            "  Do you give a HONEST critique or a KIND (white lie) response?"
        ),
        "conflicting_choice": "KIND",
        "consistent_choice": "HONEST",
        "reask": "Now, thinking again — how important is being completely honest with people?",
        "rationalizations": [
            "Kindness matters more than brutal honesty.",
            "A white lie isn't really dishonest — it's social intelligence.",
            "Being honest doesn't mean being harsh. Tact is a form of honesty.",
            "Protecting someone's feelings is the more ethical choice.",
        ],
    },
]


def show_intro():
    print("=" * 58)
    print("  COGNITIVE DISSONANCE")
    print("  Based on Festinger (1957)")
    print("=" * 58)
    print()
    print("  You'll state your beliefs, then face tough choices.")
    print("  Afterward, we'll see if your beliefs quietly shifted")
    print("  to match what you did — just as Festinger predicted.")
    print()
    input("  Press Enter to begin...\n")


def get_rating(prompt):
    while True:
        try:
            print(f"  (1 = not important ... 10 = extremely important)")
            val = int(input(f"  {prompt}: "))
            if 1 <= val <= 10:
                return val
            print("  Please enter a number from 1 to 10.")
        except ValueError:
            print("  Please enter a number from 1 to 10.")


def get_choice(option_a, option_b):
    while True:
        choice = input(f"  Type {option_a} or {option_b}: ").strip().upper()
        if choice == option_a:
            return option_a
        if choice == option_b:
            return option_b
        print(f"  Please type {option_a} or {option_b}.")


def run_scenario(scenario, index):
    print("-" * 58)
    print(f"\n  SCENARIO {index}: {scenario['topic']}")
    print()

    before = get_rating(scenario["belief_question"])
    print()

    print(f"  SITUATION:")
    print(f"  {scenario['action_prompt']}")
    print()

    choice = get_choice(
        scenario["conflicting_choice"], scenario["consistent_choice"]
    )
    conflicted = choice == scenario["conflicting_choice"]

    if conflicted:
        print()
        print("  Interesting — that choice clashes with your stated belief.")
        print("  Let's see if your brain does something about that tension...")
        print()
    else:
        print()
        print("  That's consistent with your stated belief. No conflict there.")
        print()

    after = get_rating(scenario["reask"])
    print()

    return {
        "topic": scenario["topic"],
        "before": before,
        "after": after,
        "conflicted": conflicted,
        "choice": choice,
        "rationalizations": scenario["rationalizations"],
    }


def show_bar(value, max_val=10, label=""):
    filled = "█" * value
    empty = "░" * (max_val - value)
    return f"  {label:<12} [{filled}{empty}] {value}/10"


def debrief(results):
    print("\n" + "=" * 58)
    print("  DEBRIEF — DID YOUR BELIEFS SHIFT?")
    print("=" * 58)

    total_conflicted = 0
    shifted_count = 0

    for r in results:
        print(f"\n  {r['topic']}")
        print(show_bar(r["before"], label="Before"))
        print(show_bar(r["after"], label="After"))

        diff = r["before"] - r["after"]

        if r["conflicted"]:
            total_conflicted += 1
            if diff > 0:
                shifted_count += 1
                print(f"  >> You acted against your belief AND softened it by {diff} point(s).")
                print(f"     Your brain may have told itself something like:")
                print(f'     "{random.choice(r["rationalizations"])}"')
            elif diff == 0:
                print(f"  >> You acted against your belief but held firm. Strong resolve!")
            else:
                print(f"  >> You acted against your belief and rated it HIGHER after.")
                print(f"     That's unusual — perhaps guilt reinforced the belief.")
        else:
            if diff == 0:
                print(f"  >> Consistent choice, stable belief. No dissonance to resolve.")
            else:
                change_dir = "dropped" if diff > 0 else "rose"
                print(f"  >> Consistent choice, but your rating {change_dir} by {abs(diff)}.")

    print("\n" + "=" * 58)
    print("  THE SCIENCE")
    print("=" * 58)
    print()
    print("  Festinger (1957) discovered that when behaviour")
    print("  contradicts belief, the mind resolves the discomfort")
    print("  by CHANGING THE BELIEF — not the behaviour.")
    print()
    if total_conflicted > 0:
        pct = (shifted_count / total_conflicted) * 100
        print(f"  In your session: {shifted_count}/{total_conflicted} conflicting")
        print(f"  choices led to belief shifts ({pct:.0f}%).")
    else:
        print("  You stayed consistent in every scenario — your choices")
        print("  matched your beliefs, so there was no dissonance to resolve.")
    print()
    print("  WHY THIS MATTERS FOR MARKETING:")
    print()
    print("  Once a customer ACTS (buys, signs up, commits publicly),")
    print("  their beliefs shift to justify the action. This is why:")
    print("  - Post-purchase emails reinforce 'great choice!'")
    print("  - Free trials convert — using the product creates commitment")
    print("  - High prices can increase satisfaction (more to justify)")
    print("  - Loyalty programs deepen through action, not just rewards")
    print()
    print("  Behaviour leads. Belief follows.")
    print()


def main():
    show_intro()

    selected = random.sample(SCENARIOS, min(3, len(SCENARIOS)))
    results = []

    for i, scenario in enumerate(selected, 1):
        result = run_scenario(scenario, i)
        results.append(result)

    debrief(results)


if __name__ == "__main__":
    main()
