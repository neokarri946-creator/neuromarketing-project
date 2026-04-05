"""
THE ESCALATION GAME: Foot-in-the-Door
Based on: Compliance Without Pressure (1966) — Freedman & Fraser

A series of small, reasonable requests that slowly escalate.
Will you notice the shift? Most people don't — until it's too late.
"""

import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def intro():
    clear()
    print("=" * 55)
    print("  THE ESCALATION GAME")
    print("=" * 55)
    print()
    print("  You'll receive a series of requests from different")
    print("  organisations and people. For each one, simply")
    print("  decide: do you say YES or NO?")
    print()
    print("  There's no trick — just respond honestly.")
    print()
    input("Press Enter to begin... ")

# Two tracks: one with small-first escalation, one without
ESCALATION_TRACK = [
    {
        "request": (
            "A friendly student approaches you on the street.\n"
            "  'Hi! Would you sign this petition to keep local\n"
            "   parks clean? It's just your name — takes 2 seconds.'"
        ),
        "size": "tiny",
    },
    {
        "request": (
            "The same organisation emails you a week later.\n"
            "  'Thanks for signing! Could you share our parks\n"
            "   petition on your social media? Just one post.'"
        ),
        "size": "small",
    },
    {
        "request": (
            "They email again.\n"
            "  'We're doing a neighbourhood cleanup this Saturday\n"
            "   morning, 10am-12pm. Could you join us for a couple\n"
            "   of hours? Bring your own gloves!'"
        ),
        "size": "medium",
    },
    {
        "request": (
            "After the cleanup, the organiser approaches you.\n"
            "  'You were great! We're looking for someone to\n"
            "   coordinate the monthly cleanups in your area.\n"
            "   It's about 5 hours per month. Interested?'"
        ),
        "size": "large",
    },
    {
        "request": (
            "A month later, the charity director calls.\n"
            "  'Your area is our best-performing zone! We'd love\n"
            "   you to become a regional volunteer manager — it's\n"
            "   a 10-hour weekly commitment, but you'd be leading\n"
            "   something really meaningful.'"
        ),
        "size": "huge",
    },
]

COLD_TRACK = [
    {
        "request": (
            "A charity you've never heard of knocks on your door.\n"
            "  'Hi! We're looking for a regional volunteer manager\n"
            "   to coordinate park cleanups. It's a 10-hour weekly\n"
            "   commitment. Would you be interested?'"
        ),
        "size": "huge",
    },
    {
        "request": (
            "A different charity emails you out of the blue.\n"
            "  'We need someone to run our monthly food drive.\n"
            "   It's about 8 hours per month of organising.\n"
            "   Can we sign you up?'"
        ),
        "size": "large",
    },
    {
        "request": (
            "A political campaign calls your phone.\n"
            "  'Could you spend this Saturday canvassing for\n"
            "   our candidate? It's door-to-door from 9am to 5pm\n"
            "   in the rain. We'll provide a clipboard.'"
        ),
        "size": "large",
    },
]

def ask_yn(prompt_text="  Your answer (Y/N): "):
    while True:
        answer = input(prompt_text).strip().upper()
        if answer in ("Y", "N", "YES", "NO"):
            return answer[0] == "Y"
        print("  Please type Y or N.")

