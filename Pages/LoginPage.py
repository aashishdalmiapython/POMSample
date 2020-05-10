from Libraries import ConfigReader

class loginclass():

    def __init__(self,obj):
        global driver
        driver = obj

    def click_login_tab(self):
        driver.find_element_by_xpath(ConfigReader.readLocators('Login','login_tab_xpath')).click()

    def enter_username(self, username):
        driver.find_element_by_xpath(ConfigReader.readLocators('Login','username_xpath')).send_keys(username)

    def enter_password(self,password):
        driver.find_element_by_xpath(ConfigReader.readLocators('Login','password_xpath')).send_keys(password)

    def click_login_button(self):
        driver.find_element_by_xpath(ConfigReader.readLocators('Login','login_xpath')).click()



