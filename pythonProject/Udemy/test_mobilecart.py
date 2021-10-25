import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_addtocart():
    path = "C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe"
    url = "https://rahulshettyacademy.com/angularpractice"
    # options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=path)
    driver.get(url)
    driver.find_element_by_css_selector("[href*='shop']").click()
    products = driver.find_elements_by_xpath("//div[@class='card h-100']")
    #//div[@class='card h-100']/div/h4   To navigate under the same class
    #//div[@class='card h-100']/div[2]/button
    for product in products:
        all_products = product.find_element_by_xpath("div/h4/a").text
        if all_products == "Blackberry":
            product.find_element_by_xpath("div[2]/button").click()
            break
    driver.find_element_by_css_selector("[class*='btn-primary']").click()
    driver.find_element_by_css_selector("[class*='btn-success']").click()
    driver.find_element_by_xpath("//input[@id='country']").send_keys("Ind")
    wait = WebDriverWait(driver,8)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
    driver.find_element_by_link_text("India").click()
    driver.find_element_by_xpath("//div[contains(@class,'checkbox-primary')]").click()
    driver.find_element_by_css_selector("[class*='btn-success']").click()
    success_message = driver.find_element_by_css_selector("[class*='alert-success']").text
    message = "Success! Thank you!"
    assert message in  success_message
    driver.get_screenshot_as_file("Cart.png")
    time.sleep(5)
    driver.close()

