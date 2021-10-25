import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.find_element_by_css_selector("[name='q']").send_keys("mukesh otwani")
time.sleep(3)

google_auto = driver.find_elements_by_xpath("//li[@class='sbct']//div[@class='wM6W7d']//span")
print("Total Auto Suggests Counts :",len(google_auto))
for i in google_auto:
    print(i.text)
    if i.text == "mukesh otwani youtube":
        i.click()
        break
driver.find_element_by_css_selector("[href*='UCcTII5pbZYkU4fgFtb4uesg']").click()

time.sleep(50)
driver.close()