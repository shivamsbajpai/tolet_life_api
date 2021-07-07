import smtplib
import os
from email.message import EmailMessage


def send_email(receiver_email_id: str, subject: str, body: str):
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    sender_email_id = os.environ.get("sender_email_id")
    sender_email_id_password = os.environ.get("sender_email_id_password")

    s.login(sender_email_id, sender_email_id_password)

    message = EmailMessage()
    message.set_content(body)
    message['Subject'] = subject
    message['From'] = sender_email_id
    message['To'] = receiver_email_id

    s.send_message(message, sender_email_id, receiver_email_id)

    s.quit()


def otp_email_subject():
    subject = "OTP for ToLet Life: Do not share"
    return subject


def otp_email_body(otp: str):
    body = f"Hello User, \n\nYour OTP is {otp}. Please do not share it with anyone. \n\nRegards,\nToLet Life Team"
    return body
