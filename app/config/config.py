import configparser

def getConfig():
    config = configparser.ConfigParser()
    config.read('app/config/properties.ini')
    return config
