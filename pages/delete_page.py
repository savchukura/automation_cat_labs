from pages.base_page import NextPage
from locators.Main_Page import MainPageLocators as locators

class DeletePage(NextPage):

    def delete_images_case(self):
        self.element_is_visible(locators.HOME_BUTTON).click()
        images_side_button = self.elements_are_visible(locators.SIDE_MENU_BUTTONS)
        images_side_button[0].click()
        self.elements_are_visible(locators.DELETE_BUTTON)[3].click()
        self.element_is_visible(locators.CONFIRM_DELETE).click()

    def delete_browser_case(self):
        self.element_is_visible(locators.HOME_BUTTON).click()
        images_side_button = self.elements_are_visible(locators.SIDE_MENU_BUTTONS)
        images_side_button[1].click()
        self.elements_are_visible(locators.DELETE_BUTTON)[3].click()
        self.element_is_visible(locators.CONFIRM_DELETE).click()

    def delete_email_case(self):
        self.element_is_visible(locators.HOME_BUTTON).click()
        images_side_button = self.elements_are_visible(locators.SIDE_MENU_BUTTONS)
        images_side_button[2].click()
        self.elements_are_visible(locators.DELETE_BUTTON)[3].click()
        self.element_is_visible(locators.CONFIRM_DELETE).click()

    def delete_document_case(self):
        self.element_is_visible(locators.HOME_BUTTON).click()
        images_side_button = self.elements_are_visible(locators.SIDE_MENU_BUTTONS)
        images_side_button[3].click()
        self.elements_are_visible(locators.DELETE_BUTTON)[3].click()
        self.element_is_visible(locators.CONFIRM_DELETE).click()

    def delete_usb_history_case(self):
        self.element_is_visible(locators.HOME_BUTTON).click()
        images_side_button = self.elements_are_visible(locators.SIDE_MENU_BUTTONS)
        images_side_button[4].click()
        self.elements_are_visible(locators.DELETE_BUTTON)[3].click()
        self.element_is_visible(locators.CONFIRM_DELETE).click()

    def delete_application_case(self):
        self.element_is_visible(locators.HOME_BUTTON).click()
        images_side_button = self.elements_are_visible(locators.SIDE_MENU_BUTTONS)
        images_side_button[5].click()
        self.elements_are_visible(locators.DELETE_BUTTON)[3].click()
        self.element_is_visible(locators.CONFIRM_DELETE).click()

    def delete_case(self, side_menu_button):
        self.element_is_visible(locators.HOME_BUTTON).click()
        side_button = self.elements_are_visible(locators.SIDE_MENU_BUTTONS)
        side_button[side_menu_button].click()
        self.elements_are_visible(locators.DELETE_BUTTON)[3].click()
        self.element_is_visible(locators.CONFIRM_DELETE).click()
