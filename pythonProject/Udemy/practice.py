import time
from selenium import webdriver
validate_alert = "external site"

def test_alert():
    driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
    driver.get("https://licindia.in/Home-(1)/Customer-Portal")
    driver.implicitly_wait(20)
    driver.find_element_by_css_selector("[href*=Login]").click()
    parent_window = driver.current_window_handle
    alert_message = driver.switch_to.alert
    assert validate_alert in alert_message.text
    alert_message.accept()
    windows = driver.window_handles
    print(windows)
    for win in windows:
        if win != parent_window:
            driver.switch_to.window(win)
            print(driver.current_url)

    time.sleep(10)
    driver.find_element_by_css_selector("[name='userId']").send_keys("rhanu.gr89")
    driver.switch_to_default.content

# print(driver.current_window_handle)
# driver.switch_to.window("CDwindow-D2F2F4D7CED60E3227F2EA33A3D18109")



    time.sleep(2)
    driver.close()