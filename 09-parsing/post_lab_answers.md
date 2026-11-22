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

---

### a. *The dogs cried*

**Tokens:** the, dogs, cried  

**Steps (top-down sketch):**

1. `S → NP VP`  
2. `NP → Det N` → `the` + `dogs`  
3. `VP → V` → `cried`  

**Parse tree:**

```text
          S
       /     \
     NP       VP
    /  \       |
  Det   N      V
   |    |      |
  the  dogs  cried
```

---

### b. *The old man cried*

**Tokens:** the, old, man, cried  

**Steps:**

1. `S → NP VP`  
2. `NP → Det Adj N` → `the` + `old` + `man`  
3. `VP → V` → `cried`  

**Parse tree:**

```text
            S
         /     \
       NP       VP
     / | \       |
  Det Adj  N     V
   |   |   |     |
  the old man  cried
```

Ambiguity note: without `Adj`, *old* could be mis-tagged; the grammar forces `Det Adj N` for this pattern.
