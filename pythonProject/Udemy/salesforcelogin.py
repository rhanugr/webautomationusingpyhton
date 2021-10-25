import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\Hanamanta_Data\\geckodriver.exe")
# driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
select_dropdown_static = Select(driver.find_element_by_css_selector("#exampleFormControlSelect1"))
select_dropdown_static.select_by_index(1)
select_dropdown_static.select_by_visible_text("Male")
driver.find_element_by_css_selector("[type='submit']").click()
message = driver.find_element_by_class_name("alert-success").text
print(message)
assert "Success" in message

time.sleep(2)
driver.close()


