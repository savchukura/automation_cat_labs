from selenium.webdriver.common.by import By


class MainPageLocators():
    # Create Case and Delete
    HOME_BUTTON = (By.XPATH, "//div[@class='style_logoWrap__xK7Eu']")
    SIDE_MENU_BUTTONS = (By.XPATH, "//li[@class='MuiListItem-root MuiListItem-gutters css-1j1dt5v']")
    NEWCASE_BUTTON = (By.ID, "home_new_case_btn")
    CASE_NAME_INPUT = (By.ID, "name")
    FILE_INPUT = (By.XPATH, "//input[@type='file']")

    CANCEL_BUTTON = (By.ID, "create_card_cancel_btn")

    UPLOAD_COMPLETE = [(By.XPATH, '//*[text() = "test image"]'),  # 0
                       (By.XPATH, '//*[text() = "test browser"]'),  # 1
                       (By.XPATH, '//*[text() = "test email"]'),  # 2
                       (By.XPATH, '//*[text() = "test document"]'),  # 3
                       (By.XPATH, '//*[text() = "test usb"]'),  # 4
                       (By.XPATH, '//*[text() = "test application"]'),  # 5
                       (By.XPATH, '//*[text() = "test_image_eth_full"]'),  # 6
                       (By.XPATH, '//*[text() = "test_image_eth_part"]'),  # 7
                       (By.XPATH, '//*[text() = "test_qr_eth_wallet"]'),  # 8
                       (By.XPATH, '//*[text() = "test_seed_eth_txt_doc"]'),  # 9
                       (By.XPATH, '//*[text() = "test_seed_eth_docx_doc"]'),  # 10
                       (By.XPATH, '//*[text() = "test_seed_eth_odt_doc"]'),  # 11
                       (By.XPATH, '//*[text() = "test_seed_eth_xlsx_doc"]'),  # 12
                       (By.XPATH, '//*[text() = "test_wallet_adr_eth_doc_txt"]'),  # 13
                       (By.XPATH, '//*[text() = "test_wallet_adr_eth_doc_docx"]'),  # 14
                       (By.XPATH, '//*[text() = "test_wallet_adr_eth_doc_odt"]'),  # 15
                       (By.XPATH, '//*[text() = "test_wallet_adr_eth_doc_xlsx"]'),  # 16
                       (By.XPATH, '//*[text() = "test_seed_eth_application"]'),  # 17
                       (By.XPATH, '//*[text() = "test_wallet_adr_bit_doc_txt"]'),  # 18
                       (By.XPATH, '//*[text() = "test_dmg_file"]'),  # 19
                       (By.XPATH, '//*[text() = "test_dashboard_bitcoin_doc"]'),  # 20
                       (By.XPATH, '//*[text() = "test_dashboard_browser_arch"]')]  # 21

    UPLOAD_COMPLETE_IMAGE = [(By.XPATH, '//*[text() = "test image"]')]
    UPLOAD_COMPLETE_BROWSER = [(By.XPATH, '//*[text() = "test browser"]')]
    UPLOAD_COMPLETE_EMAILS = [(By.XPATH, '//*[text() = "test email"]')]

    UPLOAD_COMPLETE_DOCUMENT = [(By.XPATH, '//*[text() = "test document"]'),
                                (By.XPATH, '//*[text() = "test_seed_eth_txt_doc"]'),
                                (By.XPATH, '//*[text() = "test_seed_eth_docx_doc"]')]

    UPLOAD_COMPLETE_USB = [(By.XPATH, '//*[text() = "test usb"]')]
    UPLOAD_COMPLETE_APP = [(By.XPATH, '//*[text() = "test application"]')]

    START_BUTTON = (By.ID, "case_card_start_btn")
    OPEN_BUTTON = (By.ID, "case_card_open_btn")
    DELETE_BUTTON = (By.ID, "case_card_delete_btn")
    CONFIRM_DELETE = (By.ID, "delete_modal_open_btn")

    # Results

    START_SEARCH_BUTTON = (By.ID, "accordion_card_start_search_btn")

    DASHBOARD_RESULT = (By.XPATH, "//p[@class='subtitle style_desc__tSskh']")
    CASE_RESULT = (By.XPATH, "//p[@class='small-text style_desc__tSskh']")

    TABS_IN_CASE = [(By.ID, "card_detail_tabs_Images"),
                    (By.ID, "card_detail_tabs_Browsers"),
                    (By.ID, "card_detail_tabs_Emails"),
                    (By.ID, "card_detail_tabs_Documents"),
                    (By.ID, "card_detail_tabs_USB History"),
                    (By.ID, "card_detail_tabs_App"),
                    (By.ID, "card_detail_tabs_All Traces")]

    CASE_RESULTS = (By.XPATH, "//div[@class='style_wrap__6TU-e style_infoRow__zvGUv']")
    RESULTS_FIELDS = (By.XPATH, "//div[@class='style_card__HaMfE']")

    PAGINATION_PREV = (By.XPATH, "//li[@class='style_item__f8jL1 style_prevArrow__i8XDY']")
    PAGINATION_NEXT = (By.XPATH, "//li[@class='style_item__f8jL1 style_nextArrow__I9OMr']")

    # Navigation buttons in case
    MAIN_BUTTON = (By.ID, "breadcrumbs-Main")
    CASE_BUTTON = (By.ID, "breadcrumbs-Case")


    # RESULT = (By.XPATH, "//a[@class='MuiBox-root css-kxoxyh']")
    # seed phrase and wallet address
    PURSE_WALLET_BUTTON = (By.ID, "trace_detail_action_btn")
    SAVE_PDF_BUTTON = (By.ID, "trace_detail_save_PDF_btn")
    FETCH_UPDATES_BUTTON = (By.ID, "trace_detail_fetch_updates_btn")
    # RESULT_SCANING_SEED = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-16q5o7z']")
    RESULT_SCANING = (By.XPATH, "//div[@class='style_wrap__6TU-e style_column__Wegf8']")
    RESULT_SCANING_ASSETS = (By.XPATH, "//div[@class='style_assetsWraper__POolV']")

    # usb results
    USB_RESULTS = (By.XPATH, "//div[@class='style_wrap__6TU-e style_column__Wegf8']")
    USB_RESULTS_TEST = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-h5 css-hi4jmm']")

    # browser, emails domains results
    HISTORY_DOMAINS = (By.XPATH, "//div[@class='style_domainsWrap__fcuAe style_history_domains__swXc7']")
    EMAIL_DOMAINS = (By.XPATH, "//div[@class='style_domainsWrap__fcuAe style_email_domains__t43M-']")
    APPLICATION_DOMAINS = (By.XPATH, "//div[@class='style_domainsWrap__fcuAe style_applications__xoZEd']")
