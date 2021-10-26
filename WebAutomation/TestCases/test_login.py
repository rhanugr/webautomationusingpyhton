import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_browser():
            driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
            driver.maximize_window()
            driver.get("https://www.topuniversities.com/")
            print("Title of the Page : ",driver.title)
            wait = WebDriverWait(driver, 10)
                # time.sleep(5)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.agree-button')))
            driver.find_element_by_css_selector(".agree-button").click()
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.agree-button')))
            get_login = driver.find_elements_by_xpath("//*[@class='top_right_menu']/li")
            print(len(get_login))
            for i in get_login:
                    text = i.text
                    if text == "LOGIN":
                            i.click()
                            break
                # time.sleep(3)
            driver.get_screenshot_as_file("loginpage.png")
                # wait.until(EC.visibility_of_element_located((By.NAME,"edit-name")))
            driver.find_element_by_id("edit-name").send_keys("hanamantaste@gmail.com")
            driver.find_element_by_id("edit-pass").send_keys("Ragha@90")
            time.sleep(2)
            driver.find_element_by_name("op").click()
            print("Login is successfully Done")
            time.sleep(8)
            driver.get_screenshot_as_file("HomePage.png")
            print(driver.title)
            driver.close()