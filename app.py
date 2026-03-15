import streamlit as st
import google.generativeai as genai
from prompts import get_tutor_prompt, get_eli5_prompt, get_bullet_prompt, get_professional_prompt

# API key from Streamlit secrets
api_key = st.secrets["GOOGLE_API_KEY"]

# Background image styling
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://i.pinimg.com/1200x/6b/bd/18/6bbd18163ab6832009f96e806f86e497.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
</style>
""", unsafe_allow_html=True)

# Page title
st.title("AI Chatbot")

# Dropdown to select prompt mode
prompt_mode = st.selectbox("Select a mode", ["Python Tutor", "Explain Like I'm 5", "5 Bullet Points", "Professional Analyst"])

# Input for user question
user_input = st.text_input("Ask a question")

# Button to get response
if st.button("Send"):
    if user_input == "":
        st.warning("Please enter a question")
    else:
        # Pick the right prompt based on mode
        if prompt_mode == "Python Tutor":
            prompt = get_tutor_prompt(user_input)
        elif prompt_mode == "Explain Like I'm 5":
            prompt = get_eli5_prompt(user_input)
        elif prompt_mode == "5 Bullet Points":
            prompt = get_bullet_prompt(user_input)
        else:
            prompt = get_professional_prompt(user_input)

        # Configure Gemini and get response
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)

        # Show the response
        st.write("Response:")
        st.write(response.text)
