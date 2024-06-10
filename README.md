# Stock Price Prediction API

This project is a Flask-based web application for predicting stock prices using a pre-trained Ridge Regression model. The model expects input features like opening price, highest price, lowest price, adjusted closing price, volume, and other related metrics.

## Project Structure


- `app.py`: The main Flask application file that contains the code to load the model and handle prediction requests.
- `ridge_regression_model.pkl`: The pre-trained Ridge Regression model.
- `requirements.txt`: A file listing the Python dependencies required for the project.
- `README.md`: This file, providing an overview and setup instructions for the project.
- `templates/`: Directory containing HTML templates for the Flask application.

## Setup Instructions

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

### Usage

Once the Flask application is running, you can test the prediction endpoint using tools like curl, Postman, or any other API testing tool.

## Deployed Application

The application is hosted on Render and can be accessed at the following URL:
https://stock-price-prediction-2qcg.onrender.com

## Testing the /predict Endpoint

To get a stock price prediction, send a POST request to the following endpoint:
https://stock-price-prediction-2qcg.onrender.com/predict