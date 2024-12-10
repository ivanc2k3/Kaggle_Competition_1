import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Load the training data to train the models
data = pd.read_csv('./train.csv')  # Replace with the actual path

# Define new features for gender prediction
gender_features = ['az_mean', 'gx_mean', 'gy_mean', 'gz_mean', 'gx_var', 'gy_var', 'gx_rms']
X_gender = data[gender_features]
y_gender = data['gender']

# Original features for hold racket handed prediction
X_hold_racket = data.drop(columns=['play years', 'player_ID', 'gender', 'hold racket handed', 'level', 'data_ID'])
y_hold_racket = data['hold racket handed']

# Initialize and train the gender model with new features
gender_model = RandomForestClassifier(n_estimators=100, random_state=42)
gender_model.fit(X_gender, y_gender)

# Initialize and train the hold racket handed model with original features
hold_racket_model = RandomForestClassifier(n_estimators=100, max_depth = 12, random_state=42)
hold_racket_model.fit(X_hold_racket, y_hold_racket)

# Load the test data
test_data = pd.read_csv('./test.csv')  # Replace with the actual path
X_gender_test = test_data[gender_features]
X_hold_racket_test = test_data.drop(columns=['data_ID'])

# Predict probabilities and apply thresholds
gender_prob = gender_model.predict_proba(X_gender_test)[:, 1] > 0.35
hold_racket_prob = hold_racket_model.predict_proba(X_hold_racket_test)[:, 1] > 0.03

# Convert probabilities to binary predictions
gender_pred = np.where(gender_prob, 1, 0)
hold_racket_pred = np.where(hold_racket_prob, 1, 0)

# Create a DataFrame with predictions
predictions_df = pd.DataFrame({
    'gender': gender_pred,
    'hold_racket_handed': hold_racket_pred
})

# Save to CSV
predictions_df.to_csv('wy1.csv', index=False)
