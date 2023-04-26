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


FILE =[os.path.abspath("../tests/files/USBSTOR.reg"),
       os.path.abspath("../tests/files/2_USB.zip")]


class TestUSBCase:

    def test_1_identify_usb_file(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('USB file .reg', "101", FILE[0])
        create_case.add_witness()
        create_case.create_case_find_crypto('USB file .reg', "101")

        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact_without_parse(2)

        delete = DeletePage(driver)
        delete.delete_case()

    def test_2_identify_two_usb_file(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('USB file .reg', "101", FILE[1])
        create_case.add_witness()
        create_case.create_case_find_crypto('USB file .reg', "101")

        open_case = OpenCase(driver)
        open_case.open_case_with_witness()
        open_case.open_artifact_without_parse(2)

        delete = DeletePage(driver)
        delete.delete_case()
