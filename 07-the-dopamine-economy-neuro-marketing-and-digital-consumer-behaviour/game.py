"""
THE DOPAMINE LOOP
=================
Based on: The Dopamine Economy (2025) — Jain & Mishra

Digital platforms use variable rewards to keep you hooked.
This game simulates a social media feed so you can feel
how unpredictable rewards create compulsive behaviour.
"""

import random
import time

def intro():
    print("=" * 50)
    print("  THE DOPAMINE LOOP")
    print("  A Social Media Simulation")
    print("=" * 50)
    print()
    print("You just posted a photo on a social platform.")
    print("You can CHECK your notifications at any time")
    print("to see if you got new likes, comments, or follows.")
    print()
    print("You have 60 seconds. You can check as often")
    print("or as rarely as you want.")
    print()
    print("Type 'c' to check notifications.")
    print("Type 'q' to quit early and stop checking.")
    print()
    input("Press Enter to start the clock...\n")

def generate_notification():
    """Variable reward schedule — sometimes big, sometimes nothing."""
    roll = random.random()
    if roll < 0.30:
        # Nothing — the empty check
        return None
    elif roll < 0.55:
        # Small reward
        likes = random.randint(1, 3)
        return f"  +{likes} like{'s' if likes > 1 else ''} on your photo"
    elif roll < 0.75:
        # Medium reward
        options = [
            "  Someone commented: 'This is amazing!'",
            "  You got a new follower!",
            "  Someone shared your photo!",
            f"  +{random.randint(5, 12)} likes in the last minute!",
        ]
        return random.choice(options)
    elif roll < 0.90:
        # Big reward
        options = [
            f"  YOUR PHOTO IS TRENDING! +{random.randint(30, 80)} likes!",
            "  A popular account reposted your photo!",
            "  Someone sent you a DM: 'Love your content!'",
        ]
        return random.choice(options)
    else:
        # Jackpot — rare
        return f"  VIRAL! +{random.randint(100, 500)} likes! You're blowing up!"

def run_game():
    intro()

    start_time = time.time()
    duration = 60  # seconds
    checks = []
    total_likes = 0
    rewards_received = 0
    empty_checks = 0

    print(f"  Timer started! You have {duration} seconds.")
    print(f"  Type 'c' to check, 'q' to quit.\n")

    while True:
        elapsed = time.time() - start_time
        remaining = duration - elapsed

        if remaining <= 0:
            print("\n  TIME'S UP!")
            break

        try:
            choice = input(f"  [{int(remaining)}s left] > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            break

        if choice == 'q':
            print("\n  You chose to stop checking. Interesting.")
            break
        elif choice == 'c':
            check_time = time.time() - start_time
            checks.append(check_time)

            # Small delay to simulate loading
            print("  Checking...")
            time.sleep(0.5)

            notification = generate_notification()
            if notification is None:
                empty_checks += 1
                print("  Nothing new.\n")
            else:
                rewards_received += 1
                print(notification)
                print()
        else:
            print("  Type 'c' to check or 'q' to quit.\n")

    # === DEBRIEF ===
    print()
    print("=" * 50)
    print("  YOUR DOPAMINE PROFILE")
    print("=" * 50)
    print()

    total_checks = len(checks)
    actual_duration = min(time.time() - start_time, duration)

    print(f"  Total checks:          {total_checks}")
    print(f"  Time spent:            {int(actual_duration)} seconds")
    if total_checks > 0:
        avg_gap = actual_duration / total_checks
        print(f"  Average gap between:   {avg_gap:.1f} seconds")
        print(f"  Rewarded checks:       {rewards_received} ({int(rewards_received/total_checks*100)}%)")
        print(f"  Empty checks:          {empty_checks} ({int(empty_checks/total_checks*100)}%)")
    print()

    # Analyse checking pattern
    if total_checks >= 2:
        first_half = sum(1 for t in checks if t < actual_duration / 2)
        second_half = total_checks - first_half
        if second_half > first_half:
            print("  PATTERN: You checked MORE as time went on.")
            print("  This is the dopamine loop in action — each")
            print("  reward (or near-miss) pulled you back faster.")
        elif second_half < first_half:
            print("  PATTERN: You checked LESS as time went on.")
            print("  You may have started to notice the pull and")
            print("  consciously resisted. That takes effort.")
        else:
            print("  PATTERN: Your checking rate stayed steady.")

    if total_checks == 0:
        print("  You never checked at all — impressive restraint,")
        print("  or perhaps you saw through the game immediately.")
    elif total_checks >= 10:
        print("  You checked frequently — the variable rewards")
        print("  had you hooked. No shame: the system is designed")
        print("  to do exactly this.")
    print()

    print("  THE SCIENCE:")
    print("  Jain & Mishra (2025) showed that digital platforms")
    print("  exploit variable reward schedules — the same")
    print("  mechanism that makes slot machines addictive.")
    print()
    print("  Your dopamine system doesn't respond to rewards")
    print("  themselves — it responds to the UNCERTAINTY of")
    print("  rewards. That's why 'nothing new' doesn't make")
    print("  you stop checking. The next check MIGHT have")
    print("  something. That 'might' is the hook.")
    print()
    print("  Every time you felt the urge to type 'c' again,")
    print("  that was your dopamine system predicting a reward.")
    print("  Platforms engineer this feeling on purpose.")
    print()

if __name__ == "__main__":
    run_game()
