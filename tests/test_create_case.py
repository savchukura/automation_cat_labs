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
FILE = [os.path.abspath("../tests/files/Full_seed_eth.png"),
        os.path.abspath("../tests/ethereum/Full_seed_eth.png"),
        os.path.abspath("../tests/ethereum/seed_without_one word_eth_2.png"),
        os.path.abspath("../tests/ethereum/QR_5.png")]


class TestCreateCase:

    def test_check_analyst_and_supervisor(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()

        analyst, supervisor = create_case.get_analyst_supervisor()

        assert analyst == ""
        assert supervisor == ""

