#Joesphan Lu, copyright @ 2020 Ok for non-commercial use. Redistribution prohibited
import CHIP_IO.GPIO as GPIO
import threading
import time
import os
import ConfigParser
import scan
try:
    import LCDSend
except:
    pass

#def scanGPIO():
config = ConfigParser.ConfigParser()
config.read('Settings/Profiles.conf')



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


#setup all gpio
GPIO.setup(profile1btn, GPIO.IN)
GPIO.setup(profile2btn, GPIO.IN)
GPIO.setup(profile3btn, GPIO.IN)
GPIO.setup(profile4btn, GPIO.IN)
GPIO.setup(scanpagebtn, GPIO.IN)
GPIO.setup(finishscanbtn, GPIO.IN)

try:
    LCDSend.LCDSend("     Ready     ", -1, "Select  Profile", -1, "", "")
except:
    pass

try:
    while True:
        #profile 1 selection
        if not(GPIO.input(profile1btn)):
            #debounce
            if not(profile1btnpressed):
                profile1btnpressed = True
                config.set('global', 'currentprofile', 'profile1')
                #update the config file
                config.write(open('./Settings/Profiles.conf', 'w'))
                try:
                    LCDSend.LCDSend("", -1, "   Profile 1   ", -1, "", "")
                except:
                    pass
                print("profile 1 pressed \n")
        else:
            profile1btnpressed = False
            
        #profile 2 selection
        if not(GPIO.input(profile2btn)):
            #debounce
            if not(profile2btnpressed):
                profile2btnpressed = True
                config.set('global', 'currentprofile', 'profile2')
                #update the config file
                config.write(open('./Settings/Profiles.conf', 'w'))
                try:
                    LCDSend.LCDSend("", -1, "   Profile 2   ", -1, "", "")
                except:
                    pass
                print("profile 2 pressed \n")
        else:
            profile2btnpressed = False
            
        #profile 3 selection
        if not(GPIO.input(profile3btn)):
            #debounce
            if not(profile3btnpressed):
                profile3btnpressed = True
                config.set('global', 'currentprofile', 'profile3')
                #update the config file
                config.write(open('./Settings/Profiles.conf', 'w'))
                try:
                    LCDSend.LCDSend("", -1, "   Profile 3   ", -1, "", "")
                except:
                    pass
                print("profile 3 pressed \n")
        else:
            profile3btnpressed = False
            
        #profile 4 selection
        if not(GPIO.input(profile4btn)):
            #debounce
            if not(profile4btnpressed):
                profile4btnpressed = True
                config.set('global', 'currentprofile', 'profile4')
                #update the config file
                config.write(open('./Settings/Profiles.conf', 'w'))
                try:
                    LCDSend.LCDSend("", -1, "   Profile 4   ", -1, "", "")
                except:
                    pass
                print("profile 4 pressed \n")
        else:
            profile4btnpressed = False
            
        #scan page
        if not(GPIO.input(scanpagebtn)):
            #debounce
            if not(scanpagebtnpressed):
                scanpagebtnpressed = True
                try:
                    LCDSend.LCDSend("  Scanning...  ", -1, "", -1, "", "")
                except:
                    pass
                #run scan
                scan.scan("-a")
                print("scan page pressed \n")
        else:
            scanpagebtnpressed = False
                        
        #scan page
        if not(GPIO.input(finishscanbtn)):
            #debounce
            if not(finishscanbtnpressed):
                finishscanbtnpressed = True
                #finish scan
                scan.scan("-f")
                
                try:
                    LCDSend.LCDSend("     Ready     ", -1, "", -1, "", "")
                except:
                    pass
                print("finish scan pressed \n")
        else:
            finishscanbtnpressed = False
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

#x = threading.Thread(target=scanGPIO)
#x.daemon = True
#x.start()
