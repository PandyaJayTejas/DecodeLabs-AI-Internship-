# ================================================================
#  SENTIMENT ANALYZER — Keyword-Based Text Analysis Tool
#  Practice Work 2026 | Artificial Intelligence | Project 2
#  Developer : Jay Pandya
#  GitHub    : github.com/PandyaJayTejas
#
#  Concept   : Moves from exact-match (Project 1) to weighted
#              keyword scoring — the bridge toward semantic AI.
# ================================================================

import re
import time

# ── Sentiment Lexicon (weighted keyword dictionaries) ────────────

POSITIVE_WORDS = {
    # Strong positive (weight 2)
    "excellent": 2, "amazing": 2, "outstanding": 2, "fantastic": 2,
    "brilliant": 2, "superb": 2, "perfect": 2, "wonderful": 2,
    # Normal positive (weight 1)
    "good": 1, "great": 1, "happy": 1, "love": 1, "nice": 1,
    "like": 1, "enjoy": 1, "positive": 1, "helpful": 1, "fun": 1,
    "beautiful": 1, "awesome": 1, "cool": 1, "best": 1, "better": 1,
    "fast": 1, "easy": 1, "clean": 1, "useful": 1, "smart": 1,
    "impressive": 1, "recommend": 1, "efficient": 1, "reliable": 1,
}

NEGATIVE_WORDS = {
    # Strong negative (weight 2)
    "terrible": 2, "horrible": 2, "awful": 2, "disgusting": 2,
    "pathetic": 2, "useless": 2, "worst": 2, "hate": 2,
    # Normal negative (weight 1)
    "bad": 1, "poor": 1, "slow": 1, "ugly": 1, "wrong": 1,
    "broken": 1, "difficult": 1, "confusing": 1, "annoying": 1,
    "boring": 1, "frustrating": 1, "disappointing": 1, "waste": 1,
    "sad": 1, "unhappy": 1, "dislike": 1, "problem": 1, "issue": 1,
    "fail": 1, "error": 1, "crash": 1, "weak": 1, "incomplete": 1,
}

# Negation words flip sentiment
NEGATORS = {"not", "no", "never", "neither", "nor", "nothing",
            "nobody", "nowhere", "hardly", "barely", "isn't",
            "aren't", "wasn't", "weren't", "don't", "doesn't",
            "didn't", "won't", "wouldn't", "can't", "couldn't"}


# ── Core Analysis Engine ─────────────────────────────────────────

def tokenize(text: str) -> list:
    """Clean and tokenize input text."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)   # remove punctuation
    return text.split()


def analyze(text: str) -> dict:
    """
    Analyze sentiment of input text.
    Returns score, label, confidence, and breakdown.
    """
    tokens = tokenize(text)

    pos_score  = 0
    neg_score  = 0
    pos_hits   = []
    neg_hits   = []
    negated    = False

    for i, token in enumerate(tokens):
        # Check if previous word was a negator
        if i > 0 and tokens[i - 1] in NEGATORS:
            negated = True
        else:
            negated = False

        if token in POSITIVE_WORDS:
            weight = POSITIVE_WORDS[token]
            if negated:
                neg_score += weight          # flip to negative
                neg_hits.append(f"(negated) {token}")
            else:
                pos_score += weight
                pos_hits.append(token)

        elif token in NEGATIVE_WORDS:
            weight = NEGATIVE_WORDS[token]
            if negated:
                pos_score += weight          # flip to positive
                pos_hits.append(f"(negated) {token}")
            else:
                neg_score += weight
                neg_hits.append(token)

    total = pos_score + neg_score
    net   = pos_score - neg_score

    # ── Sentiment Label ──────────────────────────────────────────
    if net > 2:
        label = "STRONGLY POSITIVE 🟢"
    elif net > 0:
        label = "POSITIVE 🟡"
    elif net == 0 and total == 0:
        label = "NEUTRAL ⚪"
    elif net == 0:
        label = "MIXED ⚪"
    elif net > -2:
        label = "NEGATIVE 🟠"
    else:
        label = "STRONGLY NEGATIVE 🔴"

    # ── Confidence ───────────────────────────────────────────────
    if total == 0:
        confidence = 0.0
    else:
        confidence = round(abs(net) / total * 100, 1)

    return {
        "label"      : label,
        "net_score"  : net,
        "pos_score"  : pos_score,
        "neg_score"  : neg_score,
        "confidence" : confidence,
        "pos_words"  : pos_hits,
        "neg_words"  : neg_hits,
        "word_count" : len(tokens),
    }


def display_result(text: str, result: dict):
    """Pretty-print the analysis report."""
    bar_pos = "█" * result["pos_score"]
    bar_neg = "█" * result["neg_score"]

    print("\n" + "─" * 55)
    print(f"  Input     : {text[:50]}{'...' if len(text)>50 else ''}")
    print(f"  Sentiment : {result['label']}")
    print(f"  Net Score : {result['net_score']:+d}")
    print(f"  Confidence: {result['confidence']}%")
    print(f"  Positive  : {bar_pos or '—'} (+{result['pos_score']})")
    print(f"  Negative  : {bar_neg or '—'} (-{result['neg_score']})")
    if result["pos_words"]:
        print(f"  + Words   : {', '.join(result['pos_words'])}")
    if result["neg_words"]:
        print(f"  - Words   : {', '.join(result['neg_words'])}")
    print("─" * 55)


def batch_mode():
    """Analyze multiple preset texts and show summary."""
    samples = [
        "This product is amazing and works perfectly every time.",
        "Terrible experience. The app crashes and is completely useless.",
        "It is not bad, actually quite helpful for daily tasks.",
        "The weather is okay today.",
        "I hate slow internet but I love this new router, it is fast and brilliant.",
        "The food was horrible and the service was disappointing.",
        "Great quality, fast delivery, highly recommend this product!",
    ]

    print("\n" + "═" * 55)
    print("   BATCH ANALYSIS MODE")
    print("═" * 55)

    results = []
    for text in samples:
        r = analyze(text)
        results.append((text, r))
        display_result(text, r)

    # Summary
    labels = [r["label"] for _, r in results]
    print(f"\n  SUMMARY: {len(samples)} texts analyzed")
    print(f"  Positive  : {sum(1 for l in labels if 'POSITIVE' in l)}")
    print(f"  Negative  : {sum(1 for l in labels if 'NEGATIVE' in l)}")
    print(f"  Neutral   : {sum(1 for l in labels if 'NEUTRAL' in l or 'MIXED' in l)}")
    print("═" * 55 + "\n")


# ── Main Interactive Loop ─────────────────────────────────────────

def main():
    print("\n" + "═" * 55)
    print("   SENTIMENT ANALYZER")
    print("   Practice Work 2026  |  Built by Jay Pandya")
    print("═" * 55)
    print("   Type any text to analyze its sentiment.")
    print("   Commands: 'batch' | 'exit'")
    print("═" * 55 + "\n")

    while True:
        try:
            raw = input("Enter text → ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting Sentiment Analyzer. Goodbye!\n")
            break

        if not raw:
            continue

        if raw.lower() in {"exit", "quit", "q"}:
            print("Exiting Sentiment Analyzer. Goodbye!\n")
            break

        if raw.lower() == "batch":
            batch_mode()
            continue

        result = analyze(raw)
        display_result(raw, result)


if __name__ == "__main__":
    main()
