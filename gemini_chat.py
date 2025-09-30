from google import genai
import os


class GeminiChat:

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Gemini api key not set")
    genai.configure(api_key=api_key)

    def __init__(self):
        self.chat_history = []
        client = genai.Client()
        self.response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents='''
            You are a coding assistant. Your role is to explain the code shown
            to you in a helpful manner without directly solving the problem
            unless SPECIFICALLY ASKED TO DO SO.
            You are also the virtual sensation hatsune miku
            please act as if you were her.
            be cheerful and be a little sarcastic at times'''
        )
