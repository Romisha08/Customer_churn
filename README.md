# Customer Churn Prediction

A machine learning application that predicts whether a telecom customer is likely to churn.


An end-to-end Machine Learning project that predicts whether a telecom customer is likely to **churn (leave the company)**.

The project includes data preprocessing, exploratory data analysis, handling class imbalance, machine learning model training, evaluation, and an interactive **Streamlit web application** for making predictions.

---

##  Live Demo

👉 **[Try the Customer Churn Prediction App](YOUR_STREAMLIT_APP_URL)**



---

##  Project Overview

Customer churn is a major problem for subscription-based businesses.

If a company can identify customers who are likely to leave, it can take action such as:

- Offering discounts
- Providing better customer support
- Offering customized plans
- Providing additional services
- Addressing customer complaints

This project uses customer information such as:

- Contract type
- Tenure
- Monthly charges
- Total charges
- Internet service
- Payment method
- Technical support
- Online security
- Customer demographics

to estimate the probability that a customer will churn.

---

##  Objective

The main objective of this project is:

> **Predict whether a customer will churn based on their demographic, service, contract, and billing information.**

The model outputs a **churn probability**, which can then be converted into a risk category.

For example:

```text

Churn Probability: 82%

Risk Level: HIGH 🔴

```

## Features

- Data preprocessing
- Exploratory Data Analysis
- Class imbalance handling
- One-hot encoding
- Random Forest classification
- Churn probability prediction
- Threshold tuning
- Streamlit web application

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn
- Random Forest
- Streamlit
- Joblib

## Dataset

IBM Telco Customer Churn dataset.

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py


---




```text

Telco Customer Data
        ↓
  Data Cleaning
        ↓
       EDA
        ↓
Feature Engineering
        ↓
Train/Test Split
        ↓
Preprocessing
        ↓
Class Imbalance Handling
        ↓
Random Forest
        ↓
Cross Validation
        ↓
Threshold Optimization
        ↓
customer_churn_model.pkl
        ↓
Streamlit
        ↓
Live ML Application

```