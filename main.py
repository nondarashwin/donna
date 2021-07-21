# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import speech_to_text
import text_to_speech
import command_handler
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        print("start")
        value = speech_to_text.speech_to_text()
        print(value)
        command_handler.command_handler(value)
        print("end")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
