# Assignment 02 — POS Tagging, Parsing & Logic

**Course:** Natural Language Processing Techniques  
**Student:** Nabila Tajrin Bristy · PRN 1262243611  
**Program:** PGD AI & ML (2024–25) · MIT WPU

Theory answers + runnable Python for HMM POS, Viterbi POS, and CYK parsing.

---

## Folder structure

```text
03-assignment-02-pos-parsing/
├── README.md
├── requirements.txt
├── 01_hmm_pos_tagging.py          # Q1 — POS with HMM (training corpus)
├── 02_viterbi_pos_tagging.py      # Q2 — POS with Viterbi
├── 03_cyk_parser.py               # Q3 — CYK parse of example sentence
├── 04_oracle_pp_attachment.md     # Q4 — oracle + PP-attachment ambiguity
└── 05_smart_home_logic.md         # Propositional + predicate logic rules
```

---

## Questions covered

| # | Topic | Deliverable |
|---|--------|-------------|
| 1 | POS tags for *"The dog barked loudly at the cat."* using **HMM** | `01_hmm_pos_tagging.py` |
| 2 | POS tags for *"The duck swam peacefully."* using **Viterbi** | `02_viterbi_pos_tagging.py` |
| 3 | Parse *"The black cat chased the white mouse."* with **CYK** | `03_cyk_parser.py` |
| 4 | Build an **oracle** for PP-attachment ambiguity | `04_oracle_pp_attachment.md` |
| — | Smart home security (**propositional / predicate logic**) | `05_smart_home_logic.md` |

---

## Run the code

```bash
cd 03-assignment-02-pos-parsing
pip install -r requirements.txt
python 01_hmm_pos_tagging.py
python 02_viterbi_pos_tagging.py
python 03_cyk_parser.py
```

No external data files required — training sentences are embedded in the scripts (from the assignment).

---

## Expected results (short)

**Q1 / HMM**

```text
[('The', 'Det'), ('dog', 'Noun'), ('barked', 'Verb'),
 ('loudly', 'Adverb'), ('at', 'Prep'), ('the', 'Det'), ('cat', 'Noun')]
```

**Q2 / Viterbi**

```text
[('The', 'Det'), ('duck', 'Noun'), ('swam', 'Verb'), ('peacefully', 'Adverb')]
```

**Q3 / CYK** — valid parse under the given CFG (`S → NP VP`, `NP → Det Adj Noun`, …).
