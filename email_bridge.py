import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import speech_to_text
import text_to_speech
import sys
import os
import json
import re

regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'


class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidEmail(Error):
    """Invalid Email Error"""
    pass


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


def check(email):
    if re.search(regex, email):
        return True
    else:
        return False


try:
    print("inside try")
    loc = "files/email.json"

    print("**location**")
    print(loc)
    emails_file = open(loc)
    print("file found opening")
    emails = json.load(emails_file)
    print(emails)
except:
    print("file not found")
    sys.exit(1)
try:
    data = json.loads(sys.argv[1])
    print(data)
    SERVER = 'smtp.gmail.com'
    PORT = 465

    FROM = emails["from"]
    PASSWORD = emails["password"]
    TO = data["to"]
    if not check(TO):
        raise InvalidEmail
    SUBJECT = data["subject"]
    messages = data["message"]
    message = MIMEMultipart()
    message['From'] = FROM
    message['To'] = verify_email(TO)
    message['Subject'] = SUBJECT
    # The body and the attachments for the mail
    message.attach(MIMEText(messages, 'plain'))
    print("setting up server")
    session = smtplib.SMTP_SSL(SERVER, PORT)
    print("login into mail")
    session.login(FROM, PASSWORD)  # login with mail_id and password
    text = message.as_string()
    print("sending mail")
    session.sendmail(FROM, TO, text)
    print("mail sent")
    session.quit()
except json.JSONDecodeError:
    print("Failed to Execute")
    sys.exit(1)
except InvalidEmail:
    print("Invalid Email Error")
    sys.exit(1)
