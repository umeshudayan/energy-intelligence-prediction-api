import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def train_energy_model(data_path):
    df = pd.read_csv(data_path)

    # Features (your renamed columns)
    X = df[[
        "Relative_Compactness",
        "Surface_Area",
        "Wall_Area",
        "Roof_Area",
        "Overall_Height"
    ]]

    # Target
    y = df["Heating_Load"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"Model Accuracy (R² score): {score}")

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