import pytest
import requests
from requests.exceptions import MissingSchema
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging


@pytest.mark.smoke
def test_broken_images():
    path = "C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe"
    url_d8test_topmba = "https://d8-test.topmba.com/"
    url_live_topmba = "https://www.topmba.com/"
    url_d8test_topuniversities = "https://d8-test.topuniversities.com/"
    url_live_topuniversities = "https://www.topuniversities.com/"
    #----------------------------------------------------------------------------------------------------
    # Log information printing in report
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler('logfile.log')
    logger.addHandler(file_handler)
    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    file_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    #======================================================================================================

    # To Execute Headless broswer
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=path, options =options)
    #========================================================================================================
    driver.get(url_live_topmba)
    # print('\n'"=============================",driver.current_url,"==========================================")
    print('\n')

    # Broken Images Test Logic
    images = driver.find_elements_by_tag_name("img")
    print(len(images))
    count = 1
    for image in images:
        try:
            response = requests.head(image.get_attribute("src"))
            print(count, image.get_attribute("src"),response.status_code)
        except MissingSchema:
            print("======>>",image.get_attribute("src"),response.status_code)
        count += 1