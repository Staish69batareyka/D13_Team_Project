import os


class SMTPSettings:
    def __init__(self):
        env_vars = os.environ

        # Получаем значения и сразу их очищаем
        self.server = env_vars.get('SMTP_SERVER', '').strip()

        port_str = env_vars.get('SMTP_PORT', '').strip()
        if port_str:
            try:
                self.port = int(port_str)
            except ValueError:
                print(f"Warning: Invalid port value: {port_str}")
                self.port = None
        else:
            self.port = None

        self.email = env_vars.get('SMTP_EMAIL', '').strip()
        self.email_password = env_vars.get('SMTP_EMAIL_PASSWORD', '').strip()

        # Отладка
        print("\n=== SMTPSettings INIT ===")
        print(f"Server: '{self.server}'")
        print(f"Port: {self.port}")
        print(f"Email: '{self.email}'")
        print(f"Password length: {len(self.email_password)}")