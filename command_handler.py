import json
import time_teller
import email_bridge
import setup_email_bridge
import speech_to_text
import text_to_speech

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
    print("execution_handler")
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
    print(bridge_input)
    if bridge_location == "email_bridge.py":
        email_bridge.email_bridge(bridge_input)
    elif bridge_location == "setup_email_bridge.py":
        setup_email_bridge.setup_email_bridge(bridge_input)
    elif bridge_location == "time_teller.py":
        time_teller.timeteller()


def command_handler(value):
    print("command_handler")
    if type(value) != str:
        return
    value = value.lower()
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
    print("after trigger word")
    print(words)
    for command in commands["commands"]:
        print(command)
        command_words = command["command"].split(" ")
        if command["command"] in words:
            # print(command["command"])
            command_file_location = command["location"]
            command_found = command
            flag = False
            break
    if flag:
        text_to_speech.text_to_speech("Command Not Found")
    else:
        execution_handler(command_found, command_file_location)
