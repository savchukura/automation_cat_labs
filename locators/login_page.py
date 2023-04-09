from selenium.webdriver.common.by import By


class LoginPageLocators:

    LOGIN_INPUT = (By.ID, "login_email")
    PASSWORD_INPUT = (By.ID, "login_password")

    # BUTTONS
    CONFIRM_BUTTON = (By.ID, "login_btn")
    DISABLED_CONFIRM_BUTTON = (
        By.XPATH, "//button[@class='style_btn__hsBKJ style_primary__puVxW style_btn__ldHic style_disable__TOkYo']")

    # ERRORS

    EMPTY_FIELD_ERROR = (By.XPATH, "//div[@class='style_container__helper__5LuEU']")
