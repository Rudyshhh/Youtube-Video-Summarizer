# Youtube-Video-Summarizer
This application is designed to provide comprehensive summaries of YouTube video transcripts using Google GenerativeAI and Gemini. It offers two key functionalities: Transcript Extraction and Summary Generation. 

The Transcript Extraction feature takes a YouTube video URL as input and extracts the transcript using the youtube-transcript-api. It also handles potential exceptions that may occur during the extraction process. 

This Streamlit application is designed to provide comprehensive summaries of YouTube video transcripts using Google GenerativeAI and the youtube-transcript-api library. It offers two key functionalities: Transcript Extraction and Summary Generation. 

The Summary Generation feature utilizes Google GenerativeAI's gemini-pro model for content generation. To set up this functionality, you need to create a project in the Google Cloud Console and enable the GenerativeAI API. You should obtain your API key and store it securely using environment variables. Use the load_dotenv() function from the dotenv library to load the API key from a .env file. Once you have set up the API key, you can run the application using streamlit run app.py (replace app.py with the actual filename if different). 

To generate a summary, enter a YouTube video URL in the text input field and click the "Get Detailed Notes" button. 

Please note that you should have a valid Google GenerativeAI API key with appropriate permissions. Additionally, consider the rate limits and pricing associated with the Google GenerativeAI service. The application relies on the youtube-transcript-api library, which may have its own limitations or terms of use. Refer to the library's documentation for further details.
