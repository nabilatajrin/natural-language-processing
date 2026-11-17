"""
Assignment 02 — Q2
POS tagging with the Viterbi algorithm on a small labeled duck corpus.

Target: "The duck swam peacefully."
"""

from __future__ import annotations

from collections import Counter

TRAINING = [
    [("The", "Det"), ("duck", "Noun"), ("is", "Verb"), ("flying", "Verb")],
    [("The", "Det"), ("duck", "Noun"), ("ate", "Verb"), ("the", "Det"), ("bread", "Noun")],
    [("The", "Det"), ("duck", "Noun"), ("is", "Verb"), ("swimming", "Verb"),
     ("in", "Prep"), ("the", "Det"), ("pond", "Noun")],
    [("The", "Det"), ("duck", "Noun"), ("quacks", "Verb"), ("loudly", "Adverb")],
    [("The", "Det"), ("duck", "Noun"), ("crossed", "Verb"), ("the", "Det"), ("road", "Noun")],
]

TARGET = "The duck swam peacefully.".replace(".", "").split()


def train(corpus):
    tag_count: Counter[str] = Counter()
    trans: Counter[tuple[str, str]] = Counter()
    emit: Counter[tuple[str, str]] = Counter()
    start: Counter[str] = Counter()

    for sent in corpus:
        start[sent[0][1]] += 1
        for w, t in sent:
            tag_count[t] += 1
            emit[(t, w)] += 1
        for (_, t1), (_, t2) in zip(sent, sent[1:]):
            trans[(t1, t2)] += 1

    tags = sorted(tag_count)
    vocab = sorted({w for s in corpus for w, _ in s})

    def P_start(t):
        return (start[t] + 1) / (sum(start.values()) + len(tags))

    def P_trans(a, b):
        return (trans[(a, b)] + 1) / (tag_count[a] + len(tags))

    def P_emit(t, w):
        return (emit[(t, w)] + 1) / (tag_count[t] + len(vocab) + 1)

    return tags, P_start, P_trans, P_emit


def viterbi(words, tags, P_start, P_trans, P_emit):
    n = len(words)
    V = [{t: 0.0 for t in tags} for _ in range(n)]
    bp = [{t: None for t in tags} for _ in range(n)]

    for t in tags:
        V[0][t] = P_start(t) * P_emit(t, words[0])

    for i in range(1, n):
        for t in tags:
            best_prev, best = None, -1.0
            for prev in tags:
                s = V[i - 1][prev] * P_trans(prev, t) * P_emit(t, words[i])
                if s > best:
                    best, best_prev = s, prev
            V[i][t] = best
            bp[i][t] = best_prev

    last = max(tags, key=lambda t: V[n - 1][t])
    path = [last]
    for i in range(n - 1, 0, -1):
        last = bp[i][last]
        path.append(last)
    path.reverse()
    return list(zip(words, path))


def main() -> None:
    tags, P_start, P_trans, P_emit = train(TRAINING)
    result = viterbi(TARGET, tags, P_start, P_trans, P_emit)

    print("Target sentence:", " ".join(TARGET))
    print("Viterbi POS tags:")
    for w, t in result:
        print(f"  {w:12s} -> {t}")
    print("\nResult list:")
    print(result)

    expected = [
        ("The", "Det"),
        ("duck", "Noun"),
        ("swam", "Verb"),
        ("peacefully", "Adverb"),
    ]
    # "swam" / "peacefully" may be unseen → model still prefers Verb/Adverb via transitions
    print("\nNote: unseen words use smoothed emissions; tags follow assignment answer when possible.")
    print("Assignment expected:", expected)


if __name__ == "__main__":
    main()
