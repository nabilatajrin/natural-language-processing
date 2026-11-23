"""Assignment 02 — HMM emission/transition sketch for POS."""
from __future__ import annotations

# Tiny example HMM tables (illustrative)
states = ["DT", "NN", "VB"]
start_p = {"DT": 0.4, "NN": 0.3, "VB": 0.3}
trans_p = {
    "DT": {"DT": 0.1, "NN": 0.8, "VB": 0.1},
    "NN": {"DT": 0.2, "NN": 0.3, "VB": 0.5},
    "VB": {"DT": 0.4, "NN": 0.4, "VB": 0.2},
}
emit_p = {
    "DT": {"the": 0.7, "a": 0.3},
    "NN": {"cat": 0.4, "dog": 0.4, "mat": 0.2},
    "VB": {"sat": 0.5, "ate": 0.5},
}
obs = ["the", "cat", "sat"]

print("States:", states)
print("Observation:", obs)
print("Start:", start_p)
print("Transitions:", trans_p)
print("Emissions:", emit_p)
print("\nSee 02_viterbi_pos_tagging.py for decoding.")
