"""
NLP Experiment 01 — Part A
Operations on a Single Sentence

Saves charts to images/ and shows them on screen.
"""

from __future__ import annotations

import re
import string
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # works headless; still opens windows if backend allows
import matplotlib.pyplot as plt
import nltk
import seaborn as sns
from nltk import pos_tag
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

IMAGES = Path(__file__).resolve().parent / "images"
IMAGES.mkdir(exist_ok=True)

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


def get_wordnet_pos(tag: str) -> str:
    if tag.startswith("J"):
        return wordnet.ADJ
    if tag.startswith("V"):
        return wordnet.VERB
    if tag.startswith("N"):
        return wordnet.NOUN
    if tag.startswith("R"):
        return wordnet.ADV
    return wordnet.NOUN


def preprocess_sentence(sentence: str) -> dict:
    text = sentence.strip().lower()
    text = re.sub(
        r"\b(marks|teacher'?s signature with date|expt\.?\s*\d+-\d+|www\.\S+)\b",
        "",
        text,
        flags=re.IGNORECASE,
    )
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [
        w for w in tokens if w not in stop_words and w not in string.punctuation and w.strip()
    ]
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(w) for w in filtered_tokens]
    lemmatizer = WordNetLemmatizer()
    tagged = pos_tag(filtered_tokens)
    lemmatized_tokens = [
        lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in tagged
    ]
    return {
        "original": sentence,
        "tokens": tokens,
        "filtered": filtered_tokens,
        "stemmed": stemmed_tokens,
        "lemmatized": lemmatized_tokens,
        "pos_tags": tagged,
    }


def save_and_show(path: Path) -> None:
    plt.tight_layout()
    plt.savefig(path, dpi=120, bbox_inches="tight")
    print(f"Saved: {path}")
    try:
        plt.show()
    except Exception:
        pass
    plt.close()


def plot_word_frequency(tokens: list[str]) -> None:
    counts = Counter(tokens)
    labels, values = list(counts.keys()), list(counts.values())
    plt.figure(figsize=(10, 5))
    sns.barplot(x=labels, y=values, hue=labels, palette="viridis", legend=False)
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Word Frequency Distribution")
    plt.xticks(rotation=45, ha="right")
    save_and_show(IMAGES / "01_word_frequency.png")


def plot_pos_pie(pos_tags: list[tuple[str, str]]) -> None:
    pos_counts = Counter(tag for _, tag in pos_tags)
    plt.figure(figsize=(7, 7))
    plt.pie(
        pos_counts.values(),
        labels=pos_counts.keys(),
        autopct="%1.1f%%",
        colors=sns.color_palette("Set2"),
    )
    plt.title("POS Tag Distribution")
    save_and_show(IMAGES / "02_pos_pie.png")


def plot_ngrams(tokens: list[str], n: int, title: str, palette: str, filename: str) -> None:
    grams = list(ngrams(tokens, n))
    if not grams:
        print(f"No {n}-grams to plot.")
        return
    counts = Counter(grams)
    labels = [" ".join(g) for g in counts.keys()]
    values = list(counts.values())
    plt.figure(figsize=(10, 5))
    sns.barplot(x=labels, y=values, hue=labels, palette=palette, legend=False)
    plt.xlabel(f"{n}-grams")
    plt.ylabel("Frequency")
    plt.title(title)
    plt.xticks(rotation=45, ha="right")
    save_and_show(IMAGES / filename)


def main() -> None:
    sentence = (
        "Artificial intelligence (AI) is transforming industries by enabling "
        "machines to learn from data, automate tasks, and make intelligent decisions."
    )
    result = preprocess_sentence(sentence)

    print("Original Sentence:", result["original"])
    print("Tokenized Words:", result["tokens"])
    print("Filtered Tokens:", result["filtered"])
    print("Stemmed Tokens:", result["stemmed"])
    print("Lemmatized Tokens:", result["lemmatized"])

    plot_word_frequency(result["filtered"])
    plot_pos_pie(result["pos_tags"])
    plot_ngrams(result["filtered"], 2, "Bigram Frequency Distribution", "magma", "03_bigrams.png")
    plot_ngrams(result["filtered"], 3, "Trigram Frequency Distribution", "coolwarm", "04_trigrams.png")


if __name__ == "__main__":
    main()
