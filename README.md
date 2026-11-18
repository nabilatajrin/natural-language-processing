# Natural Language Processing

> NLP experiments, coursework, and practice projects.

**Author:** [Nabila Tajrin](https://github.com/nabilatajrin)

---

## Contents

| Folder | Description |
|--------|-------------|
| [`01-introduction-to-natural-language-processing-in-python`](01-introduction-to-natural-language-processing-in-python/) | DataCamp-style intro: regex, tokenization, NER, fake-news classifier |
| [`02-text-preprocessing`](02-text-preprocessing/) | **Experiment 01** — tokenize, stopwords, stem, lemma, POS, n-grams, word cloud |
| [`03-assignment-02-pos-parsing`](03-assignment-02-pos-parsing/) | **Assignment 02** — HMM/Viterbi POS, CYK parsing, oracle, smart-home logic |
| [`04-zipfs-law`](04-zipfs-law/) | **Experiment 04** — Zipf's Law: rank–frequency, log–log plot, top words |
| [`07-word2vec-vs-bert-embeddings`](07-word2vec-vs-bert-embeddings/) | **Experiment 07** — Word2Vec vs transformer similarity + resume semantic search |

---

## Experiment 01 — Text Preprocessing

```bash
cd 02-text-preprocessing
pip install -r requirements.txt
python part_a_single_sentence.py
python part_b_document_analysis.py
```

---

## Assignment 02 — POS & Parsing

```bash
cd 03-assignment-02-pos-parsing
python 01_hmm_pos_tagging.py
python 02_viterbi_pos_tagging.py
python 03_cyk_parser.py
```

---

## Experiment 04 — Zipf's Law

```bash
cd 04-zipfs-law
pip install -r requirements.txt
python zipfs_law.py
```

---

## Experiment 07 — Embeddings & Semantic Search

```bash
cd 07-word2vec-vs-bert-embeddings
pip install -r requirements.txt
python 01_word2vec_vs_bert_similarity.py
python 02_resume_semantic_search.py
```

Post-lab: [`07-word2vec-vs-bert-embeddings/post_lab_answers.md`](07-word2vec-vs-bert-embeddings/post_lab_answers.md)

---

## Tech stack

- Python 3
- NLTK, NumPy, Pandas, SciPy, scikit-learn
- Matplotlib / Seaborn
- Gensim, sentence-transformers
- WordCloud, contractions

---

## License

MIT © Nabila Tajrin
