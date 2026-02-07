from flask import Flask, render_template, request
import pandas as pd
from src.predict_pipeline import predict_yield

app = Flask(__name__)

df = pd.read_csv("data/crop_yield.csv")
crop_list = sorted(df["Crop"].unique())
season_list = sorted(df["Season"].unique())
state_list = sorted(df["State"].unique())

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            input_data = {
                "Crop": request.form["crop"],
                "Season": request.form["season"],
                "State": request.form["state"],
                "Crop_Year": int(request.form["year"]),
                "Area": float(request.form["area"]),
                "Production": float(request.form["production"]),
                "Annual_Rainfall": float(request.form["rainfall"]),
                "Fertilizer": float(request.form["fertilizer"]),
                "Pesticide": float(request.form["pesticide"])
            }

            prediction = predict_yield(input_data)

        except:
            error = "⚠ Please enter valid values in all fields!"

    return render_template(
        "index.html",
        prediction=prediction,
        error=error,
        crops=crop_list,
        seasons=season_list,
        states=state_list
    )

if __name__ == "__main__":
    app.run(debug=True)
