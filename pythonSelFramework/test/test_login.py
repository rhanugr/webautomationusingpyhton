import time
from selenium import webdriver

from Pageobjects.Homepage import HomePage
from Utilities.BaseClass import BaseClass


class TestLogin(BaseClass):

    def test_login(self):
        homepage = HomePage(self.driver)
        print("After Browser Open Executed")
        title = self.driver.title
        print("Browser Title Name is = ", title)
        homepage.shopItems().click()
        print(self.driver.current_url)
        self.driver.get_screenshot_as_file("test.png")
