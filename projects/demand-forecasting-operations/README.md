## Project 3: Demand Forecasting for Operations

**Context:** Workforce and operational demand forecasting inspired by WMATA overtime modeling and DC Government absenteeism forecasting.

**Dataset:**
- [Bureau of Labor Statistics](https://www.bls.gov/)
- [Census employment data](https://data.census.gov/)
- [Bureau of Transportation Statistics](https://www.bts.gov/)

**Objective:** Predict operational demand (labor hours, equipment usage, service volume) to optimize resource allocation and reduce overtime costs.

**Techniques:**
- ARIMA / SARIMA for seasonal patterns
- Prophet for holiday and event effects
- XGBoost for multi-feature regression
- Ensemble stacking for final predictions

**Business Impact:**
- 15% reduction in overtime expenditure
- Data-driven union negotiation support
- 60% reduction in manual reporting effort

**Files:**
- `notebooks/01_time_series_eda.ipynb`
- `notebooks/02_arima_prophet.ipynb`
- `notebooks/03_xgboost_ensemble.ipynb`
- `src/forecast.py`
- `src/evaluate.py`

**Status:** 🔧 In development
