#!/usr/bin/env python3
"""Using EmailSender to send out multiple emails"""
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

users = [
    {'name': 'Abraham',
     'email': 'olagunjusola070@gmail.com'},
    {'name': 'Wisdom',
     'email': 'wisdomsays.g@gmail.com'},
    {'name': 'Olagunju',
     'email': 'aolagunju@lodlc.lautech.edu.ng'}]

mail = EmailSender(SMTP_SERVER, SMTP_PORT, SMTP_USERNAME,
                   SMTP_PASSWORD)


def make_body(user):
    """Returns a rendered HTML template for user"""
    with app.app_context():
        body = render_template('text.html', name=user.get('name'))
    return body


mail.send_multiple(
    users=users,
    make_subject=lambda user:
    'It is weekend vibes, {}!'.format(user.get('name')),
    make_body=make_body,
    content_type='html'
)
