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

FILE_ETH = [
        os.path.abspath("../tests/files/wallet_addresses/wallet_address_eth.docx"),
        os.path.abspath("../tests/files/wallet_addresses/wallet_address_eth.jpeg"),
        os.path.abspath("../tests/files/wallet_addresses/wallet_address_eth.jpg"),
        os.path.abspath("../tests/files/wallet_addresses/wallet_address_eth.odt"),
        os.path.abspath("../tests/files/wallet_addresses/wallet_address_eth.png"),
        os.path.abspath("../tests/files/wallet_addresses/wallet_address_eth.txt"),
        os.path.abspath("../tests/files/wallet_addresses/wallet_address_eth.xlsx"),
        os.path.abspath("../tests/files/wallet_addresses/wallet_address_qr_eth.png"),


        os.path.abspath("../tests/files/bitcoin_wallet_with_balance.txt"), ]


class TestWalletAddressCase:

    def test_0_create_doc_case_wallet_address_docx(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('wallet address doc .docx', "101", FILE_ETH[0])
        create_case.add_witness()
        create_case.create_case_find_crypto('wallet address doc .docx', "101")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(1)
        time.sleep(15)
        wallet_address, balance, assets = open_case.check_parse_result_wallet_address()

        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_1_create_doc_case_wallet_address_jpeg(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('wallet address doc .jpeg', "101", FILE_ETH[1])
        create_case.add_witness()
        create_case.create_case_find_crypto('wallet address doc .jpeg', "101")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(1)
        time.sleep(15)
        wallet_address, balance, assets = open_case.check_parse_result_wallet_address()

        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_2_create_doc_case_wallet_address_jpg(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('wallet address doc .jpg', "102", FILE_ETH[2])
        create_case.add_witness()
        create_case.create_case_find_crypto('wallet address doc .jpg', "102")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(1)
        time.sleep(15)
        wallet_address, balance, assets = open_case.check_parse_result_wallet_address()

        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_3_create_doc_case_wallet_address_odt(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('wallet address doc .odt', "103", FILE_ETH[3])
        create_case.add_witness()
        create_case.create_case_find_crypto('wallet address doc .odt', "103")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(1)
        time.sleep(15)
        wallet_address, balance, assets = open_case.check_parse_result_wallet_address()

        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_4_create_doc_case_wallet_address_png(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('wallet address doc .png', "104", FILE_ETH[4])
        create_case.add_witness()
        create_case.create_case_find_crypto('wallet address doc .png', "104")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(1)
        time.sleep(15)
        wallet_address, balance, assets = open_case.check_parse_result_wallet_address()

        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_5_create_doc_case_wallet_address_txt(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('wallet address doc .txt', "105", FILE_ETH[5])
        create_case.add_witness()
        create_case.create_case_find_crypto('wallet address doc .txt', "105")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(1)
        time.sleep(15)
        wallet_address, balance, assets = open_case.check_parse_result_wallet_address()

        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_6_create_doc_case_wallet_address_xlsx(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('wallet address doc .xlsx', "106", FILE_ETH[6])
        create_case.add_witness()
        create_case.create_case_find_crypto('wallet address doc .xlsx', "106")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(1)
        time.sleep(15)
        wallet_address, balance, assets = open_case.check_parse_result_wallet_address()

        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_7_create_doc_case_wallet_address_qr_png(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('wallet address qr .png', "107", FILE_ETH[7])
        create_case.add_witness()
        create_case.create_case_find_crypto('wallet address qr .png', "107")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(1)
        time.sleep(15)
        wallet_address, balance, assets = open_case.check_parse_result_wallet_address()

        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()