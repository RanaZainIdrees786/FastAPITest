import smtplib
from email.message import EmailMessage


def send_email(receiver_email, text=""):
    # Sender Email
    sender_email='rzi.93.rzi@gmail.com'

    # Email content setup
    msg = EmailMessage()
    msg['Subject'] = 'Welcome to AKTI!'
    msg['From'] = sender_email         # Replace with your email
    msg['To'] = receiver_email      # Replace with recipient email
    msg.set_content(text)

    # Gmail SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Your Gmail credentials
    email_address = sender_email
    email_password = 'qdezdebjfibbljvd'  # Use an app password if 2FA is enabled

    # Sending the email
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()  # Secure the connection
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

    
    print("✅ Email sent successfully!")
