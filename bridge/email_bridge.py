import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
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


def check(email):
    if re.search(regex, email):
        return True
    else:
        return False


try:
    print("inside try")
    loc = os.getcwd() + "\files\email.json"

    print("**location**")
    print(loc)
    emails_file = open(loc)
    print("file found opening")
    emails = json.load(emails_file)
    print(emails)
except:
    print("file not found")
try:
    data = json.loads(sys.argv[1])
    print(data)
    SERVER = "smtp-mail.outlook.com"
    PORT = 587

    FROM = emails["from"]
    PASSWORD = emails["password"]
    TO = data["to"]
    if not check(TO):
        raise InvalidEmail
    SUBJECT = data["subject"]
    messages = data["message"]
    message = MIMEMultipart()
    message['From'] = FROM
    message['To'] = TO
    message['Subject'] = SUBJECT
    # The body and the attachments for the mail
    message.attach(MIMEText(messages, 'plain'))
    print("setting up server")
    session = smtplib.SMTP_SSL(SERVER, PORT)
    session.ehlo()
    session.starttls()  # enable security
    session.ehlo()
    print("login into mail")
    session.login(FROM, PASSWORD)  # login with mail_id and password
    text = message.as_string()
    print("sending mail")
    session.sendmail(FROM, TO, text)
    print("mail sent")
    session.quit()
except json.JSONDecodeError:
    print("Failed to Execute")
except InvalidEmail:
    print("Invalid Email Error")
except :
    print("Failed to Execute")
