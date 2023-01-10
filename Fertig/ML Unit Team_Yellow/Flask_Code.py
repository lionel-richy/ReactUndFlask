
import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template , make_response
import joblib
from joblib import load



import pandas as pd 
#import h5py






app = Flask(__name__, template_folder='Template')


 
#results = joblib.load("results.pkl")
#results = pickle.load(open("results.pkl", "rb"))
model = pickle.load(open("lr.pkl", "rb"))




@app.route("/", methods=["POST", "GET"], strict_slashes=False)  # this sets the route to this page

def user():
    #if request.method == "POST":
        
        return  render_template("login.html")
        
        #return make_response("Succes", 200)
        
    #else:
        #return make_response("Make sure you write the right address", 200)


@app.route("/data", methods=["POST", "GET"], strict_slashes=False)  # Json data

def dataReactToFlask():
    f = open('log.txt' , 'r')
    contents=f.readlines()
    return  contents[0:60]



@app.route("/result", methods=["POST", "GET"], strict_slashes=False)  # 
def modelToFlask():
    return  render_template("result.html")




@app.route("/predict", methods = ["POST", "GET"])


def predict():
    # If a form is submitted
    if request.method == "POST":
        
        prediction = "Blabla"
        
        
    else:
        # getting input with name = fname in HTML form
        LatitudeStart = request.args.get("LatitudeStart")
        LongitudeStart = request.args.get("LongitudeStart")
        LatitudeEnd = request.args.get("LatitudeEnd")
        LongitudeEnd = request.args.get("LongitudeEnd")
    
        X = pd.DataFrame([[LatitudeStart, LongitudeStart, LatitudeEnd, LongitudeEnd]], columns = ["latitudeStart", "longitudeStart", "latitudeEnd", "longitudeEnd" ])
        # Get prediction
        print("-----------REQUEST###--------------->")
        print(request.args)
        
        prediction = model.predict(X)[0]
        
        print( prediction )
       
        print("-----------PREDICTION###--------------->")
        
        
    
        
    return render_template("result.html", prediction_text = "The average Speed is {}".format(prediction))
    

    
    #float_features = [float(x) for x in request.form.values()] # Get the data from the POST request
    #features = [np.array(float_features)]
    
    
    
    

    #prediction = model.predict(features)
    #y_pred = regressor.predict(features)
    































if __name__ == '__main__':
    app.run(debug=True)