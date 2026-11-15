# Post Lab Answers — Experiment 04 (Zipf's Law)

## Q1. State Heap's Law

**Heap's Law** describes how vocabulary size grows with corpus size.

The number of unique words \(V\) in a text of \(N\) total tokens grows approximately as:

\[
V(N) = K \cdot N^{\beta}
\]

Where:

- \(V(N)\) = number of unique words (vocabulary size)
- \(N\) = total number of tokens in the text
- \(K\) = constant (often roughly 10–100)
- \(\beta\) = exponent (typically about 0.4–0.6)

**Interpretation:** As more text is added, new unique words still appear, but the rate of growth slows down (sublinear growth because \(\beta < 1\)).

---

## Q2. How to calculate the number of words that appear \(n\) times using Zipf's Law

Zipf's Law relates **frequency** of a word to its **rank** (\(f(r) \propto 1/r^{\alpha}\)). It does not by itself give an exact count of how many distinct words occur exactly \(n\) times, but under common Zipfian assumptions one useful estimate is:

\[
\text{NumberWordsOccur}(n) \approx \frac{V}{n(n + 1)}
\]

Where:

- \(\text{NumberWordsOccur}(n)\) = estimated number of unique words that appear exactly \(n\) times
- \(V\) = total number of unique words in the collection
- \(n\) = target frequency (e.g. 1 for hapax legomena)

**Note:** This is an approximation derived from Zipf-like rank–frequency structure. For exact counts on a given corpus, count from the frequency table directly:

```python
sum(1 for freq in word_counts.values() if freq == n)
```
