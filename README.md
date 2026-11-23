# Natural Language Processing

MIT-WPU coursework, labs, and practice projects.

**Author:** [Nabila Tajrin](https://github.com/nabilatajrin)

---

## Structure

```text
natural-language-processing/
├── 01-text-preprocessing/          # Lab Experiment 01
├── 02-handle-unstructured-data/    # Lab Experiment 02
├── 03-minimum-edit-distance/       # Lab Experiment 03
├── 04-zipfs-law/                   # Lab Experiment 04
├── 05-bag-of-words/                # Lab Experiment 05
├── 06-parsing/                     # Lab Experiment 06
├── 07-word2vec-vs-bert-embeddings/ # Lab Experiment 07
├── assignment-02-pos-parsing/      # Assignment 02 (HMM, CYK, logic)
└── 01-introduction-to-natural-language-processing-in-python/  # DataCamp-style intro
```

Each lab folder has: `README.md`, `requirements.txt`, runnable `.py` scripts, and `post_lab_answers.md` where relevant.

---

## Quick start (any experiment)

```bash
git clone https://github.com/nabilatajrin/natural-language-processing.git
cd natural-language-processing/<folder>
pip install -r requirements.txt
python <script>.py
```

### Labs

| # | Folder | Run |
|---|--------|-----|
| 01 | `01-text-preprocessing` | `python part_a_single_sentence.py` then `part_b_document_analysis.py` |
| 02 | `02-handle-unstructured-data` | `python process_unstructured_text.py` |
| 03 | `03-minimum-edit-distance` | `python minimum_edit_distance.py` |
| 04 | `04-zipfs-law` | `python zipfs_law.py` |
| 05 | `05-bag-of-words` | `python bag_of_words.py` |
| 06 | `06-parsing` | `python parsing_demo.py` |
| 07 | `07-word2vec-vs-bert-embeddings` | `python 01_word2vec_vs_bert_similarity.py` |

### Assignment 02

```bash
cd assignment-02-pos-parsing
python 01_hmm_pos_tagging.py
python 02_viterbi_pos_tagging.py
python 03_cyk_parser.py
```

---

## Stack

Python 3 · NLTK · NumPy · scikit-learn · Matplotlib · Gensim · sentence-transformers

---

## License

MIT © Nabila Tajrin
