"""Experiment 02 — Handle unstructured data (NLTK pipeline)."""
from __future__ import annotations

from collections import Counter
from pathlib import Path

import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tree import Tree

DATA = Path(__file__).resolve().parent / "data" / "sample_article.txt"

for r in ("punkt", "punkt_tab", "stopwords", "averaged_perceptron_tagger",
          "averaged_perceptron_tagger_eng", "maxent_ne_chunker", "maxent_ne_chunker_tab",
          "words", "wordnet", "omw-1.4"):
    nltk.download(r, quiet=True)


def get_wordnet_pos(tag: str):
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
    text = DATA.read_text(encoding="utf-8")
    print("RAW PREVIEW:\n", text[:300], "...\n")
    tokens = word_tokenize(text)
    words = [t for t in tokens if t.isalnum()]
    lower = [w.lower() for w in words]
    print("Tokens:", len(tokens), "| Alphanumeric:", len(words))
    print("Top freq:", FreqDist(lower).most_common(10))
    stop = set(stopwords.words("english"))
    filtered = [w for w in lower if w not in stop]
    stemmer = PorterStemmer()
    print("Stemmed sample:", [stemmer.stem(w) for w in filtered[:15]])
    tagged = pos_tag(filtered)
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(w, get_wordnet_pos(t)) for w, t in tagged]
    print("Lemmas sample:", lemmas[:15])
    print("POS sample:", pos_tag(words)[:15])
    entities = []
    for node in ne_chunk(pos_tag(words)):
        if isinstance(node, Tree):
            entities.append((" ".join(t for t, _ in node.leaves()), node.label()))
    print("Entities:", entities or "(none)")
    for term in ("computer", "algorithm", "science"):
        syns = wordnet.synsets(term)
        if syns:
            print(f"WordNet {term}:", syns[0].definition())
    print("Conclusion focus terms:", [w for w, _ in Counter(filtered).most_common(8)])


if __name__ == "__main__":
    main()
