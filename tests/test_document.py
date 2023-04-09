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


FILE = [os.path.abspath("../tests/text_doc.txt"),
        os.path.abspath("../tests/files/seed_with_full_phrase.txt"),
        os.path.abspath("../tests/files/seed_phrase_eth.docx"),
        os.path.abspath("../tests/files/seed_phrase_eth.odt"),
        os.path.abspath("../tests/files/seed_phrase_eth.pdf"),
        os.path.abspath("../tests/files/seed_phrase_eth.doc"),
        os.path.abspath("../tests/files/seed_phrase_eth.ppt"),
        os.path.abspath("../tests/files/seed_phrase_eth.xls"),
        os.path.abspath("../tests/files/seed_phrase_eth.xlsx"),

        os.path.abspath("../tests/files/wallet_address_eth.docx"),
        os.path.abspath("../tests/files/wallet_address_eth.odt"),
        os.path.abspath("../tests/files/wallet_address_eth.txt"),
        os.path.abspath("../tests/files/wallet_address_eth.xlsx"),

        os.path.abspath("../tests/files/bitcoin_wallet_with_balance.txt"), ]


class TestCreateDocumentCase:

    def test_create_doc_case_full_seed_txt(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc txt', "101", FILE[1])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc txt', "101")

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

    def test_create_doc_case_full_seed_docx(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc docx', "102", FILE[2])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc docx', "102")

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

    def test_create_doc_case_full_seed_odt(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc odt', "103", FILE[3])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc odt', "103")

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

    def test_create_doc_case_full_seed_pdf(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc pdf', "104", FILE[4])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc pdf', "104")

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

    def test_create_doc_case_full_seed_doc(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc .doc', "105", FILE[5])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc .doc', "105")

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

    def test_create_doc_case_full_seed_ppt(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc .ppt', "106", FILE[6])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc .ppt', "106")

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

    def test_create_doc_case_full_seed_xls(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc .xls', "107", FILE[7])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc .xls', "107")

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

    def test_create_doc_case_full_seed_xlsx(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc .xlsx', "108", FILE[8])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc .xlsx', "108")

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

    def test_create_doc_case_wallet_address_docx(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('wallet address doc .docx', "109", FILE[9])
        create_case.add_witness()
        create_case.create_case_find_crypto('wallet address doc .docx', "109")

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

    def test_create_doc_case_wallet_address_odt(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('wallet address doc .odt', "110", FILE[10])
        create_case.add_witness()
        create_case.create_case_find_crypto('wallet address doc .odt', "110")

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

    def test_create_doc_case_wallet_address_txt(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('wallet address doc .txt', "111", FILE[11])
        create_case.add_witness()
        create_case.create_case_find_crypto('wallet address doc .txt', "111")

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

    def test_create_doc_case_wallet_address_xlsx(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('wallet address doc .xlsx', "112", FILE[12])
        create_case.add_witness()
        create_case.create_case_find_crypto('wallet address doc .xlsx', "112")

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


