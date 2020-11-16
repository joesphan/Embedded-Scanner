import RPI_I2C_LCD_driver
import sys
import ConfigParser
from time import *
# to run: python LCDSend.py "hello" "world"

#config file, reads i2c settings off [lcd] in Profiles.conf
config = ConfigParser.ConfigParser()
config.read('Profiles.conf')
i2caddress = config.get('lcd', 'i2caddr')
i2cbus = config.get('lcd', 'i2cbus')
arglist = sys.argv
mylcd = RPI_I2C_LCD_driver.lcd(int(i2cbus), int(i2caddress, base=16))
mylcd.lcd_display_string(arglist[1], 1, 1)
mylcd.lcd_display_string(arglist[2], 2, 1)
