import pytest
from requests.exceptions import MissingSchema, InvalidSchema
from selenium import webdriver
import requests




@pytest.mark.sanity
def test_broken_images():
    path = "C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    url_d8test = "https://d8-test.topmba.com/"
    url_live = "https://www.topmba.com/"
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get(url_live)
    placeholdertext = driver.find_element_by_xpath("//input[@placeholder='Search for rankings, universities, programs, tips and advice']")
    print("=============================================================================================================================")
    print(placeholdertext.get_attribute("placeholder"))

    # links = driver.find_elements_by_xpath("//*[@class='ranklogo-desc']")
    links = driver.find_elements_by_tag_name("a")
    images = driver.find_elements_by_tag_name("img")

    print("============================================================:-->",len(links))
    print("--------------:-->",len(images))
    # for link in links:
    #     response = requests.head(link.get_attribute("href"))
    #     print(response.status_code)
    count = 1
    notfound = []
    for image in images:
        try:
            resp = requests.head(image.get_attribute("src"))
            print(count ,".", image.get_attribute("src"), ": ", resp.status_code)
            if resp.status_code == 404:
                notfound.append(image.get_attribute("src"))
        except MissingSchema :
            print(count ,".","====================== :-- > ",image.get_attribute("src"))
        count +=1

    for errorpage in notfound:
        print("===========================:",errorpage)

print("=========================================Test 2 Begins====================================================")




@pytest.mark.sanity
def test_broken_links():
    path = "C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    url_d8test = "https://d8-test.topmba.com/"
    url_live = "https://www.topmba.com/"
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get(url_d8test)
    all_links = driver.find_elements_by_tag_name("a")
    print(len(all_links))
    count1 = 1
    for linkbroken in all_links:
        try:
            link_response = requests.head(linkbroken.get_attribute("href"))
            print(count1,".",linkbroken.get_attribute("href"),link_response.status_code)

        except MissingSchema:
            print("=====----==== Missing Schema ",linkbroken.get_attribute("href"))
        except InvalidSchema:
            print("=======================Invalid Schema",linkbroken.get_attribute("href"))
        count1 +=1

