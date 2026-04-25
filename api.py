from fastapi import FastAPI
from pipeline.process_data import process_energy_data
from pipeline.train_model import train_energy_model, predict_energy

app = FastAPI()

input_file = "data/energy_data.csv"
processed_file = "data/processed_data.csv"

process_energy_data(input_file, processed_file)
model = train_energy_model(processed_file)


@app.get("/")
def home():
    return {"message": "Energy Prediction API is running"}


@app.get("/predict")
def predict(rc: float, sa: float, wa: float, ra: float, oh: float):
    result = predict_energy(model, rc, sa, wa, ra, oh)
    return {"predicted_heating_load": result}