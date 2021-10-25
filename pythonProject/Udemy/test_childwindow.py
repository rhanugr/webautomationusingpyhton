import time
from selenium import webdriver
validate_alert = "external site"


def test_verify_childwindow():
    driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.implicitly_wait(20)
    parent_window = driver.current_window_handle
    # print(parent_window)

    driver.find_element_by_link_text("Click Here").click()
    # child_win =   driver.window_handles[1]
    # driver.switch_to.window(child_win)
    # child_wintext = driver.find_element_by_tag_name("h3").text
    # print("========child_wintext=========",child_wintext)
    # driver.close()
    # parent_win = driver.window_handles[0]
    # driver.switch_to.window(parent_win)
    # parent_wintext = driver.find_element_by_tag_name("h3").text
    # print("==========parent_wintext=======", parent_wintext)


    all_window = driver.window_handles
    for wind in all_window:
        if wind != parent_window :
            driver.switch_to.window(wind)
            child_wintext = driver.find_element_by_tag_name("h3").text
            driver.get_screenshot_as_file("test.png")
            print("=================",child_wintext)
            driver.close()
    driver.switch_to.window(parent_window)
    print(driver.find_element_by_tag_name("h3").text)
    time.sleep(3)
    driver.close()


