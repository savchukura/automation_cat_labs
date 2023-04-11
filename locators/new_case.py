from selenium.webdriver.common.by import By


class NewCasePageLocators:
    # Buttons case
    NEW_CASE_BUTTON = (By.ID, "new-case-btn")
    BACK_BUTTON = (By.XPATH, "//div[@class='style_back__-zdqF']")
    SAVE_CASE_BUTTON = (By.ID, "cancel_save_case_btn")
    CANCEL_BUTTON = (By.ID, "cancel_create_btn")
    FIND_CRYPTO_BUTTON = (By.ID, "cancel_find_crypto_btn")
    ADD_EXH_BUTTON = (
        By.XPATH, "//button[@class='style_btn__hsBKJ style_primary-outline__8tDXS style_btn__CdAyc style_small__Ps3pP']")

    ADD_WIT_BUTTON = (
        By.XPATH, "//button[@class='style_btn__hsBKJ style_primary-outline__8tDXS style_btn__J6lNW style_small__Ps3pP']")

    # POP AFTER USER CLICK ON CANCEL BUTTON
    POP_UP_CANCEL_BUTTON = (By.ID, "cancel_modal_cancel_btn")
    PIP_UP_CONFIRM_BUTTON = (By.ID, "cancel_modal_confirm_btn")

    # drop down case
    SELECT_TYPE_OF_SCAN = (By.XPATH, "//div[@class='style_select__-S04X']")
    SELECTED = (By.XPATH, "//div[@class='style_option__M2vbJ style_isSelect__m4FOF']")
    NOT_SELECTED = (By.XPATH, "//div[@class='style_option__M2vbJ']")

    # Inputs case
    CASE_NAME_INPUT = (By.ID, "case_create_name")
    CASE_NUMBER_INPUT = (By.ID, "case_create_number")

    # EXHIBIT
    # EXHIBIT INPUTS
    DESCRIPTION_INPUT = (By.ID, "case_exhibits_description")
    EXHIBIT_ID_INPUT = (By.ID, "case_exhibits_id")
    DETAILS_INPUT = (By.XPATH, "//textarea[@class='style_container__input__Vl8cW style_hasError__9ZRU5']")
    FILE_INPUT = (By.XPATH, "//input[@type='file']")

    EXHIBIT_UPLOAD_FILE = (By.XPATH, "//h3[@class='style_filename__gXrMZ']")

    ALERT_MESSAGE = (By.XPATH, "//div[@role='alert']")

    # Exhibit buttons
    EXHIBIT_CANCEL_BUTTON = (By.ID, "cancel_create_exhibit_btn")
    ADD_EXHIBIT_BUTTON = (By.XPATH, "//button[@class='style_btn__hsBKJ style_primary__puVxW style_btn__PIxBk']")

    # CASE WITNESSES

    # CASE WITNESSES BUTTONS
    WITNESSES_BACK_BUTTON = (By.ID, "witness_modal_back_btn")
    ADD_WITNESSES_BUTTON = (By.ID, "witness_modal_add_witness_btn")

    # WITNESSES DROP DOWN
    SELECT_WITNESSES_DROP = (By.XPATH, "//div[@class='style_select__x2ik+']")

    WITNESS_CHECK_BOX = (By.XPATH, "//div[@class='style_option__RdVYA']")
    CLICK = (By.XPATH, "//*[text() = 'Select Witness']")

    # who created
    ANALYST_AND_SUP = (By.XPATH, "//p[@class='style_info__kVVxz h3']")

    # Disabled buttons

    DIS_FIND_CRYPTO = (
        By.XPATH, "//button[@class='style_btn__hsBKJ style_primary__puVxW style_btn__8TGvf style_disable__TOkYo']")
    DIS_SAVE_CASE = (
        By.XPATH, "//button[@class='style_btn__hsBKJ style_primary__puVxW style_btnSaveCase__WQ8sR style_disable__TOkYo']")
