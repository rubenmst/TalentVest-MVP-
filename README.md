# TalentVest – MVP: Empowering Education through ISAs

A FinTech MVP platform connecting students and investors via tradable **Income Share Agreements (ISAs)**. Developed for the MSc Business Analytics & Management programm and its FinTech course at Rotterdam School of Management (RSM). The goal is to allow more students to access higher education while creating a new impact assest class for Investors. 

---

## Overview

TalentVest enables:
* both parties (Investors and Students) to connect in a single platform 
* Students to apply for funding and update their academic journey in the student portal/dashboard
* Investors to browse, fund, and trade ISA shares in the Investor Dashboard 
* Portfolio tracking with ML-based estimates used for ISA right valuation and profit projections to aim to increase transparency 
* increased liquidity for Investors by offering a Trading functionality, which results in higher investment incentives 

All data used is **simulated**. The ISA valuation engine leverages simple regression models to project salary, growth, and discounting. At a later scaling stage, a real-life data will be collected and utilized to create a unqiue student database as a foundation for the ML models and ISA valuation. 

---

## Features

### Student Portal

* Application form + document upload to request funding and be listed on the website + a Questionarry with further a further personal fit assessment is in planning
* Academic progress and quarterly update form is required to continously update a students profil, as students need to be transparent about their academic journey
* Privacy and ethic standards are always considered by TalentVest 

### Investor Dashboard

* Explore student funding opportunities
* 1st stage: High-school graduates that applied for a University but require the money 
* Student Details: Several details and variables are displayed about the student and upcoming studys
* Financials: yieling finanical variables, such as required funding, ML estimates for salary, discount rate,etc. 
* Funding a flexible amount directly in the platform 
* Navigate and filtered across student to fund and invest in


### ISA Trading Module

* Browse existing funded students available for resale: submit offers on secondary market ISAs
* 2nd stage: The ISA rights for Unversity Students or already employed students can be listed and traded by Investors 
* Student Details: similiar as before and updated quarterly 
* Finanicals: similar as before and updated quarterly, updated ML estimates and ISA valuation as a guideline for Investors 
* Offer: Investors can submit an offer (price) to the other Investors for the ISA rights of the student 

### Portfolio Overview

* Listing of the ISA rights that are hold by an Investor
* Detailed View and detailed Financials as before
* Including NPV and ROI calculations per student to track process and profitability 
* Aggregated financial visualizations
* Option to list students in the ISA Trading Module to other Investors 

---

## Tech Stack

* **Frontend**: Streamlit (entirely Python-based)
* **Backend**:
  * `pandas`, `scikit-learn`, `matplotlib`
  * ISA logic implemented via custom Python modules
* **Data**: Fully simulated to show feasibility of salary, discount rate (risk), and salary growth prediction 

---

## Project Structure

```bash
TalentVest_MVP/
├── app.py                            # Streamlit UI & navigation
├── requirements.txt                  # bundeled libraries/packages used  
├── README.md                         # the file you are reading right now  
├── .gitignore
│
├── data/                             # students.csv, trading.csv, portfolio_sample.csv (simulated profiles with ML estimates)
├── static/                           # Logo and image assets 
├── models/                           # Trained salary/discount models
│
├── generate_students.py              # Student profile generator 
├── train_salary_models.py            # Model training
├── predict_targets_on_new_datasets.py   # predict salary, growth, and discount rate  
├── recalculate_isa_value_from_predictions.py # update ISA right valuation for simulated data sets used 
├── portfolio.py                      # Portfolio aggregation logic
├── npv.py                            # Discounting & NPV helper functions
├── dataset.py                        # ML feature schema and transformations
```

---

## ISA Valuation Engine

Trains and applies ML models to estimate:

* `predicted_salary`
* `salary_growth`
* `discount_rate`

These values feed into:

* ISA Share (%), NPV, ROI, Estimated Profit 

Thereby, increase transaprency and liquidity is provided by TalentVest. 

All calculations done with:

* Discounted cash flow logic
* Assumed 15% ISA share fixed across investments across 10 years pay-pack period from Students to Investors 
* Simulated Data sets to show feasibility 
* Basic OLS and Lasso model including interaction effects were constructed, more sophisticated Neural Networks will be utilized later  

---

## Installation Guide

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

## MVP Demo Video
Video: https://drive.google.com/file/d/1TgwYixqvp8guzAwtrgo5lWFDLrGSg-SO/view?usp=sharing 
Folder: (https://drive.google.com/drive/u/0/folders/1lLRTIlLR1c11MVrKoXgqKVFiXFrml0Db)

---

## Academic Context

Built as part of:

* **Course**: Business Models & Applications in FinTech (BM26BAM)
* **Programm** Business Analytics and Management 
* **University**: RSM, Erasmus University
* **Assignment 2**: MVP implementation of business idea - TalentVest 

This MVP reflects the execution of Assignment 1 (Business Plan) into a working, testable prototype.

---

## Disclaimer

This is an educational project. All data is simulated and predictions are hypothetical. This is not financial advice.

---

## Future Improvements

* Demo with a first cohort of students 
* Add database integration (PostgreSQL)
* Track student data (anonyously) to build real-life data set for ISA right valuation in the long-term   
* Enrich databank by connecting ISA logic to real-world salary APIs / market data
* Deploy on Streamlit Cloud or Heroku
* Add authentication for separated Investor and Student Access 
* Improve ML models with hyperparameter tuning

---

## License

MIT License – Free to use and modify for educational or demo purposes.

---

**Maintainer**: Ruben Maxim Stauch | MSc BAM | RSM
