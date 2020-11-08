import configparser
config = configparser.ConfigParser()
print(config.read('PrintSettings.conf'))
print(config.sections())
input()
print(config['global']['currentprofile'])
print(config['profile1']['device'])
print(config['profile1']['resolution'])
print(config['profile1']['filename'])
input()
config['profile1']['resolution'] = '300'
with open('PrintSettings.conf', 'w') as configfile:
   config.write(configfile)
config.read('PrintSettings.conf')
print(config['profile1']['resolution'])
input()