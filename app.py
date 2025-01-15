import streamlit as st
import sklearn
import joblib
from footer import footer_page
from side_bar import sidebar_page
from prediction_plots import show_plotting

# Streamlit app
st.set_page_config(page_title="House Price Prediction", page_icon="🏡", layout="wide")
# Sidebar
sidebar_page()

st.title("House Price Prediction 🏠")

st.markdown("""
### How it works
This app uses a linear regression model trained on house age to predict its price. The model predicts how the price of a house decreases as its age increases.
""")

model = joblib.load('House_price_prediction_model.pkl')
age = st.number_input("Enter the age of the house (in years):", min_value=1, max_value=100, step=1)

st.subheader("Price Prediction")
st.write("Based on the input, the model predicts the price of the house.")

if st.button("Predict Price"):
    predicted_price = model.predict([[age]])
    st.write(f"The predicted price of the house is: **${predicted_price[0]:,.2f}**")
    st.markdown("""
    ### Model Breakdown
    - **Linear Regression Model**: The model predicts the price of a house based on its age. The price decreases as the age of the house increases.
    - The model uses a **simple linear regression** formula where the dependent variable is the house price and the independent variable is the age of the house.
    """)
    show_plotting(age, predicted_price)
    
    

# Footer
footer_page()