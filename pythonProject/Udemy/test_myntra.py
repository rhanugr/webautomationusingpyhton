from selenium import webdriver
from selenium.webdriver import ActionChains


def test_addtocart():
    path = "C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe"
    url = "https://www.myntra.com"
    # options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=path)
    driver.get(url)
    actions = ActionChains(driver)
    men = driver.find_element_by_xpath("//*[@href='/shop/men' and @class='desktop-main']")
    actions.move_to_element(men).perform()
    
    # products = driver.find_elements_by_xpath("//li[@class='product-base']")
    # for product in products:
    #     print(product.find_element_by_xpath("a/div[2]/h4").text)