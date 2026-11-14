# Experiment 01 — Text Preprocessing

**Course:** PGD AI & ML (2024–25) · MIT WPU  
**Student:** Nabila Tajrin Bristy · PRN 1262243611

This experiment covers fundamental NLP text preprocessing and exploratory analysis using **NLTK**.

---

## Folder structure

```text
02-text-preprocessing/
├── README.md
├── requirements.txt
├── data/
│   └── ai_sample.txt          # Sample document for Part B
├── part_a_single_sentence.py  # Operations on one sentence
└── part_b_document_analysis.py # Operations on a full text file
```

---

## What you will learn

| Step | Technique |
|------|-----------|
| 1 | Strip whitespace, lowercase |
| 2 | Tokenization (`word_tokenize`) |
| 3 | Stopword removal |
| 4 | Punctuation removal |
| 5 | Stemming (Porter) |
| 6 | Lemmatization (WordNet + POS) |
| 7 | POS tagging |
| 8 | N-grams (bigrams, trigrams) |
| 9 | Frequency analysis & visualization |
| 10 | Word cloud |

---

## Setup

```bash
cd 02-text-preprocessing
pip install -r requirements.txt

# One-time NLTK data (also downloaded by the scripts)
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('averaged_perceptron_tagger'); nltk.download('averaged_perceptron_tagger_eng'); nltk.download('wordnet'); nltk.download('omw-1.4'); nltk.download('stopwords')"
```

---

## How to run

### Part A — Single sentence

```bash
python part_a_single_sentence.py
```

Produces:
- Cleaned / tokenized / filtered / stemmed / lemmatized tokens
- Word frequency bar chart
- POS distribution pie chart
- Bigram & trigram frequency charts

### Part B — Full document (`data/ai_sample.txt`)

```bash
python part_b_document_analysis.py
```

Produces:
- Unique token count
- Punctuation count
- Unique lemma count
- POS tag bar chart (green)
- Stopword frequency chart (orange)
- Top 10 words
- Word cloud

---

## Sample results (from original experiment)

**Part A filtered tokens:**  
`artificial, intelligence, ai, transforming, industries, enabling, machines, learn, data, automate, tasks, make, intelligent, decisions`

**Part B (document):**
| Metric | Value |
|--------|-------|
| Unique tokens | 296 |
| Punctuation characters | 80 |
| Unique lemmas | 236 |
| Top word | `ai` (23) |

---

## Notes

- Code is cleaned from the lab notebook: missing imports fixed, seaborn `hue` deprecation avoided, Google Drive path replaced with local `data/ai_sample.txt`.
- Original lab PDF and notebook remain at the repo root for reference.
