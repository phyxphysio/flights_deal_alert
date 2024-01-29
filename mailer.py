# Send email 

import os
import smtplib
from_email = os.getenv("FROM_EMAIL")
to_email = os.getenv("TO_EMAIL")
username = os.getenv("EMAIL_USERNAME")
password = os.getenv("PASSWORD")
smtp_port = 587
smtp_server = "smtp.gmail.com"


def send_email(message, subject="Flight Alert"):
    # Create the email headers
    email_message = f"Subject: {subject}\n\n{message}"

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(username, password)
            server.sendmail(from_email, to_email, email_message)
            print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")


