import pytest
from requests.exceptions import MissingSchema, InvalidSchema
from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options

@pytest.mark.smoke
def test_broken_link():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    path = "C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
    url_d8test_topmba = "https://d8-test.topmba.com/"
    url_live_topmba = "https://www.topmba.com/"
    url_d8test_topuniversities = "https://d8-test.topuniversities.com/"
    url_live_topuniversities = "https://www.topuniversities.com/"
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get("https://staging.topuniversities.com/")
    print("=================================",driver.current_url,"====================================")
    all_links = driver.find_elements_by_tag_name("a")
    print(len(all_links))
    count1 = 1
    broken_links = []
    for anchor_tag in all_links:
        try:
            response_link = requests.head(anchor_tag.get_attribute("href"))
            # print(count1,".",anchor_tag.get_attribute("href"),response_link.status_code)
            if response_link.status_code != 200:
                broken_links.append(anchor_tag.get_attribute("href"))

        except MissingSchema:
            print("Missing Schemas ==============", anchor_tag.get_attribute("href"))
        except InvalidSchema:
            print("InvalidSchema Schemas ========", anchor_tag.get_attribute("href"))
        count1 +=1
    for linksin in broken_links:
        print("---->>>>",linksin)
    print("=====================================Test Verify Broken Links in TU is Done===========================")

