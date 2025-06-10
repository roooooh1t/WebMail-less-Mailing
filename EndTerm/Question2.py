import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# SETUP PORT NUMBER AND MICROSOFT SMTP SERVER
smtp_port = 587
smtp_server = "smtp.office365.com"

# SET UP THE EMAIL ADDRESSES
sender_email = "rohitsingh23iitk@outlook.com"
receiver_email = "rohitsingh23@iitk.ac.in"

# DEFINE THE PASSWORD (BETTER TO REFERENCE EXTERNALLY)
with open("password.txt", "r") as file:
    password = file.read()

# NAME THE EMAIL SUBJECT
subject = "Happy New Year !!!"

# DEFINE THE EMAIL FUNCTION
def send_email():

    # MAKE THE BODY OF THE EMAIL
    body = "Happy New Year!\n\nWishing you a joyful and prosperous year ahead!"

    # MAKE A MIME OBJECT TO DEFINE PARTS OF THE EMAIL
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # ATTACH THE BODY OF THE MESSAGE
    msg.attach(MIMEText(body, 'plain'))

    # DEFINE THE FILE TO ATTACH
    filename = "HappyNewYear.jpg"

    # OPEN THE FILE IN PYTHON AS A BINARY
    attachment = open(filename, 'rb')  # r for read and b for binary

    # ENCODE AS BASE64
    attachment_package = MIMEBase('application', 'octet-stream')
    attachment_package.set_payload((attachment).read())
    encoders.encode_base64(attachment_package)
    attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
    msg.attach(attachment_package)

    # CAST AS STRING
    text = msg.as_string()

    # CONNECT WITH THE SERVER
    print("CONNECTING TO SERVER...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(sender_email, password)
    print("CONNECTED TO SERVER")
    print()

    # SEND EMAIL
    print(f"SENDING email TO {receiver_email}...")
    TIE_server.sendmail(sender_email, receiver_email, text)
    print(f"email SENT TO: {receiver_email}")
    print()

    # CLOSE THE PORT
    TIE_server.quit()

# RUN THE FUNCTION
send_email()
