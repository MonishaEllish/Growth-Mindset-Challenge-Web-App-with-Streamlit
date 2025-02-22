import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Check if API key is available
if not api_key:
    st.error("🚨 Gemini API Key is missing! Please check your .env file.")
else:
    genai.configure(api_key=api_key)

# Streamlit UI
st.title("💬 Gemini AI Chatbot")
st.write("Ask anything and get a response from Google's Gemini AI!")

user_input = st.text_input("Enter your question:")
if st.button("🚀 Ask Gemini") and user_input:
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
        st.subheader("🤖 AI Response:")
        st.write(response.text)
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

