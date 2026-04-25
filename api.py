from fastapi import FastAPI
from pipeline.process_data import process_energy_data
from pipeline.train_model import train_energy_model, predict_energy

app = FastAPI()

# Run pipeline + train model once when API starts
input_file = "data/energy_data.csv"
processed_file = "data/processed_data.csv"

process_energy_data(input_file, processed_file)
model = train_energy_model(processed_file)


@app.get("/")
def home():
    return {"message": "Energy Prediction API is running"}


@app.get("/predict")
def predict(size: float, year_built: int):
    result = predict_energy(model, size, year_built)
    return {"predicted_energy_usage": result}