import os

from email.mime.multipart import MIMEMultipart

from src.config_6 import SMTPSettings, Configuration
from src.doctor_5 import Doctor
from src.email_6 import EmailMessage

def main() -> MIMEMultipart:


    email = input('Enter patient email: ')

    # Это обращение к атрибутам из .env
    smtp_settings = SMTPSettings()

    # Этот кусок будет нужен, если захотим отправить что-то вещественное
    # conf = Configuration()
    # doctor = Doctor(conf)
    #
    # file_path = os.path.join(
    #     conf.base_folder,
    #     'doctor',
    #     f"{conf.login}.json"
    # )
    # recipe = doctor.write_recipe(file_path)

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
    message = main()
