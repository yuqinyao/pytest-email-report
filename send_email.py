import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import glob


def send_email():
    sender_email = "email@example.com"
    receiver_email = "email@example.com"
    password = "password"

    combined_report_content = ""
    for report_file in glob.glob("test_report+.txt"):
        with open(report_file, "r") as file:
            combined_report_content += f"{report_file.split('_')[-1].split('.')[0]} store test results:\n\n"
            combined_report_content += file.read() + "\n\n"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Test Results"

    message.attach(MIMEText(combined_report_content, "plain"))

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


if __name__ == "__main__":
    send_email()