def run_game():
    intro()

    # --- PHASE 1: The escalation track ---
    clear()
    print("=" * 55)
    print("  PART 1: A COMMUNITY CAUSE")
    print("=" * 55)
    print()
    print("  You'll receive a sequence of requests over time.")
    print()
    input("Press Enter to start... ")

    escalation_responses = []

    for i, step in enumerate(ESCALATION_TRACK):
        clear()
        print(f"  Request {i + 1} of {len(ESCALATION_TRACK)}")
        print("-" * 55)
        print()
        print(f"  {step['request']}")
        print()
        agreed = ask_yn()
        escalation_responses.append({
            "agreed": agreed,
            "size": step["size"],
        })

        if agreed:
            print("\n  You said YES.")
        else:
            print("\n  You said NO.")
        time.sleep(0.8)

    # --- PHASE 2: Cold requests (no buildup) ---
    clear()
    print("=" * 55)
    print("  PART 2: COLD REQUESTS")
    print("=" * 55)
    print()
    print("  Now some requests from people you have NO prior")
    print("  relationship with. No buildup. Just the ask.")
    print()
    input("Press Enter to continue... ")

    cold_responses = []

    for i, step in enumerate(COLD_TRACK):
        clear()
        print(f"  Request {i + 1} of {len(COLD_TRACK)}")
        print("-" * 55)
        print()
        print(f"  {step['request']}")
        print()
        agreed = ask_yn()
        cold_responses.append({
            "agreed": agreed,
            "size": step["size"],
        })

        if agreed:
            print("\n  You said YES.")
        else:
            print("\n  You said NO.")
        time.sleep(0.8)

    # --- DEBRIEF ---
    clear()
    print("=" * 55)
    print("  YOUR RESULTS")
    print("=" * 55)

    esc_yes = sum(1 for r in escalation_responses if r["agreed"])
    cold_yes = sum(1 for r in cold_responses if r["agreed"])

    print()
    print("  ESCALATION TRACK (small -> large):")
    sizes = ["tiny", "small", "medium", "large", "huge"]
    labels = {"tiny": "Sign petition", "small": "Share on social media",
              "medium": "2hr cleanup", "large": "Monthly coordinator (5hr/mo)",
              "huge": "Regional manager (10hr/wk)"}
    for r in escalation_responses:
        status = "YES" if r["agreed"] else "NO "
        print(f"    [{status}] {labels[r['size']]}")

    print()
    print("  COLD REQUESTS (large asks, no buildup):")
    cold_labels = ["Regional manager (10hr/wk)", "Monthly food drive (8hr/mo)",
                   "Full-day canvassing in rain"]
    for i, r in enumerate(cold_responses):
        status = "YES" if r["agreed"] else "NO "
        print(f"    [{status}] {cold_labels[i]}")

    print()
    print("-" * 55)

    # Check if they went further on the escalation track
    biggest_esc = -1
    for i, r in enumerate(escalation_responses):
        if r["agreed"]:
            biggest_esc = i

    if biggest_esc >= 3 and cold_yes == 0:
        print()
        print("  Look at that: you agreed to a HUGE commitment in")
        print("  the escalation track but refused similar-sized")
        print("  cold requests. The gradual buildup pulled you in.")
    elif biggest_esc >= 3 and cold_yes > 0:
        print()
        print("  You're a generous person! You said yes to big asks")
        print("  both ways. But notice: did the escalation track")
        print("  feel EASIER to say yes to? That's the foot-in-the-door.")
    elif biggest_esc <= 1 and cold_yes == 0:
        print()
        print("  You're a tough audience! You resisted the escalation.")
        print("  Most people don't — the original study found 76%")
        print("  compliance after a small initial request, vs just 17%")
        print("  for a cold large request.")
    else:
        print()
        print(f"  You went up to step {biggest_esc + 1} on the escalation")
        print(f"  track and agreed to {cold_yes} cold requests.")

    print()
    print("=" * 55)
    print("  THE SCIENCE")
    print("=" * 55)
    print()
    print("  Freedman & Fraser (1966) found that people who")
    print("  agreed to a SMALL request first were 4.5x more")
    print("  likely to agree to a LARGE request later.")
    print()
    print("  Why? It's not obligation — it's IDENTITY SHIFT.")
    print()
    print("  When you sign that petition, you don't just do a")
    print("  favour. You become 'someone who cares about parks.'")
    print("  Each yes reinforces that identity. By the time the")
    print("  big ask comes, saying yes feels CONSISTENT with")
    print("  who you now believe you are.")
    print()
    print("  Marketers use this everywhere:")
    print("  - Free trials -> paid subscriptions")
    print("  - Email sign-up -> first purchase -> loyalty member")
    print("  - 'Just try one lesson' -> full course enrolment")
    print("  - Small donation -> monthly donor -> major gift")
    print()
    print("  The path to a big YES starts with a tiny one.")
    print()
    input("Press Enter to exit... ")

if __name__ == "__main__":
    run_game()
