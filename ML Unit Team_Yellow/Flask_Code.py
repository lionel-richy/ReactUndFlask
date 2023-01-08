
import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template
import joblib
from joblib import load


app = Flask(__name__, template_folder='Template')

#
# Unpickle 
#results = joblib.load("results.pkl")
#results = pickle.load(open("results.pkl", "rb"))
@app.route('/')



def home():
    return  render_template("result.html")

@app.route("/predict", methods = ["POST"])

def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = results.predict(features)
    return render_template("result.html", prediction_text = "The average Speed is {}".format(prediction))





if __name__ == '__main__':
    app.run(debug=True)