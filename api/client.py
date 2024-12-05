# Code for the app (e.g., web app/Mobile app)
# Creation of web app. Creation f front-end that will interact with the API created in the app.py file

import requests
import streamlit as st


# functions to get the response

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke", json={"input": {"topic": input_text}})
    #st.write("Response status:", response.status_code)
    #st.write("Raw response text:", response.text)  # This will display the raw response in Streamlit
    response.raise_for_status()  # Raise an error if the response status is not 200
    return response.json()["output"]["content"]

def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke", json={"input": {"topic": input_text}})
    #st.write("Response status:", response.status_code) # For Debug
    #st.write("Raw response text:", response.text) # For Debug
    response.raise_for_status()
    return response.json()["output"]


# Create streamlit framework

st.title("Langchain Demo with LLMs")
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write an poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))

