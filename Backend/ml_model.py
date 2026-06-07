import numpy as np
from sklearn.linear_model import LinearRegression

# Training Data
X = np.array([
    [50, 20, 30],
    [100, 40, 32],
    [200, 60, 28],
    [300, 80, 25],
    [400, 100, 22]
])

y = np.array([20, 40, 60, 80, 95])

model = LinearRegression()
model.fit(X, y)

def predict_risk(rainfall, wind_speed, temperature):
    prediction = model.predict([[rainfall, wind_speed, temperature]])
    score = round(float(prediction[0]), 2)

    if score < 30:
        level = "Low"
        action = "Normal monitoring."
    elif score < 70:
        level = "Moderate"
        action = "Prepare emergency teams."
    else:
        level = "High"
        action = "Immediate evacuation required!"

    return {
        "score": score,
        "severity": level,
        "action": action
    }