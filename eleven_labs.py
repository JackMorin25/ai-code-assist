from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
from dotenv import load_dotenv
import os


load_dotenv()


class ElevenLabsManager:
    def __init__(self):
        self.elevenlabs = ElevenLabs(
            api_key=os.getenv("11LABS_API_KEY")
        )

    def play_text_to_speech(self, input_text, voice="zEc80FtpUcM40u6WiffU"):
        audio = self.elevenlabs.text_to_speech.convert(
            text=input_text,
            voice_id=voice,
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128"
        )
        play(audio)
