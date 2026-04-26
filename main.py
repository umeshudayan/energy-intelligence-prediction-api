from pipeline.process_data import process_energy_data
from pipeline.train_model import train_energy_model, predict_energy


input_file = "data/energy_data.csv"
processed_file = "data/processed_data.csv"

# Run pipeline
process_energy_data(input_file, processed_file)

# Train model
model = train_energy_model(processed_file)

# 🔮 Make prediction
predicted_value = predict_energy(
    model,
    0.98,      # Relative Compactness
    514.5,     # Surface Area
    294,       # Wall Area
    110.25,    # Roof Area
    7          # Overall Height
)


print(f"Predicted Energy Usage: {predicted_value}")

print("Project completed successfully!")