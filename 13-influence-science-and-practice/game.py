"""
SPOT THE TECHNIQUE: Cialdini's Six Principles of Persuasion
Based on: Influence: Science and Practice (1984) — Cialdini

Six invisible levers control most of your "yes" decisions.
Can you spot which one is being pulled?
"""

import random
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

PRINCIPLES = {
    "Reciprocity": "We feel obligated to return favours — even ones we didn't ask for.",
    "Commitment & Consistency": "Once we take a stand, we feel pressure to stay consistent with it.",
    "Social Proof": "When unsure, we copy what others are doing.",
    "Authority": "We trust and obey perceived experts or authority figures.",
    "Liking": "We say yes more easily to people we like, find attractive, or feel similar to.",
    "Scarcity": "Things seem more valuable when they're rare or running out.",
}

SCENARIOS = [
    {
        "situation": (
            "A salesperson at a department store sprays you with\n"
            "  a free perfume sample and hands you a small gift bag.\n"
            "  Then she asks if you'd like to see the full collection."
        ),
        "answer": "Reciprocity",
        "explanation": "The free gift creates a sense of obligation. You didn't ask for it, but now you feel rude saying no."
    },
    {
        "situation": (
            "A charity caller asks: 'Would you say you care about\n"
            "  children's education?' You say yes. Then they ask\n"
            "  for a monthly donation to a children's education fund."
        ),
        "answer": "Commitment & Consistency",
        "explanation": "By getting you to publicly say you care, they've locked in a position. Now refusing to donate feels inconsistent with what you just said."
    },
    {
        "situation": (
            "A restaurant lists one dish as 'OUR MOST POPULAR —\n"
            "  ordered 2,000 times this month!' You've never been\n"
            "  here before and don't know what's good."
        ),
        "answer": "Social Proof",
        "explanation": "When you're uncertain, '2,000 other people chose this' is a powerful shortcut. If everyone else likes it, it must be good."
    },
    {
        "situation": (
            "A toothpaste advert features a dentist in a white\n"
            "  coat saying '9 out of 10 dental professionals\n"
            "  recommend this brand.'"
        ),
        "answer": "Authority",
        "explanation": "The white coat and professional title trigger automatic trust. We defer to experts even when we can't verify their claims."
    },
    {
        "situation": (
            "A car salesperson notices your university hoodie\n"
            "  and says 'No way — I went there too!' They chat\n"
            "  about campus life before showing you cars."
        ),
        "answer": "Liking",
        "explanation": "Finding shared identity makes you like them more. We buy from people we feel connected to, and similarity is one of the fastest routes to liking."
    },
    {
        "situation": (
            "An online shop shows: 'Only 2 left in stock!'\n"
            "  and 'This deal expires in 00:14:32' with a\n"
            "  countdown timer ticking."
        ),
        "answer": "Scarcity",
        "explanation": "Limited quantity + time pressure makes the item feel more valuable. Fear of missing out overrides careful evaluation."
    },
    {
        "situation": (
            "A software company lets you use their premium\n"
            "  features free for 30 days. On day 25 they email:\n"
            "  'Your trial is ending — keep your setup for £9.99/month.'"
        ),
        "answer": "Commitment & Consistency",
        "explanation": "You've spent a month customising and using it. You've committed time and effort. Cancelling feels like abandoning that investment."
    },
    {
        "situation": (
            "A negotiator brings coffee and pastries to the\n"
            "  meeting room before presenting a difficult contract\n"
            "  proposal to the other party."
        ),
        "answer": "Reciprocity",
        "explanation": "Hospitality before negotiation creates obligation. Saying no to the proposal now feels like ingratitude."
    },
    {
        "situation": (
            "A booking site shows: '47 people are looking at\n"
            "  this hotel right now' and 'Booked 12 times in\n"
            "  the last 24 hours.'"
        ),
        "answer": "Social Proof",
        "explanation": "Seeing other people's interest makes you feel the hotel must be good — and creates urgency that it'll be gone soon."
    },
    {
        "situation": (
            "A fitness influencer you follow posts about a\n"
            "  protein shake brand. They show their workout,\n"
            "  their physique, and say 'This is what I use.'"
        ),
        "answer": "Authority",
        "explanation": "The influencer's visible results make them a perceived expert. Their endorsement carries weight because of demonstrated competence."
    },
    {
        "situation": (
            "A real estate agent compliments your taste in\n"
            "  homes, agrees with every preference you mention,\n"
            "  and says 'You clearly have a great eye for design.'"
        ),
        "answer": "Liking",
        "explanation": "Flattery and agreement make you like the agent. We're more persuadable by people who make us feel good about ourselves."
    },
    {
        "situation": (
            "A luxury brand releases only 500 numbered units\n"
            "  of a new watch. The advert says 'Once they're\n"
            "  gone, they're gone forever.'"
        ),
        "answer": "Scarcity",
        "explanation": "Artificial limitation makes the watch feel exclusive and more desirable. The fear of permanent loss drives action."
    },
]

