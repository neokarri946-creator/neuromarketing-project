"""
Neural Predictors of Purchases — Interactive Experience
Based on Knutson et al. (2007)

Feel the tug-of-war between DESIRE and PRICE PAIN that your brain
runs every time you consider buying something.
"""

import random
import time

PRODUCTS = [
    ("A premium noise-cancelling headphone set", 349),
    ("A handmade leather wallet", 85),
    ("A top-of-the-line espresso machine", 599),
    ("A limited-edition sneaker collaboration", 220),
    ("A cosy cashmere scarf", 140),
    ("A smartwatch with health tracking", 279),
    ("A vintage vinyl record (rare pressing)", 65),
    ("A designer sunglasses pair", 310),
    ("A portable Bluetooth speaker", 45),
    ("A silk pillowcase set", 70),
    ("A gourmet chocolate gift box", 38),
    ("A high-end mechanical keyboard", 175),
]


def show_intro():
    print("=" * 58)
    print("  NEURAL PREDICTORS OF PURCHASES")
    print("  Based on Knutson et al. (2007)")
    print("=" * 58)
    print()
    print("In this experiment, you'll see products with prices.")
    print()
    print("For each one, you'll rate TWO things separately:")
    print("  1. DESIRE  — how much you WANT it (1-10)")
    print("  2. PRICE PAIN — how much the price HURTS (1-10)")
    print()
    print("Then you'll decide: BUY or PASS.")
    print()
    print("Afterward, we'll reveal what your brain was doing")
    print("behind the scenes — just like the fMRI did.")
    print()
    input("Press Enter to start...\n")


def get_rating(prompt, low_label, high_label):
    while True:
        try:
            print(f"  ({low_label} = 1 ... {high_label} = 10)")
            val = int(input(f"  {prompt}: "))
            if 1 <= val <= 10:
                return val
            print("  Please enter a number from 1 to 10.")
        except ValueError:
            print("  Please enter a number from 1 to 10.")


def get_buy_decision():
    while True:
        choice = input("  Your decision — BUY or PASS? ").strip().upper()
        if choice in ("BUY", "B"):
            return True
        if choice in ("PASS", "P"):
            return False
        print("  Type BUY or PASS.")


def neural_prediction(desire, pain):
    """The model: desire vs pain predicts the purchase."""
    net_signal = desire - pain
    if net_signal > 1:
        return True  # predicted BUY
    elif net_signal < -1:
        return False  # predicted PASS
    else:
        return desire >= 6  # borderline — slight lean toward desire


def run_trial(product_name, price):
    print("-" * 58)
    print(f"\n  PRODUCT: {product_name}")
    print(f"  PRICE:   £{price}")
    print()

    desire = get_rating("How much do you WANT this?", "meh", "must have")
    print()
    pain = get_rating("How much does the price HURT?", "barely notice", "ouch")
    print()

    predicted = neural_prediction(desire, pain)
    actual = get_buy_decision()

    return {
        "product": product_name,
        "price": price,
        "desire": desire,
        "pain": pain,
        "predicted": predicted,
        "actual": actual,
    }


def show_bar(value, max_val=10, label=""):
    filled = "█" * value
    empty = "░" * (max_val - value)
    return f"  {label:<12} [{filled}{empty}] {value}/10"


def debrief(results):
    print("\n" + "=" * 58)
    print("  DEBRIEF — YOUR NEURAL PURCHASE MAP")
    print("=" * 58)

    correct = 0
    total = len(results)

    for i, r in enumerate(results, 1):
        print(f"\n  Trial {i}: {r['product']} (£{r['price']})")
        print(show_bar(r["desire"], label="Desire"))
        print(show_bar(r["pain"], label="Price Pain"))

        net = r["desire"] - r["pain"]
        if net > 0:
            signal = f"Desire wins by {net}"
        elif net < 0:
            signal = f"Pain wins by {abs(net)}"
        else:
            signal = "Dead heat"

        pred_label = "BUY" if r["predicted"] else "PASS"
        act_label = "BUY" if r["actual"] else "PASS"
        match = "✓" if r["predicted"] == r["actual"] else "✗"

        if r["predicted"] == r["actual"]:
            correct += 1

        print(f"  Net signal:  {signal}")
        print(f"  Brain predicted: {pred_label}  |  You chose: {act_label}  {match}")

    accuracy = (correct / total) * 100 if total > 0 else 0

    print("\n" + "=" * 58)
    print(f"  PREDICTION ACCURACY: {correct}/{total} ({accuracy:.0f}%)")
    print("=" * 58)
    print()
    print("  THE SCIENCE:")
    print()
    print("  Knutson et al. (2007) found that just two brain signals")
    print("  predicted purchases BEFORE people consciously decided:")
    print()
    print("  • Nucleus accumbens (DESIRE) — fires when you want something")
    print("  • Insula (PRICE PAIN) — fires when the cost feels too high")
    print()
    print("  When desire outweighed pain, people bought.")
    print("  When pain outweighed desire, they passed.")
    print()
    print("  This is why credit cards boost spending — they reduce the")
    print("  pain signal. It's why 'free trials' work — zero pain.")
    print("  And it's why even a great product won't sell if the price")
    print("  triggers that visceral 'ouch' in your insula.")
    print()
    print("  Your ratings above recreated this neural tug-of-war.")
    if accuracy >= 70:
        print("  The model predicted your choices well — your brain's")
        print("  desire-vs-pain balance was driving your decisions.")
    else:
        print("  The model didn't fully capture your choices — which")
        print("  shows that other factors (mood, memory, identity) also")
        print("  play a role beyond the basic two-signal model.")
    print()


def main():
    show_intro()

    selected = random.sample(PRODUCTS, 6)
    results = []

    for product_name, price in selected:
        result = run_trial(product_name, price)
        results.append(result)
        print()

    debrief(results)


if __name__ == "__main__":
    main()
