from pages.page import Page
from selenium.webdriver.common.by import By


class ComposePage(Page):

    send_form_locator = '//*[@class="composeForm editorHTMLMode"]'

    to_field_locator = '//*[@data-original-name="To"]'
    subject_field_locator = '//*[@name="Subject"]'
    editor_locator = '//*[@class="compose__editor__frame"]'
    send_button_locator = '//*[@data-name="send"]'

    def is_send_form_visible(self):
        return self.is_element_visible((By.XPATH, self.send_form_locator))

    def is_to_field_visible(self):
        return self.is_element_visible((By.XPATH, self.to_field_locator))

    def is_subject_field_visible(self):
        return self.is_element_visible((By.XPATH, self.subject_field_locator))

    def is_editor_visible(self):
        return self.is_element_visible((By.XPATH, self.editor_locator))

    def is_send_button_visible(self):
        return self.is_element_visible((By.XPATH, self.send_button_locator))

    def to_field(self):
        return self.driver.find_element_by_xpath(self.to_field_locator)

    def subject_field(self):
        return self.driver.find_element_by_xpath(self.subject_field_locator)

    def body_field(self):
        return self.driver.find_element_by_xpath(self.editor_locator)

    def send_button(self):
        return self.driver.find_element_by_xpath(self.send_button_locator)

    def switch_to_editor_iframe(self):
        iframe_id = ''
        list = self.driver.find_elements_by_tag_name('iframe')
        for i in list:
            if 'composeEditor' in i.get_attribute('id'):
                iframe_id = i.get_attribute('id')
        self.driver.switch_to.frame(iframe_id)

    def switch_from_editor_iframe(self):
        self.driver.switch_to.default_content()