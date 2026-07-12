"""
Email Sender
Responsible for sending one invoice PDF
to the Gmail inbox monitored by n8n.
"""

import smtplib
import ssl
from pathlib import Path

from email.message import EmailMessage

from config import (
    EMAIL_ADDRESS,
    APP_PASSWORD,
    RECIPIENT_EMAIL,
    EMAIL_SUBJECT,
    EMAIL_BODY
)


def send_invoice(pdf_path: Path) -> bool:
    """
    Sends one invoice PDF.

    Returns:
        True  -> Email sent successfully
        False -> Failed
    """

    try:

        message = EmailMessage()

        message["From"] = EMAIL_ADDRESS
        message["To"] = RECIPIENT_EMAIL
        message["Subject"] = EMAIL_SUBJECT

        message.set_content(EMAIL_BODY)

        with open(pdf_path, "rb") as file:

            pdf_data = file.read()

            message.add_attachment(
                pdf_data,
                maintype="application",
                subtype="pdf",
                filename=pdf_path.name
            )

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465,
            context=context
        ) as smtp:

            smtp.login(
                EMAIL_ADDRESS,
                APP_PASSWORD
            )

            smtp.send_message(message)

        return True

    except Exception as error:

        print(f"\nEmail sending failed:\n{error}")

        return False

