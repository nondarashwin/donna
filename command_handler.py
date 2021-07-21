import json
import text_to_speech
import speech_to_text
import os

try:
    main_command_file = open("files/commands.json")
except:
    print("file not found")
    speech_to_text.speech_to_text("Command not found")
try:
    commands = json.load(main_command_file)
except:
    print("not a json")


def execution_handler(command_found, command_file_location):
    try:
        command_file = open(command_file_location)
        command_details = json.load(command_file)
    except:
        return "failed to execute"
    command_input = dict()
    for i in command_details["keyword"]:
        text_to_speech.text_to_speech(i["keyword_command"])
        command_input[i["keyword_bridge_name"]] = speech_to_text.speech_to_text()
    bridge_input = json.dumps(command_input)
    bridge_location = command_details["handler"]
    b = os.system("python " + bridge_location + " " + bridge_input)
    text_to_speech.text_to_speech(b)


def command_handler(value):
    if type(value) != str:
        return
    global commands
    flag = True
    command_file_location = ""
    command_found = ""
    print(commands)
    trigger_keyword = commands["trigger_keyword"]
    print(trigger_keyword)
    trigger_keyword_index = value.find(trigger_keyword)
    if trigger_keyword_index == -1:
        return
    command_keyword_index = trigger_keyword_index + len(trigger_keyword)
    words = value[command_keyword_index:]
    for command in commands["commands"]:
        if command["command"] in words:
            command_file_location = command["location"]
            command_found = command
            flag = False
            break
    if flag:
        text_to_speech.text_to_speech("Command Not Found")
    else:
        execution_handler(command_found, command_file_location)
