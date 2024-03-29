import json
import sys
import re
import text_to_speech
import speech_to_text

regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'


def check(email):
    if re.search(regex, email):
        return True
    else:
        return False


def verify_email_and_password(email, password):
    print("verify_email_and_password")
    flag = True
    for i in range(5):
        email = email.lower()
        email = email.replace(" ", "")
        email = email.replace("at", "@")
        email = email.replace("dot", ".")
        if check(email):
            return email, verify_password(password)
        else:
            text_to_speech.text_to_speech("please say the email again")
            email = speech_to_text.speech_to_text()
    if flag:
        while True:
            text_to_speech.text_to_speech("please enter the email manually")
            email = input("Enter the mail again")

            if check(email):
                text_to_speech.text_to_speech("please enter the password manually")
                password = input("Enter the password again")
                return email, verify_password(password)


def verify_password(password):
    password = password.replace(" ", "")
    return password


class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidEmail(Error):
    """Invalid Email Error"""
    pass


def setup_email_bridge(input_data):
    try:
        data = input_data
        data1 = json.loads(data)
        data1["from"], data1["password"] = verify_email_and_password(data1["from"], data1["password"])
        # data1["password"] = verify_password(data1["password"])
        data = json.dumps(data1)
        a = data1.keys()
        print(data1)
        if "from" in a and "password" in a and "gmail" in data1["from"]:
            if not check(data1["from"]):
                raise InvalidEmail
            with open("files/email.json", "w") as outfile:
                outfile.write(data)
                text_to_speech.text_to_speech("task successful")
        else:
            raise InvalidEmail
    except InvalidEmail:
        print("email not found")
        text_to_speech.text_to_speech("email not found")
        sys.exit(1)
    except:
        print("failed to execute")
        text_to_speech.text_to_speech("failed to execute")
        sys.exit(1)
