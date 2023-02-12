from pages.base_page import NextPage
from locators.Main_Page import MainPageLocators as locators


class DeletePage(NextPage):

    def delete_case(self):
        self.element_is_visible(locators.HOME_BUTTON).click()
        self.elements_are_visible(locators.DELETE_BUTTON)[3].click()
        self.element_is_visible(locators.CONFIRM_DELETE).click()
