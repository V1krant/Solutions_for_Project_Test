from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
#-----------Uncomment this to send a mail to iitk account--------------------#
# mail = MIMEMultipart()
# mail['From'] = "vikrant"
# mail['to']="vm.dma1@gmail.com"
# password="I cannot reveal it here ;)"
# mail['Subject']="Test Script"

# body = "ABC"

# mail.attach(MIMEText(body,'html'))
# print(mail)

# server = smtplib.SMTP("smtp.cc.iitk.ac.in",25)
# server.starttls()
# server.login(mail['From'],password)
# server.sendmail(mail['From'],mail['To'],mail.as_string())
# server.quit()

mail = MIMEMultipart()
mail['From'] = "vikrant"
mail['to']="kushgpt99@gmail.com"
password="I cannot reveal it here ;)"
mail['Subject']="Test Script"

body = "My submission for Subtitle Auto- Synchronizer Project. Could not think of smothing humorous as I have to submit application for other project too :). BTW, I have learned how to send email by python script from youtube"

mail.attach(MIMEText(body,'html'))   # can also use plain text instead of html
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(mail['From'],password)
server.sendmail(mail['From'],mail['To'],mail.as_string())
server.quit()