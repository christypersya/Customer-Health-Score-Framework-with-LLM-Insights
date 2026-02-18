# Customer Health Score Framework

## Production-Ready Customer Health Score (CHS) Framework with LLM Insights

Linking Customer Experience (CX) Metrics to Business Outcomes through Predictive Analytics and LLM-powered Insights

🚀 Overview

This project demonstrates a full end-to-end Customer Health Score (CHS) framework, covering all phases of the customer journey:

Learn → Buy → Get → Use → Pay → Renew

It combines:

- Predictive Modeling (LightGBM) per phase
- Explainable AI (SHAP) to identify key drivers
- LLM Insights (GPT-4) to generate business-friendly summaries
- Interactive Dashboard (Streamlit) for exploration

This is a public-friendly recreation of a production-level framework originally developed in a corporate environment, using synthetic data.

📊 Problem Statement

CX impacts ROI but is often hard to quantify.

- Need phase-wise health scores to proactively identify at-risk customers.
- Business leaders need actionable insights, not just model outputs.

**Solution:** A predictive framework that models customer health at each journey phase, provides explainability, and generates natural-language insights for decision-makers.

🗂 Architecture

Synthetic CX Data → Preprocessing → Phase-wise LightGBM Models
      ↓                      ↓
 SHAP Explainability       LLM Insights
      ↓                      ↓
      Interactive Streamlit Dashboard

### Components:

- **data/** – synthetic dataset per phase
- **src/** – preprocessing, feature engineering, modeling, SHAP, LLM code
- **models/** – saved LightGBM models per phase
- **dashboard/** – Streamlit dashboard for interactive exploration
- **api/** – optional FastAPI endpoints
- **notebooks/** – exploratory analysis, training, explainability

�� Features

- **Predictive Modeling:** LightGBM classifiers per customer journey phase
- **Explainability:** SHAP summary plots to identify top drivers
- **LLM Insights:** GPT-4 generates executive-friendly summaries for each phase
- **Interactive Dashboard:** Users can select a phase, view predictions, SHAP plots, and LLM narratives

💾 Dataset

- Synthetic CX + Operational Metrics
- 1000 customers × 6 phases = 6000 rows

Metrics per phase: 5 touchpoint metrics + 1 operational metric

- **Target:** health (0 = at-risk, 1 = healthy)

Example row:

| customer_id | phase | metric_1 | metric_2 | metric_3 | metric_4 | metric_5 | operational_metric | health |
|--------------|-------|-----------|-----------|-----------|-----------|-----------|-------------------|--------|
| 1            | Learn | 0.75      | 0.40      | 0.65      | 0.80      | 0.55      | 100               | 1      |

📈 Usage

1️⃣ Generate Synthetic Data  
`python synthetic_data.py`

2️⃣ Train Phase-wise Models  
`python train_models.py`

3️⃣ Generate SHAP Explainability Plots  
`python shap_explain.py`

4️⃣ Run Streamlit Dashboard  
`streamlit run dashboard/streamlit_app.py`

- Select a phase to view predictions
- Explore SHAP plots
- See LLM-generated insights

🧩 LLM Integration

Uses OpenAI GPT-4 API to summarize phase-wise health scores

- Converts predictions + SHAP feature importances into business-friendly language

Example output:

"In the Learn phase, customers with low engagement and low download metrics are at risk. Focus on improving onboarding content to reduce churn."

🔧 Requirements

- pandas
- numpy
- scikit-learn
- lightgbm
- shap
- matplotlib
- joblib
- streamlit
- openai

⚙️ Deployment

Dockerized Streamlit & API ready for cloud deployment: AWS, GCP, Render, or Heroku

- Can be extended to CI/CD pipelines for model retraining

📖 Future Improvements

- Add real-world CX datasets when available
- Enhance LLM insights with RAG (retrieval-augmented generation) from historical dashboards
- Implement alerting system for at-risk customers
- Deploy multi-phase monitoring & logging

🎯 Key Takeaways

- Demonstrates end-to-end ML system thinking, not just isolated models
- Integrates explainability + LLM insights for business impact
- Fully public-ready and deployable, even with synthetic data
- Highlights strategic problem-solving + technical excellence — exactly what hiring managers look for