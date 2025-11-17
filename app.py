from flask import Flask, render_template, request, Response
import pickle
import pandas as pd
import numpy as np
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Load ML model + data
model = pickle.load(open('LR.pkl', 'rb'))
car = pd.read_csv("Cleaned_car.csv")

# Prometheus metrics
PREDICTIONS = Counter('ml_predictions_total', 'Total predictions made')
ERRORS = Counter('ml_prediction_errors_total', 'Total prediction errors')

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = car['fuel_type'].unique()

    return render_template("index.html",
                           companies=companies,
                           car_models=car_models,
                           years=years,
                           fuel_types=fuel_types)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        company = request.form['company']
        model_name = request.form['car_model']
        year = int(request.form['year'])
        fuel_type = request.form['fuel_type']
        kms = int(request.form['kilo_driven'])

        df = pd.DataFrame([[model_name, company, year, kms, fuel_type]],
                          columns=['name','company','year','kms_driven','fuel_type'])

        prediction = model.predict(df)[0]
        
        PREDICTIONS.inc()
        return str(prediction)

    except Exception as e:
        ERRORS.inc()
        print("Error:", e)
        return "Prediction failed"

# Prometheus metrics endpoint
@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
