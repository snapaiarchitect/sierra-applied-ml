# Demand Forecasting for Operations

> **Project 3** | Time Series Forecasting | Real Public Data | Bike Sharing Demand
> **Status**: ✅ **FULLY EXECUTED** — Real metrics from UCI Bike Sharing (2026-05-30)

[![Status](https://img.shields.io/badge/Status-Complete-brightgreen)](.)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)](https://python.org)
[![Data](https://img.shields.io/badge/Data-UCI%20Bike%20Sharing-blue)]()
[![R²](https://img.shields.io/badge/Random%20Forest-R²%200.97-success)]()

---

## 📊 Data Source

**UCI Machine Learning Repository — Bike Sharing Dataset**

- **URL**: https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset
- **Citation**: Fanaee-T, H., & Gama, J. (2013). *Event labeling combining ensemble detectors and background knowledge*. Progress in Artificial Intelligence, 2(2-3), 113-127. DOI: https://doi.org/10.24432/C5W894
- **System**: Capital Bikeshare, Washington D.C.
- **Period**: 2011-01-01 to 2012-12-31
- **Records**: 17,379 hourly / 731 daily
- **Total rentals**: ~3.29 million

**This project uses 100% real data. No synthetic data anywhere.**

---

## 🎯 What This Project Demonstrates

| Capability | Demonstrated |
|------------|-------------|
| **Time-series forecasting** | Hourly and daily demand prediction |
| **Seasonal decomposition** | Trend, seasonal, residual extraction |
| **Feature engineering** | Lag features, rolling statistics, cyclical encodings |
| **Multiple models** | Seasonal naive, Random Forest, XGBoost, SARIMA |
| **Baseline comparison** | Naive vs ML models with improvement % |
| **Model evaluation** | MAE, RMSE, MAPE on holdout test set |
| **Real-world insight** | Weather impact, rush-hour patterns, growth curves |

---

## 🏗️ Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  UCI Bike Data  │────▶│  Feature Eng.    │────▶│  Random Forest  │
│  (hour.csv)     │     │  (time/lag/roll) │     │  XGBoost        │
└─────────────────┘     └──────────────────┘     │  SARIMA         │
                                                │  Seasonal Naive │
                                                └─────────────────┘
                                                          │
                                                ┌─────────────────┐
                                                │  Model Compare  │
                                                │  MAE/RMSE/MAPE  │
                                                │  (30-day holdout)│
                                                └─────────────────┘
```

---

## 📊 Real Results — Executed 2026-05-30

All metrics computed from **real UCI Bike Sharing data** with proper temporal split (train through Nov 2012, test Dec 2012).

| Model | MAE | RMSE | MAPE | R² | Notes |
|-------|-----|------|------|----|-------|
| **Random Forest** | **18.90** | **29.82** | **25.17%** | **0.97** | **Best performer**. Ensemble handles non-linear patterns. |
| **XGBoost** | 19.10 | 29.74 | 27.12% | 0.97 | Strong gradient boosting. Nearly tied with RF. |
| **Seasonal Naive** | 57.82 | 98.46 | 87.89% | 0.64 | Baseline. Predicts same hour from 7 days ago. |
| **SARIMA** | 1418.22 | 1779.18 | 92.92% | 0.01 | Poor fit. Model misspecification on hourly data. |

**Key insight:** ML models (RF/XGBoost) reduce MAE by **67%** vs seasonal naive. SARIMA failed on this dataset — we report it honestly rather than hiding it. This demonstrates proper model evaluation and baseline comparison.

**Feature importance:** Hour of day, temperature, lag_1h, and working day are the top predictors. Weather features (humidity, windspeed) have moderate impact.

---

## 🖼️ Visualizations

| Figure | Description | Status |
|--------|-------------|--------|
| Ensemble Forecast | Interactive forecast with model toggles | ✅ Generated |
| Feature Importance | CSV of feature importance scores | ✅ Generated |
| Forecast Predictions | CSV of predicted vs actual | ✅ Generated |
| Actual vs Predicted | Scatter plot with residuals | ✅ Generated |
| Model Comparison | Bar chart of MAE/RMSE/MAPE | ✅ Generated |
| Seasonal Decomposition | Trend + seasonal + residual | ✅ Generated |

**Interactive dashboard:** [🚀 Open Bike Sharing Dashboard](https://gosidehustlesisi.github.io/sierra-applied-ml/interactive-dashboards/bike-sharing.html)

---

## 📓 Notebook

**Primary Analysis**: `notebooks/demand_forecasting.ipynb`

This notebook contains:
1. Data loading from UCI ML Repository
2. Exploratory data analysis (hourly patterns, seasonality, weather)
3. Feature engineering (lag, rolling, cyclical encodings)
4. Seasonal decomposition
5. Model training (4 models)
6. Evaluation on 30-day holdout
7. Interactive dashboard generation

**Status:** ✅ **EXECUTED 2026-05-30** — All metrics are real.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.12** | Core language |
| **Pandas** | Data manipulation |
| **NumPy** | Numerical computing |
| **scikit-learn** | Random Forest, metrics |
| **XGBoost** | Gradient boosting |
| **statsmodels** | SARIMA |
| **Plotly** | Interactive dashboard |
| **Matplotlib** | Static visualizations |

---

## 🚀 Quick Start

```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn xgboost statsmodels plotly

# Run the notebook
jupyter notebook notebooks/demand_forecasting.ipynb
```

---

## 📁 Project Structure

```
demand-forecasting-operations/
├── data/
│   └── raw/              # UCI Bike Sharing files (hour.csv, day.csv)
├── figures/              # Interactive HTML + CSV outputs + PNGs
├── notebooks/
│   └── demand_forecasting.ipynb  # Primary analysis (EXECUTED)
├── src/                  # Data fetchers, preprocessors, forecast models
├── tests/                # Unit tests
├── results.json          # Real metrics from execution
└── README.md             # This file
```

---

## ✅ Reproducibility Checklist

- [x] Data source verified: UCI ML Repository
- [x] Code implemented: 4 models + evaluation
- [x] Notebook executed: **EXECUTED 2026-05-30**
- [x] Figures verified: Regenerated from executed notebook
- [x] No synthetic data: 100% real UCI bike sharing records
- [x] No data leakage: Time-series split, no future data in training
- [x] Baseline defined: Seasonal naive (same hour, 1 week ago)
- [x] Honest reporting: SARIMA failure documented, not hidden

---

## 📧 Contact

**Sierra Napier** — Data Scientist | AI Architect | MPA/MPH
- GitHub: [@gosidehustlesisi](https://github.com/gosidehustlesisi)
- Portfolio: [e3-ai.com](https://e3-ai.com)
- LinkedIn: [sierra-napier](https://linkedin.com/in/sierra-napier)

---

**License**: Data sourced from UCI Machine Learning Repository. Code provided for portfolio and educational use.
