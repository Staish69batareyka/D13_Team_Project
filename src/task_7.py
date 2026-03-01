
from src.config_6 import SMTPSettings
from src.email_7 import EmailMessage, EmailSender


def main() -> None:
    patient_email: str = input('Enter patient email: ')
    smtp_settings: SMTPSettings = SMTPSettings()

    email_message = EmailMessage(
        from_email=smtp_settings.email,
        to_email=patient_email,
        subject='Receipt',
        body='Test'
    )

    email_sender = EmailSender(smtp_settings)
    email_sender.send_email(email_message)

if __name__ == '__main__':
    main()