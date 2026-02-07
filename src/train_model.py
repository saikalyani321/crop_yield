import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from preprocess import preprocess_data

df = pd.read_csv("data/crop_yield.csv")

X, y, preprocessor = preprocess_data(df)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

preds = model.predict(X_test)
print("Model R2 Score:", r2_score(y_test, preds))

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.pkl")
joblib.dump(preprocessor, "models/preprocessor.pkl")

print("✅ Model & Preprocessor Saved!")
