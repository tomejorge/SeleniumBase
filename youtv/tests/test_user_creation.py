import pytest
import json
from pathlib import Path
from seleniumbase import BaseCase
from youtv.pages.subscription_mix_page import SubscriptionMixPage
from youtv.pages.registration_page import RegistrationPage
from youtv.pages.payment_page import PaymentPage
from youtv.pages.home_page import HomePage
from youtv.utils.write_to_csv import add_user_data_to_csv
from youtv.utils import random_data
import pytest
from parameterized import parameterized

home = Path(__file__).resolve().parent.resolve().parent
user_data = home.joinpath('test_data/user_payment.json')
with open(user_data) as json_file:
    user_details = json.load(json_file)


class TestCreateUser(BaseCase):

    @parameterized.expand([("Mix 3", 3, '3'),
                           ("Mix 10", 10, '10'),
                           ("Mix 20", 20, '20'),
                           ("Mix 30", 30, '30')],
                          ids=['mix_3', 'mix_10', 'mix_20', 'mix_30'])
    def test_mix(self, mix_name, mix, expected_points_text):
        random_email = random_data.random_email_address()
        SubscriptionMixPage().visit_onboarding_page(self)
        SubscriptionMixPage().select_default_mix(self, mix)
        SubscriptionMixPage().assert_points_in_mix_wheel(self, expected_points_text)
        SubscriptionMixPage().click_continue(self)
        RegistrationPage().fill_customer_details(self,
                                name=user_details['name'],
                                email=random_email,
                                phone_number=user_details['phone_number'],
                                password=user_details['password'])
        RegistrationPage().click_accept_terms(self)
        RegistrationPage().click_accept_marketing(self)
        RegistrationPage().click_continue(self)
        PaymentPage().fill_cc_details(self,
                                cc_number=user_details['cc_number'],
                                cc_date=user_details['exp_date'],
                                cc_cvv=user_details['cvv'],
                                cc_name=user_details['name'])
        HomePage().assert_welcomed(self)
        add_user_data_to_csv(r'../users.csv', mix=mix_name, email=random_email)


if __name__ == '__main__':
    pytest.main()
