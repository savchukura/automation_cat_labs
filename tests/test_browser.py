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

CASE_NAME = "test browser"
FILE = "C:/Users/WellDone/PycharmProjects/automation_cat_labs/tests/safari.zip"
BROWSER_UPLOAD = 1

class Test_Create_browser_case:

    def test_identify_browser_file_safari_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME, FILE, BROWSER_UPLOAD)

        check_result = ResultPage(driver)
        check_result.check_browser_result_safari()

        delete_case = DeletePage(driver)
        delete_case.delete_browser_case()



    def test_identify_browser_file(self, driver):
        browser_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=browser_service)
        driver.maximize_window()
        driver.get(URL)
        wait = WebDriverWait(driver, 20, 0.3)

        wait.until(ec.visibility_of_element_located((locators.NEWCASE_BUTTON)))

        driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedSecondary MuiButton-sizeLarge MuiButton-containedSizeLarge css-rrwplu']").click()
        # create case with application file
        driver.find_element(By.ID, "name").send_keys("test browser")
        #wait.until(ec.visibility_of_element_located((locators.FILE_INPUT)))
        input_file = driver.find_element(By.XPATH, "//input[@type='file']")

        input_file.send_keys("C:/Users/WellDone/PycharmProjects/automation_cat_labs/tests/safari.zip")
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((locators.UPLOAD_COMPLETE_BROWSER)))
        driver.find_element(By.XPATH, "//a[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-fullWidth css-26f9rp']").click()
        # start search
        wait.until(ec.visibility_of_element_located((locators.START_SEARCH_BUTTON)))
        driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiLoadingButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-542qq9']").click()
        # check result on dashboard page
        wait.until(ec.visibility_of_element_located((locators.RESULTS_FIELDS)))
        time.sleep(2)
        # go to application tab
        tab = driver.find_elements(By.XPATH, "//a[@class='MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary css-xu8ymu']")
        browser_tab = tab[1]
        browser_tab.click()
        # open case
        wait.until(ec.visibility_of_element_located((locators.RESULT)))
        result = driver.find_element(By.XPATH, "//a[@class='MuiBox-root css-127qeu']")
        result.click()
        # check result
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='MuiBox-root css-1j8l0ob']")))
        domains = driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-1j8l0ob']").text
        assert domains == ('coinbase.com\n'
                            'bybit.com\n'
                            'kraken.com\n'
                            'crypto.com\n'
                            'capital.com\n'
                            'binance.com\n'
                            'blockchain.com\n'
                            'metamask.io\n'
                            'bit.com\n'
                            'cex.io\n'
                            'coinlist.co\n'
                            'pancakeswap.finance\n'
                            'coinmarketcap.com')
        # delete case
        #home_button = driver.find_element(By.XPATH, "//a[@class='MuiTypography-root MuiTypography-body1 css-9oncje']")
        #home_button.click()
        #wait.until(ec.visibility_of_element_located((locators.SIDE_MENU_BUTTONS)))
        #side_menu = driver.find_elements(By.XPATH, "//li[@class='MuiListItem-root MuiListItem-gutters css-1j1dt5v']")
        #side_browser = side_menu[1]
        #side_browser.click()
        #wait.until(ec.visibility_of_element_located((locators.DELETE_BUTTON)))
        #delete_button = driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeSmall css-1y8nu6u']")
        #delete_button.click()
        #wait.until(ec.visibility_of_element_located((locators.CONFIRM_DELETE)))
        #confirm_delete = driver.find_element(By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-fullWidth css-m5xjv7']")
        #confirm_delete.click()
        #driver.quit()

        delete_usb_case = DeletePage(driver)
        delete_usb_case.delete_browser_case()

