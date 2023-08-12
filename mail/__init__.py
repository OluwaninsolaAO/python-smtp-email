#!/usr/bin/env python3
"""A SMTP Email Sender"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


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
        elif To is not None:
            message['To'] = To
        else:
            return None

        if all([hasattr(self, 'header'), hasattr(self, 'footer')]):
            body = self.header + body + self.footer
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
