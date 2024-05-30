from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Function to move product to production line based on predicted product
def move_product(predicted_product):
    production_lines = {
        'Can': 'A',
        'Milk Bottle': 'B',
        'Water Bottle': 'C',
        'Carton': 'D'
    }

    if predicted_product in production_lines:
        production_line = production_lines[predicted_product]
        return f"Move product to production line {production_line}"
    else:
        return "Unknown product type"

# API endpoint and keys
url = "https://westeurope.api.cognitive.microsoft.com/customvision/v3.0/Prediction/0bea104e-2d67-45ba-a91f-fb91e311d57b/classify/iterations/FridgeObjects/image"
prediction_key = "5bf2b233edb94d888cd7c5cc54595458"
content_type = "application/octet-stream"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        image_file = request.files['file']
        image_data = image_file.read()

        # Set headers
        headers = {
            'Prediction-Key': prediction_key,
            'Content-Type': content_type
        }

        # Make the API call
        response = requests.post(url, headers=headers, data=image_data)

        # Check the response
        if response.status_code == 200:
            results = response.json()  # Parsing JSON response directly

            # Get the top predicted product
            top_prediction = max(results['predictions'], key=lambda x: x['probability'])

            predicted_product = top_prediction['tagName']
            probability = top_prediction['probability']

            # Perform action based on the top predicted product
            action = move_product(predicted_product)

            return render_template('result.html', predicted_product=predicted_product, probability=probability, action=action)

        else:
            return "Error: {}".format(response.status_code)

if __name__ == '__main__':
    app.run(debug=True)
