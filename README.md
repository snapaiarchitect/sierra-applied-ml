# Sierra Napier — Applied ML Portfolio

> **Real public datasets for predictive maintenance, NLP, and demand forecasting — zero synthetic records.**

| **Project** | **Records** | **Source** | **Status** |
|---|---|---|---|
| Predictive Maintenance | 20,631 cycles / 100 engines | NASA C-MAPSS FD001 | Archived |
| NLP Text Classification | 18,846 real Usenet posts | 20 Newsgroups (sklearn) | Archived |
| Demand Forecasting | 17,379 hourly / 731 daily | UCI Bike Sharing | Archived |

**Total real records: 56,856+**

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/gosidehustlesisi/sierra-applied-ml.git
cd sierra-applied-ml

# Install dependencies
pip install -r requirements.txt

# Run notebooks (generates figures)
jupyter notebook projects/predictive-maintenance-transit/notebooks/01_nasa_data_exploration.ipynb
jupyter notebook projects/nlp-text-classification-pipeline/notebooks/01_20newsgroups_data_exploration.ipynb
jupyter notebook projects/demand-forecasting-operations/notebooks/01_bike_sharing_data_exploration.ipynb
```

---

## Data Sources & Citations

### NASA C-MAPSS FD001 — Predictive Maintenance
- **NASA Prognostics Center of Excellence**
  - URL: `https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/`
  - Files: `train_FD001.txt`, `test_FD001.txt`, `RUL_FD001.txt`
  - Records: 100 engines, 20,631 cycles, 21 sensor measurements
  - Task: Predict Remaining Useful Life (RUL) before engine failure

### 20 Newsgroups — NLP Text Classification
- **sklearn.datasets.fetch_20newsgroups**
  - URL: `https://scikit-learn.org/0.19/datasets/twenty_newsgroups.html`
  - Records: 11,314 training + 7,532 test documents
  - Categories: 20 discussion groups (comp.graphics, sci.space, talk.politics, etc.)
  - Task: Multi-class text classification

### UCI Bike Sharing — Demand Forecasting
- **UCI Machine Learning Repository**
  - URL: `https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset`
  - Files: `hour.csv` (17,379 records), `day.csv` (731 records)
  - Period: 2011–2012, Capital Bikeshare, Washington D.C.
  - Features: Weather, temperature, humidity, windspeed, season, hour, holiday
  - Task: Predict hourly bike rental demand

---

## Project Structure

```
sierra-applied-ml/
├── projects/
│   ├── predictive-maintenance-transit/
│   │   ├── data/raw/              # NASA C-MAPSS FD001
│   │   ├── figures/               # 7 visualizations
│   │   └── notebooks/
│   │       ├── 01_nasa_data_exploration.ipynb
│   │       ├── 02_feature_engineering.ipynb
│   │       └── 03_model_training.ipynb
│   │
│   ├── nlp-text-classification-pipeline/
│   │   ├── data/raw/              # 20 Newsgroups
│   │   ├── figures/               # 7 visualizations
│   │   └── notebooks/
│   │       ├── 01_20newsgroups_data_exploration.ipynb
│   │       ├── 02_text_preprocessing.ipynb
│   │       └── 03_model_comparison.ipynb
│   │
│   └── demand-forecasting-operations/
│       ├── data/raw/              # UCI Bike Sharing
│       ├── figures/               # 9 visualizations
│       └── notebooks/
│           ├── 01_bike_sharing_data_exploration.ipynb
│           ├── 02_feature_engineering.ipynb
│           └── 03_forecast_models.ipynb
│
├── requirements.txt
└── README.md
```

---

## Key Findings

### Predictive Maintenance (NASA C-MAPSS)
- **XGBoost MAE**: ~15 cycles (predicts failure within 15 operating cycles)
- **Random Forest MAE**: ~16 cycles
- **XGBoost R²**: ~0.58
- **Key insight**: Sensor 11 (HPC outlet temperature) and Sensor 4 (LPC outlet temperature) are the strongest predictors of engine degradation
- **Business impact**: Maintenance can be scheduled ~15 cycles before failure, reducing unplanned downtime

### NLP Text Classification (20 Newsgroups)
- **Naive Bayes Accuracy**: 67.87%
- **Logistic Regression**: 66.76%
- **Linear SVM**: 66.42%
- **Key insight**: Simple Naive Bayes with TF-IDF outperforms more complex models on this benchmark — speed and interpretability matter
- **Training time**: Sub-second for Naive Bayes on full dataset

### Demand Forecasting (UCI Bike Sharing)
- **XGBoost MAE**: ~30 rides per hour
- **Seasonal Naive MAE**: ~60 rides per hour (2× worse)
- **SARIMA MAPE**: ~15%
- **Key insight**: XGBoost cuts forecast error in half vs. seasonal naive by capturing weather + temporal interactions
- **Peak hours**: 8 AM and 5–6 PM (commuter rush), 12 PM (weekend leisure)

---

## Requirements

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost statsmodels
```

See `requirements.txt` for full dependency list.

---

## License

Data sourced from NASA, UCI Machine Learning Repository, and sklearn datasets. Code is provided as-is for portfolio and educational use.
