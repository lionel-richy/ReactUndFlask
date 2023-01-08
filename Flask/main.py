
import numpy as np

from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='Template')

@app.route('/')



def home():
    return  render_template("result.html")







if __name__ == '__main__':
    app.run(debug=True)