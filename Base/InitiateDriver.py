from selenium.webdriver import Chrome

def startBrowser():
    global driver
    driver = Chrome(executable_path="./Drivers/chromedriver.exe")
    url = "https://www.thetestingworld.com/testings"
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver

def closeBrowser():
    driver.close()
