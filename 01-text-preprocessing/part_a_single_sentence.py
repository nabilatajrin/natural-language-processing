"""Experiment 01 — Part A: preprocess a single sentence."""
from __future__ import annotations

import re
import string
from collections import Counter

import nltk
from nltk import pos_tag
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

for r in ("punkt", "punkt_tab", "averaged_perceptron_tagger", "averaged_perceptron_tagger_eng",
          "wordnet", "omw-1.4", "stopwords"):
    nltk.download(r, quiet=True)


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


def main() -> None:
    sentence = (
        "Natural Language Processing helps computers understand human language "
        "and extract useful information from text."
    )
    print("Original:", sentence)
    text = sentence.strip().lower()
    tokens = word_tokenize(text)
    stop = set(stopwords.words("english"))
    filtered = [t for t in tokens if t not in stop and t not in string.punctuation]
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(t) for t in filtered]
    tagged = pos_tag(filtered)
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(w, get_wordnet_pos(t)) for w, t in tagged]
    print("Tokens:", tokens)
    print("Filtered:", filtered)
    print("Stemmed:", stemmed)
    print("Lemmas:", lemmas)
    print("POS:", tagged)
    print("Bigrams:", list(ngrams(filtered, 2)))
    print("Freq:", Counter(filtered).most_common())


if __name__ == "__main__":
    main()
