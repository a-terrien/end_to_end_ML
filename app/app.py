import joblib
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

# Define the app action
app=Flask(__name__)

# Load the model
regmodel = joblib.load('../models/regmodel.joblib')

@app.route('/')
# home page
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1, -1))
    new_data = np.array(list(data.values())).reshape(1, -1)
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])
    
if __name__=='__main__':
    app.run(debug=True)
    # data = request.get_json(force=True)
    # data = np.array(data)
    # data = data.reshape(1, -1)
    # prediction = regmodel.predict(data)
    # output = prediction[0]
    # return jsonify(output)