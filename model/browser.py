from selenium import webdriver


class Browser:
    def __init__(self, type):
        self.type = type

    def create(self):
        if self.type == "firefox":
            return webdriver.Firefox()
        elif self.type == "chrome":
            return webdriver.Chrome()
