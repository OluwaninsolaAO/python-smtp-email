# Python SMTP email

The Python `email` module is a built-in library that provides a way to manage and manipulate email messages. It is used for creating, sending, receiving, and processing email messages in various formats, such as plain text, HTML, and attachments. The `email` module is part of the broader `smtplib` library, which allows sending email using the Simple Mail Transfer Protocol (SMTP).

With the email module, you can:

1. Create and format email messages: You can create email messages with various parts like the subject, sender, recipient(s), body, attachments, and more.

1. Attachments: You can attach files to your email messages, such as images, documents, or other files.

1. MIME (Multipurpose Internet Mail Extensions) support: The module supports different MIME types, which allow sending both plain text and HTML content within the same email.

1. Handling email parsing: You can parse received email messages to extract information like the sender, recipient(s), subject, and body content.

### Setting up the Application's Environment

Depending on how the EmailSender will be used, there is a need to provide a set of variables (best using environment variable) for the mail module to work with. From my `1-main.py` test case, I used `python-dotenv` to load in the required variables defined in the file named `.env` which is not included in the repository.

```bash
SMTP_USERNAME='mail@example.com'
SMTP_PASSWORD='super_secure_password'
SMTP_SERVER='smtp.example.com'
SMTP_PORT='587'
```
