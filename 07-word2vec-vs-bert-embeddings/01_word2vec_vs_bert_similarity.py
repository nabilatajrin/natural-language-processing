"""
Experiment 07 — Part A
Compare Word2Vec (static, averaged) vs transformer sentence embeddings
on semantic similarity (cosine).

Pairs from the lab sheet:
  - "I love AI" vs "AI is my passion"
  - "Dogs are cute" vs "I adore puppies"
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from gensim.models import Word2Vec
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

IMAGES = Path(__file__).resolve().parent / "images"
IMAGES.mkdir(exist_ok=True)

PAIRS = [
    ("I love AI", "AI is my passion"),
    ("Dogs are cute", "I adore puppies"),
]

# Extra sentences so a tiny Word2Vec sees related vocabulary
EXTRA_CORPUS = [
    "I love artificial intelligence and machine learning",
    "AI is my passion and I study deep learning",
    "Dogs are cute and friendly pets",
    "I adore puppies and dogs",
    "Natural language processing with embeddings",
    "Semantic similarity between sentences",
]


def tokenize(text: str) -> list[str]:
    return text.lower().replace(".", "").split()


def train_word2vec(sentences: list[str]) -> Word2Vec:
    tokens = [tokenize(s) for s in sentences]
    model = Word2Vec(
        sentences=tokens,
        vector_size=50,
        window=3,
        min_count=1,
        workers=1,
        seed=42,
        epochs=50,
    )
    return model


def sentence_vec_w2v(model: Word2Vec, text: str) -> np.ndarray:
    vecs = [model.wv[w] for w in tokenize(text) if w in model.wv]
    if not vecs:
        return np.zeros(model.vector_size)
    return np.mean(vecs, axis=0)


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    a = a.reshape(1, -1)
    b = b.reshape(1, -1)
    return float(cosine_similarity(a, b)[0, 0])


def main() -> None:
    # --- Word2Vec (small in-domain model; not Google-News) ---
    corpus = [s for pair in PAIRS for s in pair] + EXTRA_CORPUS
    w2v = train_word2vec(corpus)

    # --- Transformer sentence embedding ---
    print("Loading sentence-transformers model (first run downloads weights)...")
    st_model = SentenceTransformer("all-MiniLM-L6-v2")

    print("\n{:<45} {:>10} {:>10} {:>10}".format(
        "Sentence pair", "Word2Vec", "MiniLM", "Better"
    ))
    print("-" * 80)

    for s1, s2 in PAIRS:
        w_score = cosine(sentence_vec_w2v(w2v, s1), sentence_vec_w2v(w2v, s2))
        e1 = st_model.encode(s1)
        e2 = st_model.encode(s2)
        t_score = cosine(e1, e2)
        better = "MiniLM" if t_score >= w_score else "Word2Vec"
        label = f'"{s1}" / "{s2}"'
        print(f"{label:<45} {w_score:>10.3f} {t_score:>10.3f} {better:>10}")

    print(
        "\nLab report (Google-News W2V + BERT) reported ~0.65/0.70 vs ~0.89/0.91; "
        "MiniLM should also beat the tiny Word2Vec on these pairs."
    )


if __name__ == "__main__":
    main()
