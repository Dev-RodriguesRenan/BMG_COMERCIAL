import os
import time
import smtplib
from email import encoders
from credentials import email_credentials
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


def send_email(
    subject, body, to_email, from_email=email_credentials["user"], attachments=None
):
    """Sends an email with the given subject, body, and recipient email address.

    Args:
        subject (str): title of the email message
        body (str): body of the email message
        to_email (str): email address of receiver
        from_email (str): email address of sender
        attachments (str, optional): path to attachments. Defaults to None.
    """
    print(f'{time.strftime("%X")}>>> Sending email to {to_email}...')
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "HTML"))

    if attachments:
        att = attach_files(attachments)
        message.attach(att)
        print(f'{time.strftime("%X")}>>> Attachment {attachments} added to email.')

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(from_email, email_credentials["password"])
        server.sendmail(from_email, to_email, message.as_string())
        print(f'{time.strftime("%X")}>>> Email sent sucessfully!!')


def attach_files(attachments: str):
    with open(attachments, "rb") as file:
        filename = os.path.basename(attachments)
        attachment = MIMEBase("application", "octet-stream")
        attachment.set_payload(file.read())
        encoders.encode_base64(attachment)

        attachment.add_header(
            "Content-Disposition",
            f"attachment; filename={filename}",
        )
        return attachment
