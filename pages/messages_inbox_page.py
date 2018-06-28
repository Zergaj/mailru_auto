from pages.page import Page


class MessagesInboxPage(Page):

    nav_menu_locator = '//*[@id="b-nav_folders"]'

    write_letter_button_locator = '//*[@data-name="compose"]'

    def is_nav_menu_visible(self):
        return self.is_element_visible(self.nav_menu_locator)

    def write_letter_button(self):
        return self.element(self.write_letter_button_locator)

    def is_write_letter_button_visible(self):
        return self.is_element_visible(self.write_letter_button_locator)
