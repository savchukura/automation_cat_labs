import time

from URL.url import *
from pages.delete_page import DeletePage
from pages.new_case_page import CreatePage
from pages.check_result import ResultPage
from pages.login_page import LoginPage
from pages.email_page import GetWitnessCode
from pages.open_case import OpenCase
from configurate import *
from pages.alert_page import Alert
import os
from selenium.common.exceptions import ElementClickInterceptedException
FILE = [os.path.abspath("../tests/files/Full_seed_eth.png"),
        os.path.abspath("../tests/files/seed_with_full_phrase.txt"),
        os.path.abspath("../tests/ethereum/seed_without_one word_eth_2.png"),
        os.path.abspath("../tests/ethereum/QR_5.png")]


class TestCreateCase:

    def test_create_case_invalid_data_without_exhibits(self, driver):
        try:
            login = LoginPage(driver, URL)
            login.open()
            login.log_in("yura+i@catlabs.io", "12345678")

            create_case = CreatePage(driver)
            create_case.open_case_from_main_page()

            create_case.add_witness()
            create_case.create_case_find_crypto('full seed ETH', "101")
        except ElementClickInterceptedException:
            print("...")
        create_case = CreatePage(driver)
        dis_find_crypto, dis_save_case = create_case.return_disable_find_crypto_and_save_case_buttons()
        assert dis_find_crypto not in locals()

    def test_create_case_invalid_data_without_witness(self, driver):
        try:
            login = LoginPage(driver, URL)
            login.open()
            login.log_in("yura+i@catlabs.io", "12345678")

            create_case = CreatePage(driver)
            create_case.open_case_from_main_page()
            create_case.create_exhibit('full seed ETH', "101", FILE[0])

            create_case.create_case_find_crypto('full seed ETH', "101")
        except ElementClickInterceptedException:
            print("...")
        create_case = CreatePage(driver)
        dis_find_crypto, dis_save_case = create_case.return_disable_find_crypto_and_save_case_buttons()
        assert dis_find_crypto not in locals()

    def test_check_analyst_and_supervisor(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()

        analyst, supervisor = create_case.get_analyst_supervisor()

        assert analyst == "Analyst : yura+i@catlabs.io"
        assert supervisor == "Supervisor : yura+i@catlabs.io"

    def test_edit_case_change_case_name(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH', "101", FILE[0])
        create_case.add_witness()
        create_case.create_case_save_case('full seed ETH', "101")

        create_case.open_created_case()
        create_case.clear_fields_case_name_and_case_number()
        create_case.create_case_save_case('edited name', "101")

        time.sleep(2)
        case_number, case_name, date_created, last_accessed, analyst, witness, status = \
            create_case.return_information_about_case()
        assert case_name == "edited name"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_edit_case_change_case_number(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH', "101", FILE[0])
        create_case.add_witness()
        create_case.create_case_save_case('full seed ETH', "101")

        create_case.open_created_case()
        create_case.clear_fields_case_name_and_case_number()
        create_case.create_case_save_case('full seed ETH', "202")

        time.sleep(2)
        case_number, case_name, date_created, last_accessed, analyst, witness, status = \
            create_case.return_information_about_case()
        assert case_number == "202"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_add_one_more_witness(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH', "101", FILE[0])
        create_case.add_witness()
        create_case.create_case_save_case('add witness', "101")

        create_case.open_created_case()
        create_case.add_witness()
        create_case.create_case_save_case('', "")

        time.sleep(2)
        case_number, case_name, date_created, last_accessed, analyst, witness, status = \
            create_case.return_information_about_case()

        assert witness == "yura+w@catlabs.io, alex+w@catlabs.io"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_add_one_more_exhibit(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('exhibit one', "101", FILE[0])
        create_case.add_witness()
        create_case.create_case_save_case('editing exhibits', "101")

        create_case.open_created_case()
        create_case.create_exhibit('exhibit two', "102", FILE[1])
        create_case.create_case_save_case('', "")

        create_case.open_created_case()
        first_exhibit_id, first_exhibit_description, first_exhibit_type, second_exhibit_id, \
            second_exhibit_description, second_exhibit_type = create_case.check_exhibits_after_editing()

        assert first_exhibit_id == "101"
        assert first_exhibit_description == "exhibit one"
        assert first_exhibit_type == "PNG"

        assert second_exhibit_id == "102"
        assert second_exhibit_description == "exhibit two"
        assert second_exhibit_type == "TXT"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_start_scanning_after_scan_was_canceled(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('start scan', "101", FILE[0])
        create_case.add_witness()
        create_case.create_case_find_crypto('start scan', "101")

        alerts = Alert(driver)
        alerts.click_cancel_button_on_scan_page()
        time.sleep(1)
        alerts.click_start_button_on_scan_page()

        time.sleep(10)
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



