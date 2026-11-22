"""
Experiment 05 — Bag of Words and TF-IDF
"""
from __future__ import annotations
import math
from collections import Counter
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

DOCS = [
    "NLP is a theoretical subject",
    "NLP is interesting subject",
    "Solve the given problem",
]
DOC_IDS = ["D1", "D2", "D3"]

def tokenize(text: str) -> list[str]:
    return text.lower().split()

def build_vocab(docs: list[str]) -> list[str]:
    vocab: set[str] = set()
    for d in docs:
        vocab.update(tokenize(d))
    return sorted(vocab)

def bow_matrix(docs: list[str], vocab: list[str]) -> np.ndarray:
    index = {w: i for i, w in enumerate(vocab)}
    X = np.zeros((len(docs), len(vocab)), dtype=float)
    for i, d in enumerate(docs):
        counts = Counter(tokenize(d))
        for w, c in counts.items():
            X[i, index[w]] = c
    return X

def tf_matrix(bow: np.ndarray) -> np.ndarray:
    lengths = bow.sum(axis=1, keepdims=True)
    lengths[lengths == 0] = 1.0
    return bow / lengths

def idf_vector(bow: np.ndarray) -> np.ndarray:
    n_docs = bow.shape[0]
    df = (bow > 0).sum(axis=0)
    return np.array([math.log(n_docs / df_t) if df_t else 0.0 for df_t in df])

def print_matrix(title: str, matrix: np.ndarray, vocab: list[str], rows: list[str]) -> None:
    print("\n" + title)
    header = f"{'':4}" + " ".join(f"{w[:8]:>8}" for w in vocab)
    print(header)
    for name, row in zip(rows, matrix):
        print(f"{name:4}" + " ".join(f"{v:8.3f}" for v in row))

def main() -> None:
    vocab = build_vocab(DOCS)
    print("Vocabulary:", vocab)
    bow = bow_matrix(DOCS, vocab)
    print_matrix("Bag of Words (raw counts)", bow, vocab, DOC_IDS)
    tf = tf_matrix(bow)
    print_matrix("Term Frequency (count / doc length)", tf, vocab, DOC_IDS)
    idf = idf_vector(bow)
    print("\nIDF per term:")
    for w, v in zip(vocab, idf):
        print(f"  {w:15s} {v:.4f}")
    tfidf = tf * idf
    print_matrix("TF-IDF (from scratch)", tfidf, vocab, DOC_IDS)
    print("\n" + "=" * 60)
    print("sklearn CountVectorizer")
    cv = CountVectorizer(token_pattern=r"(?u)\b\w+\b")
    print(cv.fit_transform(DOCS).toarray())
    print("\nsklearn TfidfVectorizer")
    tv = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
    print(np.round(tv.fit_transform(DOCS).toarray(), 3))

if __name__ == "__main__":
    main()
