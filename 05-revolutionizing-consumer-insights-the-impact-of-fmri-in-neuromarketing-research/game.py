"""
Brain Region Matching Game — Interactive Experience
Based on Alsharif et al. (2024)

Learn the neural geography of consumer decisions.
Match consumer scenarios to the brain regions most involved.
"""

import random

BRAIN_REGIONS = {
    "NAcc": {
        "full_name": "Nucleus Accumbens (Ventral Striatum)",
        "role": "Anticipation of reward, desire, wanting. Fires when you see something you crave before you get it.",
        "analogy": "The 'I WANT that' signal.",
    },
    "INS": {
        "full_name": "Insula",
        "role": "Negative arousal, disgust, pain of paying. Fires when prices feel too high or something feels wrong.",
        "analogy": "The 'ouch, that hurts' alarm.",
    },
    "mPFC": {
        "full_name": "Medial Prefrontal Cortex",
        "role": "Value computation, weighing options, integrating desire against cost to reach a decision.",
        "analogy": "The 'is it worth it?' calculator.",
    },
    "AMY": {
        "full_name": "Amygdala",
        "role": "Emotional memory and associations. Processes fear, excitement, and emotional connections to brands.",
        "analogy": "The 'this makes me FEEL something' centre.",
    },
    "OFC": {
        "full_name": "Orbitofrontal Cortex",
        "role": "Experienced pleasantness, subjective reward value. Encodes how good something actually feels during consumption.",
        "analogy": "The 'mmm, that's nice' experience encoder.",
    },
}

SCENARIOS = [
    {
        "situation": "You see a teaser trailer for a product launching next month. Your heart races with excitement about what's coming.",
        "answer": "NAcc",
        "explanation": "The nucleus accumbens drives anticipation of future rewards. The excitement of 'what's coming' is pure wanting — and it's often stronger than the reward itself (Knutson et al., 2001).",
    },
    {
        "situation": "You flip over the price tag on a jacket you love and see it costs £450. You feel a sharp pang in your gut.",
        "answer": "INS",
        "explanation": "The insula fires when prices feel painful. That gut-punch feeling is real — it's the same region that processes physical disgust. Knutson et al. (2007) showed this 'price pain' signal predicts when people won't buy.",
    },
    {
        "situation": "You're comparing two phones — one costs more but has a better camera. You're mentally weighing whether the upgrade is worth the extra £200.",
        "answer": "mPFC",
        "explanation": "The medial prefrontal cortex integrates value signals — comparing the benefit of the camera against the cost of £200. It's your brain's cost-benefit calculator.",
    },
    {
        "situation": "A charity advert shows images of suffering children with emotional music. You feel a powerful emotional response that makes you want to donate.",
        "answer": "AMY",
        "explanation": "The amygdala processes strong emotional responses — especially those triggered by vivid emotional imagery. Advertisers target this region when they use emotional storytelling.",
    },
    {
        "situation": "You take a sip of wine that a friend told you costs £80. It tastes absolutely wonderful — rich and complex.",
        "answer": "OFC",
        "explanation": "The orbitofrontal cortex encodes experienced pleasantness. Plassmann et al. (2008) showed that price information changes actual OFC activation — the brain literally experiences more pleasure when it believes something is premium.",
    },
    {
        "situation": "You spot the Nike swoosh on a pair of trainers. Instantly, feelings of athletic aspiration and cool factor wash over you — before you even try them on.",
        "answer": "AMY",
        "explanation": "The amygdala stores emotional associations built up over years of brand exposure. That instant emotional reaction to a logo is learned emotional memory, not rational assessment.",
    },
    {
        "situation": "A subscription service wants £14.99/month. You think: 'That's about 50p a day... actually, that's not bad for what I get.'",
        "answer": "mPFC",
        "explanation": "The mPFC is doing value reframing — breaking down the price to make it feel proportional to the benefit. This is active valuation and comparison, the mPFC's core job.",
    },
    {
        "situation": "You browse a luxury website and add items to your basket. The total climbs to £1,200. You feel physically uncomfortable and close the tab.",
        "answer": "INS",
        "explanation": "That physical discomfort is the insula sounding the alarm. Large totals trigger stronger insula activation than individual small prices — which is why 'buy now, pay later' reduces this signal by hiding the total.",
    },
    {
        "situation": "You're eating your favourite meal. With each bite, you savour the flavour and feel deep satisfaction.",
        "answer": "OFC",
        "explanation": "The orbitofrontal cortex encodes moment-to-moment experienced pleasure during consumption. It's tracking how good each bite actually feels — your brain's real-time satisfaction meter.",
    },
    {
        "situation": "A countdown timer on a deal page reads '2 hours left.' You feel a surge of urgency and excitement — you might miss out.",
        "answer": "NAcc",
        "explanation": "Countdown timers exploit the nucleus accumbens by creating urgent anticipation. The scarcity signal amplifies wanting — your brain treats the narrowing window as an intensifying reward signal.",
    },
]


