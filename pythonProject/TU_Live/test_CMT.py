import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class TestCMT:

    def test_cmt(self):
        path = "C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe"
        driver =webdriver.Chrome(executable_path=path)
        # driver = webdriver.Chrome(ChromeDriverManger)
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)
        driver.get("https://www.topuniversities.com/")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.agree-button')))
        time.sleep(3)
        driver.find_element_by_css_selector(".agree-button").click()
        hover_on_discover = driver.find_element_by_xpath("//nav[@id='top_menu']/ul/li[2]/a")
        action = ActionChains(driver)
        action.move_to_element(hover_on_discover).perform()
        driver.find_element_by_link_text("Course Matching Tool").click()
        driver.find_element_by_xpath("//button[@class='btn _mt_start_matching']").click()
        time.sleep(2)
        # study_level = driver.find_elements_by_css_selector("[name='study_level']")
        study_level = driver.find_elements_by_xpath("//input[@name='study_level']/parent::button")

        print(len((study_level)))
        # study_level[1].click()
        for study in study_level :
            # print(study.get_attribute("InnerHTML"))
            print(study.text)
            if study.text=="Masters":
                study.click()
                break


        time.sleep(3)

        Learning_type = driver.find_elements_by_xpath("//input[@name='sp']/parent::button")
        Learning_type[1].click()
        driver.execute_script("window.scrollTo(0,400)")
        time.sleep(2)
        select_country = driver.find_element_by_xpath("//div[@id='anchor2']/div[2]/div[1]/div/input")
        select_country.click()
        # select_country.send_keys("India")
        time.sleep(2)
        countries = driver.find_elements_by_css_selector("div[class='item']")
        # print(len(countries))
        for country in countries:
            # print(country.text)
            if country.text == "India":
                country.click()
                break
        time.sleep(2)
        destination = driver.find_elements_by_xpath("//div[@id='anchor3']/div[2]/div/button")
        destination[2].click()
        time.sleep(2)
        # driver.execute_script("window.scrollTo(0,800)")
        # subject = driver.find_element_by_xpath("//div[@id='anchor4']/div[2]/div[2]/div/div")
        # subject = driver.find_element_by_xpath("//option[@class='_mt_d_none']/ancestor::div[contains(@class,'_mt_subject_specs')]")
        #subject.click()
        # wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='anchor4']/div[2]/div[2]/div/div")))
        # subject = driver.find_element_by_xpath("//*[@id='anchor4']/div[2]/div[2]/div/div")
        # driver.find_element_by_xpath("//*[@id='anchor4']/div[2]/div[2]").send_keys("Ac")
        # subject.click()


        # subject.send_keys("ac")
        # driver.implicitly_wait(20)

        # subjects_d = driver.find_elements_by_css_selector("select[name='_mt_subject_specs[]'] option")
        # print("total :-",len(subjects_d))
        #
        # for i in subjects_d:
        #     print(i.get_attribute("innerHTML"))
        #     if i.get_attribute("innerHTML")=="Accountancy":
        #         i.click()
        #         break
        driver.get_screenshot_as_file("CMT.png")





        time.sleep(2)
        driver.close()