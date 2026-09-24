# 🏥 Insurance Charge Predictor

A machine learning web application that predicts **medical insurance charges** based on customer information such as age, BMI, smoking status, number of children, sex, and region.

The project includes multiple regression models and provides an interactive **Flask web interface** as well as a REST API for making predictions.

### 🚀 Live Demo

**[Insurance Charge Predictor](https://insurance-charges-predictor.onrender.com/)**

---

## 📌 Project Overview

Insurance companies need to estimate potential medical costs based on customer characteristics.

This project applies **regression machine learning algorithms** to predict insurance charges from customer demographic and lifestyle information.

The trained models are integrated into a Flask application and deployed online using **Render**.

### Input Features

* Age
* Sex
* BMI
* Number of children
* Smoking status
* Region

### Output

The application predicts the estimated **insurance charge** based on the selected machine learning model.

---

## 🤖 Machine Learning Models

The application currently supports three regression models:

| Model                   | Type                |
| ----------------------- | ------------------- |
| Linear Regression       | Regression          |
| Decision Tree Regressor | Regression          |
| Random Forest Regressor | Ensemble Regression |

Users can select a model and generate an insurance charge prediction directly from the web interface.

---

## 🏗️ Project Structure

```text
insurance_app/
│
├── app.py                         # Flask application
├── requirements.txt               # Python dependencies
├── render.yaml                    # Render deployment configuration
│
├── templates/
│   └── index.html                 # Web interface
│
└── models/
    ├── linear_regression_model.pkl
    ├── decision_tree_model.pkl
    └── random_forest_model.pkl
```

---

## ⚙️ Technologies Used

### Programming & Frameworks

* Python
* Flask
* Gunicorn

### Machine Learning

* Scikit-learn
* Regression algorithms
* Pickle model serialization

### Deployment

* Render
* GitHub

### Frontend

* HTML
* CSS
* Flask Jinja templates

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/insurance-charge-predictor.git
cd insurance-charge-predictor
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

---

## 🌐 Deployment on Render

This application is configured for deployment on **Render**.

### Option 1 — Using `render.yaml`

Push the project to GitHub and connect the repository to Render.

Render can use the included `render.yaml` configuration.

### Option 2 — Configure manually

Use the following settings:

**Build Command**

```bash
pip install -r requirements.txt
```

**Start Command**

```bash
gunicorn app:app
```

Render provides the `PORT` environment variable automatically.

---

## 🔌 API

The application exposes a prediction endpoint:

```text
POST /predict
```

### Request

Send a JSON request containing the customer information and the model to use.

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

### Response

```json
{
  "model": "Random Forest",
  "prediction": 5321.44
}
```

The prediction value represents the estimated insurance charge.

---

## 🧪 Example API Request

Using Python:

```python
import requests

url = "https://insurance-charges-predictor.onrender.com/predict"

data = {
    "age": 34,
    "sex": "female",
    "bmi": 27.5,
    "children": 1,
    "smoker": "no",
    "region": "southeast",
    "model": "random_forest"
}

response = requests.post(url, json=data)

print(response.json())
```

---

## 🔄 Application Workflow

```text
User Input
    │
    ▼
Flask Web Application
    │
    ▼
Feature Processing
    │
    ▼
Selected ML Model
    │
    ├── Linear Regression
    ├── Decision Tree
    └── Random Forest
    │
    ▼
Insurance Charge Prediction
    │
    ▼
Result Displayed to User
```

---

## 📊 Prediction Features

| Feature    | Description                                |
| ---------- | ------------------------------------------ |
| `age`      | Customer's age                             |
| `sex`      | Customer's sex                             |
| `bmi`      | Body Mass Index                            |
| `children` | Number of children/dependents              |
| `smoker`   | Smoking status                             |
| `region`   | Customer's geographical region             |
| `model`    | Machine learning model used for prediction |

---

## 🎯 Project Objectives

* Build regression models for insurance charge prediction
* Compare different regression algorithms
* Serialize trained models for production use
* Create a Flask-based prediction API
* Build a simple web interface
* Deploy the ML application online
* Demonstrate an end-to-end machine learning deployment workflow

---

## 🚀 Future Improvements

* Add model performance comparison
* Add R², MAE, and RMSE metrics
* Improve input validation
* Add preprocessing pipelines
* Add prediction history
* Add data visualization
* Add Docker support
* Add automated CI/CD
* Add model monitoring
* Add logging and error handling
* Add API documentation with Swagger/OpenAPI

---

## 📁 Model Files

The trained models are stored in the `models/` directory as serialized `.pkl` files.

```text
models/
├── linear_regression_model.pkl
├── decision_tree_model.pkl
└── random_forest_model.pkl
```

These models are loaded by the Flask application when making predictions.

---

## 🌍 Live Application

Try the deployed application:

**https://insurance-charges-predictor.onrender.com/**

---

## 👨‍💻 Author

**Sakib Ahmed**

Data Analyst | Machine Learning Enthusiast

Interested in:

* Data Analytics
* Machine Learning
* Python
* SQL
* Power BI
* MLOps
* AI Applications
