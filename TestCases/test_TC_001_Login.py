from selenium.webdriver import Chrome
from Base import InitiateDriver
from Pages import LoginPage
import pytest
import openpyxl
from DataGenerate import Datagen

@pytest.mark.parametrize("data",Datagen.dataGen())
def test_valid_login(data):
    driver = InitiateDriver.startBrowser()
    Login = LoginPage.loginclass(driver)
    Login.click_login_tab()
    Login.enter_username(data[0])
    Login.enter_password(data[1])
    Login.click_login_button()
    InitiateDriver.closeBrowser()