import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture(scope="module")
def set_Path():
    global driver

    path = "C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe"
    driver =webdriver.Chrome(executable_path=path)
    # driver.implicitly_wait(5)

    yield
    # time.sleep(2)
    driver.close()

def test_login(set_Path):
    driver.maximize_window()
    driver.get("http://qa-integra-d8-tu.pantheonsite.io/universities/kansas-state-university")
    # print(driver.current_url)
    wait = WebDriverWait(driver,5)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"button.agree-button")))
    driver.find_element_by_css_selector("button.agree-button").click()
    driver.find_element_by_xpath("//ul[@class='top_right_menu']/li[3]/a[@id='user_login']").click()
    driver.find_element_by_xpath("//input[@id='edit-name']").send_keys("hanamanta@qs.com")
    driver.find_element_by_css_selector("input#edit-pass").send_keys("Ragha@90")
    driver.find_element_by_css_selector("input#edit-submit").click()

    wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"input#edit-submit")))
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 800);")
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "a#stars")))
    driver.find_element_by_css_selector("a#stars").click()
    time.sleep(10)

# def test_logout(set_Path):
#     driver.get("https://www.topuniversities.com/")
#     driver.maximize_window()
#     print(driver.title)
#     assert driver.title == "University Ranking Worldwide, Scholarship, Study Guides, Courses & Events | Top Universities"
#     driver.find_element_by_xpath("//div[@class='qs_logo tu']").click()

# def test_home(set_Path):
#     driver.get("https://www.topuniversities.com/")
#     print(driver.get_window_size())