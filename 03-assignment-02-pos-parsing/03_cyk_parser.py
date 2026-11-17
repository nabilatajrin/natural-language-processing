"""
Assignment 02 — Q3
CYK parser for:

  Sentence: "The black cat chased the white mouse."

  S  -> NP VP
  NP -> Det Noun | Det Adj Noun | Noun PP
  VP -> Verb NP | Verb NP PP
  PP -> Prep NP
  Det -> the
  Adj -> black | white
  Noun -> cat | mouse
  Verb -> chased
  Prep -> with

Note: grammar terminals are lowercased; input is lowercased before parse.
"""

from __future__ import annotations

from collections import defaultdict

# Chomsky Normal Form-friendly binary rules + unary lexical rules
# Nonterminals on RHS of binary rules only.
BINARY = [
    ("S", "NP", "VP"),
    ("NP", "Det", "Noun"),       # Det Noun  (will also build Det Adj Noun via intermediate)
    ("NP", "DetAdj", "Noun"),    # Det Adj  -> DetAdj, then + Noun
    ("DetAdj", "Det", "Adj"),
    ("NP", "Noun", "PP"),
    ("VP", "Verb", "NP"),
    ("VP", "VerbNP", "PP"),
    ("VerbNP", "Verb", "NP"),
    ("PP", "Prep", "NP"),
]

LEXICON = {
    "the": {"Det"},
    "black": {"Adj"},
    "white": {"Adj"},
    "cat": {"Noun"},
    "mouse": {"Noun"},
    "chased": {"Verb"},
    "with": {"Prep"},
}


def cyk(tokens: list[str]):
    n = len(tokens)
    # table[i][j] = set of nonterminals spanning tokens[i:j]
    table = [[set() for _ in range(n + 1)] for _ in range(n + 1)]
    back = [[defaultdict(list) for _ in range(n + 1)] for _ in range(n + 1)]

    for i, w in enumerate(tokens):
        for nt in LEXICON.get(w, set()):
            table[i][i + 1].add(nt)
            back[i][i + 1][nt].append(("lex", w))

    for span in range(2, n + 1):
        for i in range(0, n - span + 1):
            j = i + span
            for k in range(i + 1, j):
                for A, B, C in BINARY:
                    if B in table[i][k] and C in table[k][j]:
                        table[i][j].add(A)
                        back[i][j][A].append(("bin", B, C, k))

    return table, back


def build_tree(back, i, j, symbol):
    if symbol not in back[i][j]:
        return (symbol,)
    item = back[i][j][symbol][0]
    if item[0] == "lex":
        return (symbol, item[1])
    _, B, C, k = item
    return (symbol, build_tree(back, i, k, B), build_tree(back, k, j, C))


def pretty(tree, indent=0):
    if len(tree) == 2 and isinstance(tree[1], str):
        return "  " * indent + f"{tree[0]} -> '{tree[1]}'"
    lines = ["  " * indent + tree[0]]
    for child in tree[1:]:
        lines.append(pretty(child, indent + 1))
    return "\n".join(lines)


def main() -> None:
    sentence = "The black cat chased the white mouse."
    tokens = sentence.replace(".", "").lower().split()
    print("Sentence:", sentence)
    print("Tokens:", tokens)

    table, back = cyk(tokens)
    accepted = "S" in table[0][len(tokens)]
    print("Accepted by grammar (S spans full sentence):", accepted)

    if accepted:
        tree = build_tree(back, 0, len(tokens), "S")
        print("\nParse tree:")
        print(pretty(tree))
    else:
        print("No full parse. Cell contents for debug:")
        n = len(tokens)
        for span in range(1, n + 1):
            for i in range(n - span + 1):
                j = i + span
                if table[i][j]:
                    print(f"  [{i}:{j}] {tokens[i:j]} -> {sorted(table[i][j])}")


if __name__ == "__main__":
    main()
