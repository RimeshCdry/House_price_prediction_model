import streamlit as st

def sidebar_page():
    st.sidebar.header("House Price Prediction App")
    st.sidebar.text("Predict the price of a house based on its age.")
    st.sidebar.markdown("""
    - **Step 1**: Enter the age of the house.
    - **Step 2**: Click the "Predict Price" button.
    - **Step 3**: View the predicted house price along with additional insights.
    """)
    st.sidebar.markdown("___")
    st.sidebar.text("Data model trained with linear regression.")