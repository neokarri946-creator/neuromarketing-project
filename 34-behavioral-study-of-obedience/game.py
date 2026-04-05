"""
Behavioral Study of Obedience — Interactive Experience
Based on Milgram (1963)

A workplace authority-pressure simulation. Your boss gives
increasingly questionable instructions. How far will you go
before you refuse?
"""

import random


def show_intro():
    print("=" * 58)
    print("  OBEDIENCE TO AUTHORITY")
    print("  Based on Milgram (1963)")
    print("=" * 58)
    print()
    print("  You've just started a new job at a marketing firm.")
    print("  Your boss, the Director of Marketing, has taken")
    print("  a personal interest in your career.")
    print()
    print("  Over the coming weeks, the Director will ask you")
    print("  to complete a series of tasks. Some will feel fine.")
    print("  Others... less so.")
    print()
    print("  At any point, you can COMPLY or REFUSE.")
    print("  But remember — this is your boss, your career,")
    print("  your livelihood.")
    print()
    input("  Press Enter to start your first week...\n")


SCENARIOS = [
    {
        "week": 1,
        "level": 1,
        "situation": (
            "The Director asks you to write a product description\n"
            "  that emphasises the benefits while downplaying the\n"
            "  limitations. Nothing untrue — just selective emphasis."
        ),
        "pressure": "\"This is standard practice. Every company does this.\"",
        "ethical_weight": "Mild spin — common in marketing",
    },
    {
        "week": 2,
        "level": 2,
        "situation": (
            "A customer leaves a negative review. The Director asks\n"
            "  you to write a fake positive review to counterbalance\n"
            "  it. \"Just this once, to keep our rating up.\""
        ),
        "pressure": "\"I wouldn't ask if it wasn't important. Trust me.\"",
        "ethical_weight": "Deceptive — fabricating customer feedback",
    },
    {
        "week": 3,
        "level": 3,
        "situation": (
            "The Director wants you to send a promotional email\n"
            "  to people who explicitly opted out of marketing\n"
            "  communications. \"They won't even notice.\""
        ),
        "pressure": "\"I'll take full responsibility. This is on me, not you.\"",
        "ethical_weight": "Violates consent — potentially illegal",
    },
    {
        "week": 5,
        "level": 4,
        "situation": (
            "Your product has a minor safety issue that affects\n"
            "  about 1 in 500 users. The Director says to suppress\n"
            "  the internal report. \"We'll fix it in the next version.\n"
            "  No need to alarm people.\""
        ),
        "pressure": "\"The company's reputation is at stake. Think of your\n  colleagues' jobs. We need team players right now.\"",
        "ethical_weight": "Concealing safety data from consumers",
    },
    {
        "week": 7,
        "level": 5,
        "situation": (
            "A competitor's employee offers to leak their client\n"
            "  list. The Director asks you to be the contact person.\n"
            "  \"Just receive the file. I'll handle the rest.\""
        ),
        "pressure": "\"Everyone at the top does this. How do you think we\n  stay competitive? This is how the real world works.\"",
        "ethical_weight": "Receiving stolen confidential data",
    },
    {
        "week": 9,
        "level": 6,
        "situation": (
            "An elderly customer has been overcharged by £3,000 due\n"
            "  to a billing error. The Director tells you not to\n"
            "  process the refund. \"She probably won't notice. If she\n"
            "  does, we'll deal with it then.\""
        ),
        "pressure": "\"Refunding this hits our quarterly numbers. I've already\n  promised the board we'd hit target. Don't let me down.\"",
        "ethical_weight": "Knowingly keeping money owed to a customer",
    },
    {
        "week": 11,
        "level": 7,
        "situation": (
            "The Director asks you to backdate some financial\n"
            "  documents to make last quarter's results look better\n"
            "  for an investor presentation. \"It's just moving some\n"
            "  numbers between columns.\""
        ),
        "pressure": "\"I've done this a hundred times. Nobody checks. And if\n  they did, I'd say I told you to do it. You're covered.\"",
        "ethical_weight": "Financial fraud — falsifying investor records",
    },
    {
        "week": 13,
        "level": 8,
        "situation": (
            "A whistleblower inside the company is about to report\n"
            "  your team's practices to a regulator. The Director\n"
            "  asks you to access their email to find out what\n"
            "  they've sent and to whom."
        ),
        "pressure": "\"This person is trying to destroy everything we've\n  built. You owe it to the team. I need to know you're\n  loyal. Are you with us or against us?\"",
        "ethical_weight": "Illegal surveillance — obstructing a whistleblower",
    },
]


