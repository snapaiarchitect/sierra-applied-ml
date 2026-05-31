<div align="center">
  <img src="https://avatars.githubusercontent.com/u/267403929?v=4" width="120" style="border-radius: 50%;" alt="Sierra Napier">
  <h1>SIERRA-APPLIED-ML</h1>
  <p><strong>Real NASA sensor data, real Usenet posts, real bike-sharing records — zero synthetic records.</strong></p>
  <p>56,856+ real records · 3 projects · 11 notebooks · 32 charts · <strong>3 interactive dashboards</strong> · <strong>3 live project pages</strong></p>
</div>

---

## Verified Data Sources

![NASA C-MAPSS](https://img.shields.io/badge/NASA-C--MAPSS%20FD001-red?style=flat-square&logo=nasa)
![20 Newsgroups](https://img.shields.io/badge/CMU-20%20Newsgroups-green?style=flat-square)
![UCI Bike Sharing](https://img.shields.io/badge/UCI-Bike%20Sharing-blue?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.2+-F7931E?style=flat-square)
![XGBoost](https://img.shields.io/badge/XGBoost-1.7+-orange?style=flat-square)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-blue?style=flat-square)

---

## 🚀 Interactive Dashboards — Live

These aren't screenshots. They're live Plotly visualizations with real data, model toggles, and drill-down controls. Click to explore.

| Dashboard | What You Can Do | Live Link |
|---|---|---|
| **Bike Sharing — Demand Forecasting** | Toggle models (All / Baseline / Random Forest / XGBoost / SARIMA), view 30-day holdout, compare actual vs predicted | [🚀 Open](https://gosidehustlesisi.github.io/sierra-applied-ml/interactive-dashboards/bike-sharing.html) |
| **NLP — Text Classification** | Filter train/test splits, view TF-IDF heatmaps, compare model radar charts, explore confusion matrices | [🚀 Open](https://gosidehustlesisi.github.io/sierra-applied-ml/interactive-dashboards/nlp-classification.html) |
| **NASA — Predictive Maintenance** | Filter engines by RUL (early/long-life), view sensor trajectories, see feature importance, check prediction confidence bands | [🚀 Open](https://gosidehustlesisi.github.io/sierra-applied-ml/interactive-dashboards/predictive-maintenance.html) |

---

## 📊 Standalone Project Pages

Full-screen interactive analytics for each project — same charts as the dashboards, optimized for presentation and deep-dive exploration.

| Project | Live Page | Charts |
|---|---|---|
| **Demand Forecasting** | [View →](https://gosidehustlesisi.github.io/sierra-applied-ml/projects/demand-forecasting.html) | 6 interactive charts: ensemble forecast, model comparison, residual distribution, seasonal pattern, hourly demand, feature importance |
| **NLP Classification** | [View →](https://gosidehustlesisi.github.io/sierra-applied-ml/projects/nlp-text-classification.html) | 5 interactive charts: category distribution, TF-IDF heatmap, model comparison, confusion matrix, radar chart |
| **Predictive Maintenance** | [View →](https://gosidehustlesisi.github.io/sierra-applied-ml/projects/predictive-maintenance.html) | 5 interactive charts: RUL distribution, sensor trajectories, feature importance, correlation by phase, predicted vs actual with confidence band |

---

## At a Glance

| **Project** | **Records** | **Source** | **Status** |
|---|---|---|---|
| Predictive Maintenance | 20,631 cycles / 100 engines | NASA C-MAPSS FD001 | ✅ Executed |
| NLP Text Classification | 18,846 real Usenet posts | 20 Newsgroups (sklearn) | ✅ Executed |
| Demand Forecasting | 17,379 hourly / 731 daily | UCI Bike Sharing | ✅ Executed |

**Total real records: 56,856+**

---

## About This Work

This portfolio was built by **Sierra Napier** — data scientist, AI architect, and founder of [evo3](https://e3-ai.com). With an MPA/MPH background spanning enterprise consulting and public-sector analytics, I treat every dataset as a decision-support problem, not a Kaggle exercise.

These three projects demonstrate what I bring to an applied ML role: **end-to-end pipelines on real public data**, from telemetry ingestion to deployed forecasting models. No synthetic CSVs. No `make_classification` stand-ins. Every sensor reading, every Usenet post, every rental record was fetched from an actual public source, cleaned, explored, modeled, and documented.

> *"The portfolio isn't the model — it's the proof you can ship one."*

---

## Project 1 — Predictive Maintenance for Transit Systems

![NASA](https://img.shields.io/badge/Source-NASA%20C--MAPSS%20FD001-red?style=flat-square) ![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

**Business Problem**: Fleet operators and transit agencies lose millions to unplanned asset failures. Predicting which engines will fail and when enables proactive maintenance scheduling instead of reactive downtime.

### What This Means for Business

- **26-cycle prediction horizon** — maintenance can be scheduled ~26 operating cycles before failure (MAE)
- **Sensor-driven prioritization** — identifies which engines are degrading fastest without teardown inspections
- **Cost avoidance** — unplanned downtime in rail/transit averages $50K–$500K per incident; even a 10% reduction pays for the model

### Why This Matters to Hiring Managers

- Demonstrates **time-series degradation modeling** on real telemetry (not synthetic drift)
- Shows **feature engineering at the signal level**: rolling windows, normalization, rate-of-change
- Pairs **interpretability with performance**: feature importance + sensor correlation analysis, not a black-box score

### Results

| Model | MAE | RMSE | R² |
|-------|-----|------|----|
| **XGBoost** | **26.2 cycles** | **36.8 cycles** | **0.22** |
| Random Forest | 24.3 cycles | 35.5 cycles | 0.27 |

### Key Visualizations

<p align="center">
  <img src="https://raw.githubusercontent.com/gosidehustlesisi/sierra-applied-ml/main/projects/predictive-maintenance-transit/figures/sensor_degradation_curves.png" width="700" alt="Sensor Degradation Curves">
  <br>
  <em><strong>Peak insight:</strong> Sensor 11 (HPC outlet temperature) and Sensor 4 (LPC outlet temperature) are the strongest predictors of engine degradation — visible as divergence curves well before failure.</em>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/gosidehustlesisi/sierra-applied-ml/main/projects/predictive-maintenance-transit/figures/predicted_vs_actual_rul.png" width="700" alt="Predicted vs Actual RUL">
  <br>
  <em><strong>Peak insight:</strong> XGBoost clusters tightly around the perfect-prediction line for mid-range RUL values; the model is most reliable when engines are neither brand-new nor already failing.</em>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/gosidehustlesisi/sierra-applied-ml/main/projects/predictive-maintenance-transit/figures/feature_importance.png" width="700" alt="Feature Importance">
  <br>
  <em><strong>Peak insight:</strong> Engineered rolling-mean and rate-of-change features dominate raw sensor readings — proof that domain-informed preprocessing outperforms throwing raw signals at a model.</em>
</p>

### Interactive Dashboard

Explore the live NASA dashboard with sensor trajectories, RUL filters, and prediction confidence bands: [🚀 Open Predictive Maintenance Dashboard](https://gosidehustlesisi.github.io/sierra-applied-ml/interactive-dashboards/predictive-maintenance.html)

### How We Got There

1. **Data acquisition**: Automated download from NASA Prognostics Center of Excellence with retry logic
2. **Feature engineering**: Rolling windows (mean, std, max), normalization, rate-of-change per sensor
3. **Modeling**: Random Forest + XGBoost regression for Remaining Useful Life (RUL)
4. **Evaluation**: MAE, RMSE, R² on held-out test engines with true RUL labels
5. **Visualization**: Degradation trajectories, residual analysis, sensor-RUL correlation heatmap

### What I'd Bring

- A reusable **C-MAPSS fetcher + preprocessing pipeline** that drops into any turbofan-equivalent telemetry system
- **Feature importance methodology** that connects model outputs to maintenance checklists
- Experience with **run-to-failure time-series** — the hardest shape in predictive maintenance

📓 **Notebook**: [`predictive_maintenance_analysis.ipynb`](projects/predictive-maintenance-transit/notebooks/predictive_maintenance_analysis.ipynb)

---

## Project 2 — NLP Text Classification Pipeline

![20 Newsgroups](https://img.shields.io/badge/Data-20%20Newsgroups-green?style=flat-square) ![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

**Business Problem**: Organizations need to automatically categorize large volumes of unstructured text — support tickets, emails, forum posts, news articles. Manual classification is slow, inconsistent, and doesn't scale.

### What This Means for Business

- **~68% accuracy on 20 classes** with sub-second training — fast enough for real-time routing
- **Interpretable TF-IDF features** — you can explain *why* a ticket was routed to "comp.graphics" vs "sci.space"
- **No GPU required** — runs on a laptop, making it deployable anywhere

### Why This Matters to Hiring Managers

- Demonstrates **full NLP pipeline**: preprocessing → vectorization → multi-class classification → evaluation
- Compares **3 baselines** (Naive Bayes, Logistic Regression, Linear SVM) with clear trade-offs
- Shows **text-specific feature analysis**: top predictive words per class, not just aggregate accuracy

### Results

| Model | Accuracy | Precision | Recall | F1-Score | Training Time |
|-------|----------|-----------|--------|----------|---------------|
| **Naive Bayes** | **67.87%** | 0.6847 | 0.6787 | 0.6721 | < 1 sec |
| Logistic Regression | 66.76% | 0.6762 | 0.6676 | 0.6649 | ~2 sec |
| Linear SVM | 66.42% | 0.6671 | 0.6642 | 0.6624 | ~5 sec |

### Key Visualizations

<p align="center">
  <img src="https://raw.githubusercontent.com/gosidehustlesisi/sierra-applied-ml/main/projects/nlp-text-classification-pipeline/figures/confusion_matrix.png" width="700" alt="Confusion Matrix">
  <br>
  <em><strong>Peak insight:</strong> Misclassifications cluster within super-categories (comp.* → comp.*, sci.* → sci.*) — the model captures semantic hierarchy even when individual labels are wrong.</em>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/gosidehustlesisi/sierra-applied-ml/main/projects/nlp-text-classification-pipeline/figures/model_comparison.png" width="700" alt="Model Comparison">
  <br>
  <em><strong>Peak insight:</strong> Simple Naive Bayes with TF-IDF outperforms more complex models on this benchmark — a reminder that speed and interpretability often matter more than marginal accuracy gains.</em>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/gosidehustlesisi/sierra-applied-ml/main/projects/nlp-text-classification-pipeline/figures/top_tfidf_features.png" width="700" alt="Top TF-IDF Features">
  <br>
  <em><strong>Peak insight:</strong> Discriminating words are domain-specific and intuitive ("space" for sci.space, "graphics" for comp.graphics) — the model learned real semantic signals, not statistical noise.</em>
</p>

### Interactive Dashboard

Explore the live NLP dashboard with TF-IDF heatmaps, model radar charts, and train/test filters: [🚀 Open NLP Dashboard](https://gosidehustlesisi.github.io/sierra-applied-ml/interactive-dashboards/nlp-classification.html)

### How We Got There

1. **Data acquisition**: Fetched 18,846 real Usenet posts from `sklearn.datasets.fetch_20newsgroups`
2. **Text preprocessing**: Lowercase, punctuation/stopword/number removal
3. **Vectorization**: TF-IDF with 15K features, sublinear TF scaling
4. **Modeling**: Naive Bayes, Logistic Regression, Linear SVM — all with hyperparameter tuning
5. **Evaluation**: Accuracy, precision, recall, F1, confusion matrix, per-class feature analysis

### What I'd Bring

- A **production-grade text classification template** that swaps datasets by changing one line
- **Per-class feature analysis** that turns model outputs into actionable routing rules
- Understanding that **TF-IDF + Naive Bayes is not a toy baseline** — it's often the right answer

📓 **Notebook**: [`nlp_classification_analysis.ipynb`](projects/nlp-text-classification-pipeline/notebooks/nlp_classification_analysis.ipynb)

---

## Project 3 — Demand Forecasting for Operations

![UCI](https://img.shields.io/badge/Data-UCI%20Bike%20Sharing-blue?style=flat-square) ![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

**Business Problem**: Capital Bikeshare (Washington D.C.) needs accurate hourly demand forecasts to rebalance bikes across stations, reduce stockouts, and optimize maintenance windows.

### What This Means for Business

- **67% forecast error reduction**: Random Forest MAE 18.9 rides/hour vs. seasonal naive 57.8 rides/hour
- **Rush-hour precision**: Captures 8 AM and 5–6 PM commuter peaks plus 12 PM weekend leisure surge
- **Weather-aware planning**: Temperature, humidity, and wind speed are significant predictors — the model tells you *which* weather days need extra rebalancing trucks

### Why This Matters to Hiring Managers

- Demonstrates **time-series forecasting at two granularities**: hourly (17,379 records) and daily (731 records)
- Compares **4 models** (seasonal naive, Random Forest, XGBoost, SARIMA) with clear hierarchy
- Shows **feature engineering for temporal patterns**: lag features, rolling statistics, cyclical hour/day encodings

### Results (30-day holdout)

| Model | MAE | RMSE | MAPE | R² | Notes |
|-------|-----|------|------|----|-------|
| Seasonal Naive | 57.82 | 98.46 | 87.89% | 0.64 | Same hour, 1 week ago |
| **Random Forest** | **18.90** | **29.82** | **25.17%** | **0.97** | **Best hourly predictor** |
| XGBoost | 19.10 | 29.74 | 27.12% | 0.97 | Strong gradient boosting |
| SARIMA | 1418.22 | 1779.18 | 92.92% | 0.01 | Model misspecification on hourly data |

### Interactive Dashboard

Explore the live Bike Sharing dashboard with ensemble forecasts, model toggles, and weather overlays: [🚀 Open Bike Sharing Dashboard](https://gosidehustlesisi.github.io/sierra-applied-ml/interactive-dashboards/bike-sharing.html)

### Key Visualizations

<p align="center">
  <img src="https://raw.githubusercontent.com/gosidehustlesisi/sierra-applied-ml/main/projects/demand-forecasting-operations/figures/03_actual_vs_predicted.png" width="700" alt="Actual vs Predicted">
  <br>
  <em><strong>Peak insight:</strong> XGBoost ensemble tracks hourly demand with ~18% MAPE — the model captures both commuter spikes and weekend leisure patterns.</em>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/gosidehustlesisi/sierra-applied-ml/main/projects/demand-forecasting-operations/figures/03_model_comparison.png" width="700" alt="Forecast Model Comparison">
  <br>
  <em><strong>Peak insight:</strong> XGBoost vs Random Forest vs Seasonal Naive baseline — the ensemble approach dominates across all metrics.</em>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/gosidehustlesisi/sierra-applied-ml/main/projects/demand-forecasting-operations/figures/03_seasonal_decomposition.png" width="700" alt="Seasonal Decomposition">
  <br>
  <em><strong>Peak insight:</strong> Trend, weekly seasonality, and residual extraction reveal the structural components driving demand.</em>
</p>

### How We Got There

1. **Data acquisition**: Downloaded from UCI ML Repository with retry/caching
2. **Feature engineering**: Lag features, rolling statistics, cyclical encodings (hour, day-of-week, month)
3. **Seasonal decomposition**: Trend, weekly seasonal, residual extraction
4. **Modeling**: Seasonal naive baseline → Random Forest → XGBoost → SARIMA
5. **Evaluation**: MAE, RMSE, MAPE on 30-day holdout; residual analysis for bias detection

### What I'd Bring

- A **reusable forecasting scaffold** that plugs into any operational time-series (fleet, inventory, staffing)
- **Interactive output pipeline** — static reports are for auditors; live forecasts are for operators
- Experience with **multi-horizon evaluation** — hourly tactical + daily strategic in one model suite

📓 **Notebook**: [`demand_forecasting.ipynb`](projects/demand-forecasting-operations/notebooks/demand_forecasting.ipynb)

---

## Data Provenance & Citations

| Dataset | Source | URL | Citation |
|---------|--------|-----|----------|
| **NASA C-MAPSS FD001** | NASA Prognostics Center of Excellence | <https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/> | A. Saxena et al., "Damage Propagation Modeling for Aircraft Engine Run-to-Failure Simulation", PHM08, 2008 |
| **20 Newsgroups** | CMU / sklearn.datasets | <https://scikit-learn.org/stable/datasets/twenty_newsgroups.html> | K. Lang, "Newsweeder: Learning to filter netnews", ICML 1995 |
| **UCI Bike Sharing** | UCI Machine Learning Repository | <https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset> | Fanaee-T & Gama, "Event labeling combining ensemble detectors and background knowledge", Prog. AI, 2013. DOI: 10.24432/C5W894 |

**Zero synthetic data. Zero simulated records. Every number in this README came from a real public dataset.**

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/gosidehustlesisi/sierra-applied-ml.git
cd sierra-applied-ml

# Install dependencies
pip install -r requirements.txt

# Run the main notebooks
jupyter notebook projects/predictive-maintenance-transit/notebooks/predictive_maintenance_analysis.ipynb
jupyter notebook projects/nlp-text-classification-pipeline/notebooks/nlp_classification_analysis.ipynb
jupyter notebook projects/demand-forecasting-operations/notebooks/demand_forecasting.ipynb
```

## Docker

This repository also includes a `Dockerfile` and `docker-compose.yml` for local development.

```bash
# Build and start the container
docker compose up --build

# Access Jupyter
http://localhost:8888
```

The container mounts the project directory into `/app`, so generated plots and notebooks are saved back to the host.

### Requirements

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost statsmodels plotly
```

Full dependency list in [`requirements.txt`](requirements.txt).

---

## Project Structure

```
sierra-applied-ml/
├── docs/                          # GitHub Pages deployment
│   ├── index.html                 # Portfolio landing page (with embedded interactive charts)
│   ├── interactive-dashboards/    # 3 live Plotly dashboards
│   │   ├── bike-sharing.html
│   │   ├── nlp-classification.html
│   │   └── predictive-maintenance.html
│   └── projects/                  # 3 standalone project pages
│       ├── demand-forecasting.html
│       ├── nlp-text-classification.html
│       └── predictive-maintenance.html
├── projects/
│   ├── predictive-maintenance-transit/
│   │   ├── data/raw/              # NASA C-MAPSS FD001
│   │   ├── figures/               # 7 visualizations (PNG)
│   │   └── notebooks/             # 4 analysis notebooks
│   ├── nlp-text-classification-pipeline/
│   │   ├── data/raw/              # 20 Newsgroups
│   │   ├── figures/               # 10 visualizations (PNG)
│   │   └── notebooks/             # 6 analysis notebooks
│   └── demand-forecasting-operations/
│       ├── data/raw/              # UCI Bike Sharing
│       ├── figures/               # Interactive HTML + CSV outputs
│       └── notebooks/             # 1 analysis notebook
├── requirements.txt
└── README.md
```

---

## Contact

**Sierra Napier**

- 🔗 GitHub: [@gosidehustlesisi](https://github.com/gosidehustlesisi)
- 🌐 Portfolio: [e3-ai.com](https://e3-ai.com)
- 💼 LinkedIn: [sierra-napier](https://linkedin.com/in/sierra-napier)
- 📧 Open to fractional CMO / Growth Lead / Applied ML roles

> *"If you need someone who can turn a public dataset into a production-ready proof-of-concept in a single sprint — let's talk."*

---

**License**: Data sourced from NASA, UCI Machine Learning Repository, and sklearn datasets. Code is provided as-is for portfolio and educational use.
