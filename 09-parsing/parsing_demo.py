"""
Experiment 06 — Parsing

Small CFG + NLTK RecursiveDescentParser.
Demonstrates constituency parse trees for lab sentences.
"""

from __future__ import annotations

import nltk
from nltk import CFG, RecursiveDescentParser

grammar = CFG.fromstring(
    """
    S   -> NP VP
    NP  -> Det N | Det Adj N | N
    VP  -> V | V NP | Aux V NP
    Det -> 'the' | 'a'
    N   -> 'dogs' | 'man' | 'John' | 'game' | 'cat' | 'mouse'
    Adj -> 'old' | 'black' | 'white'
    V   -> 'cried' | 'playing' | 'chased' | 'slept'
    Aux -> 'is'
    """
)

parser = RecursiveDescentParser(grammar)

SENTENCES = [
    "the dogs cried",
    "the old man cried",
    "John is playing game",
    "the black cat chased the white mouse",
]


def parse_sentence(text: str) -> None:
    tokens = text.lower().split()
    print("=" * 60)
    print(f"Sentence: {text!r}")
    print(f"Tokens:   {tokens}")
    trees = list(parser.parse(tokens))
    if not trees:
        print("  No parse found under this grammar.")
        return
    for i, tree in enumerate(trees, 1):
        print(f"\nParse tree #{i}:")
        print(tree)
        print()
        tree.pretty_print()


def main() -> None:
    nltk.download("punkt", quiet=True)
    print("Grammar productions:")
    for p in grammar.productions():
        print(" ", p)
    print()

    for s in SENTENCES:
        parse_sentence(s)


if __name__ == "__main__":
    main()
