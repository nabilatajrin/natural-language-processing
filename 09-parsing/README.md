# Experiment 06 — Parsing

**Course:** Natural Language Processing  
**Institution:** MIT World Peace University  
**Level:** Final Year B.Tech (ECE) / PGD AI & ML

**Aim:** Implement parsing.  
**Objective:** Get familiar with syntactic parsing of natural language sentences.

---

## Folder structure

```text
09-parsing/
├── README.md
├── requirements.txt
├── parsing_demo.py           # CFG + NLTK RecursiveDescentParser
└── post_lab_answers.md       # trees for “The dogs cried” / “The old man cried”
```

---

## Theory (short)

**Parsing** analyses a sentence for structure, content, and meaning: identify constituents, POS, and how grammar rules combine them.

- Tokens: individual words (`John`, `is`, `playing`, `game`)
- POS disambiguation (e.g. *book* as noun vs verb)
- Output often a **parse tree** — order of grammar productions applied

This experiment uses a small **context-free grammar (CFG)** and NLTK’s recursive-descent parser.

---

## Run

```bash
cd 09-parsing
pip install -r requirements.txt
python parsing_demo.py
```

Parses lab examples plus a few extra sentences and prints trees.

---

## Post-lab

See [post_lab_answers.md](post_lab_answers.md).
