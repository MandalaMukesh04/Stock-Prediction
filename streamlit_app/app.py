import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from data_loader import load_data
from predict import predict

st.title("📈 Stock Price Prediction using LSTM")

stock = st.text_input("Enter Stock Symbol (e.g., AAPL)", "AAPL")

if st.button("Predict"):
    predicted_price = predict(stock)
    st.write(f"### 📊 Predicted Closing Price: ${predicted_price:.2f}")

    # Load & visualize historical data
    data = load_data(stock)
    st.line_chart(data["Close"])

st.write("Enter a stock symbol and press 'Predict' to see the LSTM-based prediction.")
