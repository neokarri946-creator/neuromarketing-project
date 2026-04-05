"""
Neuromarketing: Hope vs Hype — Interactive Experience
Based on Ariely & Berns (2010)

You're a neuromarketing consultant. Clients bring you claims
based on brain scans. Can you tell real science from hype?
"""

import random

CLAIMS = [
    {
        "client": "A soft drink company",
        "claim": "Our fMRI study of 16 people shows that seeing our logo activates the nucleus accumbens. This proves consumers LOVE our brand more than the competitor's.",
        "answer": "hype",
        "explanation": (
            "The nucleus accumbens responds to many things — novelty, "
            "anticipation, surprise — not just 'love.' With only 16 "
            "participants and no control condition, this is classic "
            "REVERSE INFERENCE: assuming one brain region = one emotion. "
            "Ariely & Berns flagged this as the most common error in "
            "commercial neuromarketing."
        ),
    },
    {
        "client": "A movie studio",
        "claim": "We showed our trailer to 30 people in an fMRI scanner. Neural engagement in emotional processing regions predicted opening weekend box office better than traditional focus groups.",
        "answer": "hope",
        "explanation": (
            "This is a LEGITIMATE use case. The brain data revealed "
            "something surveys couldn't — unconscious emotional engagement "
            "that predicted real-world behaviour. Ariely & Berns said "
            "neuromarketing has genuine value when it provides 'hidden "
            "information' that self-report methods miss."
        ),
    },
    {
        "client": "A luxury car brand",
        "claim": "Brain scans show our car activates the same region as romantic love. Our cars literally make people fall in love.",
        "answer": "hype",
        "explanation": (
            "This is reverse inference again. The brain region linked to "
            "'romantic love' also activates for chocolate, music, and "
            "gambling. Saying a car makes people 'fall in love' based on "
            "shared activation is like saying anyone who smiles must be "
            "happy — smiles mean many things."
        ),
    },
    {
        "client": "A political campaign",
        "claim": "We want to use fMRI to test which campaign messages resonate with undecided voters, since they often can't articulate what sways them.",
        "answer": "hope",
        "explanation": (
            "Undecided voters genuinely struggle to report their own "
            "preferences — this is exactly where neuroimaging could reveal "
            "'hidden information.' Ariely & Berns identified this as a "
            "legitimate application, though they noted ethical concerns "
            "about using brain data for political manipulation."
        ),
    },
    {
        "client": "A snack food company",
        "claim": "Our EEG headband measured 'neuro-engagement scores' for 200 product concepts in one afternoon. We can now rank all 200 by brain appeal.",
        "answer": "hype",
        "explanation": (
            "EEG has very poor spatial resolution — it can't pinpoint "
            "specific emotional responses. Testing 200 concepts in one "
            "session means roughly one minute each, far too little for "
            "meaningful neural data. This sounds like conventional "
            "preference ranking dressed up with neuroscience jargon."
        ),
    },
    {
        "client": "A retail chain",
        "claim": "fMRI reveals that shoppers unconsciously process store layout in ways that affect buying but that they can't report in surveys. We want to test two store designs.",
        "answer": "hope",
        "explanation": (
            "Store environment effects are largely unconscious — people "
            "don't know why they spend more time in one layout. This fits "
            "Ariely & Berns' criterion of using neuroimaging to access "
            "information consumers genuinely cannot self-report. The key "
            "is whether the fMRI data adds insight beyond what observation "
            "and sales data already show."
        ),
    },
    {
        "client": "A tech startup",
        "claim": "We've built an AI that reads a single brain scan and tells you a person's exact brand preferences across 50 product categories.",
        "answer": "hype",
        "explanation": (
            "A single brain scan cannot decode specific preferences across "
            "50 categories. fMRI measures blood flow with limited precision "
            "and temporal resolution. This massively overpromises what the "
            "technology can deliver. Ariely & Berns warned that commercial "
            "firms routinely exaggerate neuroimaging's current capabilities."
        ),
    },
    {
        "client": "A music streaming service",
        "claim": "We used fMRI to identify which neural patterns during song previews predict whether users will add a song to their playlist. The model outperformed self-reported ratings.",
        "answer": "hope",
        "explanation": (
            "Music preference involves strong unconscious emotional "
            "responses that people struggle to articulate. If the study "
            "was properly controlled and the neural patterns genuinely "
            "predicted behaviour better than self-report, this represents "
            "the 'hidden information' value that Ariely & Berns argued "
            "neuroimaging can legitimately provide."
        ),
    },
]


