#Joesphan Lu, copyright @ 2020 Ok for non-commercial use. Redistribution prohibited
import CHIP_IO.GPIO as GPIO
import threading
import time
import os
import ConfigParser



#def scanGPIO():
config = ConfigParser.ConfigParser()
config.read('Settings/Profiles.conf')

#setup all gpio
GPIO.setup("XIO-P0", GPIO.IN)
GPIO.setup("XIO-P1", GPIO.IN)
GPIO.setup("XIO-P2", GPIO.IN)
GPIO.setup("XIO-P3", GPIO.IN)
GPIO.setup("XIO-P4", GPIO.IN)
GPIO.setup("XIO-P5", GPIO.IN)
GPIO.setup("XIO-P6", GPIO.IN)
GPIO.setup("XIO-P7", GPIO.IN)

profile1btn = config.get('global', 'profile1pin')
profile1btnpressed = False

profile2btn = config.get('global', 'profile2pin')
profile2btnpressed = False

profile3btn = config.get('global', 'profile3pin')
profile3btnpressed = False

profile4btn = config.get('global', 'profile4pin')
profile4btnpressed = False

scanpagebtn = config.get('global', 'scanpagepin')
scanpagebtnpressed = False

finishscanbtn = config.get('global', 'finishscanpin')
finishscanbtnpressed = False

try:
    while True:
        #profile 1 selection
        if GPIO.input(profile1btn):
            #debounce
            if profile1btnpressed == False:
                profile1btnpressed = True
                config.set('global', 'currentprofile', 'profile1')
                #update the config file
                config.write(open('./Settings/Profiles.conf', 'w'))
                print("profile 1 pressed \n")
        else:
            profile1btnpressed = False
            
        #profile 2 selection
        if GPIO.input(profile2btn):
            #debounce
            if profile2btnpressed == False:
                profile2btnpressed = True
                config.set('global', 'currentprofile', 'profile2')
                #update the config file
                config.write(open('./Settings/Profiles.conf', 'w'))
                print("profile 2 pressed \n")
        else:
            profile2btnpressed = False
            
        #profile 3 selection
        if GPIO.input(profile3btn):
            #debounce
            if profile3btnpressed == False:
                profile3btnpressed = True
                config.set('global', 'currentprofile', 'profile3')
                #update the config file
                config.write(open('./Settings/Profiles.conf', 'w'))
                print("profile 3 pressed \n")
        else:
            profile3btnpressed = False
            
        #profile 4 selection
        if GPIO.input(profile4btn):
            #debounce
            if profile4btnpressed == False:
                profile4btnpressed = True
                config.set('global', 'currentprofile', 'profile4')
                #update the config file
                config.write(open('./Settings/Profiles.conf', 'w'))
                print("profile 4 pressed \n")
        else:
            profile4btnpressed = False
            
        #scan page
        if GPIO.input(scanpagebtn):
            #debounce
            if scanpagebtnpressed == False:
                scanpagebtnpressed = True
                #run scan
                os.system("scan.py -a")
                print("scan page pressed \n")
        else:
            scanpagebtnpressed = False
                        
        #scan page
        if GPIO.input(finishscanbtn):
            #debounce
            if finishscanbtnpressed == False:
                finishscanbtnpressed = True
                print("finish scan pressed \n")
                #finish scan
                os.system("scan.py -f")
        else:
            finishscanbtnpressed = False
            
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

#x = threading.Thread(target=scanGPIO)
#x.daemon = True
#x.start()
