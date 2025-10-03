from elevenlabs import generate, stream, set_api_key, voices, play, save
from dotenv import load_dotenv
import os


load_dotenv()
set_api_key(os.getenv("11LABS_API_KEY"))


class ElevenLabsManager:
    def __init__(self):
        all_voices = voices()
        print(f"using these voices {all_voices}")

    def play_text_to_speech(self):
        pass
