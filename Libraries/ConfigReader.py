from configparser import ConfigParser

def readConfig(section,key):
    objconfig = ConfigParser()
    objconfig.read("./ConfigurationFiles/Config.cfg")
    return objconfig.get(section,key)

def readLocators(section,key):
    objlocator= ConfigParser()
    objlocator.read("./ConfigurationFiles/Locators.cfg")
    return objlocator.get(section,key)