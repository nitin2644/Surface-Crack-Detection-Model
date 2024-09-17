import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import requests
from io import BytesIO

# Define the URL of the model file
model_url = 'https://github.com/nitin2644/Surface-Crack-Detection-Model/releases/tag/v1.0'

# Function to load model from URL
def load_model_from_url(url):
    response = requests.get(url)
    model_file = BytesIO(response.content)
    return tf.keras.models.load_model(model_file)

# Load the trained model
model = load_model_from_url(model_url)

# Define a function to preprocess the image
def preprocess_image(img):
    img = image.load_img(img, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Rescale pixel values
    return img_array

# Define the Streamlit app
st.title('Crack Detection')
st.write('Upload an image to check if it has a crack.')

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Display the image
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Preprocess and predict
    img = preprocess_image(uploaded_file)
    prediction = model.predict(img)
    result = 'Crack' if prediction[0] > 0.5 else 'No Crack'

    # Display result
    st.write(f'The image has: {result}')
