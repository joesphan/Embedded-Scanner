################################################################
# Joesphan Lu
# 10/7/2020
# this script scans the image based on the settings in scan.conf
# arguments:
#    -a: append the following scan to the previous pdf
#    -f: finish, runs final scripts (convert to pdf, email etc.)
################################################################
import ConfigParser
import sys
import os
from datetime import datetime
from time import sleep
now = datetime.now()
config = ConfigParser.ConfigParser()
config.read('./Settings/Profiles.conf')

#querys the profile
currentprofile = config.get('global', 'currentprofile')
device = config.get('global', 'device')
resolution = config.get(currentprofile, 'resolution')
mode = config.get(currentprofile, 'mode')
outputtype = config.get(currentprofile, 'outputtype')
outputlocation = config.get(currentprofile, 'outputlocation')
pageindex = int(config.get(currentprofile, 'pageindex'))
subfolder = config.get(currentprofile, 'subfolder')
headreturntime = int(config.get('global', 'headreturntime'))

fullpath = ""
args = ""
try:
    args = sys.argv[1]
except:
    print('Please enter an argument, -a to append, -f to finish')
if args == "-a":
    if subfolder == "": 
        #if a -a(ppend) has been initiated, no previous -a multi page
        subfolder = str(now.strftime("%Y")) + "-" + str(now.strftime("%m")) + "-" + str(now.strftime("%d")) + "-" + str(now.strftime("%H")) + "_" + str(now.strftime("%M")) + "_" + str(now.strftime("%S"))
        #update folder
        config.set(currentprofile, 'subfolder', subfolder)
    else:
        #-a intiiated, previous page exists
        pageindex += 1 #increment
        #update the pageindex in profiles.conf
        config.set(currentprofile, 'pageindex', pageindex)
    #create the dir 
    try:
        os.mkdir('./ScanCache/' + subfolder + '/')
    except:
        print
    fullpath = "./ScanCache/" + subfolder + "/" + subfolder + "-" + str(pageindex)
    
    #runs the actual command, checks return
    print('scanning')
    os.system("scanimage" + " -d " + device + " --resolution " + resolution + " --mode " + mode + " > " + fullpath)
    
    #wait for head to return to home
    sleep(headreturntime + 1)
    print('scanned page ' + str(pageindex))
    config.write(open('./Settings/Profiles.conf', 'w'))
    
elif args == "-f":
    #finish
    if outputtype == 'pdf':
        print("Converting to PDF...")
        #convert to pdf
        import ConvertPdf
    if outputlocation == 'email':
        print("Emailing...")
        #email address
        import SendEmail
    #reset
    config.set(currentprofile, 'subfolder', '')
    config.set(currentprofile, 'pageindex', 0)
    #update the config file
    config.write(open('./Settings/Profiles.conf', 'w'))
else:
    print("Please enter an argument, -a to append, -f to finish")

