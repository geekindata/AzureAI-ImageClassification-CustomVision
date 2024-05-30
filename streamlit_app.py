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
    st.image("static\GeekInData Black.png", caption="Company Logo", use_column_width=True)
    st.title("Product Prediction")
    st.markdown("### Instructions:")
    st.markdown("- Take a clear picture of the product [A Can, A Milk Bottle, A Water Bottle, A Carton] you want to predict.")
    st.markdown("- Upload the image using the uploader below.")
    st.markdown("- The model will predict the product and suggest an action based on the prediction.")


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
            
            st.header("Prediction Result")
            # Perform action based on the top predicted product
            if probability >= 0.7:
                action = move_product(predicted_product)
                st.write(f"Predicted Product: {predicted_product}")
                st.write(f"Probability: {probability}")
            else:
                action = "No product detected, send for review"

            st.write(f"Action: {action}")
        else:
            st.error(f"Error: {response.status_code}")


if __name__ == '__main__':
    main()
