import streamlit as st
import pickle
import numpy as np

try:
    with open('yes_bank_stock_prediction_model.pkl', 'rb') as file:
        model = pickle.load(file)

    st.title("Yes Bank Stock Closing Price Prediction")
    st.write("Enter the values to predict the Closing Price:")

    open_price = st.number_input("Open Price", min_value=0.0)
    high_price = st.number_input("High Price", min_value=0.0)
    low_price = st.number_input("Low Price", min_value=0.0)

    if st.button("Predict Closing Price"):
        features = np.array([[open_price, high_price, low_price]])
        prediction = model.predict(features)
        st.success(f"The Predicted Closing Price is: INR {prediction[0]:.2f}")
except FileNotFoundError:
    st.error("Model file not found. Please refresh.")