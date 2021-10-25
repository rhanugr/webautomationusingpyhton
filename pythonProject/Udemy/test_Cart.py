import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_synchronization():
    driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/seleniumPractise")
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 5)
    expected_cart = ['Cucumber - 1 Kg', 'Capsicum']
    add_to_list = []
    driver.find_element_by_css_selector("[type='search']").send_keys("cu")
    time.sleep(3)
    green_cart_ap = driver.find_elements_by_css_selector("[class='products'] div h4")
    for ap_vegetable in green_cart_ap:
        add_to_list.append(ap_vegetable.text)
        # print(ap_vegetable.text)
    assert expected_cart == add_to_list
    print(add_to_list)


























