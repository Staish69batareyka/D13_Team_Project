from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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