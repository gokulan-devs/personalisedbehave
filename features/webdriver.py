from selenium import webdriver
import helper_base
def __init__(self, driver):
        super(HelperFunc, self).__init__()
        self._driver_wait = WebDriverWait(driver, HelperFunc.__TIMEOUT)
        self._driver = driver


def open(self, url):
	 self._driver.get(url)
