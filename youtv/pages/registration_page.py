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

    def fill_customer_details(self, sb, name, email, password, phonenumber):
        name_fields = sb.find_elements(self.name_fields)
        email_fields = sb.find_elements(self.email_fields)
        phone_number_fields = sb.find_elements(self.phone_number_fields)
        password_fields = sb.find_elements(self.password_fields)
        name_field = name_fields[0]
        email_field = email_fields[0]
        phone_number = phone_number_fields[0]
        password_field = password_fields[0]
        name_field.send_keys(name)
        email_field.send_keys(email)
        phone_number.send_keys(phonenumber)
        password_field.send_keys(password)

    def click_accept_terms(self, sb):
        sb.click(self.accept_terms_checkbox)

    def click_accept_marketing(self, sb):
        sb.click(self.accept_newsletter_checkbox)

    def click_continue(self, sb):
        sb.click(self.continue_button)
