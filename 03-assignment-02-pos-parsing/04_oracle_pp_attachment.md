# Q4 — Oracle for PP-attachment ambiguity

## Grammar

```text
S  → NP VP
NP → ART N
NP → ART N PP
VP → V NP
VP → V NP PP
```

## Where ambiguity appears

Two choice points:

1. **NP** — `NP → ART N` vs `NP → ART N PP`
2. **VP** — `VP → V NP` vs `VP → V NP PP`

Classic example:

> *The boy saw the man with a telescope.*

- **NP attachment:** the man who has a telescope  
- **VP attachment:** the boy used a telescope to see

A deterministic **oracle** must pick one action when both are possible.

## Heuristics (Section 6.2 style)

| Heuristic | Idea |
|-----------|------|
| **Minimal Attachment** | Prefer the tree with fewer nodes |
| **Right Association / Late Closure** | Attach the PP to the nearest / most recent constituent |

### Oracle decision used here

- Prefer **`NP → ART N`** over **`NP → ART N PP`** when both possible  
- Prefer **`VP → V NP`** over **`VP → V NP PP`** when both possible  

(Equivalent to **minimal attachment**: avoid introducing a PP unless forced.)

Alternatively, a **Right Association** oracle always attaches the PP to the **nearest NP**.

## Incorrect parse caused by that decision

**Sentence:** *The boy saw the man with a telescope.*  

**Intended (VP attachment):** boy uses telescope.  
**Oracle (NP / minimal attachment):** man has the telescope.

| Sentence | Intended | Oracle | Correct? |
|----------|----------|--------|----------|
| The boy saw the man with a telescope | VP | NP | **No** |

So the oracle is consistent but **not always semantically correct** — that is the point of the exercise.
