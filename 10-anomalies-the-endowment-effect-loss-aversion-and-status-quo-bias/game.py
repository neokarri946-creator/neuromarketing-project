"""
THE ENDOWMENT EFFECT
====================
Based on: Anomalies: The Endowment Effect, Loss Aversion,
and Status Quo Bias (1991) — Kahneman, Knetsch & Thaler

You value things more just because you own them.
This game gives you items and offers trades —
watch how hard it is to let go of what's "yours."
"""

import random

def intro():
    print("=" * 50)
    print("  THE ENDOWMENT EFFECT")
    print("  Why is YOUR stuff worth more?")
    print("=" * 50)
    print()
    print("You'll be given random items throughout this game.")
    print("After each one, you'll be offered trades.")
    print("Accept or reject each trade based on how you feel.")
    print()
    print("There are no tricks — just honest choices.")
    print()
    input("Press Enter to start...\n")

ITEMS = [
    {"name": "Vintage Polaroid Camera", "category": "tech", "value": 85},
    {"name": "Handmade Ceramic Mug", "category": "home", "value": 25},
    {"name": "Leather-Bound Notebook", "category": "stationery", "value": 35},
    {"name": "Bluetooth Speaker", "category": "tech", "value": 60},
    {"name": "Scented Candle Set", "category": "home", "value": 30},
    {"name": "Mechanical Keyboard", "category": "tech", "value": 95},
    {"name": "Wool Beanie Hat", "category": "clothing", "value": 20},
    {"name": "Cast Iron Skillet", "category": "home", "value": 45},
    {"name": "Fountain Pen", "category": "stationery", "value": 50},
    {"name": "Wireless Earbuds", "category": "tech", "value": 70},
    {"name": "Silk Scarf", "category": "clothing", "value": 40},
    {"name": "Board Game (Classic)", "category": "entertainment", "value": 35},
]

def get_yn(prompt):
    while True:
        c = input(prompt).strip().lower()
        if c in ('y', 'n'):
            return c == 'y'
        print("  Please type Y or N.")

def get_price(prompt):
    while True:
        try:
            p = int(input(prompt).strip().replace('$', '').replace(',', ''))
            if p >= 0:
                return p
            print("  Please enter a positive number.")
        except ValueError:
            print("  Please enter a number (e.g., 30).")

