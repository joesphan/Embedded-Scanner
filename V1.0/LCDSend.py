#Joesphan Lu, copyright @ 2020 Ok for non-commercial use. Redistribution prohibited

# Arguments:
# topstring: 16 character string representing the top row of the 16x2
# topdelay: delay of the top row before displaying blanktopstring. Seconds, Float. -1 to disable blanking
# bottomstring: 16 character string representing the bottom row of the 16x2
# bottomdelay: delay of the bottom row before displaying blankbottomstring. Seconds, Float. -1 to disable blanking
# blanktopstring: the string to return after topdelay
# blankbottomstring: the string to return after bottomdelay
#       ex.  LCDSend.LCDSend("Hello           ", -1, "world           ", 5, "                ", "blanked         ")
#       display output
#       -----------------
#       |Hello           |
#       |world           |
#       -----------------
#       after 5 seconds
#       -----------------
#       |Hello           |
#       |blanked         |
#       -----------------
import RPI_I2C_LCD_driver
import sys
import ConfigParser
import threading
import time

def LCDSend(topstring, topdelay, bottomstring, bottomdelay, blanktopstring=None, blankbottomstring=None):
    error = False
    #config file, reads i2c settings off [lcd] in Profiles.conf
    config = ConfigParser.ConfigParser()
    config.read('Settings/Profiles.conf')
    i2caddress = config.get('lcd', 'i2caddr')
    i2cbus = config.get('lcd', 'i2cbus')
    try:
        mylcd = RPI_I2C_LCD_driver.lcd(int(i2cbus), int(i2caddress, base=16))

    except:
        error = True
        print("Wrong I2C bus or address")
    if not(error):
        # write top if arg exists
        if topstring:
            mylcd.lcd_display_string(topstring, 1, 0)
            if int(topdelay) != -1:
                blankTopTimer=threading.Timer(topdelay, LCDBlank, args=(1, blanktopstring, i2cbus, i2caddress,))
                blankTopTimer.start()
        # write bottom if arg exists
        if bottomstring:
            mylcd.lcd_display_string(bottomstring, 2, 0)
            if int(bottomdelay) != -1:
                blankBottomThread=threading.Timer(bottomdelay, LCDBlank, args=(2, blankbottomstring, i2cbus, i2caddress,))
                blankBottomThread.start()
        # check if delay is put in
        
        #nodelay plain bottom string write

    
def LCDBlank(row, string, i2cbus, i2caddress,):
    error = False
    try:
        mylcd = RPI_I2C_LCD_driver.lcd(int(i2cbus), int(i2caddress, base=16))
    except:
        error = True
        print("Wrong I2C bus or address")
    if not(error):
        print("lcdblank")
        mylcd.lcd_display_string(string, row, 0)
######################################################################################
args = []
try:
    args = sys.argv[1:]
except:
    pass
if args:
    LCDSend(args[0], args[1], args[2], args[3])
