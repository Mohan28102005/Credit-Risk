import streamlit as st
import pandas as pd
from processing import processing

st.set_page_config(page_title="Credit Risk Prediction",
                   page_icon="💳",
                   layout="wide")

st.title("💳 Credit Risk Prediction App")
st.markdown("Enter applicant details below to predict default probability.")
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Financial Details")

    credit_utilization_ratio = st.number_input(
        "Credit Utilization Ratio",
        min_value=0.0,
        max_value=1.0,
        step=0.01
    )

    delinquency_months = st.number_input(
        "Delinquency Months",
        min_value=0,
        step=1
    )

    total_months = st.number_input(
        "Total Credit History Months",
        min_value=0,
        step=1
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0.0,
        step=1000.0
    )

    income = st.number_input(
        "Annual Income",
        min_value=0.0,
        step=1000.0
    )

    total_dpd = st.number_input(
        "Total Days Past Due (DPD)",
        min_value=0,
        step=1
    )

    loan_tenure_months = st.number_input(
        "Loan Tenure (Months)",
        min_value=0,
        step=1
    )

with col2:
    st.subheader("👤 Applicant Profile")

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        step=1
    )

    number_of_open_accounts = st.number_input(
        "Number of Open Accounts",
        min_value=0,
        step=1
    )

    loan_purpose = st.selectbox(
        "Loan Purpose",
        ['Home', 'Auto', 'Personal', 'Education']
    )

    residence_type = st.selectbox(
        "Residence Type",
        ['Owned', 'Mortgage', 'Rented']
    )

    loan_type = st.selectbox(
        "Loan Type",
        ['Secured', 'Unsecured']
    )
if st.button("🔍 Predict Risk"):
    input_data = pd.DataFrame({
        "credit_utilization_ratio": [credit_utilization_ratio],
        "delinquency_months": [delinquency_months],
        "total_months": [total_months],
        "loan_amount": [loan_amount],
        "income": [income],
        "total_dpd": [total_dpd],
        "loan_tenure_months": [loan_tenure_months],
        "age": [age],
        "number_of_open_accounts": [number_of_open_accounts],
        "loan_purpose": [loan_purpose],
        "residence_type": [residence_type],
        "loan_type": [loan_type],
        "number_of_dependants":1,
        "years_at_current_address":1,
        "zipcode":1,
        "number_of_closed_accounts":1,
        "enquiry_count":1,
        "sanction_amount":1,
        "processing_fee":1,
        "gst":1,
        "net_disbursement":1,
        "principal_outstanding":1,
        "bank_balance_at_application":1,
    })
    prediction, probability,score = processing(input_data)
    rating=""
    if 300 <= score < 500:
        rating='Poor'
    elif 500 <= score < 650:
        rating= 'Average'
    elif 650 <= score < 750:
        rating= 'Good'
    elif 750 <= score <= 900:
        rating= 'Excellent'
    else:
        rating= 'Undefined'
    st.subheader("🎯 Prediction Result")

    st.write(f"Prediction: {prediction}")
    st.write(f"Default Probability: {probability:.2%}")
    st.write(f"Score: {score:.2f}")
    st.write(f"Rating: {rating}")
    st.subheader("📥 Input Data")
    st.dataframe(input_data)
