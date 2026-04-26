from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
from pipeline.train_model import predict_energy

app = FastAPI(title="Energy Intelligence Prediction API")

model = joblib.load("model.pkl")


class EnergyInput(BaseModel):
    rc: float = Field(..., gt=0)
    sa: float = Field(..., gt=0)
    wa: float = Field(..., gt=0)
    ra: float = Field(..., gt=0)
    oh: float = Field(..., gt=0)


@app.post("/predict-heating-load")
def predict_heating_load(data: EnergyInput):
    prediction = predict_energy(
        model,
        data.rc,
        data.sa,
        data.wa,
        data.ra,
        data.oh
    )

    prediction = round(prediction, 2)

    if prediction >= 26:
        risk = "High"
        recommendation = "Energy efficiency improvement recommended"
    elif prediction >= 18:
        risk = "Medium"
        recommendation = "Moderate energy usage, consider optimisation"
    else:
        risk = "Low"
        recommendation = "Energy efficient building"

    return {
        "predicted_heating_load": prediction,
        "energy_category": risk,
        "recommendation": recommendation
    }