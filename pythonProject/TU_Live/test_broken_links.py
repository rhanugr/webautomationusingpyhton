import time
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from selenium.common import exceptions
from selenium.common.exceptions import StaleElementReferenceException

class TestBrokenLinks:

    def test_verify_broken_links(self):
        driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
        driver.maximize_window()
        # driver.get("https://d8-test.topuniversities.com/")
        driver.get("https://staging.topuniversities.com/")
        print("Title of the Page : ", driver.title)
        wait = WebDriverWait(driver, 10)
        # time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.agree-button')))
        time.sleep(1)
        driver.find_element_by_css_selector(".agree-button").click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.agree-button')))
        # get_login = driver.find_elements_by_xpath("//*[@class='top_right_menu']/li")
        # print(len(get_login))
        # for i in get_login:
        #     text = i.text
        #     if text == "LOGIN":
        #         i.click()
        #         break
        # time.sleep(3)
        # driver.get_screenshot_as_file("loginpage.png")
        driver.set_page_load_timeout(10)
        wait = WebDriverWait(driver,10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a")))
        links = driver.find_elements_by_css_selector("a")
        print(len(links))
        i = 1
        for link in links:
            try:
            # response = requests.head(link.get_attribute('href'))
            # print(i ,".", link.get_attribute('href'),response.status_code)
                 if str(link.get_attribute("href")).startswith("http"):
                    req = requests.head(link.get_attribute("href"))
                    if (req.status_code !=200):
                        print(i, ".",link.get_attribute("href"), req.status_code)
                 else:
                    print("Ignoring '{}'".format(link.get_attribute("href")))
            except StaleElementReferenceException as Exception:
                print(Exception)

            i +=1

        time.sleep(10)
        # driver.get_screenshot_as_file(".png")
        print("==============================================================================================")
        driver.close()