import time

from pages.base_page import NextPage
from locators.Main_Page import MainPageLocators as locators
from locators.dashboard_page import DashboardPageLocators


class DeletePage(NextPage):

    def delete_case(self):
        time.sleep(1)
        self.element_is_visible(DashboardPageLocators.HOME_BUTTON).click()
        self.elements_are_visible(DashboardPageLocators.CASE)[0].click()
        self.elements_are_visible(DashboardPageLocators.ADMINISTRATION_BUTTONS)[1].click()
