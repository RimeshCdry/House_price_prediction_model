import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import joblib

model = joblib.load('House_price_prediction_model.pkl')

def show_plotting(age,predicted_price):
    age_range = np.arange(1, 101).reshape(-1, 1)
    price_range = model.predict(age_range)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(age_range, price_range, color='red', label="Regression Line")
    ax.scatter(age, predicted_price, color='blue', label=f"Predicted Price ({age} years)")
    ax.set_xlabel('Age of House (Years)')
    ax.set_ylabel('Price (USD)')
    ax.set_title('House Price Prediction Based on Age')
    ax.legend()
    st.pyplot(fig)