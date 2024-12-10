import pandas as pd

# Load the source data from wy.csv and target data from predictions36.csv
wy_data = pd.read_csv('./wy1.csv')  # Replace with the actual path
predictions_data = pd.read_csv('./predictions36.csv')  # Replace with the actual path

# Copy the specified columns
predictions_data['gender'] = wy_data['gender']
predictions_data['hold racket handed'] = wy_data['hold_racket_handed']

# Save the updated data back to predictions36.csv
predictions_data.to_csv('./predictions141.csv', index=False)  # Overwrite or use a new path as needed
