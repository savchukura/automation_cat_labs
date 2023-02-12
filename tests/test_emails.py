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
import os

CASE_NAME = "test email"
FILE = os.path.abspath("../tests/ethereum/CAT-00005-GMTMBOX (1).mbox")
IMAGE_UPLOAD = 2
TABS_IN_CASE = 2

class Test_Create_email_case:

    def test_identify_email_file_valid_screen(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME, FILE, IMAGE_UPLOAD)

        check_result = ResultPage(driver)
        check_result.check_email_domain_result_safari()

        delete_case = DeletePage(driver)
        delete_case.delete_case()
