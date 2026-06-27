import streamlit as st
from prediction_helper import predict

st.title("Healthcare Insurance Premium Prediction")

# ==========================
# Categorical Options
# ==========================

categorical_options = {
    "gender": ["Male", "Female"],

    "region": [
        "Northwest",
        "Northeast",
        "Southwest",
        "Southeast"
    ],

    "marital_status": [
        "Unmarried",
        "Married"
    ],

    "bmi_category": [
        "Underweight",
        "Normal",
        "Overweight",
        "Obesity"
    ],

    "smoking_status": [
        "No Smoking",
        "Occasional",
        "Regular"
    ],

    "employment_status": [
        "Salaried",
        "Self-Employed",
        "Freelancer"
    ],

    "medical_history": [
        "No Disease",
        "Diabetes",
        "High blood pressure",
        "Heart disease",
        "Thyroid",
        "Diabetes & High blood pressure",
        "Diabetes & Heart disease",
        "High blood pressure & Heart disease",
        "Diabetes & Thyroid"
    ],

    "insurance_plan": [
        "Bronze",
        "Silver",
        "Gold"
    ]
}

# ==========================
# Row 1
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=22
    )

with col2:
    gender = st.selectbox(
        "Gender",
        categorical_options["gender"]
    )

with col3:
    region = st.selectbox(
        "Region",
        categorical_options["region"]
    )

# ==========================
# Row 2
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    marital_status = st.selectbox(
        "Marital Status",
        categorical_options["marital_status"]
    )

with col2:
    number_of_dependants = st.number_input(
        "Dependants",
        min_value=0,
        max_value=5,
        value=0
    )

with col3:
    bmi_category = st.selectbox(
        "BMI Category",
        categorical_options["bmi_category"]
    )

# ==========================
# Row 3
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    smoking_status = st.selectbox(
        "Smoking Status",
        categorical_options["smoking_status"]
    )

with col2:
    employment_status = st.selectbox(
        "Employment Status",
        categorical_options["employment_status"]
    )

with col3:
    income_lakhs = st.number_input(
        "Annual Income (Lakhs)",
        min_value=1.0,
        max_value=200.0,
        value=6.0,
        step=0.5
    )

# ==========================
# Row 4
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    genetical_risk = st.number_input(
        "Genetical Risk",
        min_value=0,
        max_value=5,
        value=0
    )

with col2:
    medical_history = st.selectbox(
        "Medical History",
        categorical_options["medical_history"]
    )

with col3:
    insurance_plan = st.selectbox(
        "Insurance Plan",
        categorical_options["insurance_plan"]
    )

# ===================================
# Dictionary for Model Prediction
# ===================================

input_dict = {
    "age": age,
    "gender": gender,
    "region": region,
    "marital_status": marital_status,
    "number_of_dependants": number_of_dependants,
    "bmi_category": bmi_category,
    "smoking_status": smoking_status,
    "employment_status": employment_status,
    "income_lakhs": income_lakhs,
    "genetical_risk": genetical_risk,
    "medical_history": medical_history,
    "insurance_plan": insurance_plan
}

if st.button(
    "Predict",
    type="primary"
):
    prediction = predict(input_dict)
    st.success(f'Predicted Premium Amount: {prediction}'     )