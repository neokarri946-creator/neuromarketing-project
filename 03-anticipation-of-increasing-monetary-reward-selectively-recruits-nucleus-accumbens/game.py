"""
Anticipation vs Reward — Interactive Experience
Based on Knutson et al. (2001)

Feel the difference between WANTING and HAVING.
Your nucleus accumbens cares more about the build-up
than the payoff — and this game will show you why.
"""

import random
import time
import sys

REWARDS = [
    ("bronze", 10),
    ("silver", 50),
    ("gold", 200),
    ("diamond", 1000),
]


def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def show_intro():
    print("=" * 58)
    print("  THE ANTICIPATION GAME")
    print("  Based on Knutson et al. (2001)")
    print("=" * 58)
    print()
    print("  You'll play several rounds of a reward game.")
    print()
    print("  Each round:")
    print("    1. You'll see what PRIZE is available")
    print("    2. You'll wait through a countdown")
    print("    3. Press Enter at EXACTLY the right moment to claim it")
    print("    4. Rate your excitement at two moments:")
    print("       - During the ANTICIPATION (the countdown)")
    print("       - After RECEIVING the reward")
    print()
    print("  Be honest about your feelings. That's the whole point.")
    print()
    input("  Press Enter to start...\n")


def get_rating(prompt):
    while True:
        try:
            val = int(input(f"  {prompt} (1-10): "))
            if 1 <= val <= 10:
                return val
            print("  Pick a number from 1 to 10.")
        except ValueError:
            print("  Enter a number.")


def countdown(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\r  ⏳ Reward arriving in {i}... ")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r  ⏳                            \r")
    sys.stdout.flush()


def reaction_test():
    """Simple reaction challenge — press Enter when you see GO."""
    wait = random.uniform(1.5, 3.5)
    print("  Get ready...")
    time.sleep(wait)
    print("  >>> GO! Press Enter NOW! <<<")
    start = time.time()
    input()
    elapsed = time.time() - start
    return elapsed < 1.0  # must react within 1 second


def run_round(round_num, total_rounds, reward_name, reward_points, results):
    print(f"\n{'─' * 58}")
    print(f"  ROUND {round_num} of {total_rounds}")
    print(f"{'─' * 58}")

    # Show the stakes
    tier_display = reward_name.upper()
    print(f"\n  🎁 Available prize: {tier_display} REWARD ({reward_points} points)")
    print()

    if reward_points >= 200:
        slow_print("  This is a BIG one...", delay=0.05)
        print()

    # Build anticipation with countdown
    wait_time = 3 if reward_points < 100 else 5
    print("  The reward is loading. Watch the countdown.")
    print()
    countdown(wait_time)

    # Rate anticipation
    print()
    anticipation = get_rating("How EXCITED were you during the countdown?")
    print()

    # Reaction test to claim reward
    success = reaction_test()

    if success:
        print(f"  ✓ You claimed the {tier_display} reward! +{reward_points} points")
    else:
        half = reward_points // 2
        print(f"  ✗ Too slow! You only got half: +{half} points")
        reward_points = half

    print()

    # Rate the actual receipt
    receipt = get_rating("How EXCITED do you feel NOW that you have it?")

    results.append({
        "round": round_num,
        "tier": reward_name,
        "points": reward_points,
        "anticipation": anticipation,
        "receipt": receipt,
        "won": success,
    })

    return reward_points


def show_bar(value, max_val=10, label=""):
    filled = "█" * value
    empty = "░" * (max_val - value)
    return f"  {label:<14} [{filled}{empty}] {value}"


def debrief(results):
    print("\n" + "=" * 58)
    print("  DEBRIEF — ANTICIPATION vs REWARD")
    print("=" * 58)

    total_anticipation = 0
    total_receipt = 0
    anticipation_won = 0

    for r in results:
        print(f"\n  Round {r['round']}: {r['tier'].upper()} ({r['points']} pts)")
        print(show_bar(r["anticipation"], label="Anticipation"))
        print(show_bar(r["receipt"], label="Receipt"))
        diff = r["anticipation"] - r["receipt"]
        if diff > 0:
            print(f"  → Anticipation was {diff} point(s) MORE exciting")
            anticipation_won += 1
        elif diff < 0:
            print(f"  → Receipt was {abs(diff)} point(s) more exciting")
        else:
            print(f"  → Both felt the same")

        total_anticipation += r["anticipation"]
        total_receipt += r["receipt"]

    avg_ant = total_anticipation / len(results)
    avg_rec = total_receipt / len(results)

    print("\n" + "─" * 58)
    print(f"\n  Average anticipation excitement: {avg_ant:.1f}")
    print(f"  Average receipt excitement:      {avg_rec:.1f}")

    print("\n" + "=" * 58)
    print("  THE SCIENCE")
    print("=" * 58)
    print()

    if avg_ant > avg_rec:
        print("  Your pattern matches the study perfectly.")
        print("  The WANTING felt more exciting than the HAVING.")
    elif avg_ant == avg_rec:
        print("  Yours were equal — but in the lab, anticipation")
        print("  typically dominates.")
    else:
        print("  You rated receipt higher — interesting! In the lab,")
        print("  most brains show stronger signals during anticipation.")

    print()
    print("  Knutson et al. (2001) found that the nucleus accumbens")
    print("  — the brain's 'wanting' centre — fires MOST during")
    print("  anticipation, not during reward receipt.")
    print()
    print("  Bigger expected rewards = bigger anticipation signals.")
    print("  But the moment you actually GET the reward?")
    print("  A different brain region handles that (the mPFC),")
    print("  and the signal is often weaker.")
    print()
    print("  This is why:")
    print("  • 'Coming soon' campaigns generate huge excitement")
    print("  • Unboxing videos get millions of views")
    print("  • The wait for a holiday feels better than the holiday")
    print("  • Limited-time offers create a physical rush")
    print()
    print("  The brain is a wanting machine.")
    print("  The journey matters more than the destination.")
    print()


def main():
    show_intro()

    # Build a sequence with escalating rewards
    round_sequence = [
        ("bronze", 10),
        ("silver", 50),
        ("bronze", 10),
        ("gold", 200),
        ("silver", 50),
        ("diamond", 1000),
    ]

    results = []
    total_points = 0

    for i, (name, points) in enumerate(round_sequence, 1):
        earned = run_round(i, len(round_sequence), name, points, results)
        total_points += earned

    print(f"\n  TOTAL POINTS EARNED: {total_points}")
    debrief(results)


if __name__ == "__main__":
    main()
