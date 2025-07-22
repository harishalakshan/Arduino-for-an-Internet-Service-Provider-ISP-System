import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def train_model():
    data = pd.read_csv("sensor_data.csv")
    X = data[["temperature", "humidity", "voltage"]]
    y = data["failure_risk"]
    model = LinearRegression().fit(X, y)
    joblib.dump(model, "forecast_model.pkl")

if __name__ == "__main__":
    train_model()
