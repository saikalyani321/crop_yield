import joblib
import pandas as pd

model = joblib.load("models/model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

def predict_yield(input_dict):
    df = pd.DataFrame([input_dict])
    processed = preprocessor.transform(df)
    prediction = model.predict(processed)
    return round(prediction[0], 3)
