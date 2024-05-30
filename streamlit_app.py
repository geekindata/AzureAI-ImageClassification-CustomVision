import streamlit as st
import requests

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

def main():
    st.title("Product Prediction")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Make the API call
        headers = {'Prediction-Key': prediction_key, 'Content-Type': content_type}
        response = requests.post(url, headers=headers, data=uploaded_file.read())

        # Check the response
        if response.status_code == 200:
            results = response.json()

            # Get the top predicted product
            top_prediction = max(results['predictions'], key=lambda x: x['probability'])

            predicted_product = top_prediction['tagName']
            probability = top_prediction['probability']

            # Perform action based on the top predicted product
            action = move_product(predicted_product)

            st.header("Prediction Result")
            st.write(f"Predicted Product: {predicted_product}")
            st.write(f"Probability: {probability}")
            st.write(f"Action: {action}")
        else:
            st.error(f"Error: {response.status_code}")

if __name__ == '__main__':
    main()
