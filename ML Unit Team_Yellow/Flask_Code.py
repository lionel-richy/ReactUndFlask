
import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template , make_response, url_for
import joblib
from joblib import load




import pandas as pd 
#import h5py








app = Flask(__name__, template_folder='Template')




        ## Open a file
#results = joblib.load("results.pkl")
#results = pickle.load(open("results.pkl", "rb"))
model = pickle.load(open("lr.pkl", "rb"))






database={'lionel':'1234','katrin':'5678','pari':'9001'}

@app.route("/login", methods=["POST", "GET"], strict_slashes=False)  # this sets the route to this page

def login():
    
    
    print("-----------REQUEST###--------------->")
        
        
    #name1= request.form["username"]
    #pwd= request.form["password"]
    
    name1= request.args.get("username")
    pwd= request.args.get("password")
        
    
    if name1 not in database:
	
        return render_template('login.html',info='Invalid User')

    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	        return render_template('result.html',name=name1)
              
    
#return  render_template("login.html")
            
        
        
        
        






@app.route("/", methods=["POST", "GET"], strict_slashes=False)  # this sets the route to this page

def user():
   
        
        return  render_template("login.html")
        
        


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
        tel =  "+49 15734735727"
        print( prediction )
       
        print("-----------PREDICTION###--------------->")
        
        if prediction >= 5.2:
            message1 ="This user has moved faster than normal this user is losing too much time on his route"
            tel =  "+49 15734735727"
            
        else:
            if prediction <= 3.0:
                message1 = "This user moves slowly"
                
            else:
                message1 = "This user moves normally, no need to notify a contact person"
            
            
            
        
        
    
        
    return render_template("result.html", prediction_text = "The average Speed is {}".format(prediction), alert_text =  "Finally we can see that ,  {}".format(message1) , alert_tel =  "A message has been sent to the number ,  {}".format(tel))
    

    
    #float_features = [float(x) for x in request.form.values()] # Get the data from the POST request
    #features = [np.array(float_features)]
    
    
    
    

    #prediction = model.predict(features)
    #y_pred = regressor.predict(features)
    































if __name__ == '__main__':
    app.run(debug=True)