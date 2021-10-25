import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_verify_child_window():
    global driver
    path = "C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe"
    url = "https://www.topuniversities.com/"
    driver = webdriver.Chrome(executable_path=path)
    driver.maximize_window()
    driver.get(url)
    explicit_wait = WebDriverWait(driver,8)
    explicit_wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".agree-button")))
    driver.find_element_by_css_selector(".agree-button").click()
    time.sleep(2)
    sign_up = driver.find_elements_by_xpath("//a[contains(@class,'_new_signin')]")
    sign_up[0].click()

    driver.find_element_by_css_selector("[href*='#user_sign_in']").click()
    driver.find_element_by_id("edit-name").send_keys("hanamantaste@gmail.com")
    driver.find_element_by_name("pass").send_keys("Ragha@90")
    explicit_wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"input[value ='Sign in")))
    driver.find_element_by_css_selector("input[value ='Sign in']").click()
    time.sleep(2)

    #
    # for sign_up_today in sign_up:
    #     sign_up_today.get_attribute("")

    # time.sleep(2)
    # driver.close()