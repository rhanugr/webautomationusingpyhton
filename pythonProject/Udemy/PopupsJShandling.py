import time

from selenium import webdriver

validate_text = "Option3"
driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("#name").send_keys("Option3")
driver.find_element_by_id("alertbtn").click()
alert_message = driver.switch_to.alert
alertm = alert_message.text
assert validate_text in alertm
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element_by_css_selector("#confirmbtn").click()
driver.switch_to.alert.dismiss()

time.sleep(3)
driver.close()