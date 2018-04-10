from pages.page import Page
from selenium.webdriver.common.by import By


class SendmsgokPage(Page):

    msg_sent_title_locator = '//*[@class="message-sent__title"]'

    def is_msg_sent_title_visible(self):
        return self.is_element_visible((By.XPATH, self.msg_sent_title_locator))
