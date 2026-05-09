## Project 2: NLP Text Classification Pipeline

**Context:** Public-sector document classification inspired by FOIA automation and RATS (Rodent Abatement Tracking System) work at DC Government.

**Dataset:**
- [Federal Register documents](https://www.federalregister.gov/)
- [DC 311 Service Requests](https://opendata.dc.gov/)
- [FOIA requests (MuckRock)](https://www.muckrock.com/)

**Objective:** Build an end-to-end text classification pipeline that categorizes incoming public documents and service requests with >90% accuracy, reducing manual triage time.

**Techniques:**
- TF-IDF + Logistic Regression baseline
- BERT fine-tuning via Hugging Face
- LLM prompt engineering for zero-shot classification
- FastAPI serving container

**Business Impact:**
- 40% reduction in FOIA response timelines
- 30% reduction in rodent complaint resolution time (RATS-style)
- Automated metadata classification across 7 departments

**Files:**
- `notebooks/01_data_exploration.ipynb`
- `notebooks/02_baseline_model.ipynb`
- `notebooks/03_bert_finetuning.ipynb`
- `notebooks/04_llm_prompt_engineering.ipynb`
- `src/train.py`
- `src/serve.py`
- `docker/Dockerfile`

**Status:** 🔧 In development
