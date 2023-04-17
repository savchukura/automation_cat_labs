import time


from pages.base_page import NextPage
from locators.alert import AlertLocator


class Alert(NextPage):

    def get_alert(self):
        alert = self.element_is_visible(AlertLocator.ALERT_MESSAGE).text
        return alert

    def click_cancel_button_on_scan_page(self):
        self.element_is_visible(AlertLocator.CANCEL_BUTTON).click()

    def click_start_button_on_scan_page(self):
        self.element_is_visible(AlertLocator.START_SCAN_BUTTON).click()

    def send_witness_code(self):
        self.element_is_visible(AlertLocator.ENTER_WITNESS_PIN_BUTTON).click()
        self.element_is_visible(AlertLocator.WITNESS_DROP_DOWN).click()
        self.element_is_visible(AlertLocator.SELECT_WITNESS_EMAIL).click()
        self.element_is_visible(AlertLocator.SEND_PIN_BUTTON).click()

    def click_back_button(self):
        self.element_is_visible(AlertLocator.BACK_BUTTON).click()

    def enter_pin_and_open_case(self, pin='424242'):
        self.element_is_visible(AlertLocator.PIN_INPUT).send_keys(pin)
        self.element_is_visible(AlertLocator.OPEN_CASE_WITNESS_BUTTON).click()

    def refresh_page(self):
        self.driver.refresh()
