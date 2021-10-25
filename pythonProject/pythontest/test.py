from selenium import webdriver



driver_Path ="C:\\Hanamanta_Data\\Selenium\Drivers\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_Path)
driver.get("https://www.topuniversities.com/")
print(driver.title)
driver.close()
print("PASS")