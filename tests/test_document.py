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

CASE_NAME = ["test document",
             "test_seed_eth_txt_doc",
             "test_seed_eth_docx_doc",
             "test_seed_eth_odt_doc",
             "test_seed_eth_xlsx_doc",

             "test_wallet_adr_eth_doc_txt",
             "test_wallet_adr_eth_doc_docx",
             "test_wallet_adr_eth_doc_odt",
             "test_wallet_adr_eth_doc_xlsx"]
FILE = [os.path.abspath("../tests/text_doc.txt"),
        os.path.abspath("../tests/files/seed_with_full_phrase.txt"),
        os.path.abspath("../tests/files/seed_phrase_eth.docx"),
        os.path.abspath("../tests/files/seed_phrase_eth.odt"),
        os.path.abspath("../tests/files/seed_phrase_eth.xlsx"),

        os.path.abspath("../tests/files/wallet_address_eth.txt"),
        os.path.abspath("../tests/files/wallet_address_eth.docx"),
        os.path.abspath("../tests/files/wallet_address_eth.odt"),
        os.path.abspath("../tests/files/wallet_address_eth.xlsx")]
DOCUMENT_UPLOAD = [3, 9, 10, 11, 12, 13, 14, 15, 16]

class Test_Create_image_case:

    def test_identify_document_file_txt_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[0], FILE[0], DOCUMENT_UPLOAD[0])

        check_result = ResultPage(driver)
        check_result.check_document_result_with_seed_phrase()

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_full_seed_phrase_etherum_document_file_txt_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[1], FILE[1], DOCUMENT_UPLOAD[1])

        check_result = ResultPage(driver)
        check_result.check_result_with_eth_seed_phrase(3, 10, " Documents")

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_full_seed_phrase_etherum_document_file_docx_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[2], FILE[2], DOCUMENT_UPLOAD[2])

        check_result = ResultPage(driver)
        check_result.check_result_with_eth_seed_phrase(3, 10, " Documents")

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_full_seed_phrase_etherum_document_file_odt_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[3], FILE[3], DOCUMENT_UPLOAD[3])

        check_result = ResultPage(driver)
        check_result.check_result_with_eth_seed_phrase(3, 10, " Documents")

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_full_seed_phrase_etherum_document_file_xlsx_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[4], FILE[4], DOCUMENT_UPLOAD[4])

        check_result = ResultPage(driver)
        check_result.check_result_with_eth_seed_phrase(3, 10, " Documents")

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_wallet_address_ethereum_document_file_txt_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[5], FILE[5], DOCUMENT_UPLOAD[5])

        check_result = ResultPage(driver)
        check_result.check_eth_wallet_address(3, 10, " Documents")

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_wallet_address_ethereum_document_file_docx_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[6], FILE[6], DOCUMENT_UPLOAD[6])

        check_result = ResultPage(driver)
        check_result.check_eth_wallet_address(3, 10, " Documents")

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_wallet_address_ethereum_document_file_odt_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[7], FILE[7], DOCUMENT_UPLOAD[7])

        check_result = ResultPage(driver)
        check_result.check_eth_wallet_address(3, 10, " Documents")

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_wallet_address_ethereum_document_file_xlsx_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[8], FILE[8], DOCUMENT_UPLOAD[8])

        check_result = ResultPage(driver)
        check_result.check_eth_wallet_address(3, 10, " Documents")

        delete_case = DeletePage(driver)
        delete_case.delete_case()
