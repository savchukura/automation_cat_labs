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


FILE = os.path.abspath("../tests/ethereum/CAT-00005-GMTMBOX (1).mbox")


class TestCreateEmailCase:

    def test_identify_email_file_valid_screen(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('Email file .mbox', "101", FILE)
        create_case.add_witness()
        create_case.create_case_find_crypto('Email file .mbox', "101")

        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact_without_parse(8)

        delete = DeletePage(driver)
        delete.delete_case()
