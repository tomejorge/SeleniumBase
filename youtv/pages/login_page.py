from selenium.webdriver.common.by import By


class LoginPage:
    """ Locators"""
    email_address_field = "[placeholder='Mailadresse']"
    password_field = "[placeholder='Adgangskode']"
    # in chrome console - > $$("button[data-testid='loginButton']")
    login_button = "button[data-testid='loginButton']"
    error_login = "p[data-testid-test='errors']"

    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self, sb):
        # self.visit(base_urls.login_url)
        pass

    def click_login_button(self, sb):
        sb.click(self.login_button)

    def type_username(self, sb, username):
        sb.type(username, self.email_address_field)

    def type_password(self, sb, password):
        sb.type(password, self.password_field)

    def press_login_button(self, sb):
        sb.click(self.login_button)

    def check_is_header_displayed(self, sb, element):
        sb.is_displayed(element)

    def assert_element_displayed(self, sb, element):
        sb.is_displayed(element, 1)

    def login(self, sb, username, password):
        # complete login method
        sb.open_login_page()
        sb.type_username(username)
        sb.type_password(password)
        sb.click_login_button()
