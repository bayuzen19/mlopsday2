from pydantic import BaseModel, Field
from typing import Dict, Optional, List

class ModelMetrics(BaseModel):
    """Model metrics schema"""
    accuracy: float = Field(..., description="Model accuracy")
    precision: float = Field(..., description="Model precision")
    recall: float = Field(..., description="Model recall")
    f1: float = Field(..., description="Model F1 score")
    roc_auc: float = Field(..., description="Model ROC AUC score")

class ModelInfo(BaseModel):
    """Model information schema"""
    run_id: str = Field(..., description="MLflow run ID")
    metrics: ModelMetrics = Field(..., description="Model metrics")

class ChurnPredictionRequest(BaseModel):
    """Churn prediction request schema"""
    customerID: str = Field(..., description="Customer ID")
    gender: str = Field(..., description="Customer gender")
    SeniorCitizen: int = Field(..., ge=0, le=1, description="Whether customer is senior citizen")
    Partner: str = Field(..., description="Whether customer has partner")
    Dependents: str = Field(..., description="Whether customer has dependents")
    tenure: int = Field(..., ge=0, description="Number of months customer has stayed")
    PhoneService: str = Field(..., description="Whether customer has phone service")
    MultipleLines: str = Field(..., description="Whether customer has multiple lines")
    InternetService: str = Field(..., description="Internet service provider")
    OnlineSecurity: str = Field(..., description="Whether customer has online security")
    OnlineBackup: str = Field(..., description="Whether customer has online backup")
    DeviceProtection: str = Field(..., description="Whether customer has device protection")
    TechSupport: str = Field(..., description="Whether customer has tech support")
    StreamingTV: str = Field(..., description="Whether customer has streaming TV")
    StreamingMovies: str = Field(..., description="Whether customer has streaming movies")
    Contract: str = Field(..., description="Contract term")
    PaperlessBilling: str = Field(..., description="Whether customer has paperless billing")
    PaymentMethod: str = Field(..., description="Payment method")
    MonthlyCharges: float = Field(..., gt=0, description="Monthly charges")
    TotalCharges: float = Field(..., ge=0, description="Total charges")

    class Config:
        schema_extra = {
            "example": {
                "customerID": "7590-VHVEG",
                "gender": "Female",
                "SeniorCitizen": 0,
                "Partner": "Yes",
                "Dependents": "No",
                "tenure": 12,
                "PhoneService": "Yes",
                "MultipleLines": "No",
                "InternetService": "DSL",
                "OnlineSecurity": "No",
                "OnlineBackup": "Yes",
                "DeviceProtection": "No",
                "TechSupport": "No",
                "StreamingTV": "No",
                "StreamingMovies": "No",
                "Contract": "Month-to-month",
                "PaperlessBilling": "Yes",
                "PaymentMethod": "Electronic check",
                "MonthlyCharges": 29.85,
                "TotalCharges": 358.20
            }
        }

class ChurnPredictionResponse(BaseModel):
    """Churn prediction response schema"""
    customerID: str = Field(..., description="Customer ID")
    churn_probability: float = Field(..., ge=0, le=1, description="Probability of churn")
    churn_prediction: bool = Field(..., description="Churn prediction (True/False)")
    # model_info: ModelInfo = Field(..., description="Model information and metrics")