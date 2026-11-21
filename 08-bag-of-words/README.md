# Experiment 05 — Bag of Words

**Course:** Natural Language Processing  
**Institution:** MIT World Peace University  
**Level:** Final Year B.Tech (ECE) / PGD AI & ML

**Aim:** Implement Bag of Words (and TF-IDF scoring).

**Objective:** Get familiar with BoW and TF-IDF representations.

---

## Folder structure

```text
08-bag-of-words/
├── README.md
├── requirements.txt
├── bag_of_words.py          # BoW counts + TF-IDF (from scratch + sklearn)
└── post_lab_answers.md      # D1, D2, D3 TF / TF-IDF
```

---

## Theory (short)

**Bag of Words (BoW)** represents a document as a multiset of words:

1. Build a **vocabulary** of known words  
2. Measure **presence / count** of each word in the document  

Word **order and grammar are ignored**; only multiplicity matters.

**TF-IDF** rescales raw counts so common words across the whole collection are down-weighted:

- **TF** — how often a term appears in *this* document  
- **IDF** — how rare the term is across *all* documents  

Result: distinctive terms get higher weight.

---

## Run

```bash
cd 08-bag-of-words
pip install -r requirements.txt
python bag_of_words.py
```

Uses the post-lab documents:

- D1: `NLP is a theoretical subject`  
- D2: `NLP is interesting subject`  
- D3: `Solve the given problem`  

---

## Post-lab

See [post_lab_answers.md](post_lab_answers.md).
