import time
import text_to_speech


def timeteller():
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    text_to_speech.text_to_speech(localtime)
