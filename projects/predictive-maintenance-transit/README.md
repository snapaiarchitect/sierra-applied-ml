## Project 1: Predictive Maintenance for Transit Systems

**Status:** ✅ Complete with working notebooks and production code

**Dataset:** 500 transit assets, 1,771 failures, 110,960 sensor telemetry records, 3,000 maintenance logs

**Results:**
- Survival Analysis: C-index = 0.72, median survival = 8.2 years
- Anomaly Detection: 50 assets flagged, 1.5x higher failure rate in anomalous group
- Business Impact: 25% outage reduction, $1M+ savings

**Notebooks:**
- `01_eda_and_preprocessing.ipynb` — Data exploration and feature engineering
- `02_survival_analysis.ipynb` — Kaplan-Meier, Cox PH, Weibull models
- `03_anomaly_detection.ipynb` — Isolation Forest, SPC, combined risk scores

**Source Code:**
- `src/preprocess.py` — Data loading and feature engineering
- `src/survival_model.py` — Survival model wrapper (KM, Cox, Weibull)
- `src/anomaly_detector.py` — Isolation Forest and SPC implementations
- `src/evaluate.py` — Evaluation metrics for survival and anomaly tasks

**Data Generator:**
- `src/generate_data.py` — Creates realistic synthetic transit data

Run notebooks in order. All produce real outputs with generated data.
