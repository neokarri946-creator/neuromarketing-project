"""
Reinforcement of the Neural Valuation Signal by Social Conformity
— Interactive Experience
Based on Klucharev et al. (2009)

Feel how group opinion silently pulls your preferences —
even when you know the ratings are fake.
"""

import random
import time

ITEMS = [
    "A minimalist black watch",
    "A vintage leather satchel",
    "A neon-green running shoe",
    "A handmade ceramic coffee mug",
    "A retro-style portable radio",
    "A chrome desk lamp",
    "A floral-print silk tie",
    "A chunky knit cardigan",
    "A sleek mechanical pencil",
    "A bold geometric wall print",
    "A pastel linen tote bag",
    "A matte black water bottle",
    "A woven rattan desk tray",
    "A bright orange beanie hat",
    "A wooden phone stand",
    "A quilted navy laptop sleeve",
]


def show_intro():
    print("=" * 58)
    print("  SOCIAL CONFORMITY & THE BRAIN")
    print("  Based on Klucharev et al. (2009)")
    print("=" * 58)
    print()
    print("  You'll rate how appealing different products are.")
    print("  After each rating, you'll see what 'other people'")
    print("  supposedly rated them.")
    print()
    print("  Later, you'll rate them again.")
    print("  Let's see if the group pulls your opinions...")
    print()
    input("  Press Enter to start Round 1...\n")


def get_rating(prompt):
    while True:
        try:
            val = int(input(f"  {prompt} (1-10): "))
            if 1 <= val <= 10:
                return val
            print("  Enter a number from 1 to 10.")
        except ValueError:
            print("  Enter a number from 1 to 10.")


def generate_group_rating(player_rating):
    """Create a fake group rating that sometimes agrees, sometimes diverges."""
    if random.random() < 0.5:
        # Agree roughly
        offset = random.choice([-1, 0, 0, 1])
        return max(1, min(10, player_rating + offset))
    else:
        # Diverge noticeably (2-4 points away)
        direction = random.choice([-1, 1])
        offset = random.randint(2, 4) * direction
        return max(1, min(10, player_rating + offset))


def show_bar(value, max_val=10):
    filled = "█" * value
    empty = "░" * (max_val - value)
    return f"[{filled}{empty}] {value}/10"


def round_one(items):
    print("-" * 58)
    print("  ROUND 1: Your initial ratings")
    print("-" * 58)
    print()

    data = []
    for item in items:
        print(f"  Item: {item}")
        rating = get_rating("How appealing is this?")

        group = generate_group_rating(rating)
        diff = group - rating

        print(f"\n  Your rating:   {show_bar(rating)}")
        print(f"  Group average: {show_bar(group)}")

        if abs(diff) >= 2:
            if diff > 0:
                print("  ^ The group rated this HIGHER than you.")
            else:
                print("  ^ The group rated this LOWER than you.")
        else:
            print("  ~ You and the group roughly agree.")

        print()
        data.append({
            "item": item,
            "round1": rating,
            "group": group,
            "gap": diff,
        })

    return data


def round_two(data):
    print("-" * 58)
    print("  ROUND 2: Rate them again (from memory)")
    print("-" * 58)
    print()
    print("  Now rate the same items again. Just go with your gut.")
    print()

    for entry in data:
        print(f"  Item: {entry['item']}")
        rating2 = get_rating("How appealing is this now?")
        entry["round2"] = rating2
        print()

    return data


def debrief(data):
    print("\n" + "=" * 58)
    print("  DEBRIEF — DID THE GROUP MOVE YOU?")
    print("=" * 58)

    conform_count = 0
    diverge_cases = 0

    for entry in data:
        r1 = entry["round1"]
        r2 = entry["round2"]
        group = entry["group"]
        gap = entry["gap"]
        shift = r2 - r1

        print(f"\n  {entry['item']}")
        print(f"    Round 1: {r1}  |  Group: {group}  |  Round 2: {r2}")

        # Only count cases where group notably disagreed
        if abs(gap) >= 2:
            diverge_cases += 1
            moved_toward = (gap > 0 and shift > 0) or (gap < 0 and shift < 0)
            if moved_toward:
                conform_count += 1
                print(f"    >> You shifted TOWARD the group by {abs(shift)} point(s).")
            elif shift == 0:
                print(f"    >> You held your ground despite the group disagreeing.")
            else:
                print(f"    >> You shifted AWAY from the group — counter-conformity!")
        else:
            if shift == 0:
                print(f"    >> You and the group agreed. Rating unchanged.")
            else:
                print(f"    >> Rating changed by {shift:+d}, but group was already close.")

    print("\n" + "=" * 58)
    print("  YOUR CONFORMITY PROFILE")
    print("=" * 58)
    print()

    if diverge_cases > 0:
        pct = (conform_count / diverge_cases) * 100
        print(f"  Cases where the group disagreed with you: {diverge_cases}")
        print(f"  Times you shifted toward the group:       {conform_count} ({pct:.0f}%)")
    else:
        print("  The group happened to agree with you on everything!")
        print("  (Try again — the group ratings are somewhat random.)")

    print()
    print("  THE SCIENCE:")
    print()
    print("  Klucharev et al. (2009) found that disagreeing with a")
    print("  group triggers a 'prediction error' in the brain — the")
    print("  same signal used for learning from mistakes.")
    print()
    print("  Your brain treats 'I'm different from the group' like")
    print("  'I got the answer wrong,' and quietly adjusts your")
    print("  preference to match — often without you realising.")
    print()
    print("  WHY THIS MATTERS FOR MARKETING:")
    print()
    print("  - Star ratings don't just inform — they neurally recalibrate")
    print("  - 'Most popular' labels change how much you VALUE a product")
    print("  - Social proof (reviews, endorsements, trends) exploits this")
    print("    automatic correction signal in the brain")
    print("  - It's not persuasion. It's neural recalibration.")
    print()


def main():
    show_intro()
    selected = random.sample(ITEMS, 6)
    data = round_one(selected)

    print()
    input("  Press Enter to begin Round 2...\n")

    data = round_two(data)
    debrief(data)


if __name__ == "__main__":
    main()
