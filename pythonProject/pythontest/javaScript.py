import time

import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pythontest.data import Data


driver_Path = "C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_Path)

driver.get("https://d8-test.topuniversities.com/programs")
driver.maximize_window()
wait = WebDriverWait(driver,30)

driver.find_element_by_css_selector(".agree-button").click()
driver.implicitly_wait(2)
wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='study_level']/parent::div")))
select_study_level = driver.find_element_by_xpath("//*[@id='study_level']/parent::div")
select_study_level.click()



wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='menu transition visible']//div")))
lenth_drop_dwon = driver.find_elements_by_xpath("//*[@class='menu transition visible']//div")
print(len(lenth_drop_dwon))


for i in lenth_drop_dwon:
     study = i.get_attribute("innerHTML")
     print(study)
     if study == "Masters":
          i.click()
          break

print(driver.current_url)

driver.close()
print("PASS")