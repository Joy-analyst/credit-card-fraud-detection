import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("xgb_Fraud Detection_model.pkl")

# Page title
st.set_page_config(page_title="Fraud Detection App")
st.title("🚨 Fraud Detection Predictor")
st.write("Enter the transaction features below:")

# Input form
user_input = st.text_input("Comma-separated features (e.g. 0.1, -1.2, 3.3, ..., 0.5)")

if user_input:
    try:
        features = np.array([float(i) for i in user_input.split(",")]).reshape(1, -1)

        prediction = model.predict(features)[0]
        proba = model.predict_proba(features)[0][1]

        result = "FRAUD" if prediction == 1 else "NOT FRAUD"
        st.success(f"✅ Prediction: **{result}** (Probability: {round(proba, 4)})")

    except ValueError:
        st.error("❌ Please enter only numbers, separated by commas.")

