from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class SubscriptionMixPage:
    dialog_choose_package_text = "//div[text()='Du kan starte på to måder']"
    vaelg_mix_3_button = "button[data-testid='packageSelectionButton0']"
    vaelg_mix_10_button = "button[data-testid='packageSelectionButton1']"
    vaelg_mix_20_button = "button[data-testid='packageSelectionButton2']"
    vaelg_mix_30_button = "button[data-testid='packageSelectionButton3']"

    vaelg_2_mix_3_button = "button[data-testid='packageSelectionOpenButton0']"
    vaelg_2_mix_10_button = "button[data-testid='packageSelectionOpenButton1']"
    vaelg_2_mix_20_button = "button[data-testid='packageSelectionOpenButton2']"
    vaelg_2_mix_30_button = "button[data-testid='packageSelectionOpenButton3']"

    mix_nu_button = "button[data-testid='packageSelectionMixSelfButton']"

    header_mix_page = "//h1/span"
    channel_tiles = "div[class^='styled__HighlightBorder-sc']"
    mix_number_wheel_text = "div[data-testid='PointMeter-StyledPointText']"
    continue_button = "button[data-testid='continueButton']"

    def visit_onboarding_page(self, sb):
        sb.goto('https://YouTv:DuBestemmer@stg.youtv.dk/onboarding/mix')

    def click_on_mix_nu(self, sb):
        sb.click(self.mix_nu_button)

    def assert_text_in_mix_page(self, sb):
        sb.assert_text("Mix din egen tjeneste", self.header_mix_page)

    def select_default_mix(self, sb, mix=3):
        sb.assert_element_visible(self.dialog_choose_package_text)
        valid_mix = {3, 10, 20, 30}
        if mix == 3:
            sb.click(self.vaelg_mix_3_button)
            sb.click(self.vaelg_2_mix_3_button)
        elif mix == 10:
            sb.click(self.vaelg_mix_10_button)
            sb.click(self.vaelg_2_mix_10_button)
        elif mix == 20:
            sb.click(self.vaelg_mix_20_button)
            sb.click(self.vaelg_2_mix_20_button)
        elif mix == 30:
            sb.click(self.vaelg_mix_30_button)
            sb.click(self.vaelg_2_mix_30_button)
        else:
            raise ValueError("can only accept the following mix values %r." % valid_mix)

    def assert_points_in_mix_wheel(self, sb, text_expected_in_wheel):
        sb.assert_text(text_expected_in_wheel, self.mix_number_wheel_text)

    def add_channel_to_cart(self, sb, index):
        channel_tiles = sb.find_elements(self.channel_tiles, 20)
        channel = channel_tiles[index]
        sb.click(channel)

    def add_10_points_to_mix(self, sb):
        self.add_channel_to_cart(0)
        self.add_channel_to_cart(3)
        sb.assert_text("10", self.mix_number_wheel_text)

    def click_continue(self, sb):
        sb.click(self.continue_button)
