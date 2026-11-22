# Folder naming (aligned with experiment numbers)

| Experiment / work | Folder |
|-------------------|--------|
| Experiment 01 — Text Preprocessing | `01-text-preprocessing/` |
| Experiment 02 — Handle Unstructured Data | `02-handle-unstructured-data/` |
| Experiment 03 — Minimum Edit Distance | `03-minimum-edit-distance/` |
| Experiment 04 — Zipf's Law | `04-zipfs-law/` |
| Experiment 05 — Bag of Words | `05-bag-of-words/` |
| Experiment 06 — Parsing | `06-parsing/` |
| Experiment 07 — Word2Vec vs BERT | `07-word2vec-vs-bert-embeddings/` |
| Assignment 02 — POS & Parsing | `assignment-02-pos-parsing/` |
| Intro course materials | `01-introduction-to-natural-language-processing-in-python/` |

**Old paths** (from earlier numbering) may still appear until you delete them in GitHub. Prefer the folders in the table above.

### Optional cleanup on your machine

```bash
git clone https://github.com/nabilatajrin/natural-language-processing.git
cd natural-language-processing
# after verifying new folders work:
git rm -r 02-text-preprocessing 05-handle-unstructured-data 06-minimum-edit-distance 08-bag-of-words 09-parsing 03-assignment-02-pos-parsing
git commit -m "Remove old misnumbered experiment folders"
git push
```
