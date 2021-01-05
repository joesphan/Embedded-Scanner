import subprocess
import re

def Devices():
    #get output
    output = subprocess.check_output("scanimage -L")
    #parse output
    devices = re.findall("`.*'", output)
    return devices

# Inputs: deviceID (str) from Devices() ex: "pixma:04A926EF_SJ3029112970S)
# Return dict:
#   ['resolution', 'mode']
def Capabilities(deviceID):
    #get output
    output = subprocess.check_output("scanimage --help -d " + deviceID)
    
    return
def UsbID(VendorID):
    return
