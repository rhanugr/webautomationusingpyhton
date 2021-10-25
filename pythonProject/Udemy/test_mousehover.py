import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#iframe, frames,fremaset

def test_verify_mouse_hover():
    path = "C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe"
    # url = "https://the-internet.herokuapp.com/hovers"
    url = "https://www.topmba.com/"
    expected_url = "https://www.topmba.com/mba-rankings/global/2022"
    driver = webdriver.Chrome(executable_path=path)
    driver.maximize_window()
    action = ActionChains(driver)
    driver.implicitly_wait(5)
    driver.get(url)
    wait = WebDriverWait(driver,5)
    print("========================================")
    print(driver.find_element_by_xpath("//meta[@name='description']").get_attribute("content"))
    # wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".agree-button")))
    #
    # action.move_to_element(driver.find_element_by_css_selector(".agree-button")).click().perform()
    # # time.sleep(5)
    action  = ActionChains(driver)
    action.move_to_element(driver.find_element_by_xpath("//li[contains(@class,'consult-rankings')]/a")).perform()
    child_menu = driver.find_element_by_link_text("Full-Time MBA Rankings")
    action.move_to_element(child_menu).perform()
    second_child = driver.find_element_by_link_text("Global")
    action.move_to_element(second_child).click().perform()
    global_link = driver.current_url
    assert global_link == expected_url
    driver.get_screenshot_as_file("Global.png")



