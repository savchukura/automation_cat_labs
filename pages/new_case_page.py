import time

from pages.base_page import BasePage
from pages.base_page import NextPage
from locators.Main_Page import MainPageLocators as locators

class CreatePage(NextPage):

    def create_image_case(self):
        self.element_is_visible(locators.NEWCASE_BUTTON).click()
        self.element_is_visible(locators.CASE_NAME_INPUT).send_keys("test usb")
        self.element_not_visible(locators.FILE_INPUT).send_keys(r'C:\Users\WellDone\PycharmProjects\automation_cat_labs\tests\valid_screen_one.png')
        self.element_is_visible(locators.UPLOAD_COMPLETE_USB)
        time.sleep(1)
        self.element_is_visible(locators.OPEN_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(locators.START_SEARCH_BUTTON).click()
        time.sleep(1)
        self.elements_are_visible(locators.TABS_IN_CASE)[0].click()
        self.element_is_visible(locators.RESULT).click()
        self.element_is_visible(locators.PURSE_WALLET_BUTTON).click()
        time.sleep(2)
        self.element_is_visible(locators.FETCH_UPDATES_BUTTON).click()
        result_seed_phrase = self.elements_are_visible(locators.RESULT_SCANING_SEED)
        result_
        assert result[0].text == "VID(0x): 2b24"
        assert result[1].text == "PID(0x): 846"
        assert result[2].text == "Vendor Name: Generic"
        assert result[3].text == "Device Description: desc"

    def create_usb_case(self):
        self.element_is_visible(locators.NEWCASE_BUTTON).click()
        self.element_is_visible(locators.CASE_NAME_INPUT).send_keys("test usb")
        self.element_not_visible(locators.FILE_INPUT).send_keys(r'C:\Users\WellDone\PycharmProjects\automation_cat_labs\tests\USBSTOR.reg')
        self.element_is_visible(locators.UPLOAD_COMPLETE_USB)
        time.sleep(1)
        self.element_is_visible(locators.OPEN_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(locators.START_SEARCH_BUTTON).click()
        time.sleep(1)
        self.elements_are_visible(locators.TABS_IN_CASE)[4].click()
        self.element_is_visible(locators.RESULT).click()
        result = self.elements_are_visible(locators.USB_RESULTS_TEST)
        assert result[0].text == "VID(0x): 2b24"
        assert result[1].text == "PID(0x): 846"
        assert result[2].text == "Vendor Name: Generic"
        assert result[3].text == "Device Description: desc"

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


