from email.mime.text import MIMEText
import random
import smtplib


def function(email):
    appPass= "dtxkbcpspdrrldyk"
    sender='usamaikram228@gmail.com'
    msg = MIMEText('Your Inpection has Booked.Our team will be there on Time.Contact us for more details')
    msg['Subject'] = 'Wheels on Wheels'
    msg['From'] = sender
    msg['To'] = email

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.ehlo()
    server.login(sender,appPass)
    server.sendmail(sender,email,msg.as_string())
    server.quit()
    print("Ssented")

#function('bsef20m043@pucit.edu.pk')