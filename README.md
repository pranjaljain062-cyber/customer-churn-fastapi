# 🚀 Customer Churn Prediction API

A Machine Learning prediction API built with **FastAPI**, connected to a **Streamlit frontend** for real-time customer churn predictions.

## 📌 About the Project

This project demonstrates how a trained Machine Learning model can be converted into a usable API using FastAPI.

The API accepts customer information, processes the input through the trained model, and returns the predicted churn status along with the churn probability.

A Streamlit application is used as the frontend to interact with the API.

## 🎯 Project Goals

- ✔ Serve a trained ML model through FastAPI
- ✔ Create REST API endpoints for predictions
- ✔ Validate incoming data using Pydantic
- ✔ Return churn prediction and probability
- ✔ Handle API errors properly
- ✔ Test the API using Swagger UI
- ✔ Connect Streamlit with FastAPI

## 🔄 Application Workflow

    User
      ↓
    Streamlit Interface
      ↓
    POST /predict
      ↓
    FastAPI
      ↓
    Pydantic Validation
      ↓
    Trained ML Model
      ↓
    Prediction + Probability
      ↓
    FastAPI Response
      ↓
    Streamlit

## 🧠 Machine Learning Model

The trained model is stored as:

    churn_model.pkl

FastAPI loads the saved model when the application starts and uses it to generate predictions from customer input.

The API returns:

- **Prediction:** Churn / Not Churn
- **Churn Probability**
- **Customer Age**
- **Customer Tenure**

## 📊 Input Features

| Feature | Description |
|---|---|
| Tenure | Customer tenure |
| Total Spend | Total customer spending |
| Usage Frequency | Frequency of service usage |
| Gender | Customer gender |
| Subscription Type | Customer subscription |
| Age | Customer age |
| Support Calls | Number of support calls |
| Contract Length | Contract duration |
| Last Interaction | Last customer interaction |
| Payment Delay | Payment delay |

## 🔌 API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API information |
| GET | `/health` | Check API and model status |
| POST | `/predict` | Generate churn prediction |

## 📖 Swagger Documentation

FastAPI automatically provides interactive API documentation.

Open:

    http://127.0.0.1:8000/docs

From Swagger UI, you can:

- View available endpoints
- Enter customer data
- Send POST requests
- Test predictions
- View API responses

## 🖥️ Streamlit Frontend

The Streamlit application provides a simple interface for entering customer information.

    Streamlit
        ↓
    requests.post()
        ↓
    FastAPI /predict
        ↓
    ML Model
        ↓
    Prediction

Streamlit application:

    http://localhost:8501

Network URL:

    http://10.235.139.97:8501

> The Network URL is accessible only on the same local network while the application is running.

## ⚠️ Error Handling

The API uses `HTTPException` to return proper HTTP error responses when prediction fails.

This prevents backend errors from being returned as normal successful responses.

## 🛠️ Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- Scikit-learn
- Pandas
- Streamlit
- Requests
- Pickle
- Git & GitHub

## 📂 Project Structure

    Customer-Churn-FastAPI/
    │
    ├── app.py
    ├── churn_app.py
    ├── churn_model.pkl
    ├── test_api.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md

## ▶️ Run Locally

### 1. Create Virtual Environment

    python -m venv .venv

### 2. Activate Virtual Environment

    .venv\Scripts\activate

### 3. Install Dependencies

    pip install -r requirements.txt

### 4. Start FastAPI

    uvicorn app:app --reload

### 5. Start Streamlit

Open another terminal:

    streamlit run churn_app.py

## 🧪 API Testing

### API Home

    http://127.0.0.1:8000/

### Health Check

    http://127.0.0.1:8000/health

### Swagger UI

    http://127.0.0.1:8000/docs

## 📚 Key Learnings

- Building REST APIs with FastAPI
- Creating GET and POST endpoints
- Pydantic data validation
- Loading trained ML models
- Sending JSON requests
- Returning prediction results
- Handling API errors
- Testing APIs with Swagger
- Connecting Streamlit with FastAPI
- Structuring an ML API project
- Preparing an ML API for deployment

## 🚀 Project

**Customer Churn Prediction API — FastAPI + Machine Learning + Streamlit**