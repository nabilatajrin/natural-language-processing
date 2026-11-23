"""Assignment 02 — CYK parser (CNF toy grammar)."""
from __future__ import annotations

# CNF productions: A -> B C  or  A -> word
grammar = {
    ("S", ("NP", "VP")),
    ("NP", ("Det", "N")),
    ("VP", ("V", "NP")),
    ("Det", ("the",)),
    ("N", ("cat",)),
    ("N", ("mat",)),
    ("V", ("sat",)),
}


def cyk(words: list[str]) -> bool:
    n = len(words)
    table = [[set() for _ in range(n)] for _ in range(n)]
    for i, w in enumerate(words):
        for lhs, rhs in grammar:
            if rhs == (w,):
                table[i][i].add(lhs)
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                for lhs, rhs in grammar:
                    if len(rhs) == 2 and rhs[0] in table[i][k] and rhs[1] in table[k + 1][j]:
                        table[i][j].add(lhs)
    return "S" in table[0][n - 1]


def main() -> None:
    sent = ["the", "cat", "sat"]
    # grammar only covers Det N / V NP style fully for "the cat sat" if VP -> V only added
    # extend VP -> V for this demo
    grammar.add(("VP", ("V",)))
    ok = cyk(sent)
    print("Sentence:", sent)
    print("Accepted by grammar:", ok)


if __name__ == "__main__":
    main()
