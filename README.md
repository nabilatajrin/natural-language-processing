# Natural Language Processing

> NLP experiments, coursework, and practice projects.

**Author:** [Nabila Tajrin](https://github.com/nabilatajrin)

---

## Contents

| Folder | Description |
|--------|-------------|
| [`01-introduction-to-natural-language-processing-in-python`](01-introduction-to-natural-language-processing-in-python/) | Intro course: regex, tokenization, NER, fake-news classifier |
| [`01-text-preprocessing`](01-text-preprocessing/) | **Experiment 01** — tokenize, stopwords, stem, lemma, POS, n-grams, word cloud |
| [`02-handle-unstructured-data`](02-handle-unstructured-data/) | **Experiment 02** — unstructured text pipeline (tokenize → NER → WordNet) |
| [`03-minimum-edit-distance`](03-minimum-edit-distance/) | **Experiment 03** — Levenshtein minimum edit distance (DP) |
| [`04-zipfs-law`](04-zipfs-law/) | **Experiment 04** — Zipf's Law: rank–frequency, log–log plot, top words |
| [`05-bag-of-words`](05-bag-of-words/) | **Experiment 05** — Bag of Words + TF-IDF |
| [`06-parsing`](06-parsing/) | **Experiment 06** — CFG constituency parsing |
| [`07-word2vec-vs-bert-embeddings`](07-word2vec-vs-bert-embeddings/) | **Experiment 07** — Word2Vec vs transformer similarity + resume semantic search |
| [`assignment-02-pos-parsing`](assignment-02-pos-parsing/) | **Assignment 02** — HMM/Viterbi POS, CYK, oracle, smart-home logic |

---

## Experiment 01 — Text Preprocessing

```bash
cd 01-text-preprocessing
pip install -r requirements.txt
python part_a_single_sentence.py
python part_b_document_analysis.py
```

---

## Experiment 02 — Handle Unstructured Data

```bash
cd 02-handle-unstructured-data
pip install -r requirements.txt
python process_unstructured_text.py
```

---

## Experiment 03 — Minimum Edit Distance

```bash
cd 03-minimum-edit-distance
python minimum_edit_distance.py
```

---

## Experiment 04 — Zipf's Law

```bash
cd 04-zipfs-law
pip install -r requirements.txt
python zipfs_law.py
```

---

## Experiment 05 — Bag of Words

```bash
cd 05-bag-of-words
pip install -r requirements.txt
python bag_of_words.py
```

---

## Experiment 06 — Parsing

```bash
cd 06-parsing
pip install -r requirements.txt
python parsing_demo.py
```

---

## Experiment 07 — Embeddings & Semantic Search

```bash
cd 07-word2vec-vs-bert-embeddings
pip install -r requirements.txt
python 01_word2vec_vs_bert_similarity.py
python 02_resume_semantic_search.py
```

---

## Assignment 02 — POS & Parsing

```bash
cd assignment-02-pos-parsing
python 01_hmm_pos_tagging.py
python 02_viterbi_pos_tagging.py
python 03_cyk_parser.py
```

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
