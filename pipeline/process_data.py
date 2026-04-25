import pandas as pd


def process_energy_data(input_path, output_path):
    # Load raw data
    df = pd.read_csv(input_path)

    print("Original Data:")
    print(df)

    # 🔹 Remove missing values
    df = df.dropna()

    # 🔹 Remove duplicate rows
    df = df.drop_duplicates()

    # 🔹 Ensure correct data types (optional but good practice)
    df["Size"] = df["Size"].astype(float)
    df["Energy_Usage"] = df["Energy_Usage"].astype(float)

    # 🔹 Create new feature
    df["Energy_per_Size"] = df["Energy_Usage"] / df["Size"]

    # Save processed data
    df.to_csv(output_path, index=False)

    return df