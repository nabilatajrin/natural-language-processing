"""
Assignment 02 — Q1
POS tagging with a simple Hidden Markov Model (HMM).

Training corpus = labeled sentences from the assignment sheet.
Target sentence: "The dog barked loudly at the cat."
"""

from __future__ import annotations

from collections import Counter, defaultdict

# ---------- Training data (assignment Q1) ----------
TRAINING = [
    [("The", "Det"), ("cat", "Noun"), ("chased", "Verb"), ("the", "Det"), ("mouse", "Noun")],
    [("The", "Det"), ("mouse", "Noun"), ("ran", "Verb"), ("away", "Adverb"), ("quickly", "Adverb")],
    [("The", "Det"), ("dog", "Noun"), ("barked", "Verb"), ("loudly", "Adverb"),
     ("at", "Prep"), ("the", "Det"), ("mouse", "Noun")],
    [("The", "Det"), ("mouse", "Noun"), ("hid", "Verb"), ("behind", "Prep"),
     ("the", "Det"), ("chair", "Noun")],
    [("The", "Det"), ("cat", "Noun"), ("slept", "Verb"), ("peacefully", "Adverb"),
     ("on", "Prep"), ("the", "Det"), ("chair", "Noun")],
]

TARGET = "The dog barked loudly at the cat.".replace(".", "").split()


def train_hmm(corpus: list[list[tuple[str, str]]]):
    """Estimate transition and emission counts (MLE, add-one smoothed lightly)."""
    tag_count: Counter[str] = Counter()
    trans: Counter[tuple[str, str]] = Counter()
    emit: Counter[tuple[str, str]] = Counter()
    start: Counter[str] = Counter()

    for sent in corpus:
        if not sent:
            continue
        start[sent[0][1]] += 1
        for word, tag in sent:
            tag_count[tag] += 1
            emit[(tag, word)] += 1
        for (w1, t1), (w2, t2) in zip(sent, sent[1:]):
            trans[(t1, t2)] += 1

    tags = sorted(tag_count)
    vocab = sorted({w for sent in corpus for w, _ in sent})

    def P_start(t: str) -> float:
        return (start[t] + 1) / (sum(start.values()) + len(tags))

    def P_trans(t1: str, t2: str) -> float:
        return (trans[(t1, t2)] + 1) / (tag_count[t1] + len(tags))

    def P_emit(tag: str, word: str) -> float:
        # Unknown words: uniform over tags (tiny mass)
        return (emit[(tag, word)] + 1) / (tag_count[tag] + len(vocab) + 1)

    return tags, P_start, P_trans, P_emit


def viterbi_tag(words: list[str], tags, P_start, P_trans, P_emit):
    """Standard Viterbi decode for HMM POS."""
    n = len(words)
    V = [{t: 0.0 for t in tags} for _ in range(n)]
    bp = [{t: None for t in tags} for _ in range(n)]

    for t in tags:
        V[0][t] = P_start(t) * P_emit(t, words[0])

    for i in range(1, n):
        for t in tags:
            best_prev, best_score = None, -1.0
            for prev in tags:
                score = V[i - 1][prev] * P_trans(prev, t) * P_emit(t, words[i])
                if score > best_score:
                    best_score, best_prev = score, prev
            V[i][t] = best_score
            bp[i][t] = best_prev

    last = max(tags, key=lambda t: V[n - 1][t])
    path = [last]
    for i in range(n - 1, 0, -1):
        last = bp[i][last]
        path.append(last)
    path.reverse()
    return list(zip(words, path))


def main() -> None:
    tags, P_start, P_trans, P_emit = train_hmm(TRAINING)
    result = viterbi_tag(TARGET, tags, P_start, P_trans, P_emit)

    print("Target sentence:", " ".join(TARGET))
    print("HMM POS tags:")
    for w, t in result:
        print(f"  {w:12s} -> {t}")
    print("\nResult list:")
    print(result)

    # Assignment expected answer
    expected = [
        ("The", "Det"),
        ("dog", "Noun"),
        ("barked", "Verb"),
        ("loudly", "Adverb"),
        ("at", "Prep"),
        ("the", "Det"),
        ("cat", "Noun"),
    ]
    print("\nMatches assignment answer:", result == expected)


if __name__ == "__main__":
    main()
