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

        video_path = youtubeObject.download(output_path=default_download_folder)
        return video_path
    except:
        st.write("An error has occurred")


st.title("YouTube video downloader")
link = st.text_input("Enter the youtube link")

if st.button("Get video file"):
    st.write("Downloading...")
    video_path = Download(link)
    if video_path:
        with open(video_path, "rb") as file:
            btn = st.download_button(label="Download video", data=file, file_name=os.path.basename(video_path), mime="video/mp4")


