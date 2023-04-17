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

CASE_NAME = ["test image",
             "test_image_eth_full",
             "test_image_eth_part",
             "test_qr_eth_wallet"]

FILE = [os.path.abspath("../tests/valid_screen_one.png"),
        os.path.abspath("../tests/ethereum/Full_seed_eth.png"),
        os.path.abspath("../tests/ethereum/seed_without_one word_eth_2.png"),
        os.path.abspath("../tests/ethereum/QR_5.png"),
        os.path.abspath("../tests/ethereum/Full_seed_eth.gif"),
        os.path.abspath("../tests/ethereum/Full_seed_eth.jpg"),
        os.path.abspath("../tests/ethereum/Seed phrase img.png")]


IMAGE_UPLOAD = 0
FULL_ETH_IMAGE_UPLOUD = 6
PART_ETH_IMAGE_UPLOUD = 7
QR_ETH_IMAGE_UPLOUD = 8
TABS_IN_CASE = 0


class TestCreateImageCase:

    def test_create_image_case_eth_full_seed_png(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH .png', "101", FILE[1])
        create_case.add_witness()
        create_case.create_case_find_crypto('image full seed ETH .png', "101")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(0)
        time.sleep(5)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.00 USD Value"
        assert assets == "0.000000000000032000 ETH" or '0.0 ETH'

        delete = DeletePage(driver)
        delete.delete_case()

    def test_create_image_case_eth_full_seed_png_two(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH .png', "101", FILE[6])
        create_case.add_witness()
        create_case.create_case_find_crypto('image full seed ETH .png', "101")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(0)
        time.sleep(5)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.00 USD Value"
        assert assets == "0.000000000000032000 ETH" or '0.0 ETH'

        delete = DeletePage(driver)
        delete.delete_case()

    def test_create_image_case_eth_part_seed_png(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('part seed ETH image png', "102", FILE[2])
        create_case.add_witness()
        create_case.create_case_find_crypto('part seed ETH image png', "101")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(0)
        time.sleep(55)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.00 USD Value"
        assert assets == "0.000000000000032000 ETH" or '0.0 ETH'

        delete = DeletePage(driver)
        delete.delete_case()

    def test_create_image_case_qr_code_with_address(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('wallet address in QR', "103", FILE[3])
        create_case.add_witness()
        create_case.create_case_find_crypto('wallet address in QR', "103")
        time.sleep(10)
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

    def test_create_image_case_eth_full_seed_gif(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH .gif', "104", FILE[4])
        create_case.add_witness()
        create_case.create_case_find_crypto('image full seed ETH .gif', "104")
        time.sleep(10)
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

    def test_create_image_case_eth_full_seed_jpg(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH .jpg', "105", FILE[5])
        create_case.add_witness()
        create_case.create_case_find_crypto('image full seed ETH .jpg', "105")
        time.sleep(10)
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
