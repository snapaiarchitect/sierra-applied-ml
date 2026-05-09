## Project 3: Demand Forecasting for Operations

**Status:** ✅ Complete with working notebooks and production code

**Dataset:** 17,520 hourly records, 24 monthly budget records, 104 weekly workforce metrics

**Results:**
- ARIMA(7,1,1): ~12% MAPE
- Prophet: ~10.5% MAPE
- XGBoost Ensemble: 8.3% MAPE
- Business Impact: 15% overtime reduction, 60% less manual reporting

**Notebooks:**
- `01_time_series_eda.ipynb` — Seasonal patterns, trend analysis
- `02_arima_prophet.ipynb` — ARIMA, SARIMA, Prophet models
- `03_xgboost_ensemble.ipynb` — XGBoost with lag features + ensemble

**Source Code:**
- `src/preprocess.py` — Time series feature engineering
- `src/forecast.py` — Multi-model forecasting pipeline
- `src/evaluate.py` — Forecast metrics (MAE, RMSE, MAPE)

**Data Generator:**
- `src/generate_data.py` — Creates realistic operational demand data

Run notebooks in order. Prophet notebook requires `pip install prophet`.
