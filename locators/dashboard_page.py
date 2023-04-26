from selenium.webdriver.common.by import By


class DashboardPageLocators:
    # Check boxes
    HIDE_CASES_WITHOUT_PKM = (By.ID, "without")
    HIDE_CLOSED_CASES = (By.ID, "closed")

    # Sorting
    ALL_SORTING_BUTTONS = (By.XPATH, "//div[@class='style_rightAlign__coGlf style_column__wMKeM']")

    # CASES
    CASE = (By.XPATH, "//div[@class='style_row__ZKW3R style_hasSelect__SLcOG']")

    # Open case
    OPEN_CASE_BUTTON = (By.ID, "case-detail-open-case")

    # Search
    SEARCH_INPUT = (By.XPATH, "//input[@class='style_container__input__PxHZE']")

    # Home Button
    HOME_BUTTON = (By.XPATH, "//div[@class='style_logoWrap__xK7Eu']")

    # Buttons in case on dashboard
    ADMINISTRATION_BUTTONS = (
        By.XPATH, "//button[@class='style_btn__hsBKJ style_primary-outline__8tDXS style_small__Ps3pP']")

    CASE_INFORMATION = (By.XPATH, "//div[@class='style_column__wMKeM']")


class DashboardInCaseLocators:

    CASE_INFORMATION_COUNTERS = (By.XPATH, "//div[@class='small-text']")

    TOTAL_BALANCE_PER_CHAIN = (By.XPATH, "//div[@class='style_infoDetails__JsP5m']")
