# Insurance Charge Predictor — Flask App

Deployable Flask app for the insurance charges regression models from your notebook.

## Project structure
```
insurance_app/
├── app.py
├── requirements.txt
├── render.yaml
├── templates/
│   └── index.html
└── models/
    ├── linear_regression_model.pkl
    ├── decision_tree_model.pkl
    └── random_forest_model.pkl
```

## 1. Add your model files
Copy the `.pkl` files your notebook already saves via `joblib.dump(...)` into `models/`:
- `linear_regression_model.pkl`
- `decision_tree_model.pkl`
- `random_forest_model.pkl`

Each file must be the **full pipeline** (`preprocessor` + model), exactly as your
notebook's "Saving model" cell does — the app calls `pipeline.predict(row)` directly
on raw columns (`age, sex, bmi, children, smoker, region`), so the preprocessing
(OneHotEncoder + StandardScaler) must already be baked into the pickle.

The app auto-detects which of the three files are present; the dropdown in the UI
disables any model whose file is missing, so you can deploy with just one model if
you prefer.

⚠️ **scikit-learn version**: pickle files are sensitive to the scikit-learn version
used to create them. Set the same version in `requirements.txt` as the one in your
notebook environment to avoid unpickling errors (check with `import sklearn; sklearn.__version__`).

## 2. Run locally
```bash
cd insurance_app
python -m venv venv && source venv/bin/activate   # optional but recommended
pip install -r requirements.txt
python app.py
```
Visit http://localhost:5000

## 3. Deploy on Render
1. Push this folder to a GitHub repo.
2. In Render: **New → Web Service**, connect the repo.
3. Render will detect `render.yaml` automatically, or set manually:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
4. Deploy. Render assigns a public URL automatically (the app reads `PORT` from the
   environment, which Render sets for you).

## API
`POST /predict` — JSON body:
```json
{
  "age": 34,
  "sex": "female",
  "bmi": 27.5,
  "children": 1,
  "smoker": "no",
  "region": "southeast",
  "model": "random_forest"
}
```
Response:
```json
{ "model": "Random Forest", "prediction": 5321.44 }
```
