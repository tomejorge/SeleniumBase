from seleniumbase import BaseCase

class HomePage:
    # LOCATORS
    new_user_welcome_dialog = "//div[text()='Velkommen til']"
    header_div = "div[data-test='menu']"

    def assert_welcomed(self, sb):
        sb.assert_element(self.new_user_welcome_dialog, timeout=30)
        sb.assert_element(self.header_div, timeout=40)
