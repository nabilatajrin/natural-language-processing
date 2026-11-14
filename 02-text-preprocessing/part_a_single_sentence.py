"""
NLP Experiment 01 — Part A
Operations on a Single Sentence

Steps:
  1. Trim spaces
  2. Lowercase
  3. Remove unwanted lab/meta phrases (if present)
  4. Tokenization
  5. Stopword removal
  6. Punctuation removal
  7. Stemming (Porter) & Lemmatization (WordNet + POS)
  8. Visualizations: word frequency, POS pie, bigrams, trigrams
"""

from __future__ import annotations

import re
import string
from collections import Counter

import matplotlib.pyplot as plt
import nltk
import seaborn as sns
from nltk import pos_tag
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

# ---------------------------------------------------------------------------
# NLTK resources (safe to call repeatedly)
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


def get_wordnet_pos(tag: str) -> str:
    """Map Penn Treebank POS tag to WordNet POS for accurate lemmatization."""
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
    """Full preprocessing pipeline for one sentence."""
    # 1. Trim
    text = sentence.strip()

    # 2. Lowercase
    text = text.lower()

    # 3. Remove lab boilerplate / URLs if accidentally present
    text = re.sub(
        r"\b(marks|teacher'?s signature with date|expt\.?\s*\d+-\d+|www\.\S+)\b",
        "",
        text,
        flags=re.IGNORECASE,
    )

    # 4. Tokenize
    tokens = word_tokenize(text)

    # 5 & 6. Remove stopwords and punctuation
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [
        w
        for w in tokens
        if w not in stop_words and w not in string.punctuation and w.strip()
    ]

    # 7. Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(w) for w in filtered_tokens]

    # 7. Lemmatization with POS
    lemmatizer = WordNetLemmatizer()
    tagged = pos_tag(filtered_tokens)
    lemmatized_tokens = [
        lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in tagged
    ]

    return {
        "original": sentence,
        "cleaned": text,
        "tokens": tokens,
        "filtered": filtered_tokens,
        "stemmed": stemmed_tokens,
        "lemmatized": lemmatized_tokens,
        "pos_tags": tagged,
    }


def plot_word_frequency(tokens: list[str]) -> None:
    counts = Counter(tokens)
    labels = list(counts.keys())
    values = list(counts.values())

    plt.figure(figsize=(10, 5))
    sns.barplot(x=labels, y=values, hue=labels, palette="viridis", legend=False)
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Word Frequency Distribution")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


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
    plt.tight_layout()
    plt.show()


def plot_ngrams(tokens: list[str], n: int, title: str, palette: str) -> None:
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
    plt.tight_layout()
    plt.show()


def main() -> None:
    sentence = (
        "Artificial intelligence (AI) is transforming industries by enabling "
        "machines to learn from data, automate tasks, and make intelligent decisions."
    )

    result = preprocess_sentence(sentence)

    print("Original Sentence:", result["original"])
    print("Tokenized Words:", result["tokens"])
    print("Filtered Tokens (stopwords & punctuation removed):", result["filtered"])
    print("Stemmed Tokens:", result["stemmed"])
    print("Lemmatized Tokens:", result["lemmatized"])

    plot_word_frequency(result["filtered"])
    plot_pos_pie(result["pos_tags"])
    plot_ngrams(result["filtered"], 2, "Bigram Frequency Distribution", "magma")
    plot_ngrams(result["filtered"], 3, "Trigram Frequency Distribution", "coolwarm")


if __name__ == "__main__":
    main()
