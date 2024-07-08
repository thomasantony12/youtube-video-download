from pytube import YouTube
import streamlit as st
import os

def Download(link):
    try:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        folder = os.path.expanduser("~")
        default_download_folder = os.path.join(folder, "Downloads")

        if not os.path.exists(default_download_folder):
            os.makedirs(default_download_folder)

        youtubeObject.download(output_path=default_download_folder)
        st.write("Download is completed successfully to", default_download_folder)
    except:
        st.write("An error has occurred")


def process_input(link):
    # Process the input text here
    st.write("Input Text:", link)

st.title("YouTube video downloader")
link = st.text_input("Enter the youtube link")

if st.button("Download"):
    process_input(link)
    Download(link)
    if video_path:
        # Provide a link to download the file through the browser
        st.markdown(f"[Download video](./{os.path.basename(video_path)})")
        
        # Copy the video to the Streamlit static folder
        if not os.path.exists('static'):
            os.makedirs('static')
        shutil.copy(video_path, os.path.join('static', os.path.basename(video_path)))
        
        st.write("You can download the video from the link above.")

# Serve the static files in the Streamlit static folder
# st.static('static')

