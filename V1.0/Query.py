import subprocess
import re

def Devices():
    #get output
    output = subprocess.check_output("scanimage -L")
    #parse output
    devices = re.findall("'(.*)'", output)
    return devices

# Inputs: deviceID (str) from Devices() ex: "pixma:04A926EF_SJ3029112970S)
# Return dict:
#   ['resolution', 'mode']
#   resolutions is [] with dpi values
#   mode is [] with a string of modes
def Capabilities(deviceID):
    resolutions = []
    modes = []
    #get output
    output = subprocess.check_output("scanimage --help -d " + deviceID)
    #parse output
    resolutionstr = re.findall("--resolution (.*)dpi \[", output)
    # "auto||75|150|300|600"
    resolutions = re.findall("\d{2,3}", resolutionstr)
    
    modestrt = re.findall("--mode (.*) \[", output)
    # "auto|Color|Gray"
    modes = re.findall("[[a-zA-Z]{1,}", modestrt)
    
    #set output
    dict = {
        'resolution': resolutions,
        'mode': modes,
    }
    return dict
def I2c():
    
    return
def UsbID(VendorID):
    return
