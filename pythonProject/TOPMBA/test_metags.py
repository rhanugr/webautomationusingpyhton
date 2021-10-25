import time

from selenium import webdriver


def test_broken_links():
    path = "C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    url_d8test = "https://d8-test.topmba.com/"
    url_live = "https://www.topmba.com/"
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get(url_d8test)
    # all_links = driver.find_elements_by_tag_name("a")
    # print(len(all_links))
    fb = driver.find_element_by_css_selector(".facbook")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    driver.execute_script("arguments[0].click();",fb)
    time.sleep(10)