import streamlit as st
import pandas as pd
import joblib
import json


# -------------------------
# Load model
# -------------------------

model = joblib.load(
    "models/customer_churn_model.pkl"
)

with open("models/threshold.json", "r") as f:
    threshold_data = json.load(f)

THRESHOLD = threshold_data["threshold"]


# -------------------------
# Page configuration
# -------------------------

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide"
)


# -------------------------
# Title
# -------------------------

st.title("📊 Customer Churn Prediction")

st.write(
    "Enter customer information to estimate "
    "the probability of customer churn."
)


# -------------------------
# Customer information
# -------------------------

st.header("Customer Information")

col1, col2, col3 = st.columns(3)


with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=100,
        value=5
    )


with col2:

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

    online_security = st.selectbox(
        "Online Security",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    online_backup = st.selectbox(
        "Online Backup",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )


with col3:

    device_protection = st.selectbox(
        "Device Protection",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    tech_support = st.selectbox(
        "Tech Support",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )


# -------------------------
# Billing information
# -------------------------

st.header("Contract & Billing")

col1, col2, col3 = st.columns(3)


with col1:

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )


with col2:

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )


with col3:

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0,
    step=1.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=350.0,
    step=10.0
)


# -------------------------
# Prediction
# -------------------------

if st.button(
    "🔮 Predict Churn",
    use_container_width=True
):

    customer = pd.DataFrame([
        {
            "gender": gender,
            "SeniorCitizen": senior_citizen,
            "Partner": partner,
            "Dependents": dependents,
            "tenure": tenure,
            "PhoneService": phone_service,
            "MultipleLines": multiple_lines,
            "InternetService": internet_service,
            "OnlineSecurity": online_security,
            "OnlineBackup": online_backup,
            "DeviceProtection": device_protection,
            "TechSupport": tech_support,
            "StreamingTV": streaming_tv,
            "StreamingMovies": streaming_movies,
            "Contract": contract,
            "PaperlessBilling": paperless_billing,
            "PaymentMethod": payment_method,
            "MonthlyCharges": monthly_charges,
            "TotalCharges": total_charges
        }
    ])

    st.write("Customer sent to model:")
    st.write(customer.columns.to_list())
    
    st.write("columns expected by model:")
    st.write(model.named_steps["preprocessor"].feature_names_in_.tolist())

    probability = model.predict_proba(
        customer
    )[0][1]


    prediction = int(
        probability >= THRESHOLD
    )


    st.divider()

    st.subheader("Prediction")


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Churn Probability",
            f"{probability * 100:.2f}%"
        )


    with col2:

        if prediction == 1:

            st.error(
                "⚠️ Customer is likely to churn"
            )

        else:

            st.success(
                "✅ Customer is unlikely to churn"
            )


    st.progress(
        float(probability)
    )