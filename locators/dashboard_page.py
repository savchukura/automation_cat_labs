from selenium.webdriver.common.by import By


class DashboardPageLocators:
    # Check boxes
    HIDE_CASES_WITHOUT_PKM = (By.ID, "without")
    HIDE_CLOSED_CASES = (By.ID, "closed")

    # Sorting
    ALL_SORTING_BUTTONS = (By.XPATH, "//div[@class='style_rightAlign__coGlf style_column__wMKeM']")

    # CASES
    CASE = (By.XPATH, "//div[@class='style_row__ZKW3R style_hasSelect__SLcOG']")

    # Search
    SEARCH_INPUT = (By.XPATH, "//input[@class='style_container__input__PxHZE']")

    # Home Button
    HOME_BUTTON = (By.XPATH, "//div[@class='style_logoWrap__xK7Eu']")

    # Buttons in case on dashboard
    ADMINISTRATION_BUTTONS = (
        By.XPATH, "//button[@class='style_btn__hsBKJ style_primary-outline__8tDXS style_small__Ps3pP']")

