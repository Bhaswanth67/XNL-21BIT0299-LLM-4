import google.generativeai as genai
import os

def process_audio_file(file_path: str, mime_type: str) -> str:
    """Process an uploaded audio file using the Gemini API and return the response."""
    try:
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        audio_file = genai.upload_file(path=file_path, mime_type=mime_type)
        response = model.generate_content([audio_file])
        return response.text
    except Exception as e:
        return f"Error processing audio: {str(e)}"
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)