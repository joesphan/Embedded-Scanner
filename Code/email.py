import smtplib 

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

import ConfigParser
import os
import zipfile



#read config options
config = ConfigParser.ConfigParser()
config.read('Settings/Profiles.conf')
currentprofile = config.get('global', 'currentprofile')
smtp = config.get('email', 'smtp')
port = config.get('email', 'port')
fromaddr = config.get('email', 'fromaddr')
frompass = config.get('email', 'frompass')
toaddr = config.get(currentprofile, 'recepient')
body = config.get(currentprofile, 'body')
subject = config.get(currentprofile, 'subject')
filetype = config.get(currentprofile, 'outputtype')
subfolder = config.get(currentprofile, 'subfolder')

#determine the path for the file
#final output path
outfile = ""
if filetype == "image":
    path = "ScanCache/" + subfolder
    #zip archive if they are images
    #get filenames
    files = [f for f in os.listdir('ScanCache/') if os.path.isfile(f)]
    fullpath = []
    for f in files:
            fullpath.append('ScanCache/' + f)
    #zipping
    outfile = "ZipCache/" + files[0] + ".zip"
    zip = zipfile.ZipFile(outfile, mode='w')
    for x in fullpath:
        zip.write(x)
    zip.close()
elif filetype == "pdf":
    #get filenames
    files = [f for f in os.listdir('ScanCache/') if os.path.isfile(f)]
    outfile = "PdfCache/" + subfolder + files[0]

# Email stuff
msg = MIMEMultipart() 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain')) 
attachment = open(outfile, "rb") 
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p) 
s = smtplib.SMTP(smtp, port) 
s.starttls() 
s.login(fromaddr, frompass) 
text = msg.as_string() 
s.sendmail(fromaddr, toaddr, text)
