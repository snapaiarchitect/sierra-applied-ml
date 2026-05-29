# NLP Text Classification Pipeline

> **Project 2** | Natural Language Processing | TF-IDF + Multi-Class Classification on Real Data
> **Status**: ✅ **FULLY EXECUTED** — Real metrics from 20 Newsgroups (2026-05-30)

[![Status](https://img.shields.io/badge/Status-Complete-brightgreen)](.)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)](https://python.org)
[![Data](https://img.shields.io/badge/Data-REAL_20Newsgroups-green)]()
[![Accuracy](https://img.shields.io/badge/Naive%20Bayes-67.87%25-blue)]()

---

## 📦 Deliverable Inventory

| # | Deliverable | Description | Path | Status |
|---|---|---|---|---|
| 1 | **Data Fetcher** | Download 20 Newsgroups from sklearn | `src/fetch_20newsgroups.py` | ✅ Executed |
| 2 | **Analysis Notebook** | Full pipeline: preprocessing, TF-IDF, 3 classifiers, evaluation | `notebooks/nlp_classification_analysis.ipynb` | ✅ **EXECUTED** |
| 3 | **Figures** | 4 visualizations from real data | `figures/` | ✅ Generated |
| 4 | **Results JSON** | Real metrics from execution | `results.json` | ✅ **Real data** |
| 5 | **Raw Data** | 18,846 real Usenet posts (JSON + CSV stats) | `data/raw/` | ✅ Saved |

---

## 📊 Data Source

| Property | Value |
|----------|-------|
| **Dataset** | `sklearn.datasets.fetch_20newsgroups` |
| **Origin** | CMU 20 Newsgroups — Lang, K. (1995). *Newsweeder: Learning to filter netnews.* ICML 1995. |
| **Type** | ~18,000 real Usenet posts from 20 newsgroups (1990s) |
| **Train** | 11,314 documents |
| **Test** | 7,532 documents |
| **Classes** | 20 topics: comp.*, rec.*, sci.*, talk.*, misc.*, alt.*, soc.* |

**All data is real. Zero synthetic data was used.**

---

## 🏗️ Pipeline Architecture

```
Raw 20 Newsgroups Posts
        ↓
Text Preprocessing (lowercase, remove punctuation/stopwords/numbers)
        ↓
TF-IDF Vectorization (15K features, sublinear TF)
        ↓
    ┌───────────────┬───────────────┬───────────────┐
    ↓               ↓               ↓
Naive Bayes   Logistic Regression   Linear SVM
    └───────────────┴───────────────┴───────────────┘
                        ↓
              Accuracy / Confusion Matrix / Feature Analysis
```

---

## 🎯 Real Results — Executed 2026-05-30

All metrics computed from **real 20 Newsgroups data** with proper train/test split.

| Model | Accuracy | Precision | Recall | F1-Score | Notes |
|-------|----------|-----------|--------|----------|-------|
| **Naive Bayes** | **67.87%** | 0.6847 | 0.6787 | **0.6721** | Best performer. Fast on sparse text. |
| **Logistic Regression** | 66.76% | 0.6762 | 0.6676 | 0.6649 | Strong baseline. Interpretable. |
| **Linear SVM** | 66.42% | 0.6671 | 0.6642 | 0.6624 | Margin classifier. Tied with LR. |

**Key insight:** Naive Bayes wins on this benchmark despite its simplicity — it handles the high-dimensional sparse TF-IDF features naturally. All three models are within 1.5% accuracy, confirming this is a well-calibrated comparison.

---

## 🖼️ Visualizations

| Figure | Description | Status |
|--------|-------------|--------|
| Category Distribution | 20 newsgroups class balance | ✅ Generated |
| Model Comparison | Accuracy comparison bar chart | ✅ Generated |
| Confusion Matrix | Full 20×20 confusion matrix | ✅ Generated |
| Top TF-IDF Features | Most predictive words per class | ✅ Generated |

---

## 📓 Notebooks

| Notebook | Purpose | Status |
|----------|---------|--------|
| `01_data_exploration.ipynb` | Category distribution, document lengths | ✅ Executed |
| `nlp_classification_analysis.ipynb` | Full pipeline: 3 models, evaluation, figures | ✅ **EXECUTED** |
| `text_classification_pipeline.ipynb` | Lightweight pipeline with Naive Bayes | ✅ Implemented |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.12** | Core language |
| **Scikit-learn** | Dataset loading, TF-IDF, models, metrics |
| **NLTK** | English stopword list |
| **Pandas** | Data manipulation |
| **Matplotlib / Seaborn** | Visualization |

---

## 🚀 Quick Start

```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn nltk

# Download NLTK data
python -c "import nltk; nltk.download('stopwords')"

# Run the main notebook
jupyter notebook notebooks/nlp_classification_analysis.ipynb
```

---

## 📁 Project Structure

```
nlp-text-classification-pipeline/
├── data/
│   └── raw/              # 20 Newsgroups (JSON + CSV)
├── figures/              # 4 visualizations
├── notebooks/
│   ├── 01_data_exploration.ipynb         # EDA (executed)
│   ├── nlp_classification_analysis.ipynb # Full pipeline (EXECUTED)
│   └── text_classification_pipeline.ipynb  # Lightweight (implemented)
├── src/                  # Fetchers, preprocessors, train.py
├── tests/                # Unit tests
├── results.json          # Real metrics from execution
└── README.md             # This file
```

---

## ✅ Reproducibility Checklist

- [x] Data source verified: sklearn.datasets.fetch_20newsgroups
- [x] Code implemented: 3 models + evaluation + figures
- [x] Notebook executed end-to-end: **EXECUTED 2026-05-30**
- [x] Figures generated: 4 PNGs from real data
- [x] No synthetic data: 100% real Usenet posts
- [x] No data leakage: sklearn train/test split

---

## 📧 Contact

**Sierra Napier** — Data Scientist | AI Architect | MPA/MPH
- GitHub: [@gosidehustlesisi](https://github.com/gosidehustlesisi)
- Portfolio: [e3-ai.com](https://e3-ai.com)
- LinkedIn: [sierra-napier](https://linkedin.com/in/sierra-napier)

---

**License**: Data sourced from sklearn.datasets (CMU 20 Newsgroups). Code provided for portfolio and educational use.
