"""
PROSPECT THEORY GAMBLES
=======================
Based on: Prospect Theory (1979) — Kahneman & Tversky

Losses hurt more than gains feel good. You're risk-averse
for gains but risk-seeking to avoid losses. Let's find out
if your brain follows the pattern.
"""

import random

def intro():
    print("=" * 50)
    print("  PROSPECT THEORY GAMBLES")
    print("  How do you REALLY make decisions?")
    print("=" * 50)
    print()
    print("You'll face a series of choices.")
    print("There are no right or wrong answers —")
    print("just pick whichever option feels better to you.")
    print()
    print("Go with your gut. Don't overthink it.")
    print()
    input("Press Enter to begin...\n")

def get_choice():
    while True:
        c = input("  Your choice (A or B): ").strip().upper()
        if c in ('A', 'B'):
            return c
        print("  Please type A or B.")

SCENARIOS = [
    # (description, option_a, option_b, type, predicted_popular)
    # type: "gain" or "loss"
    # predicted_popular: which option prospect theory predicts most people pick
    {
        "setup": "You're offered a choice:",
        "a": "Receive $500 for certain",
        "b": "50% chance of $1,000, 50% chance of nothing",
        "type": "gain",
        "predicted": "A",
        "explain": "Most people pick the sure $500 (risk-averse for gains).\nThe expected value is identical ($500), but certainty feels safer\nwhen you're gaining something.",
    },
    {
        "setup": "You must choose one of these losses:",
        "a": "Lose $500 for certain",
        "b": "50% chance of losing $1,000, 50% chance of losing nothing",
        "type": "loss",
        "predicted": "B",
        "explain": "Most people gamble here (risk-seeking for losses).\nAgain, the expected loss is identical ($500), but the certainty\nof losing feels unbearable, so people roll the dice.",
    },
    {
        "setup": "A bonus round at work:",
        "a": "Get a guaranteed $200 bonus",
        "b": "25% chance of an $800 bonus, 75% chance of no bonus",
        "type": "gain",
        "predicted": "A",
        "explain": "The expected values are equal ($200), but most people\ntake the sure bonus. When gains are on the table, we\ndon't want to risk walking away empty-handed.",
    },
    {
        "setup": "Your car needs repairs:",
        "a": "Pay $300 in definite repair costs",
        "b": "75% chance of $400 in costs, 25% chance the problem fixes itself (free)",
        "type": "loss",
        "predicted": "B",
        "explain": "Expected cost of B is also $300, but many people gamble\nbecause there's a chance of paying nothing. The certain\nloss of $300 feels worse than risking a bigger loss.",
    },
    {
        "setup": "An investment opportunity:",
        "a": "A guaranteed return of $1,000",
        "b": "80% chance of $1,400, 20% chance of $0",
        "type": "gain",
        "predicted": "A",
        "explain": "Option B's expected value is actually higher ($1,120),\nbut most people still take the guaranteed $1,000.\nLoss aversion makes that 20% chance of nothing\nfeel terrifying.",
    },
    {
        "setup": "You owe money on a debt:",
        "a": "Pay a settled amount of $800 now",
        "b": "85% chance of paying the full $1,000, 15% chance debt is forgiven",
        "type": "loss",
        "predicted": "B",
        "explain": "Option A is the better deal on average, but the slim\nhope of the debt disappearing makes people gamble.\nWhen facing losses, even a small chance of escape\nis irresistible.",
    },
]

def run_game():
    intro()

    gain_risky = 0
    gain_safe = 0
    loss_risky = 0
    loss_safe = 0
    matched_prediction = 0
    responses = []

    for i, s in enumerate(SCENARIOS):
        print(f"  --- SCENARIO {i+1} of {len(SCENARIOS)} ---\n")
        print(f"  {s['setup']}\n")
        print(f"  A: {s['a']}")
        print(f"  B: {s['b']}")
        print()

        choice = get_choice()
        responses.append((s, choice))

        if choice == s["predicted"]:
            matched_prediction += 1

        if s["type"] == "gain":
            if choice == "A":
                gain_safe += 1
            else:
                gain_risky += 1
        else:
            if choice == "B":
                loss_risky += 1
            else:
                loss_safe += 1

        print()

    # === DEBRIEF ===
    print("=" * 50)
    print("  YOUR RESULTS")
    print("=" * 50)
    print()

    gain_total = gain_safe + gain_risky
    loss_total = loss_safe + loss_risky

    print(f"  GAIN scenarios ({gain_total} total):")
    print(f"    Safe choice:  {gain_safe}  |  Risky choice: {gain_risky}")
    print()
    print(f"  LOSS scenarios ({loss_total} total):")
    print(f"    Safe choice:  {loss_safe}  |  Risky choice: {loss_risky}")
    print()

    # Analyse the pattern
    classic_pattern = gain_safe > gain_risky and loss_risky > loss_safe

    if classic_pattern:
        print("  YOU SHOWED THE CLASSIC PROSPECT THEORY PATTERN!")
        print()
        print("  - For gains: you preferred certainty (risk-averse)")
        print("  - For losses: you preferred to gamble (risk-seeking)")
        print()
        print("  This is exactly what Kahneman & Tversky found.")
        print("  Your brain treats gains and losses asymmetrically.")
    elif gain_risky > gain_safe and loss_safe > loss_risky:
        print("  INTERESTING — you showed the REVERSE pattern.")
        print()
        print("  You gambled on gains and played it safe on losses.")
        print("  This is unusual. You may be more analytically")
        print("  oriented than the average decision-maker.")
    else:
        print(f"  Your pattern was mixed — {matched_prediction} of {len(SCENARIOS)}")
        print("  choices matched the predicted pattern.")

    print()
    print("-" * 50)
    print("  SCENARIO BREAKDOWN:")
    print("-" * 50)
    for s, choice in responses:
        print()
        print(f"  You chose: {choice}  (predicted popular choice: {s['predicted']})")
        for line in s["explain"].split("\n"):
            print(f"  {line}")

    print()
    print("  THE SCIENCE:")
    print("  Kahneman & Tversky (1979) proved that humans don't")
    print("  calculate expected value like a computer. Instead:")
    print()
    print("  1. Losses hurt ~2x more than equivalent gains feel good")
    print("  2. We're cautious with gains (protect what we have)")
    print("  3. We gamble with losses (desperate to escape pain)")
    print()
    print("  Marketers exploit this constantly: 'Don't miss out'")
    print("  works better than 'You could gain' because your")
    print("  brain weighs the loss of missing out more heavily")
    print("  than the gain of participating.")
    print()

if __name__ == "__main__":
    run_game()
