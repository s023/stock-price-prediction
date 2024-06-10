from flask import Flask, request, jsonify
from joblib import load
import pandas as pd
import os

app = Flask(__name__)

# Load the pre-trained model
model_path = os.path.join('model', 'ridge_regression_model.pkl')
model = load(model_path)


@app.route('/')
def home():
    return "Stock Price Prediction API"


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame(data)

        # Define the expected columns based on the training data
        expected_columns = [
            'Open', 'High', 'Low', 'Adj Close', 'Volume',
            'Solar', 'Wind', 'MA_5', 'MA_10', 'Close_Lag1',
            'Solar_Lag1', 'Wind_Lag1'
        ]

        # Ensure the DataFrame has the correct columns in the correct order
        df = df[expected_columns]

        # Make prediction
        prediction = model.predict(df)

        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
