# Predictive Maintenance for Transit Systems

> **Project 1** | Operations & Infrastructure | Time-Series Degradation + RUL Prediction

[![Status](https://img.shields.io/badge/Status-Complete-brightgreen)](.)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)](https://python.org)
[![Tech](https://img.shields.io/badge/ML-RandomForest%20%7C%20XGBoost-orange)]()

---

## 🎯 Business Problem

Transit agencies and fleet operators lose millions annually to unplanned asset failures. This system predicts which engines/assets will fail and when, enabling proactive maintenance scheduling and reducing unplanned downtime.

**Stakeholder:** Transit fleet operators, maintenance planners
**Success metric:** Reduce prediction error vs baseline by >50% (measured in MAE cycles)

---

## 📊 Dataset

**Source**: [NASA Prognostics Center of Excellence](https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/)

**Direct Download**: The NASA CMAPSS Turbofan Engine Degradation Simulation Dataset is publicly available at the link above. This project uses the FD001 subset:

| File | Records | Description |
|------|---------|-------------|
| `train_FD001.txt` | 20,631 | 100 engines run-to-failure, 26 columns |
| `test_FD001.txt` | 13,096 | 100 engines truncated before failure |
| `RUL_FD001.txt` | 100 | True Remaining Useful Life per test engine |

**Columns**: Unit ID, Time (cycles), 3 Operating Settings, 21 Sensor Measurements

**Citation**: A. Saxena, K. Goebel, D. Simon, and N. Eklund, "Damage Propagation Modeling for Aircraft Engine Run-to-Failure Simulation", in Proceedings of the 1st International Conference on Prognostics and Health Management (PHM08), Denver CO, Oct 2008.

---

## 🏗️ Architecture

```
NASA CMAPSS Raw Data
       ↓
src/fetch_cmapss_data.py  (download + cache)
       ↓
Data Loading & Validation
       ↓
Feature Engineering (rolling windows, normalization, rate-of-change)
       ↓
RUL Prediction Models:
  ├── Mean RUL Baseline  (predict mean training RUL for all engines)
  ├── Random Forest
  └── XGBoost
       ↓
Model Evaluation (MAE, RMSE, R²) with baseline comparison
       ↓
Visualization & Reporting
```

---

## 📊 Results

### Baseline Comparison

All metrics computed on **real NASA CMAPSS FD001 data** — zero synthetic inputs.

| Model | MAE (cycles) | RMSE (cycles) | R² | vs Baseline |
|-------|:------------:|:-------------:|:--:|:-----------:|
| **Mean RUL Baseline** | ~45 | ~58 | 0.00 | — |
| **Random Forest** | ~16 | ~23 | 0.55 | **+64% better** |
| **XGBoost** | ~15 | ~22 | 0.58 | **+67% better** |

**Baseline definition:** Predict the mean RUL of the training set (100 engines run-to-failure) for every test engine. This is the simplest credible prediction strategy.

**Key Insight:** XGBoost reduces prediction error by 67% compared to the mean RUL baseline, translating to ~30 cycles of additional planning horizon for maintenance crews — the difference between scheduling maintenance next week vs. tomorrow.

**Validation:** Train/test split on engine IDs — 100 train engines (run-to-failure), 100 test engines (truncated before failure). True RUL provided for test set. No data leakage.

---

## 📦 Deliverables

| # | Deliverable | Description | Path | Status |
|---|-------------|-------------|------|--------|
| 1 | **Analysis Notebook** | Full EDA, feature engineering, baseline + RUL prediction, visualization | `notebooks/predictive_maintenance_analysis.ipynb` | ✅ Executed |
| 2 | **Final Notebook** | Polished version with executive summary | `notebooks/predictive_maintenance_analysis_FINAL.ipynb` | ✅ Executed |
| 3 | **Data Fetcher** | Automated CMAPSS download with retry logic | `src/fetch_cmapss_data.py` | ✅ Complete |
| 4 | **Dataset** | Real NASA CMAPSS FD001 | `data/raw/` | ✅ Downloaded |
| 5 | **Figures** | 7 generated visualizations from real data + baseline scatter | `figures/` | ✅ Generated |

**Total**: 2 notebooks | 1 source module | 3 data files | 7+ visualizations

---

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Fetch NASA CMAPSS data
python src/fetch_cmapss_data.py

# Run full pipeline
make data      # Download and validate data
make train     # Train baseline + RF + XGBoost
make test      # Run reproducibility checks
make figures   # Export figures to portfolio
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.10+ | Core language |
| pandas, numpy | Data manipulation |
| scikit-learn | Random Forest, StandardScaler, metrics |
| XGBoost | Gradient boosting regressor |
| matplotlib, seaborn | Visualization |

---

## 📈 Key Visualizations

| Figure | Description | File |
|--------|-------------|------|
| RUL distribution | Histogram of remaining useful life across training set | `figures/01_rul_distribution.png` |
| Sensor degradation | 21 sensors over time for sample engines | `figures/02_sensor_degradation.png` |
| RF predicted vs actual | Scatter with perfect prediction line | `figures/03_rf_predicted_vs_actual.png` |
| XGBoost predicted vs actual | Scatter with perfect prediction line | `figures/04_xgb_predicted_vs_actual.png` |
| Baseline predicted vs actual | Mean RUL baseline scatter | `figures/rul_baseline_scatter.png` |
| Residual analysis | Error distribution for both models | `figures/05_residuals.png` |
| Feature importance | Top 20 XGBoost features | `figures/06_feature_importance.png` |
| Degradation curves | Per-engine RUL over time | `figures/07_degradation_curves.png` |

---

## 🎓 Learning Outcomes

- Time-series feature engineering (rolling statistics, rate-of-change)
- Baseline-first evaluation strategy
- Multi-model comparison on prognostics data
- Residual analysis and error interpretation
- Operational impact quantification (planning horizon)

---

## ⚠️ Limitations & Future Work

- Dataset is simulation data, not real engine telemetry (but widely accepted as benchmark)
- Single operating condition (FD001); real engines have multiple flight regimes (FD002-FD004)
- No uncertainty quantification (point predictions only); would benefit from confidence intervals
- No real-time inference pipeline; batch predictions only
- Could extend to ensemble methods and deep learning (LSTM, Transformer)

---

## 📄 License

MIT License — free to use with attribution.

---

**About the Author:** Sierra Napier, MPA/MPH — AI Architect & Data Science Leader.
