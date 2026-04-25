import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def train_energy_model(data_path):
    df = pd.read_csv(data_path)

    X = df[["Size", "Year_Built"]]
    y = df["Energy_Usage"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"Model Accuracy (R² score): {score}")

    return model


# 🔥 New function
def predict_energy(model, size, year_built):
    input_data = pd.DataFrame([[size, year_built]], columns=["Size", "Year_Built"])
    prediction = model.predict(input_data)
    return prediction[0]