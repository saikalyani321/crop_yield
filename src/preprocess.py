from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

def preprocess_data(df):
    y = df["Yield"]
    X = df.drop("Yield", axis=1)

    categorical_cols = ["Crop", "Season", "State"]
    numerical_cols = ["Crop_Year", "Area", "Production", "Annual_Rainfall", "Fertilizer", "Pesticide"]

    preprocessor = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numerical_cols)
    ])

    X_processed = preprocessor.fit_transform(X)
    return X_processed, y, preprocessor
