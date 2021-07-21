import json
import smtplib
import sys
import os

os.system("pwd")

try:
    print("inside try")
    loc = "email.json"
    print("location")
    print(loc)
    emails_file = open(loc)
    emails = json.loads(emails_file)
    print(emails)
except:
    print("file not found")
try:
    data = json.loads(sys.argv[1])
    SERVER = "smtp-mail.outlook.com"
    PORT = 587
    FROM = emails["from"]
    PASSWORD = emails["password"]
    TO = data["to"]
    SUBJECT = data["subject"]
    message = data["message"]
    server = smtplib.SMTP(SERVER, PORT)
    server.login(FROM, PASSWORD)
    server.sendmail(FROM, TO, message)
    server.quit()
except json.JSONDecodeError:
    print("Failed to Execute")
