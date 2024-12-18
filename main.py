import streamlit as st

import os

# import google.generativeai as genai

from streamlit_option_menu import option_menu

from Gemini_Utility import load_gemini_pro_model

from Gemini_Utility import Gemini_Pro_Vision

from PIL import Image

working_directory = os.path.dirname(os.path.abspath(__file__)) #my curret wd

#Now setting the page configuration

st.set_page_config(
    page_title="Pritam_Ai",
    page_icon="💀💀",
    layout="centered"
)

#Now for the side bar

with st.sidebar:

    selected = option_menu(
        menu_title="Pritam_Ai",
        options=["Chatbot",
                 "Image Captioning",
                 "Embed Text",
                 "Ask me anything"
                ],
        menu_icon = 'robot' , icons = ["chat-left-dots","card-image","justify","patch-question-fill"],
        default_index=0       
    )

# function to translate role between gemini pro and streamlit terminology

def translate_role_for_streamlit(user_role):
    if user_role == 'model':
        return "assisstant"
    else:
        return user_role
    
#Chatbot page

if selected == "Chatbot":
    
    model= load_gemini_pro_model()

    #Initialize chat session in streamlit if not already present
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    #streamlit page title
    st.title("🤖Chatbot")

    #to display the chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # input field for users message 
    user_prompt = st.chat_input("Ask Pritam_Ai anything .....")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        #display gemini-pro response

        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)



#Image captioning page




if selected == "Image Captioning":
    #streamlit page title
    st.title("Pritam_Ai Lens")
    uploaded_image = st.file_uploader("Upload Image here")
    if st.button("Generate Caption"):
        image = Image.open(uploaded_image)

        col1 , col2 = st.columns(2)
        with col1:
            resized_image = image.resize((800,500))
            st.image(resized_image)
        default_prompt = "Write a caption for this response"

    #Getting a response from gemini-1.5-flash
    caption = Gemini_Pro_Vision(default_prompt , image)
    with col2:
        st.info(caption)

