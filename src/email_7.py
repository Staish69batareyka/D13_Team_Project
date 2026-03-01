from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from src.config_6 import SMTPSettings


class EmailMessage:
    def __init__(self, from_email, to_email, subject, body):
        self.from_email = from_email
        self.to_email = to_email
        self.subject = subject
        self.body = body

    def create_mime_message(self) -> MIMEMultipart:
        message = MIMEMultipart()
        message['From'] = self.from_email
        message['To'] = self.to_email
        message['Subject'] = self.subject
        message.attach(MIMEText(self.body, 'plain'))
        return message


class EmailSender:
    def __init__(self, smtp_settings: SMTPSettings):
        self.smtp_settings = smtp_settings

    def send_email(self, email_message: EmailMessage):
        try:
            # Дополнительная отладка
            # print(f"\n=== DEBUG IN send_email ===")
            # print(f"Server: '{self.smtp_settings.server}'")
            # print(f"Port: {self.smtp_settings.port} (type: {type(self.smtp_settings.port)})")
            # print(f"Email: '{self.smtp_settings.email}'")
            # print(
            #     f"Password length: {len(self.smtp_settings.email_password) if self.smtp_settings.email_password else 0}")

            # Проверяем все настройки
            # if not self.smtp_settings.server:
            #     print("ERROR: SMTP server is empty or None")
            #     return
            #
            # if not self.smtp_settings.port:
            #     print("ERROR: SMTP port is empty or None")
            #     return
            #
            # if not self.smtp_settings.email:
            #     print("ERROR: SMTP email is empty or None")
            #     return
            #
            # if not self.smtp_settings.email_password:
            #     print("ERROR: SMTP password is empty or None")
            #     return

            mime_message: MIMEMultipart = email_message.create_mime_message()

            # Создаем соединение
            print(f"Connecting to {self.smtp_settings.server}:{self.smtp_settings.port}")

            with smtplib.SMTP(
                    self.smtp_settings.server,
                    self.smtp_settings.port
            ) as server:

                server.starttls()

                server.login(
                    self.smtp_settings.email,
                    self.smtp_settings.email_password
                )

                server.send_message(mime_message)

                server.quit()

            print("The letter has been sent successfully.")

        except Exception as e:
            print(f"Failed to send email!")
            print(f'Error: {e}')

            # для крутого отображения ошибки
            # import traceback
            # traceback.print_exc()