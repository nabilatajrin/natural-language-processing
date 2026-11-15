# Experiment 04 — Zipf's Law

**Course:** PGD AI & ML (2024–25) · MIT WPU  
**Student:** Nabila Tajrin Bristy · PRN 1262243611

Analyze word-frequency rank distributions and verify **Zipf's Law** on a sample text.

---

## Folder structure

```text
04-zipfs-law/
├── README.md
├── requirements.txt
├── data/
│   └── ai_sample.txt
├── zipfs_law.py              # Full pipeline + plots
└── post_lab_answers.md       # Heap's law & Zipf frequency questions
```

---

## What this experiment does

1. Load text from local file (no Google Drive required)
2. Expand contractions, lowercase, keep alphabetic tokens, remove stopwords
3. Count word frequencies and assign ranks
4. Compute probabilities \(P(r)\) and \(r \cdot P(r)\)
5. Log–log plot of rank vs frequency (Zipf plot + regression)
6. Top-20 word bar chart
7. Cumulative frequency distribution

**Zipf's Law (simplified):**  
If words are ranked by frequency, frequency of rank \(r\) is approximately:

\[
f(r) \propto \frac{1}{r^{\alpha}}
\]

On a log–log plot, this appears roughly as a straight line with negative slope.

---

## Setup & run

```bash
cd 04-zipfs-law
pip install -r requirements.txt
python zipfs_law.py
```

Charts are saved under `images/` and shown on screen.

---

## Outputs

| File / plot | Description |
|-------------|-------------|
| `images/01_zipf_loglog.png` | Log rank vs log frequency + regression |
| `images/02_top_words.png` | Top 20 most frequent words |
| `images/03_cumulative.png` | Cumulative % coverage by rank |
| Console | Head of frequency / rank table |

---

## Post-lab

See [post_lab_answers.md](post_lab_answers.md) for:

1. Statement of **Heap's Law**
2. Estimating how many words appear exactly \(n\) times (Zipf-related)
