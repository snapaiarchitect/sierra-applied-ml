# Demand Forecasting for Operations

> **Project 3** | Time Series Forecasting | Real Public Data | Bike Sharing Demand

[![Status](https://img.shields.io/badge/Status-Complete-brightgreen)](.)
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

## 📊 Results

### Baseline Comparison (30-Day Holdout Test)

All models evaluated on real UCI Bike Sharing data — zero synthetic inputs.

| Model | MAE (rides) | RMSE (rides) | MAPE (%) | R² | vs Baseline |
|-------|:-----------:|:------------:|:--------:|:--:|:-----------:|
| **Seasonal Naive (baseline)** | ~82 | ~112 | ~22% | 0.42 | — |
| **Random Forest** | ~28 | ~41 | ~12% | 0.78 | **+66% better** |
| **XGBoost** | ~25 | ~38 | ~11% | 0.81 | **+70% better** |
| **SARIMA** | ~30 | ~44 | ~13% | 0.75 | **+63% better** |

**Baseline definition:** Predict the same hour from 7 days ago (168-hour lag). 
This is the simplest credible forecasting strategy for hourly bike demand.

**Key Insight:** XGBoost delivers 70% lower MAE than the seasonal naive baseline,
translating to ~57 fewer missed rentals per hour on average — critical for 
rebalancing operations and station capacity planning.

**Validation:** Time-series split — trained on 2011-2012 data through Nov 2012,
tested on final 30 days (Dec 2012). No data leakage.

---

## 📁 Deliverables

| # | Deliverable | Description | Path |
|---|-------------|-------------|------|
| 1 | **Fetch Script** | Download UCI data with retry/caching | `src/fetch_bike_data.py` |
| 2 | **Preprocessing** | Feature engineering pipeline | `src/preprocess.py` |
| 3 | **Evaluation** | Forecast metrics (MAE, RMSE, MAPE) | `src/evaluate.py` |
| 4 | **Forecasting** | Model wrapper (RF, XGB, ARIMA) | `src/forecast.py` |
| 5 | **Analysis Notebook** | Full EDA + baseline + modeling + visualization | `notebooks/demand_forecasting.ipynb` |
| 6 | **Final Notebook** | Polished version with executive summary | `notebooks/demand_forecasting_FINAL.ipynb` |
| 7 | **Data Dictionary** | Schema documentation | `data/DATA_DICTIONARY.md` |

---

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Fetch data
python src/fetch_bike_data.py

# Run full pipeline
make data      # Fetch and clean data
make train     # Train all models with baseline
make test      # Run reproducibility tests
make figures   # Export figures to portfolio
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.10+ | Core language |
| pandas, numpy | Data manipulation |
| scikit-learn | Random Forest, metrics |
| XGBoost | Gradient boosting regressor |
| statsmodels | SARIMA time-series model |
| matplotlib, seaborn | Visualization |

---

## 📈 Key Visualizations

| Figure | Description | File |
|--------|-------------|------|
| Hourly demand pattern | Rush-hour bimodal peaks (8 AM, 5-6 PM) | `figures/01_hourly_pattern.png` |
| Seasonal comparison | Summer 234 vs Winter 111 rentals/hr | `figures/02_seasonal_comparison.png` |
| Actual vs predicted | 30-day holdout with all 4 models | `figures/03_actual_vs_predicted.png` |
| Model comparison bar | MAE/RMSE/MAPE side-by-side | `figures/04_model_comparison.png` |
| Residual distribution | XGBoost error analysis | `figures/05_residuals.png` |

---

## 🎓 Learning Outcomes

- Time-series feature engineering (lag, rolling, cyclical encoding)
- Baseline-first evaluation strategy
- Multi-model comparison with holdout validation
- Seasonal decomposition and SARIMA parameterization
- Operational impact quantification (rebalancing efficiency)

---

## ⚠️ Limitations & Future Work

- Dataset ends in 2012; modern bikeshare systems have e-bikes and different usage patterns
- Weather data is simplified (categorical: clear/cloudy/rain/snow); real operations would use precipitation mm, wind speed, temperature
- Model does not account for station-level granularity; system-wide forecast only
- No real-time inference pipeline; batch predictions only

---

## 📄 License

MIT License — free to use with attribution.

---

**About the Author:** Sierra Napier, MPA/MPH — AI Architect & Data Science Leader.
