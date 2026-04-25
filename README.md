# Energy Intelligence Prediction API

> Built a production-style machine learning system using a real-world energy dataset, delivering real-time predictions via a FastAPI-based API.

---

## 📌 Key Highlights

- Built end-to-end ML pipeline using real-world energy dataset (768 samples)
- Implemented data cleaning and feature engineering
- Developed regression model to predict building heating load
- Deployed model via FastAPI API for real-time predictions

---

## 🚀 Features

- Data pipeline using pandas (cleaning & transformation)
- Feature engineering using building characteristics
- Machine learning model using Linear Regression
- REST API using FastAPI for real-time predictions

---

## 🧠 How It Works

1. Load building energy dataset  
2. Clean data (missing values, duplicates removed)  
3. Select key features:
   - Relative Compactness  
   - Surface Area  
   - Wall Area  
   - Roof Area  
   - Overall Height  
4. Train regression model to predict Heating Load  
5. Expose model via API endpoint  

---

## 📸 API Demo

### 1. FastAPI Documentation
![API Docs](https://github.com/user-attachments/assets/550f7c77-5f56-436f-bd00-6480628270fe)

### 2. Input Parameters
![Input](https://github.com/user-attachments/assets/1dac0e82-01b3-466c-8e27-cbf9ca44c769)

### 3. Execution
![Execution](https://github.com/user-attachments/assets/dd4762c1-2982-47cb-8f87-9b28723954ba)

### 4. Prediction Output
![Output](https://github.com/user-attachments/assets/973b120f-dce5-4525-9962-2a2abdb62c08)

---
Relative_Compactness = 0.98
Surface_Area = 514.5
Wall_Area = 294
Roof_Area = 110.25
Overall_Height = 7

**Output:**


---

## 🛠️ Tech Stack

- Python
- pandas
- scikit-learn
- FastAPI
- Uvicorn

---

## 📁 Project Structure
energy-intelligence-prediction-api/
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

```bash
pip install -r requirements.txt
uvicorn api:app --reload

🌐 API Endpoints
Home:
http://127.0.0.1:8000
Prediction:
http://127.0.0.1:8000/predict?rc=0.98&sa=514.5&wa=294&ra=110.25&oh=7

🎯 Purpose

This project demonstrates a complete machine learning workflow, from data preprocessing and model training to API deployment, simulating a real-world energy intelligence system.

📌 Future Improvements
Use advanced models (Random Forest, XGBoost)
Deploy API to cloud (AWS / Render)
Add frontend dashboard
Integrate larger datasets

---

# 🚀 After pasting

Run:

```powershell
git add README.md
git commit -m "Upgrade README to professional level"
git push
## 📊 Example

**Input:**
