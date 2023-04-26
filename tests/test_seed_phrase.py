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
        os.path.abspath("../tests/ethereum/Full_seed_eth.jpg"),
        os.path.abspath("../tests/ethereum/Full_seed_eth.jpeg"),
        os.path.abspath("../tests/ethereum/Full_Seed_QR_eth.png"),
        os.path.abspath("../tests/ethereum/Full_Seed_QR_eth.jpg"),
        os.path.abspath("../tests/ethereum/Full_Seed_QR_eth.jpeg"),
        os.path.abspath("../tests/ethereum/seed_without_one word_eth_2.png"),
        os.path.abspath("../tests/files/seed_with_full_phrase.txt"),
        os.path.abspath("../tests/files/seed_phrase_eth.docx"),
        os.path.abspath("../tests/files/seed_phrase_eth.odt"),
        os.path.abspath("../tests/files/seed_phrase_eth.pdf"),
        os.path.abspath("files/seed_phrase_eth.docx"),
        os.path.abspath("../tests/files/seed_phrase_eth.ppt"),
        os.path.abspath("../tests/files/seed_phrase_eth.xls"),
        os.path.abspath("../tests/files/seed_phrase_eth.xlsx"),

        os.path.abspath("../tests/ethereum/QR_5.png"),
        os.path.abspath("../tests/ethereum/Full_seed_eth.gif"),

        os.path.abspath("../tests/ethereum/Seed phrase img.png"),
        os.path.abspath("../tests/ethereum/seed phrase part last.png")]


class TestCreateSeedCase:

    def test_1_create_image_case_eth_full_seed_png(self, driver):
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
        open_case.open_artifact(3)
        time.sleep(5)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_2_create_image_case_eth_full_seed_jpg(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH .jpg', "102", FILE[2])
        create_case.add_witness()
        create_case.create_case_find_crypto('image full seed ETH .jpg', "102")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(3)
        time.sleep(5)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_3_create_image_case_eth_full_seed_jpeg(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH .jpeg', "103", FILE[3])
        create_case.add_witness()
        create_case.create_case_find_crypto('image full seed ETH .jpeg', "103")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(3)
        time.sleep(5)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_4_create_image_case_eth_full_seed_qr_png(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed QR ETH .png', "104", FILE[4])
        create_case.add_witness()
        create_case.create_case_find_crypto('image full seed QR ETH .png', "104")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(3)
        time.sleep(5)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_5_create_image_case_eth_full_seed_qr_jpg(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed QR ETH .jpg', "105", FILE[5])
        create_case.add_witness()
        create_case.create_case_find_crypto('image full seed QR ETH .jpg', "105")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(3)
        time.sleep(5)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_6_create_image_case_eth_full_seed_qr_jpeg(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed QR ETH .jpeg', "106", FILE[6])
        create_case.add_witness()
        create_case.create_case_find_crypto('image full seed QR ETH .jpeg', "106")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(3)
        time.sleep(5)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_7_create_image_case_eth_part_seed_qr_png(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('image part seed  ETH .png', "107", FILE[7])
        create_case.add_witness()
        create_case.create_case_find_crypto('image part seed  ETH .png', "107")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(3)
        time.sleep(50)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_8_create_doc_case_full_seed_txt(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc txt', "108", FILE[8])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc txt', "108")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(3)
        time.sleep(15)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_9_create_doc_case_full_seed_docx(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc docx', "109", FILE[9])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc docx', "109")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(3)
        time.sleep(15)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_10_create_doc_case_full_seed_odt(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc odt', "110", FILE[10])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc txt', "110")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(3)
        time.sleep(15)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_11_create_doc_case_full_seed_pdf(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc pdf', "11", FILE[11])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc pdf', "111")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(3)
        time.sleep(15)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_12_create_doc_case_full_seed_docx(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc docx', "12", FILE[12])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc docx', "112")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(3)
        time.sleep(15)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_13_create_doc_case_full_seed_ppt(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc ppt', "13", FILE[13])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc ppt', "113")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(3)
        time.sleep(15)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_14_create_doc_case_full_seed_xls(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc xls', "14", FILE[14])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc xls', "114")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(3)
        time.sleep(15)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_15_create_doc_case_full_seed_xlsx(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH doc xlsx', "15", FILE[15])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH doc xlsx', "115")
        time.sleep(10)
        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(3)
        time.sleep(15)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()
