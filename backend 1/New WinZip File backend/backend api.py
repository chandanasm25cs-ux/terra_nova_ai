from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return "Earthquake & Flood Assessment Backend Running"

# Upload API
@app.route('/upload', methods=['POST'])
def upload_file():

    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"})

    image = request.files['image']

    filepath = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(filepath)

    return jsonify({
        "message": "Upload successful",
        "path": filepath
    })

# Flood Prediction API
@app.route('/predict/flood', methods=['POST'])
def predict_flood():

    result = {
        "disaster": "Flood",
        "severity": "High",
        "water_level": "78%",
        "timestamp": str(datetime.now())
    }

    return jsonify(result)

# Earthquake Prediction API
@app.route('/predict/earthquake', methods=['POST'])
def predict_earthquake():

    result = {
        "disaster": "Earthquake",
        "building_damage": "Severe",
        "casualty_risk": "Medium",
        "rescue_priority": "Immediate"
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)