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

CASE_NAME = "test browser"
FILE = os.path.abspath("../tests/safari.zip")
BROWSER_UPLOAD = 1


class TestCreateBrowserCase:

    def test_identify_browser_file_safari_valid(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('Safari Domains', "101", FILE)
        time.sleep(50)
        create_case.add_witness()
        create_case.create_case_find_crypto('Safari Domains', "101")

        open_case = OpenCase(driver)
        open_case.check_presents_of_domains()

        delete = DeletePage(driver)
        delete.delete_case()
