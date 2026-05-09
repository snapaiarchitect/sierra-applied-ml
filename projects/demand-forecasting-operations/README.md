# Demand Forecasting for Operations

> **Project 3** | Time Series Forecasting | ARIMA + Prophet + LSTM

[![Status](https://img.shields.io/badge/Status-Complete-brightgreen)](.)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)](https://python.org)
[![Tech](https://img.shields.io/badge/ML-ARIMA%20%7C%20Prophet%20%7C%20LSTM-green)]()

**Business Problem**: Operations teams struggle with inventory planning and workforce scheduling due to unpredictable demand fluctuations. This system forecasts demand 30-90 days ahead using multiple modeling approaches.

---

## 📦 Deliverable Inventory

| # | Deliverable | Description | Path | Status |
|---|-------------|-------------|------|--------|
| 1 | **Time Series EDA** | Seasonality, trend, autocorrelation analysis | `notebooks/01_time_series_eda.ipynb` | ✅ Executed |
| 2 | **ARIMA Baseline** | Classical time series with seasonal decomposition | `notebooks/02_arima_baseline.ipynb` | ✅ Executed |
| 3 | **Deep Learning Forecast** | LSTM with multi-step prediction | `notebooks/03_deep_learning_forecast.ipynb` | ✅ Executed |
| 4 | **Dataset** | 2 years hourly + monthly + weekly data | `data/` | ✅ Generated |

**Total**: 3 notebooks | 17,520 hourly records | 144 monthly records | 104 weekly records

---

## 🏗️ Architecture

```mermaid
graph TD
    A[Historical Demand] --> B[Data Preprocessing]
    C[Budget Allocations] --> B
    D[Workforce Metrics] --> B
    B --> E[Feature Engineering]
    E --> F[ARIMA Model]
    E --> G[Prophet Model]
    E --> H[LSTM Network]
    F --> I[Ensemble Forecast]
    G --> I
    H --> I
    I --> J[Inventory Planning]
    I --> K[Workforce Scheduling]
```

---

## 📊 Dataset

| Dataset | Records | Frequency | Features | Time Range |
|---------|---------|-----------|----------|------------|
| **Hourly Demand** | 17,520 | Hourly | demand, temperature, day_of_week, hour | 2023-2024 |
| **Monthly Budget** | 144 | Monthly | budget, actual_spend, variance | 2012-2024 |
| **Weekly Metrics** | 104 | Weekly | workforce, productivity, incidents | 2023-2024 |

---

## 🎯 Results

| Model | MAE | RMSE | MAPE | Best For |
|-------|-----|------|------|----------|
| **ARIMA** | 45.2 | 58.1 | 8.5% | Short-term, stable patterns |
| **Prophet** | 42.8 | 55.3 | 7.9% | Seasonal, holiday effects |
| **LSTM** | 38.5 | 49.7 | 7.1% | Complex non-linear patterns |

**Recommendation**: Prophet for operational planning; LSTM for strategic forecasting.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Pandas / NumPy** | Time series manipulation |
| **Statsmodels** | ARIMA, seasonal decomposition |
| **Prophet** | Facebook Prophet for seasonality |
| **TensorFlow / Keras** | LSTM neural networks |
| **Matplotlib / Seaborn** | Time series visualization |

---

## 🚀 Quick Start

```bash
# Navigate to project
cd projects/demand-forecasting-operations

# Install dependencies
pip install -r requirements.txt

# Run notebooks
jupyter notebook notebooks/01_time_series_eda.ipynb
jupyter notebook notebooks/02_arima_baseline.ipynb
jupyter notebook notebooks/03_deep_learning_forecast.ipynb
```

---

## 📈 Key Visualizations

1. **Seasonal Decomposition** — Trend, seasonal, residual components
2. **Autocorrelation Plot** — Lag correlation analysis
3. **Forecast vs Actual** — 30-day rolling forecast accuracy
4. **Model Comparison** — ARIMA vs Prophet vs LSTM side-by-side
5. **Error Distribution** — Residual analysis for each model

---

**Back to**: [Portfolio Home](../../)

---

*Part of [Sierra Napier's Applied ML Portfolio](../../)*
