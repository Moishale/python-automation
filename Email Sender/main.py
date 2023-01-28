import smtplib
import os

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(os.getenv('EMAIL'), os.getenv('PASSWORD'))

    subject = "Test"
    body = "Hi this is a test"
    msg = f'Subject : {subject}\n\n{body}'
    smtp.sendmail(os.getenv('EMAIL'), "example@gmail.com", msg)
