from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators.Main_Page import MainPageLocators as locators
from URL.url import *
from pages.delete_page import DeletePage
from pages.new_case_page import CreatePage
from pages.check_result import ResultPage
from pages.login_page import LoginPage
from configurate import *

CASE_NAME = "test application"
FILE = "C:/Users/WellDone/PycharmProjects/automation_cat_labs/tests/archive_for_app.zip"
APPLICATION_UPLOAD = 5
TABS_IN_CASE = 5

class Test_Create_application_case:

    def test_identify_browser_file_safari_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME, FILE, APPLICATION_UPLOAD)

        check_result = ResultPage(driver)
        check_result.check_image_result_with_seed_phrase(TABS_IN_CASE)

        delete_usb_case = DeletePage(driver)
        delete_usb_case.delete_case(TABS_IN_CASE)

def test_identify_seed_phrase_from_application_file():
    browser_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=browser_service)
    driver.maximize_window()
    driver.get(URL)
    wait = WebDriverWait(driver, 15, 0.3)

    wait.until(ec.visibility_of_element_located((locators.NEWCASE_BUTTON)))

    driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedSecondary MuiButton-sizeLarge MuiButton-containedSizeLarge css-rrwplu']").click()
    # create case with application file
    driver.find_element(By.ID, "name").send_keys("test app")
    input_file = driver.find_element(By.XPATH, "//input[@type='file']")
    input_file.send_keys("C:/Users/WellDone/PycharmProjects/automation_cat_labs/tests/archive_for_app.zip")
    time.sleep(1)
    wait.until(ec.visibility_of_element_located((locators.OPEN_BUTTON)))
    driver.find_element(By.XPATH, "//a[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-fullWidth css-26f9rp']").click()
    # start search
    wait.until(ec.visibility_of_element_located((locators.START_SEARCH_BUTTON)))
    driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-542qq9']").click()
    # check result on dashboard page
    wait.until(ec.visibility_of_element_located((locators.RESULTS_FIELDS)))
    time.sleep(2)
    # go to application tab
    tab = driver.find_elements(By.XPATH, "//a[@class='MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary css-xu8ymu']")
    application_tab = tab[5]
    application_tab.click()
    # open case
    wait.until(ec.visibility_of_element_located((locators.RESULT)))
    result = driver.find_element(By.XPATH, "//a[@class='MuiBox-root css-127qeu']")
    result.click()
    # start purse wallet
    wait.until(ec.visibility_of_element_located((locators.PURSE_WALLET_BUTTON)))
    parse_wallet = driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium css-1795ctr']")
    parse_wallet.click()
    time.sleep(2)
    fetch_updates_button = driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium css-1795ctr']")
    fetch_updates_button.click()
    wait.until(ec.visibility_of_element_located((locators.RESULT_SCANING)))
    # check result
    seed_phrase = driver.find_element(By.XPATH, "//p[@class='MuiTypography-root MuiTypography-h5 css-1c4mutb']").text
    result = driver.find_elements(By.XPATH, "//p[@class='MuiTypography-root MuiTypography-h5 css-hi4jmm']")
    wallet_address = result[0].text
    publick_key = result[1].text
    private_key = result[2].text
    balance = result[3].text
    assets = driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-1821gv5']").text
    assert seed_phrase == ('Seed phrase:\n'
    'teach indoor drip tunnel ladder among accident cargo viable license pulp '
    'urge')
    assert wallet_address == "Wallet Address: 0x3f3cebCb1b485Dab11C2aC9899FFaD8b253D83b0"
    assert publick_key == "Public Key: 02c5e6438944d5a86f83f9adb23bca705c4b1f02164887f8182b044bf933ffa641"
    assert private_key == "Private Key: 0614b8b234b84a6bc456f9e7edc9baf34c2b1734e89585cafe72fa4d2c5c00f3"
    assert balance == "Balance: 2.73 USD"
    assert assets == "Assets:\n3.000000000000000000 MATIC"
    # delete case
    home_button = driver.find_element(By.XPATH, "//a[@class='MuiTypography-root MuiTypography-body1 css-9oncje']")
    home_button.click()
    wait.until(ec.visibility_of_element_located((locators.SIDE_MENU_BUTTONS)))
    side_menu = driver.find_elements(By.XPATH, "//li[@class='MuiListItem-root MuiListItem-gutters css-1j1dt5v']")
    side_documents = side_menu[3]
    side_documents.click()
    wait.until(ec.visibility_of_element_located((locators.DELETE_BUTTON)))
    delete_button = driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeSmall css-1y8nu6u']")
    delete_button.click()
    wait.until(ec.visibility_of_element_located((locators.CONFIRM_DELETE)))
    confirm_delete = driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-fullWidth css-m5xjv7']")
    confirm_delete.click()
    driver.quit()
