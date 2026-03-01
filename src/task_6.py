from email.mime.multipart import MIMEMultipart

from src.config_6 import SMTPSettings
from src.email_6 import EmailMessage

def main() -> MIMEMultipart:
    email = input('Enter patient email: ')

    # Это обращение к атрибутам из секр. папки
    smtp_settings = SMTPSettings()

    # создание письма
    email = EmailMessage(
        from_email=smtp_settings.email,
        to_email=email,
        subject='Receipt for your visit on March 1',
        body=f"Dear patient,\n\nPlease find your receipt attached (or below).\n\nThank you for your visit.\n\nBest regards,\nYour Clinic"
    )

    # Отправка
    mime_message = email.create_mime_message()
    return mime_message

if __name__ == "__main__":
    print(main().as_string())