import time
from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
check_boxs = driver.find_elements_by_css_selector("[type='checkbox']")

print(len(check_boxs))
for check_box in check_boxs:
    print(check_box.get_attribute("value"))
    if(check_box.get_attribute("value")=="option2"):
        check_box.click()
        assert check_box.is_selected()
radio_button = driver.find_elements_by_xpath("//input[@name='radioButton']")
radio_button[2].click()
assert (radio_button[2].is_selected())


# print(radio_button)


time.sleep(5)
driver.close()