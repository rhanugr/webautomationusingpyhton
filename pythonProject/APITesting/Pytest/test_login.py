import time
import pytest
from selenium import webdriver

a=101


@pytest.mark.Sanity
def test_login():
    driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    driver.find_element_by_css_selector("#autosuggest").send_keys("ind")
    time.sleep(3)
    driver.close()

@pytest.mark.Smoke
def test_logout():
    driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    driver.find_element_by_css_selector("#autosuggest").send_keys("ind")
    time.sleep(3)
    driver.close()

@pytest.mark.Smoke
def test_registration():
    driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    driver.find_element_by_css_selector("#autosuggest").send_keys("ind")
    time.sleep(3)
    driver.close()