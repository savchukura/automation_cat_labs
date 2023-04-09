from selenium.webdriver.common.by import By


class AlertLocator:

    ALERT_MESSAGE = (By.XPATH, "//div[@role='alert']")

    START_SCAN_BUTTON = (By.ID, "start_scan_btn")
    CANCEL_BUTTON = (By.ID, "cancel_btn")

    ENTER_WITNESS_PIN_BUTTON = (By.ID, "enter_witness_pin_btn")
    WITNESS_DROP_DOWN = (By.XPATH, "//div[@class='style_select__-S04X']")
    SELECT_WITNESS_EMAIL = (By.XPATH, "//div[@class='style_option__M2vbJ']")
    SEND_PIN_BUTTON = (By.ID, "entered_pin_modal_send_pin_btn")
    BACK_BUTTON = (By.ID, "entered_pin_modal_back_btn")
    PIN_INPUT = (By.XPATH, "//input[@class='style_container__input__PxHZE']")
    OPEN_CASE_WITNESS_BUTTON = (By.ID, "entered_pin_modal_send_pin_btn")