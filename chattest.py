import streamlit as st
import google.generativeai as genai
import os

# API Key setup
API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello AI"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)

# Streamlit app interface
st.title("Chat with Shekhar AI..powered by gemini-1.5-flash")
st.write("Type your message below:")

# Initialize the session state for storing chat history
if "history" not in st.session_state:
    st.session_state.history = [
        {"role": "model", "parts": "Great to meet you. What would you like to know?"}
    ]

# Display the conversation history
for message in st.session_state.history:
    role = message["role"]
    text = message["parts"]
    if role == "user":
        with st.chat_message("user"):
            st.markdown(text)
    else:
        with st.chat_message("assistant"):
            st.markdown(text)

# Input box for user message
user_input = st.text_area("Your message:")

# Send button to process the message
if st.button("Send") and user_input.strip():  # Ensure the input is not empty or just whitespace
    # Add user's message to the history
    st.session_state.history.append({"role": "user", "parts": user_input.strip()})

    try:
        # Send the message to the AI and get the response
        response = chat.send_message(user_input.strip())

        # Add AI's response to the history
        st.session_state.history.append({"role": "model", "parts": response.text})
    except Exception as e:
        # Add error message to the history for better debugging
        st.session_state.history.append({"role": "model", "parts": f"Error: {e}"})

    # Clear the input field and refresh the app
    st.rerun()
