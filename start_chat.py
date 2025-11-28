from gemini_chat import GeminiChat
from audio_input import SpeechManager
from eleven_labs import ElevenLabsManager
from audio_manager import AudiManager
import keyboard
import time


gemini_handler = GeminiChat()
speech_manager = SpeechManager()
eleven_manager = ElevenLabsManager()
audio_manager = AudiManager()

while True:
    if keyboard.read_key() != 'f4':
        time.sleep(0.1)
        continue
    # once f4 is pressed we need to give program current file or text on screen
    print("!! HEARD !!")
    prompt = speech_manager.write_from_mic()

    #

    if prompt == "":
        print("speak up lil pup")
        continue
    # take gemini response turn it into voice
    response = gemini_handler.chat(prompt)

    print(response)
    # play voice mp3
    eleven_manager.save_text_to_speech(response)

    audio_manager.play("./output.mp3")
