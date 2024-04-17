from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import sklearn
import gzip

# Create a Flask application object
app = Flask(__name__)
# File path to the compressed pickle file
input_file_path = 'model/cmprsd_model.pkl.gz'

# Decompress and load the model
with gzip.open(input_file_path, 'rb') as f:
    model = pickle.load(f)


# # Load the trained model
# model = pickle.load(open(r'model\Random_Forest.pkl', 'rb'))

# List of possible classes
severity_levels = ['Fatal', 'Grievous Injury', 'Damage Only', 'Simple Injury', 'ACHARI']

@app.route('/')
def index():
    return render_template('index.html')  # Change to index.html

@app.route('/predict', methods=['POST'])
def predict_accident():
    # Extract input data from the JSON request
    data = request.json
    Weather = int(data['weather'])
    District = int(data['district'])
    NumberOfVehicles = int(data['numberOfVehicles'])
    Latitude = float(data['latitude'])
    Longitude = float(data['longitude'])

    # Make prediction
    result = model.predict(np.array([Weather, District, NumberOfVehicles, Latitude, Longitude]).reshape(1, -1))
    prediction = severity_levels[result[0]]
    return jsonify({'prediction': prediction})

@app.route("/predictions")
def prediction():
        return render_template('predict.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/heatmap')
def heatmap():
    return render_template('accidents_heatmap.html')

@app.route('/severitymap')
def severitymap():
    return render_template('accidents_map2.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(port=4949, host="0.0.0.0")