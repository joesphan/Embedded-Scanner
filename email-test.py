
import smtplib 

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = "embeddedscanner@gmail.com"
toaddr = "joesphanlu@gmail.com"
       

# instance of MIMEMultipart 
msg = MIMEMultipart() 
# storing the senders email address   
msg['From'] = fromaddr 

# storing the receivers email address  
msg['To'] = toaddr 

# storing the subject  
msg['Subject'] = "Subject of the Mail"
  
# string to store the body of the mail 
body = "Body_of_the_mail"

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
input()
# open the file to be sent  
filename = "testfile.txt"
input()
attachment = open("C:/Users/joesp/Desktop/", "rb") 
input()
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, "Pass123$") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text)