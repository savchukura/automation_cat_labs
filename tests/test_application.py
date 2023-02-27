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

CASE_NAME = ["test application",
             "test_seed_eth_application"]
FILE = [os.path.abspath("../tests/safari.zip"),
        os.path.abspath("../tests/files/Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe.zip")]

APPLICATION_UPLOAD = [5, 17]


class Test_Create_application_case():

    def test_identify_seed_phrase_in_app_eth(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[1], FILE[1], APPLICATION_UPLOAD[1])

        check_result = ResultPage(driver)
        check_result.open_wallet_address_case(5, 10)

        seed_phrase, private_key, wallet_address, public_key, balance, assets = check_result.check_result_seed_phrase()
        assert seed_phrase == ('Seed Phrase | App\n'
                               'slab wise seat vague tennis section black scare father inmate ostrich follow')
        assert private_key == ('Private Key\n'
                               'e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a')
        assert wallet_address == ('Wallet Address | App\n'
                                  '0x1c805E92F3542794d701fA7134Afe34b08a895c2')
        assert public_key == ('Public Key\n'
                              '03625a51b1447fd8b1e85a3898725a4bd08986e833501cd3f92cf8a29389f45466')
        assert balance == ('Balance\n'
                           '0.00 USD')
        assert assets == ('Assets:\n'
                          '0.000000000000032000 ETH')

        delete_case = DeletePage(driver)
        delete_case.delete_case()

