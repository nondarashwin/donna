import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys
import os
import json
print(os.system("pwd"))

try:
    print("inside try")
    loc = os.getcwd()+"/files/email.json"

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
    SUBJECT = data["subject"]
    messages = data["message"]
    message = MIMEMultipart()
    message['From'] = FROM
    message['To'] =TO
    message['Subject'] = SUBJECT
    # The body and the attachments for the mail
    message.attach(MIMEText(messages, 'plain'))
    print("setting up server")
    session = smtplib.SMTP(SERVER, PORT)
    session.starttls()  # enable security
    session.login(FROM, PASSWORD)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(FROM, TO, text)
    session.quit()
except json.JSONDecodeError:
    print("Failed to Execute")
