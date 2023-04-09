import time
from pages.base_page import NextPage
from locators.dashboard_page import DashboardPageLocators as dash_locators
from locators.open_case import CasePageLocators as case_locators
from locators.new_case import NewCasePageLocators
from locators.email import EmailLocators as EL


class GetWitnessCode(NextPage):

    def get_witness_code(self):
        self.open_mail_page()
        self.switch_to_another_window(1)
        login = self.element_is_visible(EL.LOGIN_INPUT)

        login.send_keys('testautocat')
        password = self.element_is_visible(EL.PASSWORD_INPUT)
        password.send_keys('213456qaZ')
        self.element_is_visible(EL.SIGN_IN_BUTTON).click()

        self.element_is_visible(EL.OLD_MESSAGE).click()
        security_code = self.element_is_visible(EL.SECURITY_CODE).text
        return security_code

