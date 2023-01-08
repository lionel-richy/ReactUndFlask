
import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template
import joblib
from joblib import load
#import pandas as pd 
import h5py

app = Flask(__name__, template_folder='Template')

#
# Unpickle 
#results = joblib.load("results.pkl")
results = pickle.load(open("results.pkl", "rb"))
#model = pickle.load(open("results.pkl", "rb"))
#model = pd.read_pickle('model.pkl')

#model = pd.read_pickle(open('model.pkl', 'rb'))


#with open('model.pkl', 'rb') as fo:
        #model = pickle.load(fo, encoding='latin1')



#resultat =  h5py.File('resultat.h5', 'r')






@app.route('/')



def home():
    return  render_template("result.html")

@app.route("/predict", methods = ["POST"])

def predict():
    float_features = [float(x) for x in request.form.values()] ## Get the data from the POST request
    features = [np.array(float_features)]
    
    #Make prediction using model loaded from disk as per the data.
    
    prediction = results.predict(features) 
    
    return render_template("result.html", prediction_text = "The average Speed is {}".format(prediction))





if __name__ == '__main__':
    app.run(debug=True)