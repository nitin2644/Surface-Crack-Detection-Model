# Crack Detection Model

This repository contains a Convolutional Neural Network (CNN) model for detecting cracks in images. The model is trained to classify images of surfaces as either having a crack or not having a crack.

## Overview

The project involves:
- Training a CNN model on a dataset of images with and without cracks.
- Developing a Streamlit web application to allow users to upload images and classify them as having a crack or not.
- Deploying the web application for public access.

## Files in This Repository

- `crack_detection_model.h5`: The trained CNN model saved in HDF5 format.
- `app.py`: The Streamlit app code for uploading and classifying images.

## Getting Started

### Prerequisites

To run the Streamlit app locally, you need to have Python installed along with the required libraries. If you're using Streamlit Sharing, the dependencies will be installed automatically.

### Installing Dependencies

Create a `requirements.txt` file with the following content to specify the dependencies:
streamlit tensorflow pillow numpy

csharp
Copy code

Install the dependencies locally with:

```bash
pip install -r requirements.txt
```
Running the Streamlit App Locally
Save the Model and App Code:

Make sure you have both crack_detection_model.h5 and app.py in the same directory.

Run the App:

In your terminal or command prompt, navigate to the directory containing app.py and run:

bash
Copy code
streamlit run app.py
This will start the Streamlit server and open the app in your default web browser.

Deploying the Streamlit App
The Streamlit app is deployed and accessible online. You can use the link below to access it.

Click here to use the Crack Detection Web Application

How to Use the Web Application
Upload an Image:

Click on the "Choose an image..." button and upload an image of a surface.
Classify the Image:

After uploading, the app will automatically classify the image and display whether it has a crack or not.
Model Details
Architecture: Convolutional Neural Network (CNN)
Input Size: 150x150 pixels
Output Classes: Crack (1) or No Crack (0)
Contributing
Feel free to fork the repository and submit pull requests with improvements or fixes. For any issues or feature requests, please open an issue in this repository.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
TensorFlow: For providing the powerful tools to build and train deep learning models.
Streamlit: For enabling easy deployment of interactive machine learning applications.
Google Colab: For providing a free and accessible platform for model training.
