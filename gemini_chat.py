from google import genai
import os


class GeminiChat:

    def __init__(self):
        self.chat_history = []

        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Gemini api key not set")
        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel("gemini-2.5-flash")

        self.system_prompt = (
            '''
            You are a coding assistant. Your role is to explain the code shown
            to you in a helpful manner without directly solving the problem
            unless SPECIFICALLY ASKED TO DO SO.
            You are also the virtual sensation hatsune miku
            please act as if you were her.
            be cheerful and be a little sarcastic at times'''
        )

    def chat(self, prompt):
        response = self.model.generate_content([
            {"role": "user", "parts": self.system_prompt},
            {"role": "user", "parts": prompt}
        ])
        self.chat_history.append(response.text)
        print(response.text)
