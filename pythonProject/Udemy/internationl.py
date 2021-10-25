from selenium import webdriver




def headless(self, path: str, proxy: str = "") -> None:
        ua = UserAgent()
        userAgent = ua.random
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("window-size=1500,1200")
        options.add_argument("no-sandbox")
        options.add_argument("disable-dev-shm-usage")
        options.add_argument("disable-gpu")
        options.add_argument("log-level=3")
        options.add_argument(f"user-agent={userAgent}")

        if proxy != "":
            self.proxy = True
            options.add_argument("proxy-server={}".format(proxy))

        self.driver = webdriver.Chrome("C:\\Hanamanta_Data\\Selenium\\Drivers\\chromedriver.exe", chrome_options=options)
        self.set_config()
        self._headless = True