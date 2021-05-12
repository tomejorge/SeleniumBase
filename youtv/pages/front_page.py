from selenium.webdriver.common.by import By


class FrontPage:
    # LOCATORS
    login_button = "a[class='button-cyan w-button']"
    pink_start_now_button = "a[class='button-pink button-pink-big w-button']"
    accept_cookie_banner_button = "button[class='coi-banner__accept']"

    def __init__(self, driver):
        super().__init__(driver)

    def visit_front_page(self, sb):
        # sb.visit(base_urls.home_url)
        pass

    def accept_cookies(self, sb):
        sb.click(self.accept_cookie_banner_button)

    def click_login_button(self, sb):
        sb.click(self.login_button)

    def click_start_mix_button(self, sb):
        sb.click(self.pink_start_now_button)
