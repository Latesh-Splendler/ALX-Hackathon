import streamlit as st
import pickle
import numpy as np

# -------------------------------
# 1. Load your trained model
# -------------------------------
# Example: model.pkl should be in the same folder
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# -------------------------------
# 2. Streamlit App Layout
# -------------------------------
st.title("🤖 AI Model Prediction App")
st.write("This simple app loads a trained model and makes predictions.")

# -------------------------------
# 3. User Input Section
# -------------------------------
st.header("Enter Input Features")

# Example for a model with 3 numerical inputs
feature1 = st.number_input("Feature 1", value=0.0)
feature2 = st.number_input("Feature 2", value=0.0)
feature3 = st.number_input("Feature 3", value=0.0)

# Convert inputs to NumPy array for model prediction
input_data = np.array([[feature1, feature2, feature3]])

# -------------------------------
# 4. Make Predictions
# -------------------------------
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"✅ Model Prediction: {prediction[0]}")

# -------------------------------
# 5. Optional Footer
# -------------------------------
st.write("---")
st.caption("Built with ❤️ using Streamlit")
