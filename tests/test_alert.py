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


class TestAlert:

    def test_add_exhibit_alert(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH', "101", FILE[0])

        alerts = Alert(driver)
        alert = alerts.get_alert()
        assert alert == "Exhibit created"

    def test_case_created_alert(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH', "101", FILE[0])
        create_case.add_witness()
        time.sleep(3)
        create_case.create_case_find_crypto('full seed ETH', "101")

        alerts = Alert(driver)
        alert = alerts.get_alert()
        assert alert == "Case created"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_scan_canceled_alert(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH', "101", FILE[0])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH', "101")
        time.sleep(4)

        alerts = Alert(driver)
        alerts.click_cancel_button_on_scan_page()
        alert = alerts.get_alert()
        assert alert == "Scan cancelled"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_scan_started_alert(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH', "101", FILE[0])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH', "101")

        alerts = Alert(driver)
        alerts.click_cancel_button_on_scan_page()
        time.sleep(4)
        alerts.click_start_button_on_scan_page()
        alert = alerts.get_alert()
        assert alert == "Scan started"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_email_has_been_sent_alert(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH', "101", FILE[0])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH', "101")
        time.sleep(4)

        alerts = Alert(driver)
        alerts.send_witness_code()
        alerts.click_back_button()

        alert = alerts.get_alert()
        assert alert == "Email has been sent"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_pin_confirmed_alert(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH', "101", FILE[0])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH', "101")
        time.sleep(4)

        alerts = Alert(driver)
        alerts.send_witness_code()
        time.sleep(4)
        alerts.enter_pin_and_open_case()

        alert = alerts.get_alert()
        assert alert == "Code has been confirmed"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_wrong_pin_confirmed_alert(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH', "101", FILE[0])
        create_case.add_witness()
        create_case.create_case_find_crypto('full seed ETH', "101")
        time.sleep(4)

        alerts = Alert(driver)
        alerts.send_witness_code()
        time.sleep(5)
        alerts.enter_pin_and_open_case('121212')
        alerts.click_back_button()

        alert = alerts.get_alert()
        assert alert == "The code is not valid"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_case_updated_alert(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH', "101", FILE[0])
        create_case.add_witness()
        create_case.create_case_save_case("name before", "1")
        time.sleep(4)
        create_case.open_created_case()
        create_case.create_case_save_case("name after", "1")
        alerts = Alert(driver)
        alert = alerts.get_alert()
        assert alert == "Case updated"

        delete = DeletePage(driver)
        delete.delete_case()

    def test_case_deleted_alert(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH', "101", FILE[0])
        create_case.add_witness()
        create_case.create_case_save_case("name before", "1")
        time.sleep(4)

        delete = DeletePage(driver)
        delete.delete_case()

        alerts = Alert(driver)
        alert = alerts.get_alert()
        assert alert == "Case deleted"

    def test_case_closed_alert(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH', "101", FILE[0])
        create_case.add_witness()
        create_case.create_case_save_case("case closed alert", "1")
        time.sleep(4)
        create_case.click_on_case()
        create_case.click_on_close_open_admin_button()
        alerts = Alert(driver)
        alert = alerts.get_alert()
        assert alert == "Case closed"
        alerts.refresh_page()

        delete = DeletePage(driver)
        delete.delete_case()

    def test_case_opened_alert(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("yura+i@catlabs.io", "12345678")

        create_case = CreatePage(driver)
        create_case.open_case_from_main_page()
        create_case.create_exhibit('full seed ETH', "101", FILE[0])
        create_case.add_witness()
        create_case.create_case_save_case("case opened alert", "1")

        create_case.click_on_case()
        create_case.click_on_close_open_admin_button()
        time.sleep(4)
        create_case.click_on_close_open_admin_button()
        alerts = Alert(driver)
        alert = alerts.get_alert()
        assert alert == "Case opened"
        alerts.refresh_page()

        delete = DeletePage(driver)
        delete.delete_case()

