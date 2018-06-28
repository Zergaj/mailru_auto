from pages.page import Page


class MainPage(Page):

    login_form_locator = '//*[@id="auth"]'
    login_field_locator = '//*[@id="mailbox:login"]'
    password_field_locator = '//*[@id="mailbox:password"]'
    login_button_locator = '//*[@id="mailbox:submit"]'

    def login_field(self):
        return self.element(self.login_field_locator)

    def password_field(self):
        return self.element(self.password_field_locator)

    def login_button(self):
        return self.element(self.login_button_locator)

    def is_login_form_visible(self):
        return self.is_element_visible(self.login_form_locator)

    def is_login_field_visible(self):
        return self.is_element_visible(self.login_field_locator)

    def is_password_field_visible(self):
        return self.is_element_visible(self.password_field_locator)

    def is_login_button_visible(self):
        return self.is_element_visible(self.login_button_locator)
