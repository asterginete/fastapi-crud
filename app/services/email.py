import smtplib
from email.message import EmailMessage
from app.config import EMAIL_USERNAME, EMAIL_PASSWORD

def send_email(subject: str, recipient: str, body: str):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USERNAME
    msg["To"] = recipient

    server = smtplib.SMTP_SSL("smtp.example.com", 465)
    server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()