def run_game():
    intro()

    items_pool = ITEMS.copy()
    random.shuffle(items_pool)

    trades_offered = 0
    trades_accepted = 0
    trades_rejected = 0
    selling_prices = []
    buying_prices = []
    status_quo_tests = 0
    status_quo_kept = 0

    # === PHASE 1: THE MUG EXPERIMENT ===
    print("=" * 50)
    print("  PHASE 1: WHAT'S IT WORTH?")
    print("=" * 50)
    print()

    # Give the player an item
    owned = items_pool.pop()
    print(f"  Congratulations! You've been given:")
    print(f"  >>> {owned['name']} <<<")
    print()
    print("  It's yours now. You own it.")
    print()

    # Ask selling price
    sell_price = get_price("  What's the MINIMUM you'd sell it for? $")
    selling_prices.append((owned["name"], owned["value"], sell_price))
    print()

    # Now ask what they'd pay for the same category item
    similar = items_pool.pop()
    print(f"  Now imagine you DON'T own anything.")
    print(f"  You see this in a shop:")
    print(f"  >>> {similar['name']} <<<")
    print()
    buy_price = get_price("  What's the MOST you'd pay for it? $")
    buying_prices.append((similar["name"], similar["value"], buy_price))
    print()

    # === PHASE 2: TRADE OFFERS ===
    print("=" * 50)
    print("  PHASE 2: TRADE OFFERS")
    print("=" * 50)
    print()
    print(f"  You currently own: {owned['name']}")
    print()
    print("  People will offer to trade with you.")
    print("  Accept or reject each trade.\n")

    for _ in range(4):
        if not items_pool:
            break
        offered = items_pool.pop()
        trades_offered += 1

        # Offer trades of similar or higher value
        print(f"  Someone offers you: {offered['name']}")
        print(f"  In exchange for your: {owned['name']}")
        print()

        accepted = get_yn("  Accept this trade? (Y/N): ")
        if accepted:
            trades_accepted += 1
            print(f"\n  You traded away {owned['name']}")
            print(f"  You now own: {offered['name']}\n")
            owned = offered
        else:
            trades_rejected += 1
            print(f"\n  You kept your {owned['name']}\n")

    # === PHASE 3: STATUS QUO BIAS ===
    print("=" * 50)
    print("  PHASE 3: STICK OR SWITCH?")
    print("=" * 50)
    print()

    defaults = [
        {
            "scenario": "You're on a phone plan: 5GB data, $30/month.\nA new plan is available: 8GB data, $32/month.",
            "switch": "Switch to the new plan",
            "keep": "Keep your current plan",
        },
        {
            "scenario": "Your electricity provider charges $0.15/kWh.\nA competitor offers $0.14/kWh with the same service.",
            "switch": "Switch to the competitor",
            "keep": "Stay with your current provider",
        },
        {
            "scenario": "You have a free checking account at your bank.\nAnother bank offers a free account with 1% cashback on purchases.",
            "switch": "Open the new account and switch",
            "keep": "Stay with your current bank",
        },
    ]

    for d in defaults:
        status_quo_tests += 1
        print(f"  {d['scenario']}")
        print()
        print(f"  A: {d['keep']}")
        print(f"  B: {d['switch']}")
        print()
        while True:
            c = input("  Your choice (A or B): ").strip().upper()
            if c in ('A', 'B'):
                break
            print("  Please type A or B.")
        if c == 'A':
            status_quo_kept += 1
        print()

    # === DEBRIEF ===
    print("=" * 50)
    print("  RESULTS: YOUR OWNERSHIP BIAS")
    print("=" * 50)
    print()

    # Endowment effect analysis
    print("  ENDOWMENT EFFECT:")
    for name, obj_val, price in selling_prices:
        print(f"  Item you owned: {name}")
        print(f"    Your selling price: ${price}")
    for name, obj_val, price in buying_prices:
        print(f"  Item you didn't own: {name}")
        print(f"    Your buying price:  ${price}")
    print()

    if selling_prices and buying_prices:
        avg_sell = sum(p for _, _, p in selling_prices) / len(selling_prices)
        avg_buy = sum(p for _, _, p in buying_prices) / len(buying_prices)
        if avg_sell > avg_buy:
            ratio = avg_sell / avg_buy if avg_buy > 0 else float('inf')
            print(f"  Your selling price was {ratio:.1f}x your buying price.")
            print("  This IS the endowment effect. Owning something makes")
            print("  it feel more valuable — you demand more to give it up")
            print("  than you'd pay to get something similar.")
        elif avg_sell <= avg_buy:
            print("  Interesting — your selling price wasn't higher than")
            print("  your buying price. In the classic experiments, sellers")
            print("  typically demand about 2x what buyers will pay.")

    print()

    # Trade resistance
    print("  TRADE RESISTANCE:")
    print(f"  Trades offered:  {trades_offered}")
    print(f"  Trades accepted: {trades_accepted}")
    print(f"  Trades rejected: {trades_rejected}")
    if trades_rejected > trades_accepted:
        print("  You resisted most trades — classic endowment effect.")
        print("  Giving up 'your' item felt like a loss, even when")
        print("  the offered item was just as good or better.")
    elif trades_accepted > trades_rejected:
        print("  You were open to trading — less attached than most.")
    print()

    # Status quo bias
    print("  STATUS QUO BIAS:")
    print(f"  Stuck with current option: {status_quo_kept}/{status_quo_tests}")
    if status_quo_kept >= 2:
        print("  You showed strong status quo bias. Switching felt")
        print("  like effort and risk, even when the alternative")
        print("  was clearly better on paper.")
    elif status_quo_kept == 0:
        print("  You switched every time — you may be more")
        print("  analytically driven than the average person.")
    else:
        print("  A mixed pattern — some inertia, some flexibility.")

    print()
    print("  THE SCIENCE:")
    print("  Kahneman, Knetsch & Thaler (1991) showed three")
    print("  linked biases:")
    print()
    print("  1. ENDOWMENT EFFECT: Owning something inflates its")
    print("     value in your mind (sellers want ~2x buyers' price)")
    print()
    print("  2. LOSS AVERSION: Giving something up feels like a")
    print("     loss, which hurts more than gaining feels good")
    print()
    print("  3. STATUS QUO BIAS: Switching = accepting a loss of")
    print("     the current state, so people stick with defaults")
    print()
    print("  Marketers exploit this with free trials, 'try before")
    print("  you buy', and default opt-ins. Once you 'own' it —")
    print("  even temporarily — letting go feels like losing.")
    print()

if __name__ == "__main__":
    run_game()
