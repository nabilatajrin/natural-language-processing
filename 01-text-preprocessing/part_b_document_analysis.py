"""Experiment 01 — Part B: document-level analysis."""
from __future__ import annotations

import string
from collections import Counter
from pathlib import Path

import nltk
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

for r in ("punkt", "punkt_tab", "averaged_perceptron_tagger",
          "averaged_perceptron_tagger_eng", "stopwords"):
    nltk.download(r, quiet=True)

DATA = Path(__file__).resolve().parent / "data" / "ai_sample.txt"


def main() -> None:
    text = DATA.read_text(encoding="utf-8").lower()
    tokens = word_tokenize(text)
    words = [t for t in tokens if t.isalpha()]
    stop = set(stopwords.words("english"))
    content = [w for w in words if w not in stop]
    print("Total tokens:", len(tokens))
    print("Content words:", len(content))
    print("Top 15:", Counter(content).most_common(15))
    print("POS sample:", pos_tag(content[:20]))


if __name__ == "__main__":
    main()
