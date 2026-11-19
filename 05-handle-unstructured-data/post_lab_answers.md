# Post Lab Answers — Experiment 02 (Unstructured Data)

## 1. What is the use of a corpus in Python?

In Python NLP (especially with **NLTK**), a **corpus** is a collection of text used to:

- Train or evaluate language models  
- Compute statistics (word frequencies, collocations)  
- Provide labeled data for tagging, parsing, or classification  
- Look up linguistic resources (e.g. WordNet, treebanks)  

Examples: `nltk.corpus.brown`, `gutenberg`, `stopwords`, or your own folder of `.txt` files loaded with `PlaintextCorpusReader`.

---

## 2. What are the features of a corpus?

Typical features:

| Feature | Meaning |
|---------|---------|
| **Size** | Number of documents / tokens |
| **Domain** | News, literature, social media, scientific, etc. |
| **Language(s)** | Mono- or multilingual |
| **Annotation** | Raw text only, or POS tags, entities, parse trees |
| **Balance** | Even coverage of genres vs skewed |
| **Format** | Plain text, XML, JSON, CoNLL, etc. |
| **License** | Redistribution and research use rules |

A good corpus is **representative** of the language use you care about and, when possible, **annotated** consistently.

---

## 3. State different text processing techniques

From the lab theory and common NLP practice:

1. **Sentiment analysis** — polarity / emotion  
2. **Named entity recognition** — people, places, organizations  
3. **Summarization** — extractive or abstractive short form  
4. **Topic modeling** — latent themes (e.g. LDA)  
5. **Text classification** — assign labels / categories  
6. **Keyword extraction** — important terms  
7. **Lemmatization and stemming** — normalize word forms  

Plus core **preprocessing**: tokenization, stop-word removal, POS tagging, frequency analysis, WordNet lookups.
