"""
CONTEXT SHIFTS VALUE
====================
Based on: How Context Alters Value (2017) — Schmidt et al.

The same item can feel cheap or expensive depending on
what it's sitting next to. This game lets you experience
that illusion firsthand.
"""

import random
import time

def clear():
    print("\n" * 2)

def intro():
    print("=" * 50)
    print("  CONTEXT SHIFTS VALUE")
    print("  How much is something really worth?")
    print("=" * 50)
    print()
    print("You'll see items alongside other products.")
    print("Your job: rate how good a deal each item is")
    print("on a scale of 1 (terrible deal) to 10 (amazing deal).")
    print()
    input("Press Enter to start...\n")

# Each target item has a fixed "true" price.
# We show it alongside cheap or expensive context items.
TARGETS = [
    {
        "name": "Wireless Headphones",
        "price": 85,
        "cheap_context": [
            ("Wired Earbuds", 12),
            ("Phone Case", 8),
            ("USB Cable", 5),
        ],
        "expensive_context": [
            ("Noise-Cancelling Headphones", 350),
            ("Hi-Fi Speaker System", 480),
            ("Studio Monitor Pair", 600),
        ],
    },
    {
        "name": "Leather Wallet",
        "price": 45,
        "cheap_context": [
            ("Plastic Card Holder", 3),
            ("Keyring", 2),
            ("Coin Pouch", 6),
        ],
        "expensive_context": [
            ("Designer Handbag", 320),
            ("Leather Briefcase", 275),
            ("Luxury Watch Strap", 190),
        ],
    },
    {
        "name": "Running Shoes",
        "price": 110,
        "cheap_context": [
            ("Flip Flops", 8),
            ("Cotton Socks (3-pack)", 5),
            ("Shoelaces", 3),
        ],
        "expensive_context": [
            ("Carbon Racing Shoes", 275),
            ("Custom Orthotics", 350),
            ("Trail Running Boots", 230),
        ],
    },
    {
        "name": "Smartwatch",
        "price": 199,
        "cheap_context": [
            ("Digital Pedometer", 15),
            ("Rubber Wristband", 4),
            ("Basic Alarm Clock", 10),
        ],
        "expensive_context": [
            ("Luxury Automatic Watch", 1200),
            ("Gold Bracelet", 950),
            ("Diamond Pendant", 1500),
        ],
    },
]

def show_shelf(target, context_items):
    """Display a shelf of products with the target highlighted."""
    print("-" * 45)
    print("  ITEMS ON DISPLAY:")
    print("-" * 45)
    all_items = context_items + [(target["name"], target["price"])]
    random.shuffle(all_items)
    for name, price in all_items:
        marker = " >>>  " if name == target["name"] else "      "
        print(f"{marker}{name:.<30} ${price}")
    print("-" * 45)
    print(f"\n  Target item: {target['name']} — ${target['price']}")

def get_rating():
    while True:
        try:
            r = int(input("\n  Your rating (1-10): "))
            if 1 <= r <= 10:
                return r
            print("  Please enter a number from 1 to 10.")
        except ValueError:
            print("  Please enter a number from 1 to 10.")

def run_game():
    intro()

    # Pick 3 random targets
    chosen = random.sample(TARGETS, 3)
    results = []

    for i, target in enumerate(chosen):
        # Randomly decide which context comes first
        if random.random() < 0.5:
            first_ctx, first_label = target["cheap_context"], "cheap"
            second_ctx, second_label = target["expensive_context"], "expensive"
        else:
            first_ctx, first_label = target["expensive_context"], "expensive"
            second_ctx, second_label = target["cheap_context"], "cheap"

        # Round A
        clear()
        print(f"  ROUND {i*2 + 1} of 6")
        print()
        show_shelf(target, first_ctx)
        r1 = get_rating()

        # Round B — same item, different context
        clear()
        print(f"  ROUND {i*2 + 2} of 6")
        print()
        show_shelf(target, second_ctx)
        r2 = get_rating()

        if first_label == "cheap":
            results.append((target["name"], target["price"], r1, r2))
        else:
            results.append((target["name"], target["price"], r2, r1))

    # === DEBRIEF ===
    clear()
    print("=" * 50)
    print("  RESULTS — HOW CONTEXT SHIFTED YOUR VALUES")
    print("=" * 50)
    print()

    total_cheap = 0
    total_expensive = 0

    for name, price, rating_cheap, rating_expensive in results:
        total_cheap += rating_cheap
        total_expensive += rating_expensive
        shift = rating_expensive - rating_cheap
        direction = "HIGHER" if shift > 0 else "LOWER" if shift < 0 else "SAME"
        print(f"  {name} (${price})")
        print(f"    Among cheap items:     you rated it {rating_cheap}/10")
        print(f"    Among expensive items:  you rated it {rating_expensive}/10")
        if shift != 0:
            print(f"    Context shifted your rating {abs(shift)} points {direction}")
        else:
            print(f"    Your rating stayed the same — unusual!")
        print()

    avg_cheap = total_cheap / len(results)
    avg_expensive = total_expensive / len(results)

    print("-" * 50)
    print(f"  Average rating among cheap items:     {avg_cheap:.1f}")
    print(f"  Average rating among expensive items:  {avg_expensive:.1f}")
    print("-" * 50)
    print()

    if avg_expensive > avg_cheap:
        print("  YOUR BRAIN DID EXACTLY WHAT THE STUDY PREDICTS.")
        print()
        print("  The same items — same price, same features — felt")
        print("  like better deals when surrounded by expensive")
        print("  alternatives. Your brain didn't evaluate the item")
        print("  in isolation. It computed value RELATIVE to context.")
    elif avg_expensive < avg_cheap:
        print("  INTERESTING — you bucked the typical pattern.")
        print()
        print("  Most people rate items higher when they're next to")
        print("  expensive alternatives (they seem like bargains).")
        print("  You did the opposite. You may have been anchoring")
        print("  on quality expectations rather than price contrast.")
    else:
        print("  Your ratings were perfectly consistent — rare!")
        print("  Most people's valuations shift with context.")

    print()
    print("  THE SCIENCE:")
    print("  Schmidt et al. (2017) showed that the brain's")
    print("  valuation system (vmPFC) literally recalculates")
    print("  how much something is worth based on what's nearby.")
    print("  This is why stores place mid-range products next")
    print("  to premium ones — it makes the mid-range feel like")
    print("  a steal. Your sense of 'good value' is always")
    print("  relative, never absolute.")
    print()

if __name__ == "__main__":
    run_game()
