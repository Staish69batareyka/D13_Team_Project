
from src.config_6 import Configuration, SMTPSettings
from src.doctor_5 import Doctor
from src.email_7 import EmailMessage, EmailSender


def main() -> None:
    save_answer = input("Do I need to save the recipe to the file? ")

    conf : Configuration = Configuration()
    smtp_settings: SMTPSettings = SMTPSettings()

    doctor: Doctor = Doctor(conf)

    recipe: str

    if save_answer.strip():
        filename = input("Enter the name of the file where the recipe should be saved: ")
        recipe = doctor.write_recipe(filename.strip())
    else:
        recipe = doctor.write_recipe()

    patient_email = input("Enter patient email: ").strip()

    email_body = f"Receipt\n\n{recipe}"

    email_message = EmailMessage(
        from_email=smtp_settings.email,
        to_email=patient_email,
        subject="Receipt",
        body=email_body
    )

    email_sender = EmailSender(smtp_settings)
    email_sender.send_email(email_message)


if __name__ == "__main__":
    main()