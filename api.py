from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
from pipeline.train_model import predict_energy

app = FastAPI()

# Load trained model (make sure you saved it earlier)
model = joblib.load("model.pkl")


# Input validation model
class InputData(BaseModel):
    rc: float = Field(..., gt=0, description="Relative Compactness")
    sa: float = Field(..., gt=0, description="Surface Area")
    wa: float = Field(..., gt=0, description="Wall Area")
    ra: float = Field(..., gt=0, description="Roof Area")
    oh: float = Field(..., gt=0, description="Overall Height")


@app.get("/")
def home():
    return {"message": "Energy Prediction API is running"}


@app.post("/predict-heating-load")
def predict(data: InputData):

    prediction = predict_energy(
        model,
        data.rc,
        data.sa,
        data.wa,
        data.ra,
        data.oh
    )

    # Business logic layer
    if prediction > 25:
        risk = "High"
        recommendation = "Energy efficiency improvement recommended"
    else:
        risk = "Low"
        recommendation = "Energy performance is acceptable"

    return {
        "predicted_heating_load": round(prediction, 2),
        "risk_level": risk,
        "recommendation": recommendation
    }