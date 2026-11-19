# Experiment 02 — Handle Unstructured Data

**Course:** Natural Language Processing  
**Institution:** MIT World Peace University  
**Level:** Final Year B.Tech (ECE) / PGD AI & ML

**Aim:** Implement various text processing operations on unstructured data.

**Problem statement:** Take text about a personality, movie review, etc., and apply NLP preprocessing to draw useful conclusions.

---

## Folder structure

```text
05-handle-unstructured-data/
├── README.md
├── requirements.txt
├── data/
│   └── sample_article.txt          # Unstructured sample text (local corpus)
├── process_unstructured_text.py    # Full pipeline
└── post_lab_answers.md
```

---

## Theory (short)

**Text processing** analyzes unstructured text with NLP/ML to extract value.

Common technique families:

1. Sentiment analysis  
2. Named entity recognition (NER)  
3. Summarization  
4. Topic modeling  
5. Text classification  
6. Keyword extraction  
7. Lemmatization and stemming  

**Data preprocessing with NLTK** (this experiment focuses here):

- Tokenization  
- Frequency distribution  
- Stop-word filtering  
- Stemming  
- Lemmatization  
- POS tagging  
- Named entity recognition  
- WordNet lookups  

**Corpus:** a collection of text documents (one or many files) used for training or analysis.

---

## Run

```bash
cd 05-handle-unstructured-data
pip install -r requirements.txt
python process_unstructured_text.py
```

NLTK data packages download automatically on first run.

---

## What the script prints

1. Raw text preview  
2. Tokens  
3. Word frequency (top terms)  
4. Tokens after stop-word removal  
5. Stemmed tokens  
6. Lemmatized tokens  
7. POS tags  
8. Named entities (if any)  
9. Sample WordNet synsets  
10. Short conclusion from frequencies  

---

## Post-lab

See [post_lab_answers.md](post_lab_answers.md).
