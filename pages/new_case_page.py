import time

from pages.base_page import BasePage
from pages.base_page import NextPage
from locators.Main_Page import MainPageLocators as locators


class CreatePage(NextPage):

    def create_case(self, case_name, file, upload_complete):
        self.element_is_visible(locators.NEWCASE_BUTTON).click()
        self.element_is_visible(locators.CASE_NAME_INPUT).send_keys(case_name)
        self.element_not_visible(locators.FILE_INPUT).send_keys(file)
        self.element_is_visible(locators.UPLOAD_COMPLETE[upload_complete])
        time.sleep(1)
        self.elements_are_visible(locators.OPEN_BUTTON)[3].click()
        time.sleep(1)
        self.element_is_visible(locators.START_SEARCH_BUTTON).click()
        time.sleep(2)


