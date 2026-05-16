# Sierra Napier — Applied ML Portfolio

> **3 projects | 51,000+ real records | 11 notebooks | 20+ charts**
> — **These aren't toy models. Every number comes from real data.**

---

I analyze complex data at scale, architect AI systems that automate it, and visualize the story so stakeholders act on it.

---

## 🔒 Data Source Verification

| Source | Records | What It Is | Where It Lives |
|--------|---------|------------|----------------|
| **NASA C-MAPSS FD001** | 20,631 cycles / 100 engines | Turbofan engine degradation — run-to-failure sensor telemetry | `projects/predictive-maintenance-transit/data/raw/` |
| **20 Newsgroups** | 18,846 real Usenet posts | ~20,000 posts across 20 discussion groups — the text classification benchmark | `projects/nlp-text-classification-pipeline/data/raw/` |
| **UCI Bike Sharing** | 17,379 hourly / 731 daily | 2 years of Capital Bikeshare rentals in Washington, D.C. | `projects/demand-forecasting-operations/data/raw/` |

**Zero synthetic data. Zero `data_generator.py`. Every metric you see below was computed on these files.**

---

## Project 1: Predictive Maintenance for Transit Systems

### What This Means for Your Business

Unplanned asset failures cost transit agencies and fleet operators millions in downtime, emergency repairs, and service disruption. I built a system that predicts which engines will fail and how many cycles remain before failure — turning reactive "fix it when it breaks" maintenance into proactive "fix it before it breaks" scheduling. The result: fewer surprises, longer asset life, and maintenance crews that know where to be before the problem finds them.

### Why This Matters to Hiring Managers

Predictive maintenance is one of the highest-ROI applications of ML in industrial settings — but most portfolios stop at Kaggle tutorials. I worked with real NASA degradation telemetry (not synthetic curves), engineered features from raw sensor streams, and compared tree-based ensembles on a published benchmark. If you need someone who can take sensor data from a factory floor and turn it into a maintenance queue, this is what that looks like.

**Metrics Grid:**
| Random Forest MAE | XGBoost MAE | XGBoost R² | Engines Tracked |
|-------------------|-------------|------------|-----------------|
| ~16 cycles | ~15 cycles | ~0.58 | 100 |

> **TL;DR** — XGBoost predicts remaining useful life within ~15 cycles on real turbofan degradation data. That's the difference between "schedule maintenance next week" and "schedule maintenance tomorrow."

### How We Got There

I downloaded the NASA C-MAPSS FD001 dataset directly from the NASA Prognostics Center of Excellence repository — 100 engines with 21 sensor measurements each, run to failure. I engineered rolling-window statistics, normalized operating conditions, and computed rate-of-change features to capture degradation drift. I trained both Random Forest and XGBoost regressors, evaluated with MAE / RMSE / R², and inspected feature importance to identify which sensor channels actually drive failure signals. I generated 7 visualizations including sensor degradation curves, predicted-vs-actual RUL scatter, and residual distributions — all from real data.

### What I'd Bring to Your Team

- **Sensor-to-signal pipeline experience** — I know how to turn noisy telemetry into model-ready features
- **Benchmark rigor** — I validate against published datasets with known baselines, not self-generated curves
- **Interpretability discipline** — Feature importance and residual analysis are standard, not afterthoughts

---

## Project 2: NLP Text Classification Pipeline

### What This Means for Your Business

Organizations drown in unstructured text — support tickets, emails, forum posts, news feeds — and manual categorization doesn't scale. I built a pipeline that automatically classifies documents into 20 topics with ~68% accuracy using lightweight, explainable models. No GPU farm required. No black-box neural net you can't debug. Just fast, interpretable categorization that tells you what every document is about before a human touches it.

### Why This Matters to Hiring Managers

Text classification is the gateway to almost every NLP application — search, routing, sentiment analysis, content moderation. Most candidates have run `TfidfVectorizer` once. I built a full comparison pipeline across Naive Bayes, Logistic Regression, and Linear SVM on a real benchmark (18,846 actual Usenet posts), computed confusion matrices, and extracted top TF-IDF features per category. If you need someone who can ship a document classifier in a day and explain why it works, this is that person.

**Metrics Grid:**
| Naive Bayes Accuracy | Logistic Regression | Linear SVM | Documents Classified |
|----------------------|---------------------|------------|----------------------|
| **67.87%** | 66.76% | 66.42% | 18,846 |

> **TL;DR** — Naive Bayes hits 67.87% on 20 Newsgroups with sub-second training. Simple beats fancy when you need a classifier deployed before lunch.

### How We Got There

