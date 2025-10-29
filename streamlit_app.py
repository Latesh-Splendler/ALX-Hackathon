import streamlit as st
import pickle
import numpy as np
import pandas as pd

# -------------------------------
# 1. Load Models and Feature Data
# -------------------------------
with open("beans_loan_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("beans_features.pkl", "rb") as f:
    feature_info = pickle.load(f)

with open("beans_scaler.pkl", "rb") as f:
    feature_info = pickle.load(f)

# -------------------------------
# 2. App Layout
# -------------------------------b
st.title("🧠 Beans Loan Prediction App")
st.write("This app predicts loan approval using your trained AI model.")

# Display model information
st.sidebar.header("Model Info")
st.sidebar.write("Model file: beans_loan_model.pkl")
st.sidebar.write(f"Feature set: {len(feature_info)} features")

# -------------------------------
# 3. User Input Section
# -------------------------------
st.header("Enter Applicant Data")

# Create dynamic input fields for each feature
user_inputs = {}
for feature in feature_info:
    user_inputs[feature] = st.number_input(f"{feature}", value=0.0)

# Convert input to DataFrame
input_df = pd.DataFrame([user_inputs])

# -------------------------------
# 4. Make Prediction
# -------------------------------
if st.button("Predict Loan Approval"):
    prediction = model.predict(input_df)[0]
    st.success(f"✅ Prediction Result: {prediction}")

# -------------------------------
# 5. Optional: Display Inputs
# -------------------------------
st.subheader("Input Summary")
st.dataframe(input_df)

st.write("---")
st.caption("App built with ❤️ using Streamlit")
