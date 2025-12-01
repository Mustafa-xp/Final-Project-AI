from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("best_random_forest.pkl", mmap_mode=None)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    temp = float(request.form["Temperature"])
    hum = float(request.form["Humidity"])
    wind = float(request.form["Wind_Speed"])
    cloud = float(request.form["Cloud_Cover"])
    pressure = float(request.form["Pressure"])

    # Prepare input
    features = np.array([[temp, hum, wind, cloud, pressure]])

    # Predict
    prediction = model.predict(features)[0]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
