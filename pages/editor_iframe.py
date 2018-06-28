from pages.page import Page


class EditorIframe(Page):

    body_field_locator = '//*[@id="tinymce"]'

    def body_field(self):
        return self.element(self.body_field_locator)
