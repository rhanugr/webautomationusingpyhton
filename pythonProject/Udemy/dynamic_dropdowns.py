import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_css_selector("#autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")

for country in countries:
    if(country.text=="India"):
        country.click()
        print(country.text)
        break
driver.find_element_by_css_selector("#autosuggest").text
# We cant see the updated text since selenium loads the page once it wont be having idea on updated thing
# Selenium Loads the DOM once you open the page
#you can use get Attribute on the page
ind_selected = driver.find_element_by_css_selector("#autosuggest").get_attribute('value')
assert ind_selected =="India"
print(ind_selected)
time.sleep(2)
driver.quit()