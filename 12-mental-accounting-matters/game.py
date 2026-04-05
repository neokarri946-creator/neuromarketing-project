"""
THE MENTAL ACCOUNTS GAME
Based on: Mental Accounting Matters (1999) — Thaler

Money is money... or is it? This game shows how your brain
puts money into invisible buckets and treats identical amounts
completely differently depending on the label.
"""

import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def intro():
    clear()
    print("=" * 55)
    print("  THE MENTAL ACCOUNTS GAME")
    print("=" * 55)
    print()
    print("  You'll face spending scenarios.")
    print("  In each one, you decide what to do with money.")
    print()
    print("  There are no wrong answers — but your choices")
    print("  will reveal something surprising about how your")
    print("  brain secretly categorises cash.")
    print()
    input("Press Enter to begin... ")

def ask(question, options):
    """Ask a question with lettered options. Return the chosen letter."""
    print()
    print(question)
    print()
    letters = []
    for letter, text in options:
        print(f"  [{letter}] {text}")
        letters.append(letter)
    print()
    while True:
        choice = input("  Your choice: ").strip().upper()
        if choice in letters:
            return choice
        print(f"  Please type one of: {', '.join(letters)}")

def run_game():
    intro()

    results = []

    # --- SCENARIO 1: Lost ticket vs lost cash ---
    clear()
    print("  SCENARIO 1 of 6")
    print("=" * 55)
    print()
    print("  You're going to see a film that costs £12.")
    print("  You arrive at the cinema and discover you've")
    print("  LOST a £12 note from your wallet on the way.")
    print()
    c1a = ask("Do you still buy a ticket?",
              [("A", "Yes, I'll still buy the ticket"),
               ("B", "No, I'll skip the film")])

    clear()
    print("  SCENARIO 2 of 6")
    print("=" * 55)
    print()
    print("  You're going to see a film. You bought a £12")
    print("  ticket in advance. You arrive at the cinema")
    print("  and discover you've LOST THE TICKET.")
    print()
    c1b = ask("Do you buy another ticket for £12?",
              [("A", "Yes, I'll buy another ticket"),
               ("B", "No, I'll skip the film")])

    results.append(("ticket_vs_cash", c1a, c1b))

    # --- SCENARIO 3: Windfall spending ---
    clear()
    print("  SCENARIO 3 of 6")
    print("=" * 55)
    print()
    print("  You worked overtime this week and earned an")
    print("  extra £200 on top of your normal salary.")
    print()
    c2a = ask("What do you do with the extra £200?",
              [("A", "Save it or put it toward bills"),
               ("B", "Treat yourself — you earned it"),
               ("C", "Spend some, save some")])

    clear()
    print("  SCENARIO 4 of 6")
    print("=" * 55)
    print()
    print("  You find £200 in a jacket you haven't worn")
    print("  in months. You'd completely forgotten about it.")
    print()
    c2b = ask("What do you do with the found £200?",
              [("A", "Save it or put it toward bills"),
               ("B", "Treat yourself — it's free money!"),
               ("C", "Spend some, save some")])

    results.append(("windfall_vs_earned", c2a, c2b))

    # --- SCENARIO 5: Budget compartments ---
    clear()
    print("  SCENARIO 5 of 6")
    print("=" * 55)
    print()
    print("  You budgeted £100 for eating out this month.")
    print("  You've spent £95 so far. A friend invites you")
    print("  to a restaurant — the meal will cost about £30.")
    print()
    print("  You still have £400 unspent in your general")
    print("  savings this month.")
    print()
    c3a = ask("Do you go?",
              [("A", "No — I've used up my eating-out budget"),
               ("B", "Yes — I'll take it from general savings"),
               ("C", "Yes — budgets are guidelines, not walls")])

    # --- SCENARIO 6: Sunk cost ---
    clear()
    print("  SCENARIO 6 of 6")
    print("=" * 55)
    print()
    print("  You paid £50 for a concert ticket weeks ago.")
    print("  Tonight is the concert, but it's freezing cold,")
    print("  you're tired, and you don't really feel like going.")
    print()
    print("  A friend offers you a free ticket to a different,")
    print("  closer event that you'd actually enjoy more.")
    print()
    c3b = ask("What do you do?",
              [("A", "Go to the concert — I already paid £50"),
               ("B", "Go to the free event I'd enjoy more"),
               ("C", "Stay home")])

    results.append(("budget_and_sunk", c3a, c3b))

    # --- DEBRIEF ---
    clear()
    print("=" * 55)
    print("  YOUR MENTAL ACCOUNTING REVEALED")
    print("=" * 55)

    # Analyse ticket vs cash
    ticket_cash = results[0]
    print()
    print("  LOST CASH vs LOST TICKET")
    print("  " + "-" * 40)
    if ticket_cash[1] == "A" and ticket_cash[2] == "B":
        print("  You'd still see the film after losing £12 cash,")
        print("  but NOT after losing a £12 ticket.")
        print()
        print("  >> This is classic mental accounting! Losing cash")
        print("  comes from your 'general' account, but losing the")
        print("  ticket doubles the cost in your 'entertainment'")
        print("  account. The financial loss is identical — £12 —")
        print("  but your brain treats them completely differently.")
    elif ticket_cash[1] == ticket_cash[2]:
        print("  You treated both situations the same way.")
        print()
        print("  >> Interesting! Most people treat them differently.")
        print("  Losing cash feels like a general loss, but losing")
        print("  a ticket feels like the film now costs £24.")
        print("  You seem to resist this mental accounting bias.")
    else:
        print(f"  Lost cash: {'buy ticket' if ticket_cash[1] == 'A' else 'skip'}")
        print(f"  Lost ticket: {'buy again' if ticket_cash[2] == 'A' else 'skip'}")
        print()
        print("  >> Your mental accounts influenced these choices.")
        print("  Thaler found most people will buy after losing cash")
        print("  but refuse to buy after losing the ticket — even")
        print("  though both situations leave you £12 poorer.")

    # Analyse windfall vs earned
    windfall = results[1]
    print()
    print("  EARNED MONEY vs FOUND MONEY")
    print("  " + "-" * 40)
    if windfall[1] != windfall[2]:
        print(f"  Overtime £200: {'Save' if windfall[1] == 'A' else 'Spend' if windfall[1] == 'B' else 'Mix'}")
        print(f"  Found £200:    {'Save' if windfall[2] == 'A' else 'Spend' if windfall[2] == 'B' else 'Mix'}")
        print()
        print("  >> You treated identical amounts differently based")
        print("  on WHERE the money came from. Earned money goes")
        print("  into a 'serious' mental account. Found money goes")
        print("  into a 'free money' account. But £200 is £200.")
    else:
        print("  You treated both the same way.")
        print()
        print("  >> Most people spend 'found' money more freely")
        print("  than 'earned' money, even though £200 is £200")
        print("  regardless of its source.")

    # Analyse budget / sunk cost
    budget_sunk = results[2]
    print()
    print("  BUDGET WALLS & SUNK COSTS")
    print("  " + "-" * 40)
    if budget_sunk[1] == "A":
        print("  You refused the meal because the eating-out")
        print("  budget was spent — even with £400 elsewhere.")
        print()
        print("  >> This shows rigid mental account boundaries.")
        print("  The money exists, but your brain won't move it")
        print("  across the invisible wall between accounts.")
    else:
        print("  You were willing to move money between accounts.")
        print()
        print("  >> You're more flexible than most. Many people")
        print("  treat budget categories as hard walls, refusing")
        print("  to 'borrow' between them even when it makes sense.")

    if budget_sunk[2] == "A":
        print()
        print("  You went to the paid concert even though you'd")
        print("  enjoy the free event more — classic sunk cost!")
        print("  The £50 is gone either way, but your 'concert")
        print("  account' demands you get your money's worth.")

    print()
    print("=" * 55)
    print("  THE SCIENCE")
    print("=" * 55)
    print()
    print("  Thaler (1999) showed that we don't have one big")
    print("  pile of money in our heads. We have many small pots:")
    print("  'food money,' 'fun money,' 'windfall money,' etc.")
    print()
    print("  Marketers exploit this by framing purchases to")
    print("  target the right account. Gift cards move money")
    print("  into a 'spending' account. 'Treat yourself' ads")
    print("  target windfall accounts. Bundles merge multiple")
    print("  account hits into one, reducing total pain.")
    print()
    print("  A pound is a pound — but your brain disagrees.")
    print()
    input("Press Enter to exit... ")

if __name__ == "__main__":
    run_game()