def show_intro():
    print("=" * 58)
    print("  NEUROMARKETING: HOPE OR HYPE?")
    print("  Based on Ariely & Berns (2010)")
    print("=" * 58)
    print()
    print("  You're a neuromarketing consultant.")
    print("  Clients bring you claims based on brain scans.")
    print()
    print("  Your job: decide if each claim is...")
    print("    HOPE — legitimate neuroscience with real potential")
    print("    HYPE — overpromising, bad methodology, or pseudoscience")
    print()
    print("  Ariely & Berns gave us two key questions to ask:")
    print("  1. Does the brain data reveal something surveys CAN'T?")
    print("  2. Is the interpretation scientifically sound?")
    print()
    input("  Press Enter to see your first client...\n")


def get_verdict():
    while True:
        choice = input("  Your verdict — HOPE or HYPE? ").strip().upper()
        if choice in ("HOPE", "HO"):
            return "hope"
        if choice in ("HYPE", "HY"):
            return "hype"
        print("  Type HOPE or HYPE.")


def main():
    show_intro()

    selected = random.sample(CLAIMS, 6)
    score = 0
    details = []

    for i, claim in enumerate(selected, 1):
        print(f"{'─' * 58}")
        print(f"  CLIENT {i}/6: {claim['client']}")
        print(f"{'─' * 58}")
        print()
        # Word-wrap the claim for readability
        words = claim["claim"].split()
        line = "  "
        for word in words:
            if len(line) + len(word) + 1 > 56:
                print(line)
                line = "  " + word
            else:
                line += " " + word if line.strip() else "  " + word
        if line.strip():
            print(line)
        print()

        verdict = get_verdict()
        correct = verdict == claim["answer"]

        if correct:
            print(f"\n  ✓ CORRECT! This was {claim['answer'].upper()}.")
            score += 1
        else:
            print(f"\n  ✗ Not quite. This was {claim['answer'].upper()}.")

        print()
        # Word-wrap explanation
        words = claim["explanation"].split()
        line = "  "
        for word in words:
            if len(line) + len(word) + 1 > 56:
                print(line)
                line = "  " + word
            else:
                line += " " + word if line.strip() else "  " + word
        if line.strip():
            print(line)

        details.append({"claim": claim, "verdict": verdict, "correct": correct})
        print()
        if i < 6:
            input("  Press Enter for the next client...\n")

    # Final debrief
    print("\n" + "=" * 58)
    print(f"  FINAL SCORE: {score}/6")
    print("=" * 58)

    if score >= 5:
        print("\n  Excellent critical thinking. You'd make Ariely proud.")
    elif score >= 3:
        print("\n  Decent instincts — but some hype slipped past you.")
    else:
        print("\n  The hype machine got you. That's exactly why this")
        print("  paper exists — it's hard to spot without training.")

    print()
    print("  KEY TAKEAWAYS from Ariely & Berns (2010):")
    print()
    print("  Neuromarketing is LEGITIMATE when it:")
    print("  • Reveals hidden preferences people can't self-report")
    print("  • Predicts behaviour better than traditional methods")
    print("  • Uses proper controls and sample sizes")
    print()
    print("  Neuromarketing is HYPE when it:")
    print("  • Uses reverse inference (one region = one emotion)")
    print("  • Overpromises what brain scans can actually show")
    print("  • Dresses up conventional research with neuro-jargon")
    print("  • Claims to read exact preferences from a single scan")
    print()
    print("  The critical question is always:")
    print("  'Does this brain data tell us something we couldn't")
    print("   learn by simply ASKING people?'")
    print()


if __name__ == "__main__":
    main()
