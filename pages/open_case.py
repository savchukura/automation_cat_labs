import time
from pages.base_page import NextPage
from locators.dashboard_page import DashboardPageLocators as dash_locators
from locators.open_case import CasePageLocators as case_locators
from locators.new_case import NewCasePageLocators


class OpenCase(NextPage):

    def open_case_from_dashboard(self):
        self.elements_are_visible(dash_locators.CASE)[0].click()
        self.element_is_visible(case_locators.OPEN_CASE_BUTTON)[0].click()
        self.element_is_visible(case_locators.START_SCAN_BUTTON)[0].click()
        scan_progres = self.element_is_visible(case_locators.SCANNING_PROGRESS)
        assert scan_progres == 'Scanning in progress'

    def open_case_with_witness(self):
        self.element_is_visible(case_locators.ENTER_WITNESS_PIN_BUTTON).click()
        self.element_is_visible(case_locators.WITNESS_DROP_DOWN).click()
        self.element_is_visible(case_locators.SELECT_WITNESS_EMAIL).click()
        self.element_is_visible(case_locators.SEND_PIN_BUTTON).click()
        self.element_is_visible(case_locators.PIN_INPUT).send_keys('424242')
        self.element_is_visible(case_locators.OPEN_CASE_WITNESS_BUTTON).click()

    def open_artifact(self, side_menu_button):
        self.elements_are_visible(case_locators.ARTIFACTS_SOURCE_BUTTONS)[side_menu_button].click()
        self.element_is_visible(case_locators.ARTIFACT_IN_CASE).click()
        self.element_is_visible(case_locators.PARSE_WALLET_BUTTON).click()

    def check_parse_result_seed(self):
        data = self.elements_are_present(case_locators.DATA_IN_ARTIFACT)
        seed_phrase = data[0].text
        wallet_address = data[1].text
        private_key = data[2].text
        balance = data[3].text
        assets = data[4].text

        return seed_phrase, wallet_address, private_key, balance, assets

    def check_parse_result_wallet_address(self):
        data = self.elements_are_present(case_locators.DATA_IN_ARTIFACT)
        wallet_address = data[0].text
        balance = data[1].text
        assets = data[2].text

        return wallet_address, balance, assets

    def check_presents_of_domains(self):
        self.elements_are_present(case_locators.ARTIFACTS_SOURCE_BUTTONS)[4].click()
        self.go_to_element("//div[@title='http://otnolatrnup.com/hideref.engine?d=https%3a%2f%2fbinomo.com%3fa%3dc565278f3597%26ac%3d101_Q42022']")
