"""
Experiment 02 — Handle unstructured data

Pipeline on a local article (personality / history text):
  tokenization → frequency → stopwords → stem → lemma →
  POS → NER → WordNet sample → short conclusion
"""

from __future__ import annotations

import string
from collections import Counter
from pathlib import Path

import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tree import Tree

DATA_PATH = Path(__file__).resolve().parent / "data" / "sample_article.txt"

RESOURCES = [
    "punkt",
    "punkt_tab",
    "stopwords",
    "averaged_perceptron_tagger",
    "averaged_perceptron_tagger_eng",
    "maxent_ne_chunker",
    "maxent_ne_chunker_tab",
    "words",
    "wordnet",
    "omw-1.4",
]


def ensure_nltk() -> None:
    for r in RESOURCES:
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


def extract_entities(chunked: Tree) -> list[tuple[str, str]]:
    entities = []
    for node in chunked:
        if isinstance(node, Tree):
            label = node.label()
            text = " ".join(token for token, _pos in node.leaves())
            entities.append((text, label))
    return entities


def main() -> None:
    ensure_nltk()

    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Missing sample text: {DATA_PATH}")

    text = DATA_PATH.read_text(encoding="utf-8")
    print("=" * 60)
    print("1. RAW TEXT (preview)")
    print("=" * 60)
    print(text[:400], "..." if len(text) > 400 else "")

    # --- Tokenization ---
    tokens = word_tokenize(text)
    words = [t for t in tokens if t.isalnum()]
    print("\n" + "=" * 60)
    print("2. TOKENIZATION")
    print("=" * 60)
    print(f"Total tokens (incl. punctuation): {len(tokens)}")
    print(f"Alphanumeric tokens: {len(words)}")
    print("Sample:", words[:25])

    # --- Frequency distribution ---
    lower_words = [w.lower() for w in words]
    freq = FreqDist(lower_words)
    print("\n" + "=" * 60)
    print("3. FREQUENCY DISTRIBUTION (top 15)")
    print("=" * 60)
    for w, c in freq.most_common(15):
        print(f"  {w:20s} {c}")

    # --- Stop words ---
    stop = set(stopwords.words("english"))
    filtered = [w for w in lower_words if w not in stop]
    print("\n" + "=" * 60)
    print("4. AFTER STOP-WORD REMOVAL")
    print("=" * 60)
    print(f"Count: {len(filtered)}")
    print("Sample:", filtered[:30])

    # --- Stemming ---
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(w) for w in filtered]
    print("\n" + "=" * 60)
    print("5. STEMMING (Porter)")
    print("=" * 60)
    print("Sample:", stemmed[:30])

    # --- Lemmatization (POS-aware) ---
    tagged_for_lemma = pos_tag(filtered)
    lemmatizer = WordNetLemmatizer()
    lemmatized = [
        lemmatizer.lemmatize(w, get_wordnet_pos(tag)) for w, tag in tagged_for_lemma
    ]
    print("\n" + "=" * 60)
    print("6. LEMMATIZATION")
    print("=" * 60)
    print("Sample:", lemmatized[:30])

    # --- POS tagging ---
    tagged = pos_tag(words)
    print("\n" + "=" * 60)
    print("7. POS TAGGING (sample)")
    print("=" * 60)
    for w, t in tagged[:25]:
        print(f"  {w:20s} {t}")

    # --- NER ---
    chunked = ne_chunk(tagged)
    entities = extract_entities(chunked)
    print("\n" + "=" * 60)
    print("8. NAMED ENTITY RECOGNITION")
    print("=" * 60)
    if entities:
        for text_ent, label in entities:
            print(f"  {text_ent:30s} {label}")
    else:
        print("  (no entities detected by default NE chunker)")

    # --- WordNet ---
    print("\n" + "=" * 60)
    print("9. WORDNET (sample synsets)")
    print("=" * 60)
    for term in ["computer", "algorithm", "science", "pioneer"]:
        syns = wordnet.synsets(term)
        if syns:
            s = syns[0]
            print(f"  {term}: {s.name()} — {s.definition()}")
        else:
            print(f"  {term}: (no synset)")

    # --- Conclusion from data ---
    content_freq = Counter(filtered)
    top = content_freq.most_common(8)
    print("\n" + "=" * 60)
    print("10. CONCLUSION")
    print("=" * 60)
    print(
        "After cleaning unstructured text, the most frequent content words suggest "
        "the article focuses on:"
    )
    print("  " + ", ".join(w for w, _ in top))
    print(
        "NER and POS support entity- and role-level reading of the same document. "
        "This is the usual first stage before sentiment, classification, or retrieval."
    )


if __name__ == "__main__":
    main()
