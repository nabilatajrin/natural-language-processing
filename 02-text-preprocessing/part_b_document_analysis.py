"""
NLP Experiment 01 — Part B
Operations on a document (data/ai_sample.txt)

Steps:
  1. Load text from local file (no Google Drive required)
  2. Lowercase + tokenize
  3. Stopword & punctuation filtering
  4. Lemmatization
  5. Unique token count
  6. Punctuation character count
  7. POS tag distribution (green bar chart)
  8. Unique lemma count
  9. Stopword frequency chart (orange)
 10. Top-10 most frequent content words
 11. Word cloud
"""

from __future__ import annotations

import string
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import nltk
from nltk import FreqDist, pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud

# ---------------------------------------------------------------------------
# NLTK resources
# ---------------------------------------------------------------------------
for resource in (
    "punkt",
    "punkt_tab",
    "averaged_perceptron_tagger",
    "averaged_perceptron_tagger_eng",
    "wordnet",
    "omw-1.4",
    "stopwords",
):
    nltk.download(resource, quiet=True)

DATA_PATH = Path(__file__).resolve().parent / "data" / "ai_sample.txt"


def load_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(
            f"Sample file not found: {path}\n"
            "Place your document at data/ai_sample.txt"
        )
    return path.read_text(encoding="utf-8")


def main() -> None:
    text = load_text(DATA_PATH)
    print("--- Preview (first 500 characters) ---")
    print(text[:500])
    print("...")

    # Preprocessing
    text_lower = text.lower()
    tokens = word_tokenize(text_lower)
    stop_words = set(stopwords.words("english"))

    filtered_tokens = [
        w
        for w in tokens
        if w not in stop_words and w not in string.punctuation and w.strip()
    ]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]

    # 1. Unique tokens (before filtering — matches lab definition)
    unique_tokens = set(tokens)
    print(f"\nNumber of unique tokens: {len(unique_tokens)}")

    # 2. Punctuation characters in original text
    punctuation_count = sum(1 for ch in text if ch in string.punctuation)
    print(f"Number of punctuation characters: {punctuation_count}")

    # 3. POS tag distribution (green)
    pos_tags = pos_tag(filtered_tokens)
    pos_tag_freq = FreqDist(tag for _, tag in pos_tags)

    plt.figure(figsize=(10, 6))
    plt.bar(list(pos_tag_freq.keys()), list(pos_tag_freq.values()), color="green")
    plt.title("Distribution of POS Tags")
    plt.xlabel("POS Tags")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

    # 4. Unique lemmas
    unique_lemmas = set(lemmatized_tokens)
    print(f"Number of unique lemmas: {len(unique_lemmas)}")

    # 5. Stopword distribution (orange)
    stopword_freq = Counter(w for w in tokens if w in stop_words)

    plt.figure(figsize=(12, 6))
    plt.bar(list(stopword_freq.keys()), list(stopword_freq.values()), color="orange")
    plt.xlabel("Stopwords")
    plt.ylabel("Frequency")
    plt.title("Distribution of Stopwords")
    plt.xticks(rotation=90)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

    # 6. Top 10 content words
    word_freq = Counter(filtered_tokens)
    top_words = word_freq.most_common(10)
    print("\nTop 10 Most Frequent Words:")
    for word, freq in top_words:
        print(f"  {word}: {freq}")

    # 7. Word cloud
    wordcloud = WordCloud(
        width=800, height=400, background_color="white"
    ).generate(" ".join(filtered_tokens))

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of Frequent Words")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
