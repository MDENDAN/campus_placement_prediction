from flask import Flask, request, jsonify
from model import load_model, predict # Assuming your logic is here

app = Flask(__name__) # Vercel looks for this 'app' variable

# Load models
status_model = load_model('model/status/DT_model.joblib')

@app.route('/predict', methods=['POST'])
def make_prediction():
    data = request.json
    # data would be a list of values: [0, 67.0, 0, 91.0, ...]
    prediction = predict(status_model, [data['values']])
    return jsonify({"placement_status": int(prediction[0])})

@app.route('/')
def index():
    return "Campus Placement API is Running"
