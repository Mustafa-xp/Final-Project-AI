🌦️ Weather Prediction System

A simple machine learning project that predicts precipitation type using real weather data.
The system uses a trained Random Forest model and a lightweight Flask web app that allows users to input weather conditions and receive instant predictions.

🚀 Features

Real-time precipitation prediction

Clean Flask web interface

Trained on historical weather data

Uses key weather inputs:

Temperature

Humidity

Wind Speed

Cloud Cover

Pressure

🧠 Machine Learning

Multiple models were tested (Random Forest, Decision Tree, KNN, Naive Bayes, Gradient Boosting).
The Random Forest model achieved the best accuracy and is saved as:

best_random_forest.pkl

📁 Project Structure
project/
│── app.py
│── train_and_save.py
│── best_random_forest.pkl
│── weatherHistory.csv
│── requirements.txt
│── /templates/index.html
└── /static/style.css

▶️ Running the App

Install dependencies:

pip install -r requirements.txt


Train the model (first time only):

python train_and_save.py


Run the Flask server:

python app.py


Open in browser:

http://127.0.0.1:5000

📦 Requirements
flask
scikit-learn
pandas
numpy
joblib

📜 License

This project is open-source and free to use.
