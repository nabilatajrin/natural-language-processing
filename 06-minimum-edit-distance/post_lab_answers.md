# Post Lab Answers — Experiment 03

## Q1. Operations to convert `"reading"` into `"writing"`

Using **Levenshtein** distance (insert / delete / substitute each cost **1**):

| | | |
|--|--|--|
| Source | `reading` | length 7 |
| Target | `writing` | length 7 |

**Minimum edit distance = 4**

One optimal sequence of operations (not unique):

1. Substitute `r` → `w`  → `weading`  
2. Substitute `e` → `r`  → `wrading`  
3. Substitute `a` → `i`  → `wriding`  
4. Substitute `d` → `t`  → `writing`  

(Alignment keeps the shared suffix pattern `-ing` / structure where possible; the DP table confirms cost 4.)

Run the script to print the full distance matrix for this pair.
