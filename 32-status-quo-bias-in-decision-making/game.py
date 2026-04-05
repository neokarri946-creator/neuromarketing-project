"""
Status Quo Bias in Decision Making — Interactive Experience
Based on Samuelson & Zeckhauser (1988)

You'll be given an initial portfolio of resources, then offered
trades that are objectively beneficial. Will you take them — or
cling to what you already have?
"""

import random


def show_intro():
    print("=" * 58)
    print("  STATUS QUO BIAS")
    print("  Based on Samuelson & Zeckhauser (1988)")
    print("=" * 58)
    print()
    print("  You've inherited a portfolio of investments.")
    print("  Each round, you'll be offered a trade.")
    print()
    print("  Every trade is designed to improve your portfolio")
    print("  (higher expected value or lower risk for the same")
    print("  return). Rational investors would take all of them.")
    print()
    print("  But will you?")
    print()
    input("  Press Enter to see your starting portfolio...\n")


ASSET_NAMES = [
    "Blue Chip Stock Fund",
    "Government Bonds",
    "Real Estate Trust",
    "Tech Growth Fund",
    "Emerging Markets Fund",
    "Gold & Commodities",
    "Savings Account",
    "Corporate Bond Fund",
]


def generate_portfolio():
    """Create a random starting portfolio."""
    assets = random.sample(ASSET_NAMES, 4)
    allocations = [random.randint(15, 40) for _ in range(4)]
    total = sum(allocations)
    allocations = [round(a / total * 100) for a in allocations]
    # Fix rounding
    diff = 100 - sum(allocations)
    allocations[0] += diff

    portfolio = {}
    for asset, alloc in zip(assets, allocations):
        portfolio[asset] = {
            "allocation": alloc,
            "return": round(random.uniform(3.0, 9.0), 1),
            "risk": random.choice(["Low", "Medium", "High"]),
        }
    return portfolio


def show_portfolio(portfolio, label="YOUR PORTFOLIO"):
    print(f"\n  {label}")
    print(f"  {'-' * 48}")
    print(f"  {'Asset':<28} {'Alloc':>5}  {'Return':>6}  {'Risk':>6}")
    print(f"  {'-' * 48}")
    for name, info in portfolio.items():
        print(f"  {name:<28} {info['allocation']:>4}%  {info['return']:>5.1f}%  {info['risk']:>6}")
    total_return = sum(
        info["allocation"] / 100 * info["return"]
        for info in portfolio.values()
    )
    print(f"  {'-' * 48}")
    print(f"  {'Weighted expected return:':<35} {total_return:>5.1f}%")


def weighted_return(portfolio):
    return sum(
        info["allocation"] / 100 * info["return"]
        for info in portfolio.values()
    )


def generate_trade(portfolio):
    """Generate an objectively beneficial trade."""
    assets = list(portfolio.keys())
    # Find worst performer
    worst = min(assets, key=lambda a: portfolio[a]["return"])
    worst_info = portfolio[worst]

    # Create a better replacement
    available = [a for a in ASSET_NAMES if a not in portfolio]
    new_name = random.choice(available) if available else "Index Tracker Fund"

    # Make the new option strictly better
    new_return = round(worst_info["return"] + random.uniform(1.0, 3.0), 1)
    risk_upgrade = {"High": "Medium", "Medium": "Low", "Low": "Low"}
    new_risk = risk_upgrade.get(worst_info["risk"], worst_info["risk"])

    return {
        "give_up": worst,
        "give_up_info": worst_info,
        "receive": new_name,
        "receive_info": {
            "allocation": worst_info["allocation"],
            "return": new_return,
            "risk": new_risk,
        },
    }


def run_round(portfolio, round_num, total_rounds):
    trade = generate_trade(portfolio)

    print(f"\n{'=' * 58}")
    print(f"  ROUND {round_num} of {total_rounds}")
    print(f"{'=' * 58}")

    show_portfolio(portfolio)

    print(f"\n  PROPOSED TRADE:")
    print(f"  {'-' * 48}")
    g = trade["give_up"]
    gi = trade["give_up_info"]
    r = trade["receive"]
    ri = trade["receive_info"]
    print(f"  GIVE UP:  {g}")
    print(f"            Return: {gi['return']}%  |  Risk: {gi['risk']}")
    print(f"  RECEIVE:  {r}")
    print(f"            Return: {ri['return']}%  |  Risk: {ri['risk']}")
    print()

    improvement = ri["return"] - gi["return"]
    print(f"  This trade improves return by +{improvement:.1f}%")
    if ri["risk"] != gi["risk"]:
        print(f"  AND reduces risk from {gi['risk']} to {ri['risk']}")
    print()

    while True:
        choice = input("  Accept trade? (YES / NO): ").strip().upper()
        if choice in ("YES", "Y"):
            # Apply trade
            portfolio[r] = ri
            del portfolio[g]
            print(f"\n  Trade accepted. {r} added to portfolio.")
            return True
        elif choice in ("NO", "N"):
            print(f"\n  Trade rejected. You're keeping {g}.")
            return False
        else:
            print("  Type YES or NO.")


def main():
    show_intro()

    portfolio = generate_portfolio()
    total_rounds = 8
    accepted = 0
    rejected = 0
    improvements_rejected = []

    for round_num in range(1, total_rounds + 1):
        took_trade = run_round(portfolio, round_num, total_rounds)
        if took_trade:
            accepted += 1
        else:
            rejected += 1
            trade = generate_trade(portfolio)
            improvements_rejected.append(
                trade["receive_info"]["return"] - trade["give_up_info"]["return"]
            )
        print()

    # --- DEBRIEF ---
    print("=" * 58)
    print("  DEBRIEF — STATUS QUO BIAS REVEALED")
    print("=" * 58)

    print(f"""
  Results:
    Trades accepted:  {accepted} out of {total_rounds}
    Trades rejected:  {rejected} out of {total_rounds}
""")

    if rejected == 0:
        print("  You accepted every trade! You're unusually rational")
        print("  — or at least unusually willing to let go of what")
        print("  you already have. Most people aren't.")
    elif rejected <= 2:
        print("  You rejected a few trades — even though every one")
        print("  of them was objectively better. You felt the pull")
        print("  of the status quo, even if you mostly resisted it.")
    else:
        print(f"  You rejected {rejected} beneficial trades. Each one")
        print("  would have improved your portfolio, but something")
        print("  made you want to keep what you already had.")
        print("  That 'something' is status quo bias.")

    print(f"""
  THE SCIENCE:

  Samuelson & Zeckhauser (1988) found that when one option
  was framed as the "current" choice, people selected it
  far more often than when it was just one option among
  many — even when alternatives were objectively better.

  The bias is driven by several forces:
    - Loss aversion: giving something up feels worse than
      gaining something equivalent feels good
    - Regret avoidance: if you switch and it goes wrong,
      you'll blame yourself; if you stay and it goes wrong,
      it "just happened"
    - Cognitive ease: sticking with what you have requires
      zero mental effort

  IN THE REAL WORLD:

  This is why people keep the same phone contract for years
  (even when cheaper plans exist), why voters re-elect
  incumbents, and why brands fight so hard to be your FIRST
  choice — because once you're in, switching feels costly
  even when it's free.
""")


if __name__ == "__main__":
    main()
