import os
import google.generativeai as genai
import json

#get the working directory

working_directory = os.path.dirname(os.path.abspath(__file__))

config_file_path = f"{working_directory}/config.json"
config_data = json.load(open(config_file_path))

#loading API Key now  

GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

# Configuring google.generativeai with google api key

genai.configure(api_key=GOOGLE_API_KEY)

# function to load gemini pro model for chatbot

def load_gemini_pro_model():
    gemini_pro_model = genai.GenerativeModel("gemini-pro")
    return gemini_pro_model 


#function for image captioning

def Gemini_Pro_Vision(prompt,image):
    Gemini_Pro_Vision = genai.GenerativeModel("gemini-1.5-flash")
    response = Gemini_Pro_Vision.generate_content([prompt,image])
    result = response.text
    return result
