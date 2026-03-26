import numpy as np
import joblib
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def train_model(x_train, y_train):
    model = XGBRegressor(
        n_estimators=90,
        max_depth=5,
        learning_rate=0.01,
        random_state=42
    )
    model.fit(x_train, y_train)
    return model

def evaluate_model(model, x_test, y_test):
    y_pred = model.predict(x_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"RMSE: {rmse:.2f}")
    print(f"MAE: {mae:.2f}")
    print(f"R²: {r2:.2f}")
    return rmse, mae, r2

def save_model(model, path='artifacts/ipo_model.pkl'):
    joblib.load(path)
    print(f"Model saved to {path}")

def load_model(path='artifacts/ipo_model.pkl'):
    return joblib.load(path)