import pandas as pd


def process_energy_data(input_path, output_path):
    df = pd.read_csv(input_path)

    print("Original Data:")
    print(df)

    df = df.dropna()
    df = df.drop_duplicates()

    numeric_columns = [
        "Relative_Compactness",
        "Surface_Area",
        "Wall_Area",
        "Roof_Area",
        "Overall_Height",
        "Heating_Load"
    ]

    for column in numeric_columns:
        df[column] = df[column].astype(float)

    df.to_csv(output_path, index=False)

    return df