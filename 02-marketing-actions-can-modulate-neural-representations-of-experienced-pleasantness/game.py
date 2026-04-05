"""
Marketing Actions Can Modulate Experienced Pleasantness — Interactive Experience
Based on Plassmann et al. (2008)

Discover how price labels change your actual experience of a product,
not just your expectations.
"""

import random
import time

# Each item: (description, secret_group, fake_price_cheap, fake_price_expensive)
# Items in the same secret_group are actually IDENTICAL products
PRODUCTS = [
    {
        "group": "A",
        "cheap": {
            "name": "Sunrise Blend Coffee",
            "origin": "Brazilian single-origin, light roast",
            "price": "£3.50 per bag",
        },
        "expensive": {
            "name": "Artisan Reserve Coffee",
            "origin": "Brazilian single-origin, light roast",
            "price": "£18.90 per bag",
        },
        "reveal": "These two coffees were the SAME Brazilian light roast.",
    },
    {
        "group": "B",
        "cheap": {
            "name": "Fresh Squeeze Orange Juice",
            "origin": "Concentrate blend, store brand",
            "price": "£1.20 per litre",
        },
        "expensive": {
            "name": "Grove Select Orange Juice",
            "origin": "Hand-pressed, small batch",
            "price": "£6.80 per litre",
        },
        "reveal": "Both juices were the SAME orange juice — just relabelled.",
    },
    {
        "group": "C",
        "cheap": {
            "name": "Classic Dark Chocolate Bar",
            "origin": "70% cocoa, value range",
            "price": "£1.50 per bar",
        },
        "expensive": {
            "name": "Maison Noir Artisan Chocolate",
            "origin": "70% cocoa, handcrafted in Belgium",
            "price": "£12.00 per bar",
        },
        "reveal": "The exact SAME chocolate bar — only the label differed.",
    },
    {
        "group": "D",
        "cheap": {
            "name": "Everyday Hand Cream",
            "origin": "Moisturising formula, unscented",
            "price": "£2.99 per tube",
        },
        "expensive": {
            "name": "Luxe Botanica Hand Cream",
            "origin": "Botanical moisturising formula, dermatologist approved",
            "price": "£24.00 per tube",
        },
        "reveal": "Identical cream. Same formula. Only the branding changed.",
    },
]


def show_intro():
    print("=" * 58)
    print("  THE PRICE-PLEASURE EXPERIMENT")
    print("  Based on Plassmann et al. (2008)")
    print("=" * 58)
    print()
    print("  You're going to taste-test some products.")
    print("  (Well, imagine tasting them.)")
    print()
    print("  For each one, read the description and price,")
    print("  then rate how much you'd ENJOY it on a scale of 1-10.")
    print()
    print("  Be honest — go with your gut feeling.")
    print()
    input("  Press Enter to begin...\n")


def get_rating():
    while True:
        try:
            val = int(input("  Your enjoyment rating (1-10): "))
            if 1 <= val <= 10:
                return val
            print("  Please pick 1 to 10.")
        except ValueError:
            print("  Please enter a number.")


def present_product(product_info, trial_num, total):
    print(f"\n  --- Product {trial_num} of {total} ---")
    print(f"  Name:   {product_info['name']}")
    print(f"  Detail: {product_info['origin']}")
    print(f"  Price:  {product_info['price']}")
    print()
    rating = get_rating()
    return rating


def show_bar(value, max_val=10):
    filled = "█" * value
    empty = "░" * (max_val - value)
    return f"[{filled}{empty}] {value}/10"


def main():
    show_intro()

    # Select 3 product pairs
    selected = random.sample(PRODUCTS, 3)

    # Build a mixed presentation order: all 6 items shuffled,
    # but cheap and expensive versions are separated
    cheap_items = []
    expensive_items = []

    for p in selected:
        cheap_items.append(("cheap", p))
        expensive_items.append(("expensive", p))

    # Present cheap ones first (as a "round 1"), then expensive (as "round 2")
    # This mimics the wine study's within-subject design
    random.shuffle(cheap_items)
    random.shuffle(expensive_items)

    print("  ╔══════════════════════════════════════════════╗")
    print("  ║          ROUND 1 — FIRST TASTINGS           ║")
    print("  ╚══════════════════════════════════════════════╝")

    results = {}
    trial = 1
    for version, product in cheap_items:
        info = product[version]
        rating = present_product(info, trial, 3)
        group = product["group"]
        if group not in results:
            results[group] = {"product": product}
        results[group]["cheap_rating"] = rating
        results[group]["cheap_name"] = info["name"]
        results[group]["cheap_price"] = info["price"]
        trial += 1

    print()
    input("  Press Enter for Round 2...\n")

    print("  ╔══════════════════════════════════════════════╗")
    print("  ║        ROUND 2 — PREMIUM TASTINGS           ║")
    print("  ╚══════════════════════════════════════════════╝")

    trial = 1
    for version, product in expensive_items:
        info = product[version]
        rating = present_product(info, trial, 3)
        group = product["group"]
        results[group]["expensive_rating"] = rating
        results[group]["expensive_name"] = info["name"]
        results[group]["expensive_price"] = info["price"]
        trial += 1

    # --- REVEAL ---
    print("\n" + "=" * 58)
    print("  THE REVEAL")
    print("=" * 58)

    total_cheap = 0
    total_expensive = 0
    price_won = 0

    for group, data in results.items():
        p = data["product"]
        cheap_r = data["cheap_rating"]
        expensive_r = data["expensive_rating"]
        total_cheap += cheap_r
        total_expensive += expensive_r

        print(f"\n  {p['reveal']}")
        print(f"    '{data['cheap_name']}' ({data['cheap_price']})")
        print(f"    Your rating: {show_bar(cheap_r)}")
        print(f"    '{data['expensive_name']}' ({data['expensive_price']})")
        print(f"    Your rating: {show_bar(expensive_r)}")

        diff = expensive_r - cheap_r
        if diff > 0:
            print(f"    >> You rated the 'expensive' version {diff} point(s) HIGHER.")
            price_won += 1
        elif diff < 0:
            print(f"    >> You rated the 'cheap' version {abs(diff)} point(s) higher!")
        else:
            print(f"    >> You rated them exactly the same.")

    print("\n" + "=" * 58)
    print("  THE SCIENCE")
    print("=" * 58)

    avg_cheap = total_cheap / len(results)
    avg_expensive = total_expensive / len(results)

    print(f"\n  Your average 'cheap' rating:     {avg_cheap:.1f}")
    print(f"  Your average 'expensive' rating:  {avg_expensive:.1f}")
    print()

    if price_won >= 2:
        print("  Price shaped your experience — just like in the study.")
        print("  You're not being foolish. This is how brains work.")
    elif price_won == 1:
        print("  Price influenced you on some products but not all.")
        print("  The effect is real but varies by product and person.")
    else:
        print("  You resisted the price effect — interesting!")
        print("  In the lab with real wine and fMRI, most people can't.")

    print()
    print("  Plassmann et al. (2008) found that when people were")
    print("  told wine cost more, their brains ACTUALLY generated")
    print("  more pleasure — measured in the medial orbitofrontal")
    print("  cortex. The tongue tasted the same wine, but the brain")
    print("  constructed a different experience.")
    print()
    print("  Price doesn't just set expectations.")
    print("  It rewrites your sensory reality.")
    print()


if __name__ == "__main__":
    main()
