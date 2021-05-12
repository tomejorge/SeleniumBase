from seleniumbase import BaseCase


class RegistrationPage:
    # note: name, email and password locators return a list of elements
    name_fields = "input[name='name']"
    email_fields = "input[name='email']"
    phone_number_fields = "input[name='phoneNumber']"
    password_fields = "input[name='password']"
    accept_terms_checkbox = "label[name='termsAccept']"
    accept_newsletter_checkbox = "label[name='newsletterOptOut']"

    input_fields = "div[class^='styled__InputWrapper']"
    continue_button = "button[data-testid='continueButton']"

    def fill_customer_details(self, sb, name, email, phone_number, password):
        sb.type(self.name_fields, name)
        sb.type(self.email_fields, email)
        sb.type(self.phone_number_fields, phone_number)
        sb.type(self.password_fields, password)

    def click_accept_terms(self, sb):
        sb.click(self.accept_terms_checkbox)

    def click_accept_marketing(self, sb):
        sb.click(self.accept_newsletter_checkbox)

    def click_continue(self, sb):
        sb.click(self.continue_button)
