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
        os.path.abspath("../tests/ethereum/Full_seed_eth.png"),
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

