################################################################
# Joesphan Lu
# 10/7/2020
# this script scans the image based on the settings in scan.conf
# arguments:
#    -a: append the following scan to the previous pdf
#    -f: finish, runs final scripts (convert to pdf, email etc.)
################################################################
import subprocess
import configparser
import sys
from datetime import datetime
now = datetime.now()
config = configparser.ConfigParser()
config.read('PrintSettings.conf')

#querys the profile
currentprofile = config['global']['currentprofile']

#querys the scan options

filename = ""
if sys.argv[1] == "-a":
    if config[currentprofile]['filename'] == "": 
        #if a -a(ppend) has been initiated, no previous -a multi page
        filename = now.strftime("%Y%m%d%H%M%S") + "-1"
        config[currentprofile]['filename'] = filename
    else:
        #-a intiiated, previous page exists
        filename = config[currentprofile]['filename']
        num = int(filename[-1])                      #get last char
        filename[-1] = str(num + 1)                  #increment and set
elif sys.argv[1] == "-f":
#finish
    if config[currentprofile]['outputtype'] == 'pdf':
        #convert to pdf
    if config[currentprofile]['outputlocation'] == 'email'
        #email address
    #reset
    config[currentprofile]['filename'] = ""
    
else:
    #single page scanning
    filename = now.strftime("%Y%m%d%H%M%S")
    config[currentprofile]['filename'] = ""     #reset to avoid conflicts

device = config[currentprofile]['device']
resolution = config[currentprofile]['resolution']
mode = config[currentprofile]['mode']
outputtype = config[currentprofile]['outputtype']
outputlocation = config[currentprofile]['outputlocation']
path = config[currentprofile]['path']
fullpath = str(path) + str(filename)

#runs the actual command
subprocess.run(["scanimage", "-d", device, "--resolution", resolution, "--mode", mode, ">", "fullpath"])

#update the config file
with open('PrintSettings.conf', 'w') as configfile:
   config.write(configfile)