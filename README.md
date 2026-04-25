# Energy Intelligence Prediction API

A mini machine learning project that processes building energy data, trains a regression model, and exposes predictions through a FastAPI endpoint.

## Features
- Data cleaning using pandas
- Feature engineering (energy per size)
- ML model using scikit-learn
- API using FastAPI

## Run

pip install -r requirements.txt
uvicorn api:app --reload

## Test

http://127.0.0.1:8000
http://127.0.0.1:8000/predict?size=130&year_built=2010