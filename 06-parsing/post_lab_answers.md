# Post Lab Answers — Experiment 06

## Q1. Parsing steps on paper

Grammar used (simple English CFG):

```text
S   -> NP VP
NP  -> Det N | Det Adj N
VP  -> V
Det -> the
N   -> dogs | man
Adj -> old
V   -> cried
```

### a. *The dogs cried*

```text
          S
       /     \
     NP       VP
    /  \       |
  Det   N      V
   |    |      |
  the  dogs  cried
```

### b. *The old man cried*

```text
            S
         /     \
       NP       VP
     / | \       |
  Det Adj  N     V
   |   |   |     |
  the old man  cried
```
