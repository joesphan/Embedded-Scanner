#Joesphan Lu, copyright @ 2020 Ok for non-commercial use. Redistribution prohibited
#run with -c if calling from command line
from PIL import Image
import ConfigParser
import os
import sys

def ConvertPdf():
    print("converting to pdf...")
    #read config options
    config = ConfigParser.ConfigParser()
    config.read('Settings/Profiles.conf')
    currentprofile = config.get('global', 'currentprofile')
    subfolder = config.get(currentprofile, 'subfolder')

    #get filenames
    imagelist = []
    path = './ScanCache/' + subfolder + '/'
    savepath = 'PdfCache/' + subfolder + '/' + subfolder + '.pdf'
    try:
        os.mkdir('PdfCache/' + subfolder + '/')
    except:
        print
    files = [f for f in os.listdir(path) if os.path.isfile(path + f)]
    for f in files:
        try:
            imBuf = Image.open(path + f)
            imagelist.append(imBuf)
            print("appending: " + path + f + "\n")
        except:
            pass
    imagelist[0].save(savepath, save_all=True, append_images=imagelist[1])

############################################################################

args = ''
try:
    args = sys.argv[1]
except:
    print()
if args == "-c":
    ConvertPdf()

