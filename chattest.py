import yt_dlp
import streamlit as st
import os
import google.generativeai as genai

# API Key setup for Generative AI (replace with your actual API key)
API_KEY = os.getenv("API_KEY")  # Ensure the API key is set in your environment
genai.configure(api_key=API_KEY)

# Path to the bin folder inside the ffmpeg folder in the root directory
BIN_DIR = os.path.join(os.path.dirname(__file__), "ffmeg", "bin")
FFMPEG_PATH = os.path.join(BIN_DIR, "ffmpeg.exe")
FFPROBE_PATH = os.path.join(BIN_DIR, "ffprobe.exe")



# Streamlit app interface
st.title("Shekhar Chat -powered by Gemini AI & YouTube MP3 Downloader")

# Tabs for separate functionalities
tab1, tab2 = st.tabs(["💬 Chat with AI", "🎵 YouTube MP3 Downloader[*Works on Windows OS]"])

# Tab 1: Chat with AI
with tab1:
    # Initialize the Generative AI model
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello AI"},
            {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        ]
    )

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

# Tab 2: YouTube MP3 Downloader
with tab2:
    # URL input box
    url = st.text_input("Enter YouTube URL:")

    # Function to download YouTube content as MP3
    def download_youtube_mp3(url):
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        if not os.path.exists(downloads_folder):
            os.makedirs(downloads_folder)

        ydl_opts = {
            'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'),  # Save in Downloads folder
            'format': 'bestaudio/best',  # Best audio format
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',  # Convert to MP3
                    'preferredquality': '192',  # Quality (192 kbps)
                }
            ],
            'ffmpeg_location': FFMPEG_PATH,  # Use the bundled FFmpeg binary
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            return f"Downloaded MP3 saved to {downloads_folder}"
        except Exception as e:
            return f"Error: {e}"

    # Download button
    if st.button("Download MP3"):
        if url.strip():
            with st.spinner("Downloading..."):
                result = download_youtube_mp3(url.strip())
            st.success(result) if "Downloaded" in result else st.error(result)
        else:
            st.warning("Please enter a valid YouTube URL.")