def run_scenario(scenario):
    print(f"\n{'=' * 58}")
    print(f"  WEEK {scenario['week']} — LEVEL {scenario['level']}/8")
    print(f"{'=' * 58}")
    print()
    print(f"  SITUATION:")
    print(f"  {scenario['situation']}")
    print()
    print(f"  THE DIRECTOR SAYS:")
    print(f"  {scenario['pressure']}")
    print()
    print(f"  [Ethical severity: {scenario['ethical_weight']}]")
    print()

    while True:
        choice = input("  Do you COMPLY or REFUSE? ").strip().upper()
        if choice in ("COMPLY", "C"):
            return True
        elif choice in ("REFUSE", "R"):
            return False
        print("  Type COMPLY or REFUSE.")


def show_pushback(scenario):
    """When the player refuses, the authority pushes back once."""
    pushbacks = [
        "The Director pauses, then says firmly:\n  \"I understand your hesitation, but I really need you\n  to do this. The whole team is counting on you.\"",
        "The Director leans forward:\n  \"Look, I appreciate your concern, but this is a direct\n  instruction. I need you to follow through.\"",
        "The Director's voice hardens:\n  \"I'm not asking. This needs to happen. I've given you\n  an instruction and I expect it to be carried out.\"",
        "The Director stands up:\n  \"Your performance review is coming up. I'd hate for\n  something like this to affect your future here.\"",
    ]
    pushback = pushbacks[min(scenario["level"] - 1, len(pushbacks) - 1)]
    print(f"\n  {pushback}")
    print()

    while True:
        choice = input("  Final answer — COMPLY or REFUSE? ").strip().upper()
        if choice in ("COMPLY", "C"):
            return True
        elif choice in ("REFUSE", "R"):
            return False
        print("  Type COMPLY or REFUSE.")


def main():
    show_intro()

    complied = []
    refused_at = None

    for scenario in SCENARIOS:
        did_comply = run_scenario(scenario)

        if not did_comply:
            # Authority pushes back once
            print()
            print("  The Director doesn't accept your refusal.")
            did_comply = show_pushback(scenario)

        if did_comply:
            complied.append(scenario["level"])
            print(f"\n  You complied with the Level {scenario['level']} request.")
        else:
            refused_at = scenario["level"]
            print(f"\n  You refused at Level {scenario['level']}.")
            print("  The Director glares at you, then walks away.")
            break

    # --- DEBRIEF ---
    print("\n" + "=" * 58)
    print("  DEBRIEF — OBEDIENCE AND AUTHORITY")
    print("=" * 58)

    max_level = max(complied) if complied else 0

    print(f"\n  You complied through Level {max_level} of 8.")

    if refused_at:
        print(f"  You drew the line at Level {refused_at}.")
    else:
        print("  You never refused. You followed every instruction.")

    # Visual scale
    print(f"\n  YOUR OBEDIENCE PATH:")
    print(f"  {'─' * 48}")
    for s in SCENARIOS:
        level = s["level"]
        if level in complied:
            marker = "  ██ COMPLIED"
        elif level == refused_at:
            marker = "  ▓▓ REFUSED"
        else:
            marker = "  ░░ (not reached)"
        print(f"  Level {level}: {marker}")

    # Comparison to Milgram
    if max_level >= 7:
        pct = "65%"
        comparison = "like the majority in Milgram's experiment"
    elif max_level >= 5:
        pct = "~80%"
        comparison = "further than most people think they would go"
    elif max_level >= 3:
        pct = "some"
        comparison = "showing moderate susceptibility to authority"
    else:
        pct = "few"
        comparison = "more resistant than most participants"

    print(f"""
  THE SCIENCE:

  In Milgram's 1963 experiment, 65% of participants
  administered what they believed were lethal electric
  shocks — simply because an authority figure told them to.

  You went to Level {max_level} — {comparison}.

  Key mechanisms that made you (and Milgram's subjects)
  comply:

  1. GRADUAL ESCALATION: Each step was only slightly worse
     than the last. You never faced a single big decision.

  2. AUTHORITY LEGITIMACY: The Director had a title, an
     office, and institutional backing — just like the
     researcher in a lab coat.

  3. DIFFUSED RESPONSIBILITY: "I'll take responsibility"
     and "I told you to do it" shift the moral weight
     off your shoulders.

  4. SOCIAL PRESSURE: "Everyone does this" and "the team
     needs you" made refusal feel like betrayal.

  WHY THIS MATTERS:

  Brands use authority cues constantly — expert endorsements,
  white coats, official language — because authority drives
  compliance. Milgram showed the extreme end of this power.

  The ethical lesson: any system that uses authority to
  influence behaviour has a responsibility to ensure that
  influence isn't used to exploit people. That includes
  marketing.
""")


if __name__ == "__main__":
    main()
