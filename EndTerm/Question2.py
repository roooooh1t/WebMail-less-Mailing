import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

smtp_server = "smtp-mail.outlook.com"
smtp_port = 587

sender_email = "rohit1303demo@outlook.com"
receiver_email = "rohitsingh23@iitk.ac.in"

with open("password.txt", "r") as file:
    password = file.read().strip()

subject = "Happy New Year !!!"

def send_email():
    body = "Happy New Year!\n\nWishing you a joyful and prosperous year ahead!"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    filename = "HappyNewYear.jpg"
    try:
        with open(filename, 'rb') as attachment:
            attachment_package = MIMEBase('application', 'octet-stream')
            attachment_package.set_payload(attachment.read())
            encoders.encode_base64(attachment_package)
            attachment_package.add_header(
                'Content-Disposition',
                f'attachment; filename="{filename}"'
            )
            msg.attach(attachment_package)
        print(f"✔️ Attached file: {filename}")
    except FileNotFoundError:
        print(f"⚠️ Attachment file '{filename}' not found. Sending email without attachment.")

    text = msg.as_string()

    try:
        print("📡 Connecting to Outlook SMTP server...")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        print(f"✅ Email successfully sent to {receiver_email}")
    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed. Check your password or use an App Password if 2FA is enabled.")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

send_email()