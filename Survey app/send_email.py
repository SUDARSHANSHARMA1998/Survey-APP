from email.mime.text import MIMEText
import smtplib

def send_email(email, height,average_height,count,max_height,min_height):
    from_email="sudarshansharmano.2@gmail.com"
    from_password="******"
    to_email=email

    subject="Height data"
    message="Hey there, your height is <strong>%s</strong>. <br> Average height of all is <strong>%s</strong> and that is calculated out of <strong>%s</strong> people. <br>The maximum height has been <strong>%s</strong><br>The minimum height has been <strong>%s</strong> <br> Thanks for registering with us -)" % (height, average_height, count,max_height,min_height)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
