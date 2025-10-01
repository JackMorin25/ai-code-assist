from gemini_chat import GeminiChat
from audio_input import SpeechManager
import keyboard
import time


gemini_handler = GeminiChat()
speech_manager = SpeechManager()

while True:
    if keyboard.read_key() != 'f4':
        time.sleep(0.1)
        continue
    # once f4 is pressed we need to give program current file or text on screen
    prompt = speech_manager.write_from_mic()

    if prompt == "":
        print("speak up lil pup")
        continue
    # take gemini response turn it into voice
    gemini_handler.chat(prompt)

    # play voice mp3
