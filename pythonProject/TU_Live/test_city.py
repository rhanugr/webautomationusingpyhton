import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


def test_city_list ():

    path = "C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    # driver = webdriver.Chrome(ChromeDriverManger)
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    driver.get("https://www.topuniversities.com/universities")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.agree-button')))
    time.sleep(3)
    driver.find_element_by_css_selector(".agree-button").click()
    time.sleep(20)
    city_list = driver.find_elements_by_css_selector("[id='city-select-ind'] option")
    print(len(city_list))
    temp_list = []
    count = 1
    for i in city_list:
        text = i.get_attribute("innerHTML")
        count +=1
        # print(count, '', text)
        if text == 'Abu Dhabi,':
            i.click()
            driver.find_elements_by_css_selector('')

