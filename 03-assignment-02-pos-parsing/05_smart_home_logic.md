# Smart Home Security System — Logic

Corrected propositional and predicate rules (original assignment had contradictory lock/unlock lines).

## Requirements

1. Activate camera if motion sensor 1 **or** 2 fires.  
2. Alert if door 1 opens and **no** motion was seen in the last 5 minutes.  
3. **Lock** if camera sees an **unauthorized** person.  
4. **Unlock** if an **authorized** person is detected by motion and opens the door.

---

## Propositional logic

| # | Rule | Meaning |
|---|------|---------|
| 1 | `(M1 ∨ M2) → C1` | Motion → camera |
| 2 | `D1 ∧ ¬(M1 ∨ M2) → A` | Door open, no motion → alert |
| 3 | `C1 ∧ U → ¬L1` | Camera + unauthorized → lock |
| 4 | `(M1 ∧ D1) ∨ (M2 ∧ D2) → L1` | Authorized motion + door → unlock |

(`U` = unauthorized person detected; `L1` = lock open/unlocked state as needed in your encoding.)

---

## Predicate logic

1. **Camera on motion**  
   `∀x,t [ M(x,t) → C(x,t) ]`

2. **Alert (5-minute window)**  
   `∀t [ D(1,t) ∧ ¬∃y,t' (M(y,t') ∧ t' ≥ t−5) → A(t) ]`

3. **Lock unauthorized**  
   `∀x,t [ C(x,t) ∧ ¬Authorized(x) → ¬L(x,t) ]`

4. **Unlock authorized entry**  
   `∀x,t [ Authorized(x) ∧ M(x,t) ∧ D(x,t) → L(x,t) ]`

---

## Workflow examples

1. **Authorized entry** — motion of authorized `x` + door → unlock.  
2. **Unauthorized door** — `D1` with no motion → alert.  
3. **Intruder** — camera of `¬Authorized(x)` → lock.
