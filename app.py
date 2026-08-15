from fastapi import FastAPI,HTTPException
import pickle 
from pydantic import BaseModel
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open('churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

class Customer(BaseModel):
    Tenure: int
    Total_Spend: float
    Usage_Frequency: float
    Gender: str
    Subscription_Type: str
    Age: int
    Support_Calls: int
    Contract_Length: str
    Last_Interaction: int
    Payment_Delay: int


@app.post("/predict",tags=["Prediction"])
def predict(customer: Customer):
    try:
        input_data = pd.DataFrame([{
            "Tenure": customer.Tenure,
            "Total Spend": customer.Total_Spend,
            "Usage Frequency": customer.Usage_Frequency,
            "Gender": customer.Gender,
            "Subscription Type": customer.Subscription_Type,
            "Age": customer.Age,
            "Support Calls": customer.Support_Calls,
            "Contract Length": customer.Contract_Length,
            "Last Interaction": customer.Last_Interaction,
            "Payment Delay": customer.Payment_Delay
        }])

        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)[0]
        churn_probability = probability[1]*100

        result = "Churn" if prediction[0] == 1 else "Not Churn"

        return {
            "prediction": result,
            "customer_age": customer.Age,
            "tenure": customer.Tenure,
            "churn_probability": churn_probability
        }

    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@app.get("/health",tags=["Health Check"])
def health():
    return {"status": "API is running", "model": "loaded"}


@app.get("/")
def home():
    return {
        "message": "Customer Churn API",
        "docs": "/docs",
        "health": "/health"
    }



