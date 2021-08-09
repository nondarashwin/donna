import pyttsx3


def text_to_speech(value):
    engine = pyttsx3.init()
    newvoicerate = 145
    #engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
    engine.setProperty('rate', newvoicerate)
    engine.say(value)
    engine.runAndWait()
