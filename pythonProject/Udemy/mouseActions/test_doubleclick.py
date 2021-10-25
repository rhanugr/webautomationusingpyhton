import time

from selenium import webdriver
import logging


def test_double_click():
    driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
    driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
    driver.implicitly_wait(20)
    from selenium.webdriver import ActionChains
    action  = ActionChains(driver)
    # doubl_clk =driver.find_element_by_css_selector("input#double-click")
    # # action.context_click(doubl_clk).perform()
    # action.double_click(doubl_clk).perform()

    # driver.switch_to.alert
    # text =driver.switch_to.alert.text
    # assert text == "You double clicked me!!!, You got to be kidding me"
    # # print("=========================",text)
    # logging.info("PASS",text)
    driver.save_screenshot("screeennnnn.png")
    # driver.switch_to.alert.accept()
    driver.find_element_by_css_selector("input[value='Prompt']").click()
    sendingamessage = driver.switch_to.alert
    time.sleep(2)
    sendingamessage.send_keys("Unix")
    # driver.switch_to.alert.accept()
    # time.sleep(10)
    # driver.save_screenshot("screeennnnn.png")








