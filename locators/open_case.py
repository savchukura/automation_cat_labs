from selenium.webdriver.common.by import By


class CasePageLocators:
    # Open case from Dashboard
    OPEN_CASE_BUTTON = (By.ID, "case-detail-open-case")
    ADMINISTRATION_BUTTONS = (
        By.XPATH, "//button[@class='style_btn__hsBKJ style_primary-outline__8tDXS style_small__Ps3pP']")

    # Buttons in case
    START_SCAN_BUTTON = (By.ID, "start_scan_btn")
    CANCEL_BUTTON = (By.ID, "cancel_btn")

    ENTER_WITNESS_PIN_BUTTON = (By.ID, "enter_witness_pin_btn")
    BACK_TO_MAIN_SCREEN_BUTTON = (By.ID, "main_screen_btn")

    # WITNESS POP UP
    WITNESS_DROP_DOWN = (By.XPATH, "//div[@class='style_select__-S04X']")
    SELECT_WITNESS_EMAIL = (By.XPATH, "//div[@class='style_option__M2vbJ']")

    SEND_PIN_BUTTON = (By.ID, "entered_pin_modal_send_pin_btn")
    BACK_BUTTON = (By.ID, "entered_pin_modal_back_btn")

    EMAIL_SEND = (By.XPATH, "//div[@class='Toastify__toast-body']")

    PIN_INPUT = (By.XPATH, "//input[@class='style_container__input__PxHZE']")

    OPEN_CASE_WITNESS_BUTTON = (By.ID, "entered_pin_modal_send_pin_btn")


    # Artifacts visual data about files in case(Seed Phrase, Domains, USB Devices, Private Keys, Apps, Addresses)
    ARTIFACTS = (By.XPATH, "//p[@class='h3 style_textRow__G+DgJ']")

    # Scanning progress
    SCANNING_PROGRESS = (By.XPATH, "//div[@class='style_scroll__NSq5t']")

    # Case inside

    DASH_BOARD_BUTTON = (By.XPATH, "//h3[@class='style_name__d48w4 style_link__T53TN ellipsis']")

    ARTIFACTS_SOURCE_BUTTONS = (By.XPATH, "//li[@class='style_listItem__gIc63']")
    DOMAINS_SIDE_BUTTONS = (By.XPATH, "//div[@class='style_subItem__-QdRI']")

    ARTIFACT_IN_CASE = (By.XPATH, "//div[@class='style_row__ZKW3R style_hasSelect__SLcOG']")

    ARTIFACT_SORTING = (By.XPATH, "//button[@class='style_button__aZtqW']")

    PARSE_WALLET_BUTTON = (By.ID, 'parse_wallet_artifact')

    DATA_IN_ARTIFACT = (By.CLASS_NAME, "small-text")

