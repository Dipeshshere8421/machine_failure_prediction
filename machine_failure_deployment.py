import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("machine_failure_prediction_model.pkl")

# Title
st.title("Machine Failure Prediction System")

st.write("Enter sensor values to predict whether the machine will fail.")

# User Inputs
footfall = st.number_input("Footfall")
tempMode = st.number_input("Temp Mode")
AQ = st.number_input("Air Quality (AQ)")
USS = st.number_input("USS")
CS = st.number_input("CS")
VOC = st.number_input("VOC")
RP = st.number_input("RP")
IP = st.number_input("IP")
Temperature = st.number_input("Temperature")

# Create dataframe
df = pd.DataFrame({
    "footfall": [footfall],
    "tempMode": [tempMode],
    "AQ": [AQ],
    "USS": [USS],
    "CS": [CS],
    "VOC": [VOC],
    "RP": [RP],
    "IP": [IP],
    "Temperature": [Temperature]
})

# Prediction
if st.button("Predict"):
    prediction = model.predict(df)

    if prediction[0] == 1:
        st.error("⚠️ Machine will fail")
    else:
        st.success("✅ Machine will work properly")