def show_intro():
    print("=" * 58)
    print("  BRAIN REGION MATCHING GAME")
    print("  Based on Alsharif et al. (2024)")
    print("=" * 58)
    print()
    print("  Consumer decisions involve a network of brain regions,")
    print("  each playing a different role.")
    print()
    print("  You'll see consumer scenarios and match each one")
    print("  to the brain region MOST involved.")
    print()
    print("  First, meet the key players:")
    print()

    for code, info in BRAIN_REGIONS.items():
        print(f"  [{code}] {info['full_name']}")
        print(f"         {info['analogy']}")
        print()

    input("  Press Enter when you're ready...\n")


def get_answer():
    valid = list(BRAIN_REGIONS.keys())
    while True:
        ans = input("  Your answer (NAcc/INS/mPFC/AMY/OFC): ").strip().upper()
        # Normalise common variations
        if ans in ("NACC", "NA", "NUCLEUS"):
            return "NAcc"
        if ans in ("INS", "INSULA", "IN"):
            return "INS"
        if ans in ("MPFC", "PFC", "MP", "MEDIAL"):
            return "mPFC"
        if ans in ("AMY", "AMYGDALA", "AM"):
            return "AMY"
        if ans in ("OFC", "ORBITO", "OR"):
            return "OFC"
        print(f"  Choose from: {', '.join(valid)}")


def word_wrap(text, width=54, indent="  "):
    words = text.split()
    lines = []
    line = indent
    for word in words:
        if len(line) + len(word) + 1 > width:
            lines.append(line)
            line = indent + word
        else:
            line += (" " + word) if line.strip() else (indent + word)
    if line.strip():
        lines.append(line)
    return "\n".join(lines)


def main():
    show_intro()

    selected = random.sample(SCENARIOS, 7)
    score = 0
    region_scores = {code: {"correct": 0, "seen": 0} for code in BRAIN_REGIONS}

    for i, scenario in enumerate(selected, 1):
        print(f"{'─' * 58}")
        print(f"  SCENARIO {i}/7")
        print(f"{'─' * 58}")
        print()
        print(word_wrap(scenario["situation"]))
        print()

        # Show quick reference
        print("  Brain regions: NAcc | INS | mPFC | AMY | OFC")
        print()

        answer = get_answer()
        correct_code = scenario["answer"]
        region_scores[correct_code]["seen"] += 1

        if answer == correct_code:
            region = BRAIN_REGIONS[correct_code]
            print(f"\n  ✓ CORRECT — {region['full_name']}")
            score += 1
            region_scores[correct_code]["correct"] += 1
        else:
            region = BRAIN_REGIONS[correct_code]
            your_region = BRAIN_REGIONS[answer]
            print(f"\n  ✗ The answer was [{correct_code}] {region['full_name']}")
            print(f"    You picked [{answer}] — {your_region['analogy']}")

        print()
        print(word_wrap(scenario["explanation"]))
        print()

        if i < 7:
            input("  Press Enter for the next scenario...\n")

    # Debrief
    print("\n" + "=" * 58)
    print(f"  FINAL SCORE: {score}/7")
    print("=" * 58)

    if score >= 6:
        print("\n  Outstanding — you've mapped the neural geography well.")
    elif score >= 4:
        print("\n  Good foundation — the brain network is complex,")
        print("  and you're getting the key distinctions.")
    else:
        print("\n  Tricky, isn't it? Brain regions overlap and interact.")
        print("  That's exactly why neuromarketing is hard to do well.")

    print()
    print("  YOUR BRAIN REGION SCORECARD:")
    for code, info in BRAIN_REGIONS.items():
        data = region_scores[code]
        if data["seen"] > 0:
            status = f"{data['correct']}/{data['seen']} correct"
        else:
            status = "not tested"
        print(f"  [{code}] {info['full_name']:<40} {status}")

    print()
    print("  KEY INSIGHT from Alsharif et al. (2024):")
    print()
    print("  Consumer decisions don't happen in one brain spot.")
    print("  They emerge from NETWORKS of regions working together:")
    print()
    print("  • NAcc fires up desire (wanting)")
    print("  • INS signals price pain (aversion)")
    print("  • mPFC weighs the trade-off (is it worth it?)")
    print("  • AMY adds emotional colour (brand feelings)")
    print("  • OFC encodes actual pleasure (consumption)")
    print()
    print("  fMRI has mapped these roles reliably — but the")
    print("  real insight is that every purchase is a whole-brain")
    print("  event, not a single 'buy button.'")
    print()
    print("  The future of neuromarketing lies in understanding")
    print("  these networks, not hunting for magic brain spots.")
    print()


if __name__ == "__main__":
    main()
