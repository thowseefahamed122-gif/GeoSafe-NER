from flask import Flask, render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

# Load dataset
data = pd.read_csv("landslide_data.csv")

# Features
X = data[
    [
        "rainfall",
        "soil_moisture",
        "slope",
        "water_level"
    ]
]

# Target
y = data["risk"]

# Create and train AI model
model = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

model.fit(X, y)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    score = 0
    explanation = ""

    if request.method == "POST":

        rainfall = float(request.form["rainfall"])
        soil_moisture = float(request.form["soil_moisture"])
        slope = float(request.form["slope"])
        water_level = float(request.form["water_level"])

        new_data = pd.DataFrame(
            [[
                rainfall,
                soil_moisture,
                slope,
                water_level
            ]],
            columns=[
                "rainfall",
                "soil_moisture",
                "slope",
                "water_level"
            ]
        )

        prediction = model.predict(new_data)[0]

        probability = model.predict_proba(new_data)[0]

        # Convert AI probability to percentage
        score = int(probability[1] * 100)

        if prediction == 1:

            result = "🚨 HIGH LANDSLIDE RISK"

            explanation = (
                "The AI model detected environmental conditions "
                "that may increase landslide risk. "
                "Continuous monitoring is recommended."
            )

        else:

            result = "✅ LOW LANDSLIDE RISK"

            explanation = (
                "The current environmental conditions indicate "
                "a lower estimated landslide risk."
            )

    return render_template(
        "index.html",
        result=result,
        score=score,
        explanation=explanation
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)