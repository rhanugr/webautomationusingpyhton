

#implcit wait
#Explicit Wait
#time.sleep wait class handling
import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



def test_synchronization():
    driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/seleniumPractise")
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 5)
    search_list =[]
    vegetable_list = []
    # wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class='search-keyword']")))
    driver.find_element_by_xpath("//*[@class='search-keyword']").send_keys("ber")
    # wait.until(expected_conditions.text_to_be_present_in_element_value((By.XPATH, "//*[@class='search-keyword']")))
    time.sleep(6)
    # wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,"//div[@class='products']/div")))
    fruits = driver.find_elements_by_xpath("//div[@class='products']/div")
    count =len(fruits)
    assert count == 3
    add_to_carts = driver.find_elements_by_xpath("//div[@class='product-action']/button")
    #Child to Parent transverse //div[@class='product-action']/button/parent::div/parent::div/h4
    for addtocart_button in add_to_carts:
        fruits_list = addtocart_button.find_element_by_xpath("parent::div/parent::div/h4")
        search_list.append(fruits_list.text)
        print(fruits_list.text)
        addtocart_button.click()
    print("------Cart list-----" ,search_list)

    driver.find_element_by_xpath("//a[@class='cart-icon']/img").click()
    driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

    veggies = driver.find_elements_by_css_selector("p.product-name")
    print("size : ",len(veggies))
    for vegs in veggies:
        vegetable_list.append(vegs.text)
    print("Table List------",vegetable_list)
    # assert vegetable_list in  search_list
    bill_amount = driver.find_element_by_css_selector("span.discountAmt").text
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))
    driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
    # wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"button[class='promoBtn")))
    driver.find_element_by_css_selector("button[class='promoBtn']").click()
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
    bill_amount_after_coupan = driver.find_element_by_css_selector("span.discountAmt").text
    assert float(bill_amount_after_coupan) < int(bill_amount)
    code_applied = driver.find_element_by_css_selector("span.promoInfo").text
    assert code_applied == "Code applied ..!"
    # wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
    # driver.find_element_by_xpath("//button[text()='Place Order']").click()
    sum = 0
    amount = driver.find_elements_by_xpath("//tr/td[5]/p")
    for total_amount in amount:
        sum = sum + int(total_amount.text)
    print("=======Total Amount===========",sum)
    total = int(driver.find_element_by_css_selector("span.totAmt").text)
    assert sum == total

