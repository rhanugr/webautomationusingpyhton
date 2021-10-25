import time
from selenium import webdriver
import pytest

def test_logout1():
    driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    driver.find_element_by_css_selector("#autosuggest").send_keys("ind")
    time.sleep(3)
    driver.close()