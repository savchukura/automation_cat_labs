import time

from URL.url import *
from pages.delete_page import DeletePage
from pages.new_case_page import CreatePage
from pages.check_result import ResultPage
from pages.login_page import LoginPage
from pages.email_page import GetWitnessCode
from pages.open_case import OpenCase
from configurate import *
import os


FILE = [os.path.abspath("../tests/files/Full_seed_eth.png"),
        os.path.abspath("../tests/ethereum/wallet_address_eth.txt"),
        os.path.abspath("../tests/ethereum/seed_without_one word_eth_2.png"),
        os.path.abspath("../tests/ethereum/QR_5.png")]


class TestNewCases:

    def test_get_witnesses_code(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        get_code = GetWitnessCode(driver)
        get_code.get_witness_code()
        security_code = get_code
        print(security_code)

        time.sleep(5)

    def test_create_image_case(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH', "101", FILE[0])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH', "101")

        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(0)
        time.sleep(15)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.00 USD Value"
        assert assets == "0.000000000000032000 ETH" or '0.0 ETH'

        delete = DeletePage(driver)
        delete.delete_case()

    def test_create_doc_case(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc', "102", FILE[1])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc', "102")

        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(3)
        time.sleep(15)
        wallet_address, balance, assets = open_case.check_parse_result_wallet_address()

        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert balance == "0.00 USD Value"
        assert assets == "0.000000000000032000 ETH" or '0.0 ETH'

        delete = DeletePage(driver)
        delete.delete_case()



