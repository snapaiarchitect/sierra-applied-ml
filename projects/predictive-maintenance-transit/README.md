## Project 1: Predictive Maintenance for Transit Systems

**Context:** WMATA-inspired scenario using real transit maintenance data.

**Dataset:**
- [FTA National Transit Database](https://www.transit.dot.gov/ntd)
- [WMATA Open Data](https://www.wmata.com/)
- [NYC MTA Data](https://new.mta.info/developers)

**Objective:** Predict rail and bus component failures before they occur, enabling proactive maintenance scheduling and reducing unplanned service disruptions.

**Techniques:**
- Survival analysis (Kaplan-Meier, Cox PH)
- Time-series anomaly detection (Isolation Forest, LSTM autoencoder)
- Feature engineering from sensor telemetry and maintenance logs

**Business Impact:**
- 25% reduction in unplanned outages
- 18% extension of asset lifecycle
- $1M+ in predictive maintenance savings

**Files:**
- `notebooks/01_eda_and_preprocessing.ipynb`
- `notebooks/02_survival_analysis.ipynb`
- `notebooks/03_anomaly_detection.ipynb`
- `src/train_model.py`
- `src/predict.py`
- `src/evaluate.py`

**Status:** 🔧 In development
