import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#iframe, frames,fremaset
def test_verify_child_window():
    global driver
    path = "C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe"
    url = "https://the-internet.herokuapp.com/iframe"
    driver = webdriver.Chrome(executable_path=path)
    # driver.maximize_window()
    driver.get(url)
    driver.switch_to.frame("mce_0_ifr")
    driver.find_element_by_css_selector("#tinymce").clear()
    time.sleep(3)
    driver.find_element_by_css_selector("#tinymce").send_keys("PUTTU and KITTU")
    driver.switch_to.default_content()
    title_text = driver.find_element_by_tag_name("h3").text
    print(title_text)