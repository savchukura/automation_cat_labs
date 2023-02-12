from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators.Main_Page import MainPageLocators as locators
from URL.url import *
from pages.delete_page import DeletePage
from pages.new_case_page import CreatePage
from pages.check_result import ResultPage
from pages.login_page import LoginPage
from configurate import *
import os

CASE_NAME = ["test image",
             "test_image_eth_full",
             "test_image_eth_part",
             "test_qr_eth_wallet"]

FILE = [os.path.abspath("../tests/valid_screen_one.png"),
        os.path.abspath("../tests/ethereum/Full_seed_eth.png"),
        os.path.abspath("../tests/ethereum/seed_without_one word_eth_2.png"),
        os.path.abspath("../tests/ethereum/QR_5.png")]


IMAGE_UPLOAD = 0
FULL_ETH_IMAGE_UPLOUD = 6
PART_ETH_IMAGE_UPLOUD = 7
QR_ETH_IMAGE_UPLOUD = 8
TABS_IN_CASE = 0

class Test_Create_image_case():

    def test_identify_image_file_matic_valid_screen(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_image_case = CreatePage(driver)
        new_image_case.create_case(CASE_NAME[0], FILE[0], IMAGE_UPLOAD)

        check_image_result = ResultPage(driver)
        check_image_result.check_image_result_with_seed_phrase(TABS_IN_CASE)

        delete_usb_case = DeletePage(driver)
        delete_usb_case.delete_case()

    def test_identify_image_file_ethereum_valid_screen(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[1], FILE[1], FULL_ETH_IMAGE_UPLOUD)

        check_result = ResultPage(driver)
        check_result.check_result_with_eth_seed_phrase(0, 10, ' Images')

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_image_file_with_part_phrase_ethereum_valid_screen(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[2], FILE[2], PART_ETH_IMAGE_UPLOUD)

        check_result = ResultPage(driver)
        check_result.check_result_with_eth_seed_phrase(0, 25, ' Images')

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_identify_qr_image_file_with_wallet_address_ethereum_valid_screen(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[3], FILE[3], QR_ETH_IMAGE_UPLOUD)

        check_result = ResultPage(driver)
        check_result.check_eth_wallet_address(0, 16, " Images")

        delete_case = DeletePage(driver)
        delete_case.delete_case()


