# Energy Intelligence Prediction API

A machine learning project that processes building energy data, performs feature engineering, and provides real-time energy usage predictions through a FastAPI endpoint.

---

## 🚀 Features

- Data pipeline using pandas (data cleaning & transformation)
- Feature engineering (energy usage per unit size)
- Machine learning model using Linear Regression (scikit-learn)
- REST API using FastAPI for real-time predictions

---

## 🧠 How It Works

1. Load raw building data from CSV  
2. Clean data (remove missing values and duplicates)  
3. Perform feature engineering (Energy per Size)  
4. Train regression model using Size and Year Built  
5. Expose prediction endpoint using FastAPI  

---

## 📊 Example

**Input:**
Size = 130
Year Built = 2010


**Output:**

Predicted Energy Usage: 266.67

## 🛠️ Tech Stack

- Python
- pandas
- scikit-learn
- FastAPI
- Uvicorn

---

## 📁 Project Structure

nergy project/
├── data/
│ ├── energy_data.csv
│ └── processed_data.csv
├── pipeline/
│ ├── process_data.py
│ └── train_model.py
├── api.py
├── main.py
├── requirements.txt
└── README.md


---

## ▶️ How to Run

Install dependencies:
```bash
pip install -r requirements.txt

uvicorn api:app --reload

🌐 API Endpoints

Home:

http://127.0.0.1:8000

Prediction:

http://127.0.0.1:8000/predict?size=130&year_built=2010

🎯 Purpose

This project demonstrates an end-to-end data and machine learning workflow, including data preprocessing, model training, and API deployment. It simulates a real-world energy intelligence system for predicting building energy usage.

📌 Future Improvements
Use larger real-world datasets
Improve model accuracy with advanced algorithms
Deploy API to cloud (AWS / Render)
Add frontend dashboard

---

## ✅ After pasting

Run:

```powershell
git add README.md
git commit -m "Add professional README"
git push


