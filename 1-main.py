#!/usr/bin/env python3
"""Using EmailSender to send out an email"""
from mail import EmailSender
from os import getenv
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()
SMTP_USERNAME = getenv('SMTP_USERNAME')
SMTP_PASSWORD = getenv('SMTP_PASSWORD')
SMTP_SERVER = getenv('SMTP_SERVER')
SMTP_PORT = getenv('SMTP_PORT')

app = Flask(__name__)

user = {'name': 'Abraham', 'email': 'olagunjusola070@gmail.com'}

mail = EmailSender(SMTP_SERVER, SMTP_PORT, SMTP_USERNAME,
                   SMTP_PASSWORD)

with app.app_context():
    body = render_template('text.html', name=user.get('name'))

if mail.send_mail(To=user.get('email'),
                  Subject='Yay! Hope This Works.',
                  body=body, content_type='html'):
    print("Sent!")
else:
    print("Failed!")
