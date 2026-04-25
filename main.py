from pipeline.process_data import process_energy_data
from pipeline.train_model import train_energy_model, predict_energy


input_file = "data/energy_data.csv"
processed_file = "data/processed_data.csv"

# Run pipeline
process_energy_data(input_file, processed_file)

# Train model
model = train_energy_model(processed_file)

# 🔮 Make prediction
predicted_value = predict_energy(model, size=130, year_built=2010)

print(f"Predicted Energy Usage: {predicted_value}")

print("Project completed successfully!")