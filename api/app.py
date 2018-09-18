import boto3
import pickle

from flask import Flask, request, json
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.externals import joblib

MODEL_FILE_NAME = 'model.pkl'

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():    
    # Parse request body for model input 
    body_dict = request.get_json(silent=True)    
    data = body_dict['data']     
    
    # Load model
    model = joblib.load(MODEL_FILE_NAME)
    # Make prediction 
    prediction = model.predict(data).tolist()
    # Respond with prediction result
    result = {'prediction': prediction}    
    return json.dumps(result)



if __name__ == '__main__':    
    # listen on all IPs 
    app.run(host='0.0.0.0')
