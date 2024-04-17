import streamlit as st
from dotenv import load_dotenv


load_dotenv()
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

from youtube_transcript_api import YouTubeTranscriptApi

prompt = """I'd like you to go into detail into a YouTube video for me in a comprehensive way, providing more details than the transcript itself.

Please go into extensive detail about everything mentioned in the transcript .
DO NOT SKIP ANY POINT.
Feel free to search for additional information online to enrich the summary, as long as the sources are credible.

The goal is to create a summary so detailed that I wouldn't need to read the transcript nor watch the original video.
The transcipt is given below:
 """


def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript= ""
        for i in transcript_text:
            transcript+=" " + i["text"]
        
        return transcript

    except Exception as e:
        raise e


def generate_gemini_content(transcript_text, prompt):

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

st.title("Youtube Transcript to Detailed Notes Converter")
youtube_link=st.text_input("Enter Youtube Video Link:")

if youtube_link:
    video_id=youtube_link.split("=")[1]
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg",use_column_width=True)
if st.button("Get Detailed Notes"):
    transcript_text=extract_transcript_details(youtube_link)

    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown(' ## DETAILED NOTES ')
        st.write(summary)