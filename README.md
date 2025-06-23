# TalentVest – MVP: Empowering Education through ISAs

A FinTech MVP platform connecting students and investors via **Income Share Agreements (ISAs)**. Developed for the MSc Business Analytics & Management course at Rotterdam School of Management (RSM).

---

## 🚀 Overview

TalentVest enables:

* 🤝 Students to apply for funding and update their academic journey
* 🧱 Investors to browse, fund, and trade ISA shares
* 📊 Portfolio tracking with ML-based ISA valuation and profit projections

All data used is **simulated**. The ISA valuation engine leverages simple regression models to project salary, growth, and discounting.

---

## 📄 Features

### Student Portal

* Application form + document upload
* Academic progress and quarterly update form

### Investor Dashboard

* Explore student funding opportunities
* View profile details and ISA financials
* Make funding commitments (mock logic)
* Navigate across filtered student sets

### ISA Trading Module

* Browse existing funded students available for resale
* Submit offers on secondary market ISAs

### Portfolio Overview

* NPV and ROI calculations per student
* Aggregated financial visualizations

---

## ⚙️ Tech Stack

* **Frontend**: Streamlit (Python)
* **Backend**:

  * `pandas`, `scikit-learn`, `matplotlib`
  * ISA logic implemented via custom Python modules
* **Data**: Fully simulated

---

## 📁 Project Structure

```bash
TalentVest_MVP/
├── app.py                            # Streamlit UI & navigation
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/                             # students.csv, trading.csv, portfolio_sample.csv
├── static/                           # Logo and image assets
├── models/                           # Trained salary/discount models
│
├── generate_students.py              # Student profile generator
├── train_salary_models.py            # Model training
├── predict_targets_on_new_datasets.py
├── recalculate_isa_value_from_predictions.py
├── portfolio.py                      # Portfolio aggregation logic
├── npv.py                            # Discounting & NPV helper functions
├── dataset.py                        # ML feature schema and transformations
```

---

## 💡 ISA Valuation Engine

Trains and applies ML models to estimate:

* `predicted_salary`
* `salary_growth`
* `discount_rate`

These values feed into:

* ISA Share (%), NPV, ROI, Estimated Profit

All calculations done with:

* Discounted cash flow logic
* Assumed 15% ISA share fixed across investments

---

## 📚 Installation Guide

1. **Clone the Repository**:

```bash
git clone https://github.com/rubenmst/TalentVest-MVP-.git
cd TalentVest-MVP-
```

2. **Install Requirements**:

```bash
pip install -r requirements.txt
```

3. **Run the App**:

```bash
streamlit run app.py
```

---

## 🎥 MVP Demo Video

\[Insert Your Video Link Here → YouTube, Google Drive, etc.]

---

## 🎓 Academic Context

Built as part of:

* **Course**: Business Models & Applications in FinTech (BM26BAM)
* **University**: RSM, Erasmus University
* **Assignment 2**: MVP implementation of business idea

This MVP reflects the execution of Assignment 1 (Business Plan) into a working, testable prototype.

---

## 🚨 Disclaimer

This is an educational project. All data is simulated and predictions are hypothetical. This is not financial advice.

---

## 📊 Future Improvements

* Add database integration (PostgreSQL)
* Deploy on Streamlit Cloud or Heroku
* Add authentication
* Connect ISA logic to real-world salary APIs / market data
* Improve ML models with hyperparameter tuning

---

## 📁 License

MIT License – Free to use and modify for educational or demo purposes.

---

✅ **Maintainer**: Ruben Maxim Stauch | MSc BAM | RSM
