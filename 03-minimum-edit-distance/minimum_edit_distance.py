"""
Experiment 03 — Minimum Edit Distance (Levenshtein)

Dynamic programming:
  D[i][j] = min edits to turn source[:i] into target[:j]

Operations (unit cost):
  deletion, insertion, substitution (0 if characters match)
"""

from __future__ import annotations


def min_edit_distance(
    source: str,
    target: str,
    del_cost: int = 1,
    ins_cost: int = 1,
    sub_cost: int = 1,
) -> tuple[int, list[list[int]]]:
    n, m = len(source), len(target)
    D = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        D[i][0] = D[i - 1][0] + del_cost
    for j in range(1, m + 1):
        D[0][j] = D[0][j - 1] + ins_cost

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost_sub = 0 if source[i - 1] == target[j - 1] else sub_cost
            D[i][j] = min(
                D[i - 1][j] + del_cost,
                D[i][j - 1] + ins_cost,
                D[i - 1][j - 1] + cost_sub,
            )
    return D[n][m], D


def print_matrix(source: str, target: str, D: list[list[int]]) -> None:
    header = ["#"] + ["·"] + list(target)
    print("  " + " ".join(f"{c:>3}" for c in header))
    rows_labels = ["·"] + list(source)
    for i, label in enumerate(rows_labels):
        row = [label] + [str(v) for v in D[i]]
        print("  " + " ".join(f"{c:>3}" for c in row))


def backtrace_ops(source: str, target: str, D: list[list[int]]) -> list[str]:
    i, j = len(source), len(target)
    ops: list[str] = []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and source[i - 1] == target[j - 1] and D[i][j] == D[i - 1][j - 1]:
            ops.append(f"match     '{source[i - 1]}'")
            i, j = i - 1, j - 1
        elif i > 0 and j > 0 and D[i][j] == D[i - 1][j - 1] + 1:
            ops.append(f"substitute '{source[i - 1]}' → '{target[j - 1]}'")
            i, j = i - 1, j - 1
        elif i > 0 and D[i][j] == D[i - 1][j] + 1:
            ops.append(f"delete     '{source[i - 1]}'")
            i -= 1
        else:
            ops.append(f"insert     '{target[j - 1]}'")
            j -= 1
    ops.reverse()
    return ops


def demo(source: str, target: str) -> None:
    dist, D = min_edit_distance(source, target)
    print("=" * 60)
    print(f"Source: {source!r}")
    print(f"Target: {target!r}")
    print(f"Minimum edit distance: {dist}")
    print("\nDP matrix:")
    print_matrix(source, target, D)
    print("\nOne optimal operation sequence:")
    for step, op in enumerate(backtrace_ops(source, target, D), 1):
        print(f"  {step}. {op}")
    print()


def main() -> None:
    demo("intention", "execution")
    demo("reading", "writing")
    demo("cat", "cats")
    demo("kitten", "sitting")


if __name__ == "__main__":
    main()
