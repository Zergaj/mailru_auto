from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

class Page(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def is_element_visible(self, locator):
        try:
            return self.wait.until(visibility_of_element_located((By.XPATH, locator)))
        except WebDriverException:
            return False

    def element(self, locator):
        return self.driver.find_element_by_xpath(locator)

    def open(self, url):
        return self.driver.get(url)
