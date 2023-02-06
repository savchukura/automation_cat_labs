import time

from pages.base_page import BasePage
from pages.base_page import NextPage
from locators.Main_Page import MainPageLocators as locators

class LoginPage(BasePage):

    def login(self):
        return