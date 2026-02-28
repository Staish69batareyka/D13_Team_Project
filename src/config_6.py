import os



class SMTPSettings:
    def __init__(self):

        env_vars = os.environ # <- чтобы было прост красивее =^=

        self.server = env_vars.get('SMTP_SERVER')
        self.port = env_vars.get('SMTP_PORT')
        self.email = env_vars.get('SMTP_EMAIL')
        self.email_password = env_vars.get('SMTP_EMAIL_PASSWORD')
