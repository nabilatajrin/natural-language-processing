# Experiment 07 — Word2Vec vs LLM Embeddings for Semantic Similarity

**Course:** NLPT · PGD AI-ML  
**Student:** Nabila Tajrin Bristy · PRN 1262243611

Compare **static** (Word2Vec) and **contextual / transformer** embeddings on sentence similarity, then run a small **resume semantic search** project with PCA visualization.

---

## Folder structure

```text
07-word2vec-vs-bert-embeddings/
├── README.md
├── requirements.txt
├── 01_word2vec_vs_bert_similarity.py   # Part A — cosine similarity comparison
├── 02_resume_semantic_search.py        # Part B — synthetic resumes + PCA + query
└── post_lab_answers.md                 # Natural join & many-to-many joins
```

---

## Part A — Methods

| Method | Idea |
|--------|------|
| **Word2Vec** | Static word vectors; sentence = average of word vectors |
| **Transformer (MiniLM / BERT-style)** | Contextual sentence embedding |
| **Similarity** | Cosine similarity between sentence vectors |

Dataset (from lab):

| Sentence 1 | Sentence 2 |
|------------|------------|
| I love AI | AI is my passion |
| Dogs are cute | I adore puppies |

In the lab report, **BERT** scored higher (~0.89 / ~0.91) than Word2Vec (~0.65 / ~0.70).

> **Note:** Full Google-News Word2Vec (~1.5 GB) is optional. Script A trains a small Word2Vec on a tiny corpus so it runs offline, and uses `sentence-transformers` (`all-MiniLM-L6-v2`) as the LLM-style embedding (same family as the resume project).

---

## Part B — Resume semantic search

1. Synthetic resumes + roles  
2. Embed with `SentenceTransformer("all-MiniLM-L6-v2")`  
3. PCA → 2D plot by role  
4. Query → top-k cosine matches  
5. Plot query on the same PCA space  

---

## Setup & run

```bash
cd 07-word2vec-vs-bert-embeddings
pip install -r requirements.txt

python 01_word2vec_vs_bert_similarity.py
python 02_resume_semantic_search.py
```

First run downloads the MiniLM model (~90 MB). Charts are saved under `images/`.

---

## Post-lab

See [post_lab_answers.md](post_lab_answers.md) (SQL natural join & many-to-many).
