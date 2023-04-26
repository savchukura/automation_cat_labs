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


FILE = [os.path.abspath("../tests/safari.zip"),
        os.path.abspath("../tests/files/Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe.zip"),
        os.path.abspath("../tests/files/exodus-macos-arm64-22.12.5.dmg")]


class TestCreateApplicationCase:

    def test_identify_seed_phrase_in_app_eth(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH application', "101", FILE[1])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH application', "101")

        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact(0)
        time.sleep(15)
        seed_phrase, wallet_address, private_key, balance, assets = open_case.check_parse_result_seed()
        assert seed_phrase == "slab wise seat vague tennis section black scare father inmate ostrich follow"
        assert wallet_address == "0x1c805E92F3542794d701fA7134Afe34b08a895c2"
        assert private_key == "e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a"
        assert balance == "0.34 USD Value" or balance >= "0"
        assert assets == "0.000162442392777000 ETH" or assets >= "0"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_dmg_file(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('exoduc macoc .dmg', "102", FILE[2])
        create_case.add_witness()
        create_case.create_case_find_crypto('exoduc macoc .dmg', "102")

        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact_without_parse(0)

        delete = DeletePage(driver)
        delete.delete_case()

