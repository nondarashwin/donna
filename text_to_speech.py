import pyttsx3


def text_to_speech(value):
    engine = pyttsx3.init()
    engine.say(value)
    engine.runAndWait()
