import os
import joblib
import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Map dropdown value -> pkl filename (must match names saved from the notebook,
# e.g. joblib.dump(pipeline, "random_forest_model.pkl"))
MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")
MODEL_FILES = {
    "linear_regression": "linear_regression_model.pkl",
    "decision_tree": "decision_tree_model.pkl",
    "random_forest": "random_forest_model.pkl",
}
MODEL_LABELS = {
    "linear_regression": "Linear Regression",
    "decision_tree": "Decision Tree",
    "random_forest": "Random Forest",
}

# Test R² scores reported in the notebook's evaluation cells. These are close
# approximations of the saved pipelines' real performance (the notebook evaluates
# slightly different hyperparameters than the ones it finally pickles), not an
# exact re-measurement of the .pkl files themselves. Update if you re-score them.
MODEL_R2 = {
    "linear_regression": 0.7319,
    "decision_tree": 0.8703,
    "random_forest": 0.8646,
}

# Load every model that is present at startup so requests don't hit disk each time.
models = {}
for key, filename in MODEL_FILES.items():
    path = os.path.join(MODEL_DIR, filename)
    if os.path.exists(path):
        models[key] = joblib.load(path)

REGIONS = ["southwest", "southeast", "northwest", "northeast"]


@app.route("/")
def home():
    return render_template(
        "index.html",
        models=MODEL_LABELS,
        available=list(models.keys()),
        regions=REGIONS,
    )


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or request.form

    model_key = data.get("model", "random_forest")
    if model_key not in models:
        return jsonify({
            "error": f"Model '{model_key}' is not available. "
                     f"Loaded models: {list(models.keys())}"
        }), 400

    try:
        age = float(data.get("age"))
        bmi = float(data.get("bmi"))
        children = float(data.get("children"))
        sex = data.get("sex")
        smoker = data.get("smoker")
        region = data.get("region")

        if sex not in ("male", "female"):
            raise ValueError("sex must be 'male' or 'female'")
        if smoker not in ("yes", "no"):
            raise ValueError("smoker must be 'yes' or 'no'")
        if region not in REGIONS:
            raise ValueError(f"region must be one of {REGIONS}")

    except (TypeError, ValueError) as e:
        return jsonify({"error": f"Invalid input: {e}"}), 400

    # Column order/names must match X_train columns from the notebook:
    # age, sex, bmi, children, smoker, region
    row = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region,
    }])

    pipeline = models[model_key]
    prediction = float(pipeline.predict(row)[0])

    return jsonify({
        "model": MODEL_LABELS.get(model_key, model_key),
        "prediction": round(prediction, 2),
        "r2": MODEL_R2.get(model_key),
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)