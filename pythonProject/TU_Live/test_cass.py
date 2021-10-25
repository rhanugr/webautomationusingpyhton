import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.color import Color

def test_button():
    global driver
    path = "C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe"
    url = "http://qa-integra-d8-tu.pantheonsite.io/"
    driver = webdriver.Chrome(executable_path=path)
    driver.maximize_window()
    driver.get(url)
    explicit_wait = WebDriverWait(driver,8)
    explicit_wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".agree-button")))
    driver.find_element_by_css_selector(".agree-button").click()
    time.sleep(2)
    sign_up = driver.find_elements_by_xpath("//a[contains(@class,'_new_signin')]")
    button_color = sign_up[0].value_of_css_property("background-color")
    print("========>>>",button_color)
    # hex = Color.from_string(rgb).hex