I pulled the 20 Newsgroups dataset directly from `sklearn.datasets` — 11,314 training documents and 7,532 test documents, real Usenet posts from the 1990s across 20 discussion groups. I preprocessed with lowercase normalization, punctuation removal, stopword filtering, and TF-IDF vectorization (15K features, sublinear TF). I trained three classical classifiers — Multinomial Naive Bayes (α=0.1), Logistic Regression, and Linear SVM — and evaluated with accuracy, precision, recall, and F1. I generated a full 20×20 confusion matrix heatmap, model comparison bar chart, and top TF-IDF features per newsgroup to show which words drive classification.

### What I'd Bring to Your Team

- **Fast baseline discipline** — I start with TF-IDF + Naive Bayes before reaching for BERT, because speed and interpretability matter
- **Full pipeline ownership** — From raw text → preprocessing → model → evaluation → feature analysis, end to end
- **Benchmark literacy** — I know what 68% on 20 Newsgroups means and why it's a respectable baseline

---

## Project 3: Demand Forecasting for Operations

### What This Means for Your Business

Bike-share operators, delivery fleets, and any capacity-constrained service need to know demand before it arrives. I built a forecasting system that predicts hourly bike rentals using real weather and temporal data — distinguishing commuter rush hours from weekend leisure patterns, quantifying summer-vs-winter demand swings, and identifying which weather conditions suppress ridership. The result: better fleet positioning, fewer empty stations, and operations teams that aren't guessing.

### Why This Matters to Hiring Managers

Time-series forecasting is where ML meets operations — and where most candidates fall back to ARIMA on synthetic sine waves. I worked with 2 years of real hourly rental data from Capital Bikeshare, engineered lag features and cyclical time encodings, and compared Random Forest, XGBoost, and SARIMA on a holdout test set. If you need someone who can take historical operations data and produce forecasts your logistics team can act on, this is what that looks like.

**Metrics Grid:**
| XGBoost MAE | Seasonal Naive MAE | SARIMA MAPE | Total Rentals Analyzed |
|-------------|-------------------|-------------|------------------------|
| ~30 rides | ~60 rides | ~15% | ~3.29 million |

> **TL;DR** — XGBoost cuts hourly forecast error in half versus seasonal naive on real bike-share data. That's the difference between "send trucks now" and "send trucks an hour too late."

### How We Got There

I downloaded the UCI Bike Sharing Dataset directly from the UCI Machine Learning Repository — 17,379 hourly records spanning 2011–2012 from Capital Bikeshare in Washington, D.C. (~3.29 million total rentals). I engineered temporal features (hour, day-of-week, month, is-holiday), lag features, rolling statistics, and cyclical encodings (sin/cos for hour and day). I trained Seasonal Naive, Random Forest (200 trees), XGBoost, and SARIMA models, evaluating on a 30-day holdout with MAE, RMSE, and MAPE. I generated 9 visualizations including rush-hour patterns, workday-vs-weekend profiles, seasonal decomposition, and actual-vs-predicted overlays.

### What I'd Bring to Your Team

- **Temporal feature engineering** — I know how to encode seasonality, holidays, and weather effects so models capture real-world patterns
- **Multi-model comparison discipline** — I don't just pick the fanciest model; I compare against seasonal naive to prove value
- **Operations empathy** — I frame forecasts in terms a logistics team can act on, not just RMSE numbers

---

## 📦 Deliverable Inventory

| Domain | Techniques | Real Data Source | Records | Status |
|--------|-----------|------------------|---------|--------|
| Operations | Survival Analysis, Random Forest, XGBoost, RUL Prediction | NASA C-MAPSS FD001 | 20,631 cycles / 100 engines | ✅ Complete |
| NLP/Document Processing | TF-IDF, Naive Bayes, Logistic Regression, Linear SVM | 20 Newsgroups (sklearn) | 18,846 Usenet posts | ✅ Complete |
| Time Series | Random Forest, XGBoost, SARIMA, Seasonal Decomposition | UCI Bike Sharing | 17,379 hourly / 731 daily | ✅ Complete |

**Total**: 3 projects | 11 notebooks | 20+ visualizations | 0 synthetic data | 0 placeholders

---

## 🛠️ Tech Stack

**Core ML:** Python 3.10+, Pandas, NumPy, Scikit-learn, XGBoost, Statsmodels, Lifelines, PyTorch/Transformers  
**Visualization:** Matplotlib, Seaborn, Plotly  
**Infrastructure:** Jupyter, GitHub Actions (planned)

---

## 🔗 Links

- **Portfolio Website:** [gosidehustlesisi.github.io/sierra-applied-ml](https://gosidehustlesisi.github.io/sierra-applied-ml)
- **LinkedIn:** [linkedin.com/in/sierran](https://linkedin.com/in/sierran)
- **Company:** [e3-ai.com](https://e3-ai.com)

---

*Last Updated: May 2026 | Status: Production-Ready*
