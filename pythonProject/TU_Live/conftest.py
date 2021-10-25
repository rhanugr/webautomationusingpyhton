import pytest
from selenium import webdriver



@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
    driver.get("https://www.topuniversities.com/")
    driver.maximize_window()
    request.cls.driver = driver



    yield
    driver.close()
    driver.quit()
