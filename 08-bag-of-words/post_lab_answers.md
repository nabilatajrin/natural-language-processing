# Post Lab Answers — Experiment 05

## Q1. Term frequency and TF-IDF

Documents (lowercased, simple whitespace tokens):

| Id | Text |
|----|------|
| D1 | NLP is a theoretical subject |
| D2 | NLP is interesting subject |
| D3 | Solve the given problem |

### Vocabulary (sorted unique tokens)

`a`, `given`, `interesting`, `is`, `nlp`, `problem`, `solve`, `subject`, `the`, `theoretical`

### Term frequency (raw count in each document)

| Term | D1 | D2 | D3 |
|------|----|----|----|
| a | 1 | 0 | 0 |
| given | 0 | 0 | 1 |
| interesting | 0 | 1 | 0 |
| is | 1 | 1 | 0 |
| nlp | 1 | 1 | 0 |
| problem | 0 | 0 | 1 |
| solve | 0 | 0 | 1 |
| subject | 1 | 1 | 0 |
| the | 0 | 0 | 1 |
| theoretical | 1 | 0 | 0 |

### TF-IDF (sketch)

Using common definitions:

- `TF(t, d) = count(t, d) / length(d)` (or raw count; both are used in labs)  
- `IDF(t) = log(N / df(t))` with `N = 3`  
- `TF-IDF = TF × IDF`  

Terms like **nlp**, **is**, **subject** appear in 2 of 3 docs → lower IDF.  
Terms like **theoretical**, **interesting**, **solve**, **problem** appear in 1 doc → higher IDF.

Run `python bag_of_words.py` for exact numeric matrices (from-scratch and sklearn).
