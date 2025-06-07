from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API with the key from the environment
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini 1.5 Flash Vision model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Function to generate response from Gemini
def get_gemini_response(user_input, image, prompt):
    response = model.generate_content([user_input, image[0], prompt])
    return response.text  # Return the actual text content

# Function to convert uploaded image to byte format required by Gemini API
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts

# Streamlit app setup
st.set_page_config(page_title="Multi-Language Invoice Extractor")
st.header("Multi-Language Invoice Extractor")

# File uploader for invoice image
uploaded_file = st.file_uploader("Upload an invoice image", type=["jpg", "jpeg", "png"])

#User input
user_input = st.text_input("Enter your question or prompt:", key="input")

# Display uploaded image
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_container_width=True)

# Default input prompt for the model
input_prompt = """You are an expert in understanding invoices. 
We will upload an image of an invoice, and you will answer any questions 
based on the uploaded invoice image."""

# Submit button
if st.button("Get response from invoice"):
    if uploaded_file and user_input.strip():
        image_data = input_image_details(uploaded_file)
        response = get_gemini_response(user_input, image_data, input_prompt)
        st.subheader("Extracted Information:")
        st.write(response)
    else:
        st.warning("Please upload an invoice and enter a question.")
