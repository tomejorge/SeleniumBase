

class PaymentPage:

    heading = "h1[class^='styled__Title'] > span"
    payment_iframe = "iframe[title='iframe']"
    cc_number = "input[data-testid='creditcardNumber']"
    cc_exp_date = "input[data-testid='creditcardCCExp']"
    cc_cvv = "input[data-testid='creditcardCVV']"
    cc_name = "input[data-testid='creditcardName']"
    continue_button = "//button[@type='submit' and text()='Fortsæt']"

    def fill_cc_details(self, sb, cc_number, cc_date, cc_cvv, cc_name):
        """ fill cc details and press enter with \n on the last type """
        sb.wait_for_text('Du er der næsten', self.heading, timeout=20)
        sb.switch_to_frame(self.payment_iframe, 10)
        sb.type(self.cc_number, cc_number)
        sb.type(self.cc_exp_date, cc_date)
        sb.type(self.cc_cvv, cc_cvv)
        sb.type(self.cc_name, f"{cc_name}\n")
