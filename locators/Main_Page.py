from selenium.webdriver.common.by import By

class MainPageLocators():
    # Create Case and Delete
    HOME_BUTTON = (By.XPATH, "//div[@class='style_logoWrap__xK7Eu']")
    SIDE_MENU_BUTTONS = (By.XPATH, "//li[@class='MuiListItem-root MuiListItem-gutters css-1j1dt5v']")
    NEWCASE_BUTTON = (By.ID, "home_new_case_btn")
    CASE_NAME_INPUT = (By.ID, "name")
    FILE_INPUT = (By.XPATH, "//input[@type='file']")

    CANCEL_BUTTON = (By.ID, "create_card_cancel_btn")

    UPLOAD_COMPLETE = [(By.XPATH, '//*[text() = "test image"]'),
                       (By.XPATH, '//*[text() = "test browser"]'),
                       (By.XPATH, '//*[text() = "test email"]'),
                       (By.XPATH, '//*[text() = "test document"]'),
                       (By.XPATH, '//*[text() = "test usb"]'),
                       (By.XPATH, '//*[text() = "test application"]'),
                       (By.XPATH, '//*[text() = "test_image_eth_full"]'),
                       (By.XPATH, '//*[text() = "test_image_eth_part"]'),
                       (By.XPATH, '//*[text() = "test_qr_eth_wallet"]')]

    START_BUTTON = (By.ID, "case_card_start_btn")
    OPEN_BUTTON = (By.ID, "case_card_open_btn")
    DELETE_BUTTON = (By.ID, "case_card_delete_btn")
    CONFIRM_DELETE = (By.ID, "delete_modal_open_btn")

    #Results

    START_SEARCH_BUTTON = (By.ID, "accordion_card_start_search_btn")
    TABS_IN_CASE = [(By.ID, "card_detail_tabs_Images"),
                    (By.ID, "card_detail_tabs_Browsers"),
                    (By.ID, "card_detail_tabs_Emails"),
                    (By.ID, "card_detail_tabs_Documents"),
                    (By.ID, "card_detail_tabs_USB History"),
                    (By.ID, "card_detail_tabs_App"),
                    (By.ID, "card_detail_tabs_All Traces")]



    RESULTS_FIELDS = (By.XPATH, "//div[@class='style_card__HaMfE']")

    PAGINATION_PREV = (By.XPATH, "//li[@class='style_item__f8jL1 style_prevArrow__i8XDY']")
    PAGINATION_NEXT = (By.XPATH, "//li[@class='style_item__f8jL1 style_nextArrow__I9OMr']")

    RESULT = (By.XPATH, "//a[@class='MuiBox-root css-kxoxyh']")
    # seed phrase and wallet address
    PURSE_WALLET_BUTTON = (By.ID, "trace_detail_action_btn")
    SAVE_PDF_BUTTON = (By.ID, "trace_detail_save_PDF_btn")
    FETCH_UPDATES_BUTTON = (By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium css-1bj54f1']")
    RESULT_SCANING_SEED = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-16q5o7z']")
    RESULT_SCANING = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-14wd27g']")
    RESULT_SCANING_ASSETS = (By.XPATH, "//div[@class='MuiBox-root css-1821gv5']")

    # usb results
    USB_RESULTS = (By.XPATH, "//div[@class='MuiBox-root css-yd8sa2']")
    USB_RESULTS_TEST = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-h5 css-hi4jmm']")

    #browser, emails domains results
    DOMAINS = (By.XPATH, "//div[@class='MuiBox-root css-1j8l0ob']")


