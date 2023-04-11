import time

from pages.base_page import BasePage
from pages.base_page import NextPage
from locators.open_case import CasePageLocators as case_locators
from locators.new_case import NewCasePageLocators as new_case_locators
from selenium.webdriver.common.action_chains import ActionChains
import random


class CreatePage(NextPage):

    def open_case_from_main_page(self):
        self.element_is_visible(new_case_locators.NEW_CASE_BUTTON).click()

    def create_exhibit(self, exhibit_description, exhibit_id, file):
        self.element_is_visible(new_case_locators.ADD_EXH_BUTTON).click()
        self.element_is_visible(new_case_locators.DESCRIPTION_INPUT).send_keys(exhibit_description)
        self.element_is_visible(new_case_locators.EXHIBIT_ID_INPUT).send_keys(exhibit_id)
        self.element_not_visible(new_case_locators.FILE_INPUT).send_keys(file)
        self.element_is_visible(new_case_locators.EXHIBIT_UPLOAD_FILE)
        self.element_is_visible(new_case_locators.ADD_EXHIBIT_BUTTON).click()

    def add_witness(self):
        self.element_is_visible(new_case_locators.ADD_WIT_BUTTON).click()
        self.element_is_visible(new_case_locators.SELECT_WITNESSES_DROP).click()
        self.elements_are_visible(new_case_locators.WITNESS_CHECK_BOX)[0].click()
        x_offset = 100
        y_offset = 200

        actions = ActionChains(self.driver)
        actions.move_by_offset(x_offset, y_offset)
        actions.click().perform()
        self.element_is_visible(new_case_locators.ADD_WITNESSES_BUTTON).click()

    def create_case_find_crypto(self, case_name, case_number):
        self.element_is_visible(new_case_locators.CASE_NAME_INPUT).send_keys(case_name)
        self.element_is_visible(new_case_locators.CASE_NUMBER_INPUT).send_keys(case_number)
        self.element_is_visible(new_case_locators.FIND_CRYPTO_BUTTON).click()
        scan_progres = self.element_is_visible(case_locators.SCANNING_PROGRESS).text
        assert scan_progres == 'Scanning in progress'

    def create_case_save_case(self, case_name, case_number):
        self.element_is_visible(new_case_locators.CASE_NAME_INPUT).send_keys(case_name)
        self.element_is_visible(new_case_locators.CASE_NUMBER_INPUT).send_keys(case_number)
        self.element_is_visible(new_case_locators.SAVE_CASE_BUTTON).click()

    def get_analyst_supervisor(self):
        analyst_sup = self.elements_are_visible(new_case_locators.ANALYST_AND_SUP)
        analyst = analyst_sup[0].text
        supervisor = analyst_sup[1].text

        return analyst, supervisor

    def return_disable_find_crypto_and_save_case_buttons(self):
        dis_find_crypto = self.element_is_visible(new_case_locators.DIS_FIND_CRYPTO)
        dis_save_case = self.element_is_visible(new_case_locators.DIS_SAVE_CASE)
        return dis_find_crypto, dis_save_case



