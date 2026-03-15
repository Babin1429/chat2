import streamlit as st
import google.generativeai as genai
from prompts import get_tutor_prompt, get_eli5_prompt, get_bullet_prompt, get_professional_prompt


api_key = st.secrets["GOOGLE_API_KEY"]


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


st.title("AI Chatbot")


prompt_mode = st.selectbox("Select a mode", ["Python Tutor", "Explain Like I'm 5", "5 Bullet Points", "Professional Analyst"])


user_input = st.text_input("Ask a question")


if st.button("Send"):
    if user_input == "":
        st.warning("Please enter a question")
    else:
        
        if prompt_mode == "Python Tutor":
            prompt = get_tutor_prompt(user_input)
        elif prompt_mode == "Explain Like I'm 5":
            prompt = get_eli5_prompt(user_input)
        elif prompt_mode == "5 Bullet Points":
            prompt = get_bullet_prompt(user_input)
        else:
            prompt = get_professional_prompt(user_input)

        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)

        
        st.write("Response:")
        st.write(response.text)
