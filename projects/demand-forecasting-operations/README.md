# Demand Forecasting for Operations

> **Project 3** | Time Series Forecasting | Real Public Data | Bike Sharing Demand
> **Status**: Code complete — Execute notebook to generate real metrics

[![Status](https://img.shields.io/badge/Status-Code%20Complete-yellow)](.)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)](https://python.org)
[![Data](https://img.shields.io/badge/Data-UCI%20Bike%20Sharing-blue)]()

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

## 📊 Results — Execute Notebook to Generate

**The code is implemented. The metrics are pending execution.**

This notebook implements all 4 models and evaluation metrics, but the specific MAE/RMSE/MAPE values in previous versions were **fabricated by a previous build** and never verified. The honest path is to execute the notebook and get real numbers.

| Model | MAE | RMSE | MAPE | Status |
|-------|-----|------|------|--------|
| Seasonal Naive (baseline) | TBD | TBD | TBD | ✅ Implemented |
| Random Forest | TBD | TBD | TBD | ✅ Implemented |
| XGBoost | TBD | TBD | TBD | ✅ Implemented |
| SARIMA | TBD | TBD | TBD | ✅ Implemented |

**To get real metrics:**
```bash
jupyter notebook notebooks/demand_forecasting.ipynb
```

**Validation:** Time-series split — trained on 2011-2012 data through Nov 2012, tested on final 30 days (Dec 2012). No data leakage.

**Expected behavior:** XGBoost with engineered time/lag/rolling features should outperform the seasonal naive baseline. The exact improvement % will be determined by execution.

---

## 🖼️ Visualizations

| Figure | Description | Status |
|--------|-------------|--------|
| Ensemble Forecast | Interactive forecast with model toggles | ✅ Generated |
| Feature Importance | CSV of feature importance scores | ✅ Generated |
| Forecast Predictions | CSV of predicted vs actual | ✅ Generated |

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

**Note:** The notebook was written but not executed for the initial build. Execute it to get real metrics.

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
├── figures/              # Interactive HTML + CSV outputs
├── notebooks/
│   └── demand_forecasting.ipynb  # Primary analysis
├── src/                  # Data fetchers, preprocessors, forecast models
├── tests/                # Unit tests
├── results.json          # Honest template (execute notebook to populate)
└── README.md             # This file
```

---

## ✅ Reproducibility Checklist

- [x] Data source verified: UCI ML Repository
- [x] Code implemented: 4 models + evaluation
- [ ] Notebook executed: **PENDING** — Execute to get real metrics
- [ ] Figures verified: **PENDING** — Regenerate from executed notebook
- [x] No synthetic data: 100% real UCI bike sharing records
- [x] No data leakage: Time-series split, no future data in training
- [x] Baseline defined: Seasonal naive (same hour, 1 week ago)

---

## 📧 Contact

**Sierra Napier** — Data Scientist | AI Architect | MPA/MPH
- GitHub: [@gosidehustlesisi](https://github.com/gosidehustlesisi)
- Portfolio: [e3-ai.com](https://e3-ai.com)
- LinkedIn: [sierra-napier](https://linkedin.com/in/sierra-napier)

---

**License**: Data sourced from UCI Machine Learning Repository. Code provided for portfolio and educational use.
