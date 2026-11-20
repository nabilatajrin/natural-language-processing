# Experiment 03 — Minimum Edit Distance

**Course:** Natural Language Processing  
**Institution:** MIT World Peace University  
**Level:** Final Year B.Tech (ECE) / PGD AI & ML

**Aim:** Implement the Minimum Edit Distance (Levenshtein) algorithm.

**Objective:** Get familiar with edit distance using dynamic programming.

---

## Folder structure

```text
06-minimum-edit-distance/
├── README.md
├── requirements.txt
├── minimum_edit_distance.py    # DP table + backtrace + demos
└── post_lab_answers.md         # reading → writing
```

---

## Theory (short)

**Edit distance** measures how dissimilar two strings are by counting the minimum number of operations to turn one into the other:

- **Insertion**  
- **Deletion**  
- **Substitution**  

Uses in NLP: spelling correction, fuzzy matching. Also used in bioinformatics (DNA strings).

For source `X` (length *n*) and target `Y` (length *m*):

- `D(i, j)` = edit distance between `X[1..i]` and `Y[1..j]`  
- Answer = `D(n, m)`  

Computed with a DP table (shortest path over edit operations).

Classic example from textbooks: **intention** → **execution**.

---

## Run

```bash
cd 06-minimum-edit-distance
pip install -r requirements.txt   # none required beyond Python 3
python minimum_edit_distance.py
```

Prints DP matrices and distances for:

1. `intention` → `execution`  
2. Post-lab: `reading` → `writing`  
3. A few extra pairs  

---

## Post-lab

See [post_lab_answers.md](post_lab_answers.md).
