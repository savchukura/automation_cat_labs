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

CASE_NAME = "test document"
FILE = "C:/Users/WellDone/PycharmProjects/automation_cat_labs/tests/text_doc.txt"
DOCUMENT_UPLOAD = 3

class Test_Create_image_case:

    def test_identify_document_file_txt_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME, FILE, DOCUMENT_UPLOAD)

        check_result = ResultPage(driver)
        check_result.check_document_result_with_seed_phrase()

        delete_case = DeletePage(driver)
        delete_case.delete_document_case()
