# Insurance Charge Predictor — Flask App

Deployable Flask app for the insurance charges regression models from your notebook.
## 1. Project structure
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
