"""
THE PERSUASION MANAGER: Applying Cialdini's Principles at Work
Based on: Harnessing the Science of Persuasion (2001) — Cialdini

You're a marketing manager. Your job: pick the right
persuasion strategy for each business challenge.
Not every principle works equally well in every context.
"""

import random
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

PRINCIPLES = [
    "Reciprocity",
    "Commitment & Consistency",
    "Social Proof",
    "Authority",
    "Liking",
    "Scarcity",
]

SCENARIOS = [
    {
        "title": "New Product Launch",
        "situation": (
            "You're launching a new project management tool.\n"
            "  Nobody's heard of it yet. Your target customers\n"
            "  are mid-size companies who are unsure whether to\n"
            "  switch from their current system."
        ),
        "best": "Social Proof",
        "good": "Authority",
        "explanation": (
            "When people are uncertain, social proof is most powerful.\n"
            "  Cialdini showed that 'X companies already switched' is\n"
            "  more persuasive than features lists. Authority (expert\n"
            "  endorsements) also helps but works best alongside proof\n"
            "  that others have already taken the leap."
        ),
    },
    {
        "title": "Getting Buy-In for a Budget Increase",
        "situation": (
            "You need your CEO to approve a 40% increase in\n"
            "  marketing spend. She's sceptical. You have strong\n"
            "  data showing competitors who increased spend grew\n"
            "  faster, but she's heard pitches like this before."
        ),
        "best": "Authority",
        "good": "Scarcity",
        "explanation": (
            "Cialdini found that establishing expertise BEFORE the ask\n"
            "  is critical. Present the industry data from respected\n"
            "  sources first, building your credibility. Scarcity also\n"
            "  helps: frame it as 'we'll lose market share if we don't\n"
            "  act now' — loss framing is more compelling than gain."
        ),
    },
    {
        "title": "Retaining a Key Client",
        "situation": (
            "A major client is considering switching to a\n"
            "  competitor. You've worked together for two years\n"
            "  and they've publicly praised your work at industry\n"
            "  events. The competitor is offering a lower price."
        ),
        "best": "Commitment & Consistency",
        "good": "Liking",
        "explanation": (
            "The client has publicly praised you — that's a commitment.\n"
            "  Cialdini showed that reminding people of their public\n"
            "  statements creates pressure to stay consistent. 'You've\n"
            "  said publicly that our partnership drives results — let's\n"
            "  build on that.' Liking (your personal relationship) also\n"
            "  works as a secondary lever."
        ),
    },
    {
        "title": "Motivating a Resistant Team",
        "situation": (
            "Your team needs to adopt a new CRM system. Most\n"
            "  of them hate change and have openly complained.\n"
            "  Training starts next week. You need them on board."
        ),
        "best": "Reciprocity",
        "good": "Social Proof",
        "explanation": (
            "Cialdini showed that giving FIRST — before asking — creates\n"
            "  genuine obligation. Offer the team something valuable:\n"
            "  extra training time, a team lunch, or reduced workload\n"
            "  during the transition. Then ask for their cooperation.\n"
            "  Social proof ('The sales team already loves it') also\n"
            "  helps reduce resistance."
        ),
    },
    {
        "title": "Closing a Partnership Deal",
        "situation": (
            "You're negotiating a co-marketing deal with another\n"
            "  company. Their marketing director seems interested\n"
            "  but keeps delaying the final decision. You've met\n"
            "  twice and gotten along well personally."
        ),
        "best": "Liking",
        "good": "Scarcity",
        "explanation": (
            "You've already built rapport — lean into it. Cialdini\n"
            "  showed that authentic connection and similarity are\n"
            "  powerful closers. Deepen the personal relationship\n"
            "  before pushing for the signature. Adding gentle scarcity\n"
            "  ('We need to finalise by Friday to hit the Q2 window')\n"
            "  can provide the nudge to overcome delay."
        ),
    },
    {
        "title": "Launching a Limited Collection",
        "situation": (
            "Your brand is releasing a premium product line.\n"
            "  You want maximum buzz and urgency. The product\n"
            "  is genuinely produced in limited quantities due\n"
            "  to sourcing constraints."
        ),
        "best": "Scarcity",
        "good": "Social Proof",
        "explanation": (
            "Real scarcity is the most honest and powerful form.\n"
            "  Cialdini emphasised framing it as loss: 'Once these\n"
            "  are gone, they won't be remade.' Pairing scarcity\n"
            "  with social proof ('Sold out in 3 cities already')\n"
            "  amplifies the urgency dramatically."
        ),
    },
    {
        "title": "Winning Over a Sceptical Stakeholder",
        "situation": (
            "A board member consistently blocks your proposals.\n"
            "  They don't trust marketing metrics and think your\n"
            "  department wastes money. You need their vote for\n"
            "  an upcoming strategy approval."
        ),
        "best": "Reciprocity",
        "good": "Authority",
        "explanation": (
            "Cialdini found that giving help to resistant people —\n"
            "  especially unsolicited — is the strongest way to shift\n"
            "  opposition. Offer the board member something valuable:\n"
            "  support their initiative, share useful data for their\n"
            "  project, or publicly credit their ideas. This creates\n"
            "  genuine obligation before your next ask."
        ),
    },
    {
        "title": "Getting Customers to Leave Reviews",
        "situation": (
            "Your product has thousands of happy users, but\n"
            "  hardly any online reviews. You know reviews drive\n"
            "  new sales. How do you get existing customers to\n"
            "  actually write them?"
        ),
        "best": "Commitment & Consistency",
        "good": "Reciprocity",
        "explanation": (
            "First ask a tiny question: 'Would you say you're\n"
            "  satisfied with our product?' Once they say yes,\n"
            "  THEN ask for the review. They've committed to being\n"
            "  satisfied, so writing a review is consistent. Adding\n"
            "  reciprocity (a small thank-you gift) boosts response\n"
            "  rates further."
        ),
    },
]

