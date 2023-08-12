#!/usr/bin/env python3
"""Simple mail with SMTP"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import getenv


SMTP_USERNAME = getenv('SMTP_USERNAME')
SMTP_PASSWORD = getenv('SMTP_PASSWORD')
SMTP_SERVER = getenv('SMTP_SERVER')
sender = SMTP_USERNAME
recipient = 'olagunjusola070@gmail.com'

message = MIMEMultipart()
message['From'] = 'iProjectEdu <{}>'.format(sender)
message['To'] = recipient
message['Subject'] = 'Hello, this is a test email'

with open('text.html', 'r', encoding='utf-8') as f:
    body = f.read()

message.attach(MIMEText(body, 'html'))

with smtplib.SMTP(SMTP_SERVER, 587) as server:
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.sendmail(sender, recipient, message.as_string())
    server.quit()
