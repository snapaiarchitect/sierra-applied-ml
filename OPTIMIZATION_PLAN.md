# Sierra Applied ML — Portfolio Optimization Plan
> **Goal:** Transform this repo into a bulletproof proof-of-concept that signals senior IC or staff-level engineering judgment to hiring managers.

---

## Executive Summary

Your portfolio **presents beautifully** (README, live dashboards, badges) but **fails under scrutiny** (broken tests, dead code, requirements mismatches, README claims that don't match source code). Hiring managers at top-tier companies will run `pytest`, read `src/`, and check reproducibility. The current state risks undermining the strong visual polish with broken engineering fundamentals.

**The good news:** These are fixable, high-impact issues. Most can be resolved in a focused 1–2 day sprint.

---

## Severity Heatmap

| Area | Current Grade | Target Grade | Effort |
|---|---|---|---|
| README & First Impressions | A- | A+ | Low |
| Reproducibility & Dependencies | D+ | A | Medium |
| Test Coverage & CI/CD | D | A- | Medium |
| Code Quality & Dead Code | C- | B+ | Medium |
| Architecture & Modularity | C | B+ | High |
| Documentation Accuracy | C+ | A | Low |
| Live Dashboards & Pages | A- | A | Low |

---

## Phase 1: Stop the Bleeding (Critical — Do First)

### 1.1 Fix All Broken Tests
**Why:** A hiring manager's first command is usually `pytest`. Three projects, three test failures.

| Project | Failure | Fix |
|---|---|---|
| NLP | `ModuleNotFoundError: nltk` | Add `nltk` to `requirements.txt`; add `nltk.download('stopwords')` guard in `preprocess.py` |
| Demand Forecasting | `assert 27.12 < 0.25` (MAPE decimal vs %) | Fix `results.json` to store decimal MAPE (`0.2712`) OR fix test to compare percentage correctly |
| Predictive Maintenance | `ModuleNotFoundError: lifelines` | Add `lifelines` to `requirements.txt` OR remove `survival_model` from import test if it's dead code |

**Action:**
```bash
# Add missing deps to root requirements.txt
nltk>=3.8
lifelines>=0.27
streamlit>=1.30
scipy>=1.10
```

### 1.2 Requirements.txt is a Lie
**Current state:** `requirements.txt` at root lists 34 packages but misses key runtime dependencies (`nltk`, `lifelines`, `streamlit`, `scipy`, `pydantic`). Meanwhile it includes unused heavy packages (`prophet`, `transformers`, `torch`, `spacy`, `dbt-core`, `polars`, `mlflow`, `docker`) that slow install and may fail on some environments.

**Fix:**
- Audit every `import` statement across `projects/**/src/`.
- Split into **core** vs **optional** dependencies.
- Pin upper bounds for packages with known breaking changes (e.g., `scikit-learn<1.6`, `xgboost<3.0`).
- Add per-project `requirements.txt` files that the root one can reference or install via `-r`.

### 1.3 Remove Committed Cache & Generated Artifacts
**Current state:** 10 `__pycache__` directories exist in the working tree. While `git ls-files` shows 0 committed `.pyc` files (good), they clutter the repo and can accidentally get committed.

**Fix:**
```bash
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -name "*.pyc" -delete
# Then enforce in CI with a pre-commit hook or lint step
git rm -r --cached projects/**/data/processed/ 2>/dev/null || true
git rm -r --cached projects/**/figures/*.csv 2>/dev/null || true
```

---

## Phase 2: Code Quality & Engineering Rigor

### 2.1 Eliminate Dead Code & Orphan Modules
Dead code is a red flag for senior roles — it signals "I don't maintain my own work."

| File/Module | Issue | Recommendation |
|---|---|---|
| `predictive-maintenance/src/preprocess.py` | References non-existent `transit_assets.csv`, `failure_history.csv` | **Delete** or rewrite to integrate with NASA pipeline |
| `predictive-maintenance/src/survival_model.py` | Uses `lifelines`, reads non-existent `processed_features.csv` | **Delete** or move to an `archive/` branch |
| `predictive-maintenance/src/anomaly_detector.py` | Expects dataframes never produced by active pipeline | **Delete** |
| `predictive-maintenance/src/evaluate.py` | Contains NLP classification metrics docstring — copy-paste error | **Rewrite** for regression metrics |
| `predictive-maintenance/dashboard.py` | References WMATA/MTA data, not NASA C-MAPSS | **Rewrite** for NASA sensor data or delete |
| `nlp/src/train.py` | `train_bert_classifier()` — never called, requires `transformers`/`torch` | **Delete** or gate behind `[bert]` extras |
| `nlp/src/train.py` | `create_zero_shot_prompt()` — hardcoded gov doc categories | **Delete** |
| `nlp/src/serve.py` | Hardcoded 4-class labels for 20-class dataset | **Fix immediately** (see 2.2) |
| `demand-forecasting/src/forecast.py` | `EnsembleForecaster` exists but never used | **Wire it up** in `run_analysis.py` or delete |
| `demand-forecasting/src/fetch_bike_data_live.py` | Orphan — no consumer | **Add a notebook** showing live + historical merge, or move to `experiments/` |

### 2.2 Fix Critical Bugs in Running Code

**NLP `serve.py` — Label Map Mismatch (Critical)**
```python
# CURRENT (broken)
label_map = {0: 'Budget', 1: 'Policy', 2: 'Service_Request', 3: 'FOIA'}
# SHOULD BE
from sklearn.datasets import fetch_20newsgroups
label_map = dict(enumerate(fetch_20newsgroups(subset='train').target_names))
```

**Demand Forecasting `forecast.py` — Broken Future Projection**
- The `forecast()` method for tree-based models copies the last row and only increments `day_of_week`. It fails to update `hour`, `month`, cyclical encodings, and lag features.
- **Fix:** Implement a proper recursive forecasting loop that updates all derived features per step, or switch to a simpler direct-multi-step approach.

**Demand Forecasting `forecast.py` — Target Column Mismatch**
- Defaults to `target_col='demand'`; dataset uses `cnt`. Standardize on `cnt` or alias it at load time.

### 2.3 Standardize Code Style
**Current state:** 455 flake8 violations across `projects/`.

**Fix:**
1. Run `black` and `isort` across all `src/` and `tests/`.
2. Add a `.pre-commit-config.yaml` with `black`, `isort`, `flake8`.
3. Update CI to **fail** on format violations (currently `continue-on-error: true` on everything).

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.1.0
    hooks:
      - id: black
        language_version: python3
  - repo: https://github.com/PyCQA/isort
    rev: 5.13.0
    hooks:
      - id: isort
  - repo: https://github.com/PyCQA/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        args: ['--max-line-length=100', '--extend-ignore=E203,W503']
```

### 2.4 Add Type Hints
**Current state:** Minimal typing. `shared_api_fetchers.py` has some, core `src/` modules have almost none.

**Fix:** Add type hints to all public functions. Use `mypy --strict` on new code. This signals "I write code that scales to teams."

---

## Phase 3: Testing Strategy (Move from "Smoke Tests" to "Real Tests")

### 3.1 Current State: Structural Tests Only
Every project's `test_project.py` only checks that directories and files exist. This does not demonstrate testing skill.

### 3.2 Target State: Behavior-Verified Tests

**NLP Project:**
```python
def test_preprocess_text_normalizes_input():
    from src.preprocess import preprocess_text
    assert "graphics" in preprocess_text("The Graphics are great!!! 123")

def test_text_classifier_trains_and_predicts():
    from src.train import TextClassifier
    clf = TextClassifier()
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    assert len(preds) == len(X_test)
    assert set(preds).issubset(set(y_train))
```

**Demand Forecasting:**
```python
def test_create_lag_features_produces_expected_columns():
    from src.preprocess import create_lag_features
    df = pd.DataFrame({"cnt": [1, 2, 3, 4, 5]})
    result = create_lag_features(df, target_col="cnt", lags=[1, 2])
    assert "cnt_lag_1" in result.columns
    assert result["cnt_lag_1"].iloc[2] == 2.0
```

**Predictive Maintenance:**
```python
def test_create_features_adds_rolling_stats():
    from src.execute_analysis import create_features
    df = pd.DataFrame({"engine_id": [1, 1, 1], "sensor_2": [1.0, 2.0, 3.0]})
    result = create_features(df)
    assert "sensor_2_roll_mean_10" in result.columns
```

### 3.3 CI/CD: Make It Actually Gate Merges
**Current state:** The CI workflow has `continue-on-error: true` on every step and exits with 0 even on failure. This makes CI decorative, not functional.

**Fix:**
- Remove `continue-on-error: true` from lint, format, type-check, and test steps.
- Keep it **only** for notebook validation (which is inherently flaky).
- Use a `fail-fast: false` matrix for Python versions, but let actual failures fail the job.
- Remove the "auto-retry on failure" block — it's a hack that papers over real issues.

### 3.4 Notebook Execution CI: Actually Validate Output
**Current state:** `execute-notebooks.yml` runs papermill but never fails the job (`exit 0` hardcoded). It also overwrites the original `_FINAL.ipynb` files in place, which is risky.

**Fix:**
- Write outputs to `executed/` or `/tmp/` artifacts, don't overwrite source.
- Fail the job if any notebook fails (or at least post a PR comment).
- Add a step that validates key outputs (e.g., `results.json` exists and has expected schema).

---

## Phase 4: Architecture & Modularity

### 4.1 Unify the "Two Codebases" Problem (Predictive Maintenance)
The predictive maintenance project has:
- `execute_analysis.py` — monolithic, flat script that does everything
- `preprocess.py`, `evaluate.py`, `survival_model.py` — modular but disconnected

**Fix:**
1. Refactor `execute_analysis.py` into the modular `src/` structure:
   - `load_nasa.py` — data loading
   - `engineer_features.py` — feature engineering
   - `train_models.py` — model training
   - `evaluate.py` — evaluation & visualization
2. Delete or archive the transit-asset modules (`survival_model.py`, `anomaly_detector.py`).
3. Ensure `run_analysis.py` (or `make run`) calls the modular pipeline, not a 300-line flat script.

### 4.2 Align `run_analysis.py` with Notebooks
In NLP, `run_analysis.py` writes a flat JSON schema, but `dashboard.py` and tests expect a nested schema. **Standardize on one schema** and make `run_analysis.py` the single source of truth for reproducible headless execution.

### 4.3 Consolidate Duplicate Code
**Demand Forecasting:** `load_bike.py` and `preprocess.py` both define identical `load_hourly_data()`, `load_daily_data()`, etc. Move all I/O to `load_bike.py`, all feature engineering to `preprocess.py`.

### 4.4 Add a `Makefile` at Root
Provide one command to run everything:
```makefile
.PHONY: install test lint format clean all

install:
	pip install -r requirements.txt
	python -m nltk.downloader stopwords punkt

test:
	pytest projects/ -v --tb=short

lint:
	flake8 projects/ --max-line-length=100 --extend-ignore=E203,W503
	black --check projects/

format:
	black projects/
	isort projects/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete

all: install lint test
```

---

## Phase 5: README & Documentation Accuracy

### 5.1 Fix README-to-Code Mismatches

| README Claim | Reality | Fix |
|---|---|---|
| "Random Forest + XGBoost" in Predictive Maintenance | Only RF and XGB exist, but `results.json` mislabels XGB as "Best" when RF has lower MAE | Correct `results.json`; add a note about model selection |
| "Random Forest, XGBoost, SARIMA" in Demand Forecasting | Source code only has XGBoost, Linear, ARIMA. Random Forest and SARIMA don't exist | Either implement them or correct README |
| "Or execute directly: `python notebooks/execute_real.py`" | File doesn't exist | Correct to `python src/execute_analysis.py` or `make run` |
| "30-day holdout" in Demand Forecasting | Correct in code, but ensure it's explicit | Add a one-liner in README confirming the holdout date range |

### 5.2 Add a "Engineering Decisions" Section
Hiring managers love seeing *why* you chose X over Y. Add a short `docs/ENGINEERING_DECISIONS.md` or a section in README:
- "Why TF-IDF + Naive Bayes instead of BERT?" (speed, interpretability, no GPU needed)
- "Why XGBoost over Random Forest for RUL?" (or vice versa — just be accurate)
- "Why hold out the last 30 days instead of random split?" (temporal leakage)

### 5.3 Add a "What I'd Do Next" Section
This signals self-awareness and product thinking:
- "Add MLflow tracking for hyperparameter experiments"
- "Deploy FastAPI endpoint to Azure Container Apps with health checks"
- "Add drift detection for live bike-sharing data"

---

## Phase 6: MLOps & Deployment Signal

### 6.1 Add a Minimal `pyproject.toml`
Signals modern Python packaging:
```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "sierra-applied-ml"
version = "1.0.0"
description = "End-to-end applied ML portfolio"
requires-python = ">=3.10"
dependencies = [
    "pandas>=1.5",
    "numpy>=1.23",
    # ... core deps only
]

[project.optional-dependencies]
nlp = ["nltk>=3.8", "scikit-learn>=1.2"]
forecasting = ["xgboost>=1.7", "statsmodels>=0.14"]
maintenance = ["scipy>=1.10"]
dev = ["pytest", "black", "flake8", "mypy", "isort"]
```

### 6.2 Docker: Fix Security & Best Practices
**Current `Dockerfile` issues:**
- Runs Jupyter with `--allow-root` and no token (security risk if exposed)
- Copies everything before installing deps (invalidates cache on any code change)
- No multi-stage build
- Heavy base image for a portfolio

**Improved Dockerfile:**
```dockerfile
FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1
WORKDIR /app

# Install deps first for layer caching
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python -m nltk.downloader stopwords punkt

# Copy code last
COPY . .

EXPOSE 8888
# Use a token in production; empty token is only for local demo
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", \
     "--NotebookApp.token='sierra-ml-portfolio'"]
```

### 6.3 Health Monitor: Remove or Fix
The `health-monitor.yml` tries to read cross-repo workflow runs with `GITHUB_TOKEN`, which will always fail with 403. It's dead weight.

**Options:**
- **Delete** it (simplest).
- **Fix** it by adding a `CROSS_REPO_PAT` secret and using that token instead.
- **Replace** with a simple "check my links" workflow that validates all dashboard URLs return 200.

### 6.4 Add a Link Checker Workflow
Hiring managers will click your dashboard links. Make sure they work:
```yaml
name: Check Links
on:
  schedule: [cron: '0 0 * * 0']  # Weekly
  workflow_dispatch:
jobs:
  links:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: lycheeverse/lychee-action@v1
        with:
          args: --timeout 30 README.md docs/
```

---

## Phase 7: Quick Wins (High Impact, Low Effort)

1. **Add a `CONTRIBUTING.md`** — Even if you're the only contributor, it signals process.
2. **Add GitHub issue/PR templates** — Shows you think about maintainability.
3. **Add a `LICENSE` file** — MIT or Apache-2.0. Currently missing.
4. **Pin notebook execution order** — Add a cell at the top of each notebook: `# Run order: 1-Fetch → 2-Preprocess → 3-Train → 4-Evaluate`.
5. **Add `nbstripout`** to `.pre-commit-config.yaml` — Prevents committing notebook outputs (reduces repo bloat, ensures clean diffs).
6. **Add a "Run in Google Colab" badge** to each project README — One-click execution for hiring managers who don't want to clone.
7. **Fix `tatus` file at root** — Looks like a typo for `git status` output. Delete it.

---

## Suggested Implementation Order

| Day | Focus | Deliverable |
|---|---|---|
| **Day 1** | Stop the bleeding | Fixed tests, corrected `requirements.txt`, removed dead code, fixed `serve.py` labels |
| **Day 2 AM** | Code quality | Black/isort run, flake8 clean, type hints added, pre-commit hooks installed |
| **Day 2 PM** | CI/CD hardening | Remove `continue-on-error`, make CI gate merges, fix notebook execution |
| **Day 3 AM** | Architecture | Refactor predictive maintenance into modular src, align schemas, deduplicate code |
| **Day 3 PM** | Real tests | Add behavior-based unit tests for preprocess, train, evaluate in all 3 projects |
| **Day 4** | README & polish | Fix all README-to-code mismatches, add engineering decisions, Docker improvements |
| **Day 5** | MLOps signal | `pyproject.toml`, link checker, optional MLflow experiment tracking |

---

## Bottom Line

Your portfolio has **strong data storytelling** and **excellent visual polish**. The gap is in **engineering fundamentals**: tests that fail, dependencies that don't resolve, dead code that confuses readers, and CI that decorates rather than validates.

Fixing these doesn't require new projects or new models. It requires **maintenance discipline** — exactly what hiring managers look for in senior candidates. A portfolio that passes `pytest`, installs in one command, and has no dead code signals: *"I can ship production ML, not just notebooks."*
