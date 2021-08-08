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


def verify_email(email):
    flag = True
    for i in range(5):
        email = email.lower()
        email = email.replace(" ", "")
        email = email.replace("at", "@")
        email = email.replace("dot", ".")
        if check(email):
            return email
        else:
            text_to_speech.text_to_speech("please say the email again")
            email = speech_to_text.speech_to_text()
    if flag:
        while True:
            text_to_speech.text_to_speech("please enter the email manually")
            email = input("Enter the mail again")
            if check(email):
                return email


def verify_password(password):
    password = password.replace(" ", "")
    password = password.replace("at", "@")
    return password


class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidEmail(Error):
    """Invalid Email Error"""
    pass


try:
    print(sys.argv[1])
    data = sys.argv[1]
    print(data)
    data1 = json.loads(data)
    data1["from"] = verify_email(data1["from"])
    data1["password"] = verify_password(data1["password"])
    data = json.dumps(data1)
    a = data1.keys()
    print(a)
    if "from" in a and "password" in a and "gmail" in data1["from"]:
        if not check(data1["from"]):
            raise InvalidEmail
        with open("files/email.json", "w") as outfile:
            outfile.write(data)
    else:
        raise InvalidEmail
except InvalidEmail:
    print("email not found")
    sys.exit(1)
except:
    print("failed to execute")
    sys.exit(1)
