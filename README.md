# Image Classification Web App with Azure AI and Streamlit

In today's world of rapidly advancing technology, image classification has become a fundamental aspect of many applications, from identifying objects in photos to image classification in images. Leveraging the power of cloud services can greatly simplify and accelerate the development of such applications. In this repository, we'll explore how to build an image classification web app using Microsoft Azure AI Cognitive Services - Custom Vision, and Streamlit, accompanied by a streamlined CI/CD pipeline using GitHub Codespaces and Azure App Services.

![Web App Interface](https://github.com/geekindata/AzureAI-ImageClassification-CustomVision/assets/48961406/60ee7a20-6cd0-4a24-8580-95547db49857)

## Overview of the Architecture
![Architecture Diagram](https://github.com/geekindata/AzureAI-ImageClassification-CustomVision/assets/48961406/976fcbea-f470-48de-a213-d34c8e7f3af7)

### Azure AI Services and Custom Vision
The core of our image classification model is powered by Azure AI Services - Cognitive Services. Specifically, we'll use Custom Vision, a service that allows you to easily build, deploy, and improve image classifiers. Custom Vision enables data scientists and model developers to train prediction models on image data.

### Streamlit for App Development
For the front end, we employ Streamlit, a powerful and user-friendly framework for building interactive web applications with Python. Streamlit allows app developers to create web interfaces that display model predictions in real-time.

### GitHub Codespaces and CI/CD Pipeline
The development and deployment processes are managed through GitHub Codespaces, providing a cloud-based development environment, and a CI/CD pipeline that deploys the application to Azure App Services. This ensures that the application is always up-to-date with the latest code changes and model improvements.

## Step-by-Step Implementation

1. **Setting Up Custom Vision**: Data scientists and model developers authenticate with Azure using Entra Authentication. Once authenticated, they can access the Custom Vision service to train their image classification model. This involves uploading a labelled dataset and using the Custom Vision interface to train and evaluate the model.

2. **Developing the Web App with Streamlit**: Once the model is trained, app developers use GitHub Codespaces to write the web application. The application is built using Python, CSS, and HTML, with Streamlit serving as the framework for the web interface. Streamlit makes it easy to integrate the trained model and display predictions in an interactive and user-friendly manner.

3. **Continuous Deployment with GitHub and Azure**: After developing the app, it's pushed to a GitHub repository. The CI/CD pipeline configured within the repository ensures that any changes made to the code automatically trigger a deployment process. This pipeline deploys the web app to Azure App Services, making it accessible to end users.

4. **User Interaction**: End users can access the web app through a browser, upload their images, and receive predictions in real-time. The seamless integration of all these services provides a robust and scalable solution for image classification tasks.

## Conclusion

By combining Azure AI Services, Custom Vision, Streamlit, and Azure App Services, we can build powerful and scalable image classification applications with minimal effort. This architecture not only accelerates the development process but also ensures that the application is always up-to-date with the latest advancements and improvements.

This repository provides all the necessary code and documentation to help you get started with image classification using Azure AI services and build engaging user interfaces with Streamlit. Happy coding!

## Getting Started

### Prerequisites
- [ ] Microsoft Azure account with at least resource creation rights
- [ ] GitHub account

### Installation
1. Clone the repository.
   ```bash
   git clone https://github.com/yourusername/your-repository.git

2. Install dependencies.
   ```bash
   pip install -r requirements.txt

3. Follow the step-by-step implementation guide in the README to set up Custom Vision, develop the web app with Streamlit, and deploy it using GitHub and Azure.

## License
This project is licensed under the [MIT License](https://github.com/geekindata/AzureAI-ImageClassification-CustomVision/blob/main/LICENSE).

Feel free to customize it further to suit your specific project details and requirements!
