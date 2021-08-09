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


def check(email):
    if re.search(regex, email):
        return True
    else:
        return False


class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidEmail(Error):
    """Invalid Email Error"""
    pass


def verify_email(email):
    print("verify_email_and_password")
    flag = True
    for i in range(5):
        email = email.lower()
        email = email.replace(" ", "")
        email = email.replace("at", "@")
        email = email.replace("dot", ".")
        if check(email):
            return email
        else:
            text_to_speech.text_to_speech("please say the to email again")
            email = speech_to_text.speech_to_text()
    if flag:
        while True:
            text_to_speech.text_to_speech("please enter the email manually")
            email = input("Enter the mail again")
            if check(email):
                return email


def email_bridge(input_data):
    try:
        # print("inside try")
        loc = "files/email.json"

        # print("**location**")
        # print(loc)
        emails_file = open(loc)
        # print("file found opening")
        emails = json.load(emails_file)
        # print(emails)
    except:
        print("file not found")
        sys.exit(1)
    try:
        data = json.loads(input_data)
        # print(data)
        SERVER = 'smtp.gmail.com'
        PORT = 465
        FROM = emails["from"]
        PASSWORD = emails["password"]
        TO = verify_email(data["to"])
        SUBJECT = data["subject"]
        messages = data["message"]
        print("to:", TO)
        print("subject:", SUBJECT)
        print("message:", messages)
        message = MIMEMultipart()
        message['From'] = FROM
        message['To'] = TO
        message['Subject'] = SUBJECT
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
