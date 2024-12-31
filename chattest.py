import streamlit as st
import google.generativeai as genai
import os

# API Key setup
API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello AI"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)

# Streamlit app interface
st.title("Chat with Shekhar AI..powered by gemini-pro")
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
        # User message styled in black
        st.markdown(f'<p style="color:black;"><b>You</b>: {text}</p>', unsafe_allow_html=True)
    else:
        # AI response styled in blue
        st.markdown(f'<p style="color:blue;"><b>AI</b>: {text}</p>', unsafe_allow_html=True)

# Input box for user message
user_input = st.text_input("Your message:")

# Send button to process the message
if st.button("Send"):
    if user_input.strip():  # Ensure the input is not empty or just whitespace
        # Add user's message to the history
        st.session_state.history.append({"role": "user", "parts": user_input.strip()})

        try:
            # Send the message to the AI and get the response
            response = chat.send_message(user_input.strip())

            # Add AI's response to the history
            st.session_state.history.append({"role": "model", "parts": response.text})
        except Exception as e:
            st.write(f"Error sending message: {e}")

        # Re-run the app to refresh the chat window and clear the input field
        st.rerun()
