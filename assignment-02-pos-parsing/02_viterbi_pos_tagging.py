"""Assignment 02 — Viterbi POS decoding."""
from __future__ import annotations

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


def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
    for st in states:
        V[0][st] = start_p[st] * emit_p[st].get(obs[0], 1e-6)
        path[st] = [st]
    for t in range(1, len(obs)):
        V.append({})
        new_path = {}
        for st in states:
            (prob, state) = max(
                (V[t - 1][prev] * trans_p[prev][st] * emit_p[st].get(obs[t], 1e-6), prev)
                for prev in states
            )
            V[t][st] = prob
            new_path[st] = path[state] + [st]
        path = new_path
    n = len(obs) - 1
    (prob, state) = max((V[n][st], st) for st in states)
    return prob, path[state]


def main() -> None:
    obs = ["the", "cat", "sat"]
    prob, tags = viterbi(obs, states, start_p, trans_p, emit_p)
    print("Words:", obs)
    print("Tags:", tags)
    print("Path probability:", prob)


if __name__ == "__main__":
    main()
