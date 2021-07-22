import pyttsx3


def text_to_speech(value):
    engine = pyttsx3.init()
    newVoiceRate = 145
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
    engine.setProperty('rate', newVoiceRate)
    engine.say(value)
    engine.runAndWait()
