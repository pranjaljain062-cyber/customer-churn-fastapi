import requests
import streamlit as st

st.title("Customer Churn Prediction")

tenure = st.number_input("Tenure",)
total_spend = st.number_input("Total Spend")
usage_frequency = st.number_input("Usage Frequency")
gender = st.selectbox("Gender", ["Male", "Female"])
subscription_type = st.selectbox(
    "Subscription Type",
    ["Basic", "Premium", "Standard"]
)
age = st.number_input("Age")
support_calls = st.number_input("Support Calls")
contract_length = st.selectbox(
    "Contract Length",
    ["Monthly", "Quarterly", "Annual"]
)
last_interaction = st.number_input("Last Interaction")
payment_delay = st.number_input("Payment Delay")

if st.button("Predict Churn"):

    data = {
        "Tenure": tenure,
        "Total_Spend": total_spend,
        "Usage_Frequency": usage_frequency,
        "Gender": gender,
        "Subscription_Type": subscription_type,
        "Age": age,
        "Support_Calls": support_calls,
        "Contract_Length": contract_length,
        "Last_Interaction": last_interaction,
        "Payment_Delay": payment_delay
    }
    
response = requests.post(
    "https://customer-churn-fastapi-2.onrender.com/predict",
    json=data
)
    

    if response.status_code == 200:
        result = response.json()
        st.write(f"Prediction: {result['prediction']}")
        st.write(f"Customer Age: {result['customer_age']}")
        st.write(f"Tenure: {result['tenure']}")
        st.write(f"Churn Probability: {result['churn_probability']:.2f}%")
    else:
        st.write("Error in prediction API")




    
