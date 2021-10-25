import time

import requests
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_verify_broken_links():
    driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://staging.topuniversities.com/")
    print("Title of the Page : ", driver.title)
    wait = WebDriverWait(driver, 10)
    driver.find_element_by_css_selector(".agree-button").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.agree-button')))
    # wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"a")))
    all_links_on_page = driver.find_elements_by_css_selector("a")
    time.sleep(2)
    print("Total Links ",len(all_links_on_page))
    i = 1
    for link in all_links_on_page:
        try:
        # if link.get_attribute("href") != "None":
        #     print(i,".",link.get_attribute("href"))
            resp = requests.head(link.get_attribute("href"))
            print("==",link.get_attribute("href"), resp.status_code)
        except StaleElementReferenceException as Exception:
            print("======Exception Link ======",Exception)
        i +=1

