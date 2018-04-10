from pages.page import Page


class EditorIframe(Page):

    body_field_locator = '//*[@id="tinymce"]'

    def body_field(self):
        return self.driver.find_element_by_xpath(self.body_field_locator)
