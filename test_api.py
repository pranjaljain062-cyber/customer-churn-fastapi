import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "Tenure": 12,
    "Total_Spend": 25000,
    "Usage_Frequency": 20,
    "Gender": "Male",
    "Subscription_Type": "Premium",
    "Age": 30,
    "Support_Calls": 2,
    "Contract_Length": "Annual",
    "Last_Interaction": 5,
    "Payment_Delay": 5
}

response = requests.post(url, json=data)

print(response.json())