def run_game():
    clear()
    print("=" * 58)
    print("  THE PERSUASION MANAGER")
    print("  Applying Cialdini's Principles in Business")
    print("=" * 58)
    print()
    print("  You're a marketing manager facing real challenges.")
    print("  For each scenario, choose the persuasion principle")
    print("  that would work BEST in that specific context.")
    print()
    print("  The six principles:")
    for i, p in enumerate(PRINCIPLES, 1):
        print(f"    {i}. {p}")
    print()
    print("  Every principle can 'work' — but one is the BEST")
    print("  fit for each situation. A second is also good.")
    print("  You'll score 2 for best, 1 for good, 0 otherwise.")
    print()
    input("Press Enter to begin... ")

    random.shuffle(SCENARIOS)
    selected = SCENARIOS[:6]

    score = 0
    max_score = 12

    for i, scenario in enumerate(selected, 1):
        clear()
        print(f"  Challenge {i} of 6: {scenario['title']}")
        print("=" * 58)
        print()
        print(f"  {scenario['situation']}")
        print()
        print("  Which principle would be MOST effective here?")
        print()
        for j, p in enumerate(PRINCIPLES, 1):
            print(f"    [{j}] {p}")
        print()

        while True:
            try:
                choice = int(input("  Your strategy (1-6): ").strip())
                if 1 <= choice <= 6:
                    break
            except ValueError:
                pass
            print("  Please enter a number from 1 to 6.")

        chosen = PRINCIPLES[choice - 1]
        print()

        if chosen == scenario["best"]:
            score += 2
            print(f"  EXCELLENT! {chosen} is the best fit here. (+2)")
        elif chosen == scenario["good"]:
            score += 1
            print(f"  GOOD CHOICE! {chosen} would work well. (+1)")
            print(f"  But the BEST fit is {scenario['best']}.")
        else:
            print(f"  Not the strongest choice here.")
            print(f"  Best: {scenario['best']}  |  Also good: {scenario['good']}")

        print()
        print(f"  Why: {scenario['explanation']}")
        print()
        input("  Press Enter to continue... ")

    # --- DEBRIEF ---
    clear()
    print("=" * 58)
    print("  YOUR RESULTS")
    print("=" * 58)
    print()
    print(f"  Score: {score}/{max_score}")
    print()

    pct = score / max_score * 100
    if pct >= 80:
        print("  Outstanding strategic sense. You matched the right")
        print("  principle to the right context nearly every time.")
    elif pct >= 50:
        print("  Solid instincts. You understand the principles —")
        print("  the challenge is knowing which one fits BEST in")
        print("  each specific business context.")
    else:
        print("  Choosing the right tool for the right situation is")
        print("  the hard part. Every principle works somewhere —")
        print("  but context determines which one works best.")

    print()
    print("=" * 58)
    print("  THE KEY INSIGHT")
    print("=" * 58)
    print()
    print("  Cialdini (2001) showed that persuasion in business")
    print("  is not about personality or charisma — it's a")
    print("  learnable skill with specific tools for specific")
    print("  situations:")
    print()
    print("  - Facing resistance?  -> Give first (Reciprocity)")
    print("  - Need follow-through? -> Get public commitments")
    print("  - Launching something new? -> Show others doing it")
    print("  - Building credibility? -> Lead with expertise")
    print("  - Negotiating?  -> Build genuine rapport (Liking)")
    print("  - Creating urgency? -> Frame as loss (Scarcity)")
    print()
    print("  The professionals who outperform don't just 'have")
    print("  a way with people' — they systematically match the")
    print("  right principle to the right moment.")
    print()
    input("Press Enter to exit... ")

if __name__ == "__main__":
    run_game()
