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
             "test_wallet_adr_eth_doc_xlsx",
             "test_wallet_adr_bit_doc_txt"]
FILE = [os.path.abspath("../tests/text_doc.txt"),
        os.path.abspath("../tests/files/seed_with_full_phrase.txt"),
        os.path.abspath("../tests/files/seed_phrase_eth.docx"),
        os.path.abspath("../tests/files/seed_phrase_eth.odt"),
        os.path.abspath("../tests/files/seed_phrase_eth.xlsx"),

        os.path.abspath("../tests/files/wallet_address_eth.txt"),
        os.path.abspath("../tests/files/wallet_address_eth.docx"),
        os.path.abspath("../tests/files/wallet_address_eth.odt"),
        os.path.abspath("../tests/files/wallet_address_eth.xlsx"),
        os.path.abspath("../tests/files/bitcoin_wallet_with_balance.txt"), ]
DOCUMENT_UPLOAD = [3, 9, 10, 11, 12, 13, 14, 15, 16, 18]


class Test_Create_document_case:

    def test_identify_full_seed_phrase_ethereum_document_file_txt_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[1], FILE[1], DOCUMENT_UPLOAD[1])

        check_result = ResultPage(driver)
        check_result.open_wallet_address_case(3, 10)

        seed_phrase, private_key, wallet_address, public_key, balance, assets = check_result.check_result_seed_phrase()
        assert seed_phrase == ('Seed Phrase | Documents\n'
                               'slab wise seat vague tennis section black scare father inmate ostrich follow')
        assert private_key == ('Private Key\n'
                               'e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a')
        assert wallet_address == ('Wallet Address | Documents\n'
                                  '0x1c805E92F3542794d701fA7134Afe34b08a895c2')
        assert public_key == ('Public Key\n'
                              '03625a51b1447fd8b1e85a3898725a4bd08986e833501cd3f92cf8a29389f45466')
        assert balance == ('Balance\n'
                           '0.00 USD')
        assert assets == ('Assets:\n'
                          '0.000000000000032000 ETH')

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_full_seed_phrase_ethereum_document_file_docx_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[2], FILE[2], DOCUMENT_UPLOAD[2])

        check_result = ResultPage(driver)
        check_result.open_wallet_address_case(3, 10)

        seed_phrase, private_key, wallet_address, public_key, balance, assets = check_result.check_result_seed_phrase()
        assert seed_phrase == ('Seed Phrase | Documents\n'
                               'slab wise seat vague tennis section black scare father inmate ostrich follow')
        assert private_key == ('Private Key\n'
                               'e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a')
        assert wallet_address == ('Wallet Address | Documents\n'
                                  '0x1c805E92F3542794d701fA7134Afe34b08a895c2')
        assert public_key == ('Public Key\n'
                              '03625a51b1447fd8b1e85a3898725a4bd08986e833501cd3f92cf8a29389f45466')
        assert balance == ('Balance\n'
                           '0.00 USD')
        assert assets == ('Assets:\n'
                          '0.000000000000032000 ETH')

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_full_seed_phrase_ethereum_document_file_odt_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[3], FILE[3], DOCUMENT_UPLOAD[3])

        check_result = ResultPage(driver)
        check_result.open_wallet_address_case(3, 10)

        seed_phrase, private_key, wallet_address, public_key, balance, assets = check_result.check_result_seed_phrase()
        assert seed_phrase == ('Seed Phrase | Documents\n'
                               'slab wise seat vague tennis section black scare father inmate ostrich follow')
        assert private_key == ('Private Key\n'
                               'e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a')
        assert wallet_address == ('Wallet Address | Documents\n'
                                  '0x1c805E92F3542794d701fA7134Afe34b08a895c2')
        assert public_key == ('Public Key\n'
                              '03625a51b1447fd8b1e85a3898725a4bd08986e833501cd3f92cf8a29389f45466')
        assert balance == ('Balance\n'
                           '0.00 USD')
        assert assets == ('Assets:\n'
                          '0.000000000000032000 ETH')

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_full_seed_phrase_ethereum_document_file_xlsx_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[4], FILE[4], DOCUMENT_UPLOAD[4])

        check_result = ResultPage(driver)
        check_result.open_wallet_address_case(3, 10)

        seed_phrase, private_key, wallet_address, public_key, balance, assets = check_result.check_result_seed_phrase()
        assert seed_phrase == ('Seed Phrase | Documents\n'
                               'slab wise seat vague tennis section black scare father inmate ostrich follow')
        assert private_key == ('Private Key\n'
                               'e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a')
        assert wallet_address == ('Wallet Address | Documents\n'
                                  '0x1c805E92F3542794d701fA7134Afe34b08a895c2')
        assert public_key == ('Public Key\n'
                              '03625a51b1447fd8b1e85a3898725a4bd08986e833501cd3f92cf8a29389f45466')
        assert balance == ('Balance\n'
                           '0.00 USD')
        assert assets == ('Assets:\n'
                          '0.000000000000032000 ETH')

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_wallet_address_ethereum_document_file_txt_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[5], FILE[5], DOCUMENT_UPLOAD[5])

        check_result = ResultPage(driver)
        check_result.open_wallet_address_case(3, 13)
        assets, wallet_address, balance = check_result.check_result_wallet_address()

        assert wallet_address == ('Wallet Address | Documents\n'
                                  '0x1c805E92F3542794d701fA7134Afe34b08a895c2')
        assert balance == ('Balance\n'
                           '0.00 USD')
        assert assets == ('Assets:\n'
                          '0.000000000000032000 ETH')

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_wallet_address_ethereum_document_file_docx_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[6], FILE[6], DOCUMENT_UPLOAD[6])

        check_result = ResultPage(driver)
        check_result.open_wallet_address_case(3, 13)
        assets, wallet_address, balance = check_result.check_result_wallet_address()

        assert wallet_address == ('Wallet Address | Documents\n'
                                  '0x1c805E92F3542794d701fA7134Afe34b08a895c2')
        assert balance == ('Balance\n'
                           '0.00 USD')
        assert assets == ('Assets:\n'
                          '0.000000000000032000 ETH')

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_wallet_address_ethereum_document_file_odt_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[7], FILE[7], DOCUMENT_UPLOAD[7])

        check_result = ResultPage(driver)
        check_result.open_wallet_address_case(3, 13)
        assets, wallet_address, balance = check_result.check_result_wallet_address()

        assert wallet_address == ('Wallet Address | Documents\n'
                                  '0x1c805E92F3542794d701fA7134Afe34b08a895c2')
        assert balance == ('Balance\n'
                           '0.00 USD')
        assert assets == ('Assets:\n'
                          '0.000000000000032000 ETH')

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_wallet_address_ethereum_document_file_xlsx_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[8], FILE[8], DOCUMENT_UPLOAD[8])

        check_result = ResultPage(driver)
        check_result.open_wallet_address_case(3, 13)
        assets, wallet_address, balance = check_result.check_result_wallet_address()

        assert wallet_address == ('Wallet Address | Documents\n'
                                  '0x1c805E92F3542794d701fA7134Afe34b08a895c2')
        assert balance == ('Balance\n'
                           '0.00 USD')
        assert assets == ('Assets:\n'
                          '0.000000000000032000 ETH')

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_check_bitcoin_wallet_address(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[9], FILE[9], DOCUMENT_UPLOAD[9])

        check_result = ResultPage(driver)
        check_result.open_wallet_address_case(3, 10)
        assets, wallet_address, balance = check_result.check_result_wallet_address()

        assert wallet_address == ('Wallet Address | Documents\n'
                                  '1MewpRkpcbFdqamPPYc1bXa9AJ189Succy')
        assert balance == ('Balance\n'
                           '1784333333.33 USD')
        assert assets == ('Assets:\n'
                          '83333.333333333328482695 BTC')

        delete_case = DeletePage(driver)
        delete_case.delete_case()
