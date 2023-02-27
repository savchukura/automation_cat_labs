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

CASE_NAME = "test browser"
FILE = os.path.abspath("../tests/safari.zip")
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
        delete_case.delete_case()
