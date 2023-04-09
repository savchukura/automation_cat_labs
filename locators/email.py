from selenium.webdriver.common.by import By


class EmailLocators:

    LOGIN_INPUT = (By.NAME, 'login')

    PASSWORD_INPUT = (By.NAME, 'password')

    SIGN_IN_BUTTON = (By.XPATH, "//button[@type='submit']")

    MESSAGES_BUTTON = (By.XPATH, "//a[@class='service__entry service__entry_mail']")

    MESSAGE = (By.XPATH, "//tr[@class='msglist__row unread icon0  ui-draggable']")

    OLD_MESSAGE = (By.XPATH, "//tr[@class='msglist__row icon0  ui-draggable']")

    SECURITY_CODE = (By.XPATH, "//div[@class='readmsg__body']")
