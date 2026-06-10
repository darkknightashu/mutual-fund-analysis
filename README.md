# Mutual Fund Performance, Risk & Investor Analytics Platform

## Overview

This project is an end-to-end Mutual Fund Analytics Platform developed as part of a Data Analyst Internship project. The platform analyzes mutual fund performance, investor behavior, benchmark comparison, portfolio risk, and retention patterns using financial datasets and advanced analytics techniques.

The objective is to transform raw mutual fund data into actionable insights that support investment decision-making and performance evaluation.

---

## Project Objectives

* Clean and standardize mutual fund datasets
* Store and manage data using SQLite
* Perform exploratory data analysis (EDA)
* Analyze fund performance against benchmarks
* Calculate risk metrics such as Alpha, Beta, VaR, and CVaR
* Measure investor retention using Cohort Analysis
* Evaluate SIP continuity and investment consistency
* Build a fund scoring framework
* Develop a mutual fund recommendation engine

---

## Dataset Overview

The project uses 10 datasets:

1. Fund Master Data
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

## Project Structure

```text
data/
├── raw/
├── processed/
├── db/

notebooks/
├── 02_data_cleaning.ipynb
├── 03_eda_analysis.ipynb
├── 04_performance_analytics.ipynb

reports/
├── benchmark_comparison.png
├── rolling_sharpe_chart.png
├── data_dictionary.md
├── data_quality_summary.txt

scripts/
└── recommender.py

sql/
```

## Analytics Performed

### Data Cleaning

* Missing value treatment
* Date standardization
* Duplicate removal
* Data validation

### Exploratory Data Analysis

* Fund-level analysis
* Investor transaction analysis
* NAV trend analysis
* Category-wise insights

### Performance Analytics

* Benchmark comparison
* Rolling Sharpe Ratio
* Alpha and Beta estimation

### Risk Analytics

* Value at Risk (VaR)
* Conditional Value at Risk (CVaR)
* Concentration analysis (HHI)

### Investor Analytics

* Cohort Analysis
* SIP Continuity Analysis
* Retention tracking

---

## Key Outputs

### Processed Files

* clean_nav.csv
* clean_transactions.csv
* clean_performance.csv
* alpha_beta.csv
* var_cvar_report.csv
* cohort_analysis.csv
* sip_continuity_analysis.csv
* fund_scorecard.csv
* hhi_concentration_report.csv

### Visual Reports

* Benchmark Comparison Chart
* Rolling Sharpe Ratio Chart

---

## Recommendation Engine

A recommendation engine was developed to rank and suggest mutual funds based on performance and risk-adjusted metrics.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* SQLite
* Jupyter Notebook

---

## Business Impact

* Improved mutual fund performance evaluation
* Enhanced risk assessment framework
* Investor retention analysis
* Fund ranking and recommendation system
* Data-driven investment insights

---

## Author

Data Analyst Internship Project

2026
