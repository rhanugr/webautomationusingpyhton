import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestStudy:

    def test_study_prefarance(self):
        driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.topuniversities.com/")
        print("Title of the Page : ", driver.title)
        driver.implicitly_wait(100)
        wait = WebDriverWait(driver, 30)
        time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.agree-button')))
        driver.find_element_by_css_selector(".agree-button").click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.agree-button')))
        get_login = driver.find_elements_by_xpath("//*[@class='top_right_menu']/li")
        # print(len(get_login))

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
        time.sleep(5)
        driver.find_element_by_name("op").click()
        list_actual = []
        list_expected = ["Distance / Online MBA","Executive MBA", "Full-time 1 year MBA","Full-time 2 years MBA", "Part-time MBA", "Part-time / EMBA Modular"]
        print("==============================Login has been successfully Done====================================")
        action = ActionChains(driver)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@class='user_pic']/img")))
        user = driver.find_element_by_xpath("//*[@class='user_pic']/img")
        action.move_to_element(user).perform()

        my_account = driver.find_elements_by_xpath("//*[contains(@class,'dropdown-menu')]/a")
        for account in my_account:
            # print(account.text)
            if account.text == "My Account":
                account.click()
                time.sleep(2)
                break
                print("Clicked")

        # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[href*='studyPreference']")))
        driver.find_element_by_css_selector("[href*='studyPreference']").click()
        driver.execute_script("window.scrollTo(0, 100)")
        driver.find_element_by_xpath("//*[@id='study-preferences-form']/div[2]/div[2]/fieldset/div/i").click()
        mba_program =  driver.find_elements_by_xpath("//*[@id='preferred_program_type']/option")
        # print("MBA Program Type Count ",len(mba_program))
        for mba_program_type in mba_program:

            # print(mba_program_type.get_attribute("innerHTML"))
            list_actual.append(mba_program_type.get_attribute("innerHTML"))

        print("============================================================================================")

        for i in list_actual:
            print(i)

        # assert list_actual == list_expected


        time.sleep(10)
        driver.get_screenshot_as_file("Dash_Board_Page.png")
        print("==============================================================================================")
        driver.close()