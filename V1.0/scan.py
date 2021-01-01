#Joesphan Lu, copyright @ 2020 Ok for non-commercial use. Redistribution prohibited
#call scan() with "-a" or "-f" to 
import ConfigParser
import sys
import os
from datetime import datetime
from time import sleep
import ConvertPdf
import SendEmail

def scan(args):
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
        os.system("scanimage" + " -d " + device + " --resolution " + resolution + " --mode " + mode + " > " + fullpath + ".pnm")
        
        #wait for head to return to home
        sleep(headreturntime + 1)
        print('scanned page ' + str(pageindex))
        config.write(open('./Settings/Profiles.conf', 'w'))
        
    elif args == "-f":
        #finish
        if outputtype == 'pdf':
            print("Converting to PDF...")
            #convert to pdf
            ConvertPdf.ConvertPdf()
        if outputlocation == 'email':
            print("Emailing...")
            #email address
            SendEmail.SendEmail()
        #reset
        config.set(currentprofile, 'subfolder', '')
        config.set(currentprofile, 'pageindex', 0)
        #update the config file
        config.write(open('./Settings/Profiles.conf', 'w'))
    else:
        print("Please enter an argument, -a to append, -f to finish")
################################################################################
try:
    a = sys.argv[1]
    if a:
        scan(a)
except:
    print('Please enter an argument, -a to append, -f to finish')