def run_game():
    clear()
    print("=" * 55)
    print("  SPOT THE TECHNIQUE")
    print("  Cialdini's Six Principles of Persuasion")
    print("=" * 55)
    print()
    print("  Someone is trying to persuade you in each scenario.")
    print("  Your job: identify WHICH of the six principles")
    print("  they're using on you.")
    print()
    print("  The six principles are:")
    print()
    for i, name in enumerate(PRINCIPLES.keys(), 1):
        print(f"    {i}. {name}")
    print()
    input("Press Enter to begin... ")

    # Pick 8 random scenarios (covering all 6 principles)
    random.shuffle(SCENARIOS)
    selected = SCENARIOS[:8]

    principle_list = list(PRINCIPLES.keys())
    score = 0
    wrong = []

    for i, scenario in enumerate(selected, 1):
        clear()
        print(f"  Scenario {i} of 8")
        print("=" * 55)
        print()
        print(f"  {scenario['situation']}")
        print()
        print("  Which principle is being used?")
        print()
        for j, name in enumerate(principle_list, 1):
            print(f"    [{j}] {name}")
        print()

        while True:
            try:
                choice = int(input("  Your answer (1-6): ").strip())
                if 1 <= choice <= 6:
                    break
            except ValueError:
                pass
            print("  Please enter a number from 1 to 6.")

        chosen = principle_list[choice - 1]
        correct = scenario["answer"]

        print()
        if chosen == correct:
            score += 1
            print(f"  CORRECT! It's {correct}.")
        else:
            print(f"  Not quite. The answer is {correct}.")
            wrong.append((i, correct, chosen))

        print(f"  {scenario['explanation']}")
        print()
        input("  Press Enter to continue... ")

    # --- DEBRIEF ---
    clear()
    print("=" * 55)
    print("  YOUR RESULTS")
    print("=" * 55)
    print()
    print(f"  Score: {score}/8")
    print()

    if score == 8:
        print("  Perfect! You spotted every technique.")
        print("  You'd be hard to manipulate.")
    elif score >= 6:
        print("  Strong awareness! A few slipped past you,")
        print("  but you're clearly tuned in to persuasion tactics.")
    elif score >= 4:
        print("  You caught about half. The principles you missed")
        print("  are probably the ones most effective on you.")
    else:
        print("  These techniques are sneaky — that's the point.")
        print("  Now that you know the six principles, you'll")
        print("  start spotting them everywhere.")

    if wrong:
        print()
        print("  Principles you confused:")
        for num, correct, chosen in wrong:
            print(f"    Scenario {num}: was {correct}, you said {chosen}")

    print()
    print("=" * 55)
    print("  THE SIX PRINCIPLES — QUICK REFERENCE")
    print("=" * 55)
    print()
    for name, desc in PRINCIPLES.items():
        print(f"  {name}")
        print(f"    {desc}")
        print()

    print("  Cialdini showed that compliance professionals use")
    print("  these six shortcuts systematically. Now that you")
    print("  can name them, you'll notice them in adverts,")
    print("  sales pitches, and negotiations — every day.")
    print()
    input("Press Enter to exit... ")

if __name__ == "__main__":
    run_game()
