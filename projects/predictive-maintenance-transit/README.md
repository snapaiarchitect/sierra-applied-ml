# Predictive Maintenance for Transit Systems

> **Project 1** | Operations & Infrastructure | Time-Series Degradation + RUL Prediction
> **Status**: ✅ Executed on real NASA C-MAPSS FD001 data | **Date**: 2026-05-29

[![Status](https://img.shields.io/badge/Status-Complete-brightgreen)](.)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)](https://python.org)
[![Tech](https://img.shields.io/badge/ML-RandomForest%20%7C%20XGBoost-orange)]()

---

## 🎯 Business Problem

Transit agencies and fleet operators lose millions annually to unplanned asset failures. This system predicts which engines/assets will fail and when, enabling proactive maintenance scheduling and reducing unplanned downtime.

**Stakeholder:** Transit fleet operators, maintenance planners
**Success metric:** Reduce prediction error vs baseline by >40% (measured in MAE cycles)

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

## 📊 Results — Verified by Execution

**All metrics computed on real NASA CMAPSS FD001 data — executed 2026-05-29.**

| Model | MAE (cycles) | RMSE (cycles) | R² | vs Baseline |
|-------|:------------:|:-------------:|:--:|:-----------:|
| **Mean RUL Baseline** | **40.7** | **52.3** | **-0.59** | — |
| **Random Forest** | **24.3** | **35.5** | **0.27** | **+40% better** |
| **XGBoost** | **26.2** | **36.8** | **0.22** | **+36% better** |

**Baseline definition:** Predict the mean RUL of the training set (107.3 cycles) for every test engine. This is the simplest credible prediction strategy.

**Key Insight:** XGBoost reduces prediction error by 36% compared to the mean RUL baseline, translating to ~15 cycles of additional planning horizon for maintenance crews. Random Forest performs slightly better on this specific run, which is common for small datasets (100 engines) where ensemble variance can favor bagging over boosting.

**Validation:** Train/test split on engine IDs — 100 train engines (run-to-failure), 100 test engines (truncated before failure). True RUL provided for test set. No data leakage. StandardScaler fitted on train, applied to test.

**Execution Environment:** Python 3.12, scikit-learn 1.8, XGBoost 3.2

---

## 🖼️ Visualizations

| Figure | Description | File |
|--------|-------------|------|
| Predicted vs Actual RUL | Scatter plot showing model accuracy against true RUL | `predicted_vs_actual_rul.png` |
| Feature Importance | XGBoost top 15 features from rolling-window sensors | `feature_importance.png` |
| Residual Analysis | Distribution of prediction errors per model | `rul_residuals.png` |
| Sensor Degradation Curves | How 4 key sensors evolve over engine lifetime | `sensor_degradation_curves.png` |
| RUL Distributions | True vs predicted RUL histograms | `rul_distributions.png` |
| Sensor-RUL Correlation | Which sensors most predict failure | `sensor_rul_correlation.png` |
| Degradation Trajectories | Predicted RUL decline over time for sample engines | `rul_degradation_trajectories.png` |

**All figures generated from the executed notebook.** Run `notebooks/predictive_maintenance_analysis.ipynb` to reproduce.

---

## 📓 Notebook

**Primary Analysis**: `notebooks/predictive_maintenance_analysis.ipynb`

This notebook contains the full end-to-end pipeline:
1. Data loading from NASA C-MAPSS files
2. RUL computation for training engines
3. Feature engineering (rolling windows, standardization)
4. Model training (Random Forest, XGBoost, Mean RUL Baseline)
5. Evaluation on 100 test engines with true RUL labels
6. Visualization generation

**Note:** The notebook was executed on 2026-05-29 to produce the metrics above. The figures in `figures/` match this execution.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.12** | Core language |
| **Pandas** | Data manipulation |
| **NumPy** | Numerical computing |
| **scikit-learn** | StandardScaler, RandomForestRegressor, metrics |
| **XGBoost** | Gradient boosting regressor |
| **Matplotlib / Seaborn** | Visualization |

---

## 🚀 Quick Start

```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn xgboost

# Run the notebook
jupyter notebook notebooks/predictive_maintenance_analysis.ipynb

# Or execute directly
python notebooks/execute_real.py
```

---

## 📁 Project Structure

```
predictive-maintenance-transit/
├── data/
│   └── raw/              # NASA C-MAPSS FD001 files (train, test, RUL)
├── figures/              # 7 visualizations from executed notebook
├── notebooks/
│   └── predictive_maintenance_analysis.ipynb  # Primary analysis
├── src/                  # Data fetchers, preprocessors, model code
├── tests/                # Unit tests
├── results.json          # Real executed metrics (verified 2026-05-29)
└── README.md             # This file
```

---

## ✅ Reproducibility Checklist

- [x] Data source verified: NASA C-MAPSS FD001
- [x] Notebook executed end-to-end: 2026-05-29
- [x] Metrics verified: MAE, RMSE, R² from real execution
- [x] Figures match execution: All 7 PNGs regenerated from notebook
- [x] No synthetic data: 100% real NASA sensor readings
- [x] No data leakage: Train/test split on engine IDs
- [x] Baseline defined: Mean RUL predictor (simplest credible strategy)

---

## 📧 Contact

**Sierra Napier** — Data Scientist | AI Architect | MPA/MPH
- GitHub: [@gosidehustlesisi](https://github.com/gosidehustlesisi)
- Portfolio: [e3-ai.com](https://e3-ai.com)
- LinkedIn: [sierra-napier](https://linkedin.com/in/sierra-napier)

---

**License**: Data sourced from NASA Prognostics Center of Excellence. Code provided for portfolio and educational use.
