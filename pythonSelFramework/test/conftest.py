import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox  (executable_path="C:\\Hanamanta_Data\\geckodriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
#   driver.get("https://www.topuniversities.com/")
    driver.maximize_window()
    request.cls.driver = driver


    yield
    driver.close()

