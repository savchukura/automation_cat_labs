import time

from URL.url import *
from pages.delete_page import DeletePage
from pages.new_case_page import CreatePage
from pages.check_result import ResultPage
from pages.login_page import LoginPage
from configurate import *
import os


class TestLoginTests:

    def test_login_with_valid_data(self, driver):
        login = LoginPage(driver, URL)
        login.open()
        login.log_in("alex+i@zpoken.io", "12345678")
        time.sleep(5)

    def test_user_leave_login_field_empty(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        login.login_error_empty()
        login_error_empty_field = login.login_error_empty()

        assert login_error_empty_field[0].text == "This field is required"
        assert login_error_empty_field[1].text == "This field is required"

    def test_user_fill_invalid_email(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        login.login_error_invalid_data("alex+i@zpoken.i", "12345678")
        login_error_empty_field = login.get_error()
        assert login_error_empty_field[0].text == "Invalid email address"
        assert login_error_empty_field[1].text == "Invalid password"

    def test_user_fill_invalid_password_one(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        login.login_error_invalid_data("alex+i@zpoken.io", "1234567")
        login_error_empty_field = login.get_error()
        assert login_error_empty_field[0].text == "Invalid email address"
        assert login_error_empty_field[1].text == "Invalid password"

    def test_user_fill_invalid_password_two(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        login.login_error_invalid_data("alex+i@zpoken.io", "123456789")
        login_error_empty_field = login.get_error()
        assert login_error_empty_field[0].text == "Invalid email address"
        assert login_error_empty_field[1].text == "Invalid password"
