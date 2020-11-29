from PIL import Image
import ConfigParser
import os

#read config options
config = ConfigParser.ConfigParser()
config.read('Settings/Profiles.conf')
currentprofile = config.get('global', 'currentprofile')
subfolder = config.get(currentprofile, 'subfolder')

#get the input files
#infiles
path = 'ScanCache/' + subfolder
#zip archive if they are images
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
    imBuf = Image.open(path + f)
    imBuf = imBuf.convert('RGB')
    imagelist.append(imBuf)
imagelist[0].save(savepath, save_all=True, append_images=imagelist[1:])
