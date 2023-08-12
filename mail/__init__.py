#!/usr/bin/env python3
"""A SMTP Email Sender"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from typing import Callable, Iterable


class EmailSender:
    """Basic Email Sender using smtplib"""

    def __init__(self, smtp_server, smtp_port, username, password):
        """Initializes a new instance of EmailSender"""
        self.smpt_server = smtp_server
        self.smtp_port = int(smtp_port)
        self.username = username
        self.password = password

    def make_message(self, From=None, To=None, Subject=None,
                     user=None, body=None, content_type='plain'):
        """Returns a MIMEMultipart object string instance"""
        message = MIMEMultipart()
        message['Subject'] = Subject

        # validate From
        if From is None:
            message['From'] = self.username
        else:
            message['From'] = From

        # validate To
        if To is None and hasattr(user, 'email'):
            message['To'] = getattr(user, 'email')
        elif To is None and isinstance(user, dict):
            if user.get('email', None):
                message['To'] = user.get('email')
        elif To is not None:
            message['To'] = To
        else:
            return None

        if all([hasattr(self, 'header'), hasattr(self, 'footer')]):
            body = str(self.header) + body + str(self.footer)
        message.attach(MIMEText(body, content_type))
        return message

    def send_mail(self, From=None, To=None, Subject=None,
                  user=None, body=None, content_type='plain'):
        """
        Overloads to sends out email:
        """
        message = self.make_message(From, To, Subject,
                                    user, body, content_type)
        if message is None:
            return False
        with smtplib.SMTP(self.smpt_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(message.get('From'), message.get('To'),
                            message.as_string())
        return True

    def send_multiple(self, From: str = None, users: Iterable = None,
                      make_subject: Callable = None,
                      make_body: Callable = None,
                      content_type='plain'):
        """Overload and send email to multiple recipients"""
        with smtplib.SMTP(self.smpt_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.username, self.password)
            for user in users:
                message = self.make_message(From=From, user=user,
                                            Subject=make_subject(user),
                                            body=make_body(user),
                                            content_type=content_type)
                if message is not None:
                    server.sendmail(message.get('From'),
                                    message.get('To'),
                                    message.as_string())
                    print('Sent: {}'.format(message.get('To')))
