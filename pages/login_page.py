import time

from pages.base_page import BasePage
from pages.base_page import NextPage
from locators.Main_Page import MainPageLocators as locators
from locators.login_page import LoginPageLocators as login_locators

class LoginPage(BasePage):

    def login(self):
        return

    def log_in(self, login, password):
        self.element_is_visible(login_locators.LOGIN_INPUT).send_keys(login)
        self.element_is_visible(login_locators.PASSWORD_INPUT).send_keys(password)
        self.element_is_visible(login_locators.CONFIRM_BUTTON).click()

    def login_error_empty(self):
        self.element_is_visible(login_locators.LOGIN_INPUT).send_keys("")
        self.element_is_visible(login_locators.PASSWORD_INPUT).send_keys("")
        self.element_is_visible(login_locators.LOGIN_INPUT).click()
        login_error_empty_field = self.elements_are_visible(login_locators.EMPTY_FIELD_ERROR)
        self.element_is_visible(login_locators.DISABLED_CONFIRM_BUTTON)
        return login_error_empty_field

    def login_error_invalid_data(self, login='', password=''):
        self.element_is_visible(login_locators.LOGIN_INPUT).send_keys(login)
        self.element_is_visible(login_locators.PASSWORD_INPUT).send_keys(password)
        self.element_is_visible(login_locators.CONFIRM_BUTTON).click()

    def get_error(self):
        login_error_empty_field = self.elements_are_visible(login_locators.EMPTY_FIELD_ERROR)
        return login_error_empty_field
