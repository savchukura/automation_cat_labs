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

CASE_NAME = ["test image",
             "test_image_eth_full",
             "test_image_eth_part",
             "test_qr_eth_wallet"]

FILE = [os.path.abspath("../tests/valid_screen_one.png"),
        os.path.abspath("../tests/ethereum/Full_seed_eth.png"),
        os.path.abspath("../tests/ethereum/seed_without_one word_eth_2.png"),
        os.path.abspath("../tests/ethereum/QR_5.png")]


IMAGE_UPLOAD = 0
FULL_ETH_IMAGE_UPLOUD = 6
PART_ETH_IMAGE_UPLOUD = 7
QR_ETH_IMAGE_UPLOUD = 8
TABS_IN_CASE = 0


class Test_Create_image_case():

    def test_identify_image_file_matic_valid_screen(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_image_case = CreatePage(driver)
        new_image_case.create_case(CASE_NAME[0], FILE[1], IMAGE_UPLOAD)

        check_result = ResultPage(driver)
        check_result.open_wallet_address_case(0, 10)

        seed_phrase, private_key, wallet_address, public_key, balance, assets = check_result.check_result_seed_phrase()
        assert seed_phrase == ('Seed Phrase | Images\n'
                               'slab wise seat vague tennis section black scare father inmate ostrich follow')
        assert private_key == ('Private Key\n'
                               'e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a')
        assert wallet_address == ('Wallet Address | Images\n'
                                  '0x1c805E92F3542794d701fA7134Afe34b08a895c2')
        assert public_key == ('Public Key\n'
                              '03625a51b1447fd8b1e85a3898725a4bd08986e833501cd3f92cf8a29389f45466')
        assert balance == ('Balance\n'
                           '0.00 USD')
        assert assets == ('Assets:\n'
                          '0.000000000000032000 ETH')

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_image_file_ethereum_valid_screen(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[1], FILE[1], FULL_ETH_IMAGE_UPLOUD)

        check_result = ResultPage(driver)
        check_result.open_wallet_address_case(0, 10)

        seed_phrase, private_key, wallet_address, public_key, balance, assets = check_result.check_result_seed_phrase()
        assert seed_phrase == ('Seed Phrase | Images\n'
                               'slab wise seat vague tennis section black scare father inmate ostrich follow')
        assert private_key == ('Private Key\n'
                               'e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a')
        assert wallet_address == ('Wallet Address | Images\n'
                                  '0x1c805E92F3542794d701fA7134Afe34b08a895c2')
        assert public_key == ('Public Key\n'
                              '03625a51b1447fd8b1e85a3898725a4bd08986e833501cd3f92cf8a29389f45466')
        assert balance == ('Balance\n'
                           '0.00 USD')
        assert assets == ('Assets:\n'
                          '0.000000000000032000 ETH')

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_image_file_with_part_phrase_ethereum_valid_screen(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[2], FILE[2], PART_ETH_IMAGE_UPLOUD)

        check_result = ResultPage(driver)
        check_result.open_wallet_address_case(0, 80)

        seed_phrase, private_key, wallet_address, public_key, balance, assets = check_result.check_result_seed_phrase()
        assert seed_phrase == ('Seed Phrase | Images\n'
                               'slab wise seat vague tennis section black scare father inmate ostrich follow')
        assert private_key == ('Private Key\n'
                               'e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a')
        assert wallet_address == ('Wallet Address | Images\n'
                                  '0x1c805E92F3542794d701fA7134Afe34b08a895c2')
        assert public_key == ('Public Key\n'
                              '03625a51b1447fd8b1e85a3898725a4bd08986e833501cd3f92cf8a29389f45466')
        assert balance == ('Balance\n'
                           '0.00 USD')
        assert assets == ('Assets:\n'
                          '0.000000000000032000 ETH')

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_qr_image_file_with_wallet_address_ethereum_valid_screen(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[3], FILE[3], QR_ETH_IMAGE_UPLOUD)

        check_result = ResultPage(driver)
        check_result.open_wallet_address_case(0, 20)
        assets, wallet_address, balance = check_result.check_result_wallet_address()

        assert wallet_address == ('Wallet Address | Images\n'
                                  '0x1c805E92F3542794d701fA7134Afe34b08a895c2')
        assert balance == ('Balance\n'
                           '0.00 USD')
        assert assets == ('Assets:\n'
                          '0.000000000000032000 ETH')

        delete_case = DeletePage(driver)
        delete_case.delete_case()


