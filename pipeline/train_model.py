import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import joblib


def train_energy_model(data_path):
    df = pd.read_csv(data_path)

    X = df[[
        "Relative_Compactness",
        "Surface_Area",
        "Wall_Area",
        "Roof_Area",
        "Overall_Height"
    ]]

    y = df["Heating_Load"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Linear Regression
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    lr_score = lr_model.score(X_test, y_test)

    # Random Forest
    rf_model = RandomForestRegressor()
    rf_model.fit(X_train, y_train)
    rf_score = rf_model.score(X_test, y_test)

    print(f"Linear Regression R²: {lr_score}")
    print(f"Random Forest R²: {rf_score}")

    # Choose best model
    if rf_score > lr_score:
        model = rf_model
        print("Using Random Forest model")
    else:
        model = lr_model
        print("Using Linear Regression model")

    # Save best model
    joblib.dump(model, "model.pkl")

    return model


def predict_energy(model, rc, sa, wa, ra, oh):
    input_data = pd.DataFrame(
        [[rc, sa, wa, ra, oh]],
        columns=[
            "Relative_Compactness",
            "Surface_Area",
            "Wall_Area",
            "Roof_Area",
            "Overall_Height"
        ]
    )

    prediction = model.predict(input_data)
    return prediction[0]