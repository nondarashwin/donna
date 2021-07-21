import speech_recognition as sr
import text_to_speech


def speech_to_text():
    r1 = sr.Recognizer()

    with  sr.Microphone()  as  source:
        r1.adjust_for_ambient_noise(source, duration=1)
        print("ambient done")
        print(r1)
        #text_to_speech.text_to_speech("please say the answer")
        audio = r1.listen(source)
        print("audio listened")

        try:
            print("passing to converter")
            get = r1.recognize_google(audio)
            print("audio converted")
            print(get)
            return get
        except  sr.UnknownValueError:
            print('error')
        except  sr.RequestError  as e:
            print(e)
            print('failed'.format(e))
