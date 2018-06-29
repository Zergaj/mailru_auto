from pages.main_page import MainPage
from pages.messages_inbox_page import MessagesInboxPage
from pages.compose_page import ComposePage
from pages.sendmsgok_page import SendmsgokPage
from pages.editor_iframe import EditorIframe


class Application(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.main_page = MainPage(driver)
        self.message_inbox_page = MessagesInboxPage(driver)
        self.compose_page = ComposePage(driver)
        self.sentmsgok_page = SendmsgokPage(driver)
        self.editor_iframe = EditorIframe(driver)

    def open_login_page(self):
        return self.main_page.open(self.base_url)

    def is_login_page(self):
        return self.main_page.is_login_form_visible()

    def login(self, user):
        if self.main_page.is_login_field_visible():
            self.main_page.login_field().send_keys(user[0])
        if self.main_page.is_password_field_visible():
            self.main_page.password_field().send_keys(user[1])
        if self.main_page.is_login_button_visible():
            self.main_page.login_button().click()

    def is_logged_in(self):
        return self.message_inbox_page.is_nav_menu_visible()

    def open_send_email_form(self):
        if self.message_inbox_page.is_write_letter_button_visible():
            self.message_inbox_page.write_letter_button().click()

    def is_send_email_form_opened(self):
        return self.compose_page.is_send_form_visible()

    def send_email(self, email):
        if self.compose_page.is_to_field_visible():
            self.compose_page.to_field().send_keys(email[0])
        if self.compose_page.is_subject_field_visible():
            self.compose_page.subject_field().send_keys(email[1])
        if self.compose_page.is_editor_visible():
            self.compose_page.switch_to_editor_iframe()
            self.editor_iframe.body_field().send_keys(email[2])
            self.compose_page.switch_from_editor_iframe()
        if self.compose_page.is_send_button_visible():
            self.compose_page.send_button().click()

    def is_email_sent(self):
        return self.sentmsgok_page.is_msg_sent_title_visible()
