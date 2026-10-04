# Customer Churn Prediction

A machine learning application that predicts whether a telecom customer is likely to churn.


An end-to-end Machine Learning project that predicts whether a telecom customer is likely to **churn (leave the company)**.

The project includes data preprocessing, exploratory data analysis, handling class imbalance, machine learning model training, evaluation, and an interactive **Streamlit web application** for making predictions.

---

##  Live Demo

👉 **[Try the Customer Churn Prediction App](https://customerchurn-cfg59wwrwqes5eyp4gixyt.streamlit.app/)**



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
```

---




```text
customer_churn.ipynb
│
├── 1. Project Introduction
│
├── 2. Import Libraries
│
├── 3. Load Dataset
│
├── 4. Dataset Shape
│
├── 5. Dataset Information
│
├── 6. Missing Values
│
├── 7. Data Cleaning
│
├── 8. Target Distribution
│
├── 9. Exploratory Data Analysis
│   ├── Tenure
│   ├── Monthly Charges
│   ├── Total Charges
│   ├── Contract
│   ├── Internet Service
│   ├── Payment Method
│   └── Senior Citizen
│
├── 10. Correlation Analysis
│
├── 11. Feature Preparation
│
├── 12. Train/Test Split
│
├── 13. Preprocessing Pipeline
│
├── 14. Logistic Regression
│
├── 15. Logistic Evaluation
│
├── 16. Random Forest
│
├── 17. Random Forest Evaluation
│
├── 18. Model Comparison
│
├── 19. Threshold Tuning
│
├── 20. Feature Importance
│
├── 21. Save Model
│
├── 22. Load Model
│
├── 23. Test New Customer
│
└── 24. Final Results


```
