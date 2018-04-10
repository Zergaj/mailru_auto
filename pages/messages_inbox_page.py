from pages.page import Page
from selenium.webdriver.common.by import By


class MessagesInboxPage(Page):

    nav_menu_locator = '//*[@id="b-nav_folders"]'

    write_letter_button_locator = '//*[@data-name="compose"]'

    def is_nav_menu_visible(self):
        return self.is_element_visible((By.XPATH, self.nav_menu_locator))

    def write_letter_button(self):
        return self.driver.find_element_by_xpath(self.write_letter_button_locator)

    def is_write_letter_button_visible(self):
        return self.is_element_visible((By.XPATH, self.write_letter_button_locator))
