import speech_recognition as sr


class SpeechManager:
    def __init__(self):
        self.r = sr.Recognizer()

    def write_from_mic(self):

        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)

        try:
            text = self.r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "could not understand"
        except sr.RequestError:
            return "Could not request results from Google Speech Recognition service"
