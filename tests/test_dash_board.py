from URL.url import *
from pages.delete_page import DeletePage
from pages.new_case_page import CreatePage
from pages.check_result import ResultPage
from pages.login_page import LoginPage
import os
from configurate import *

CASE_NAME = ["test_dashboard_bitcoin_doc",
             "test_dashboard_browser_arch"]
FILE = [os.path.abspath("../tests/files/bitcoin_wallet_with_balance.txt"),
        os.path.abspath("../tests/safari.zip")]
DOCUMENT_UPLOAD = [20, 21]


class Test_Check_dashboard_indicators:

    def test_dashboard_balance_bitcoin_document(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[0], FILE[0], DOCUMENT_UPLOAD[0])

        check_result = ResultPage(driver)
        check_result.open_wallet_address_case(3, 10)
        balance_in_case = check_result.get_data_from_wallet_scan()

        go_to_dashboard = ResultPage(driver)
        go_to_dashboard.go_from_case_to_dashboard()

        files, traces, seed_phrase, wallet_addresses, app, domains, usb_devices, last_update, case_created, balance_in_usd, witness, executor = check_result.check_dashboard()

        assert files == '1'
        assert balance_in_case == balance_in_usd
        assert traces == '1'
        assert seed_phrase == '0'
        assert wallet_addresses == '1'
        assert app == '0'
        assert domains == '0'
        assert usb_devices == '0'

        delete_case = DeletePage(driver)
        delete_case.delete_case()

    def test_dashboard_browser_archive(self, driver):
        login = LoginPage(driver, URL)
        login.open()

        new_case = CreatePage(driver)
        new_case.create_case(CASE_NAME[1], FILE[1], DOCUMENT_UPLOAD[1])

        check_result = ResultPage(driver)
        check_result.check_browser_result_safari()

        go_to_dashboard = ResultPage(driver)
        go_to_dashboard.go_from_case_to_dashboard()

        files, traces, seed_phrase, wallet_addresses, app, domains, usb_devices, last_update, case_created, balance_in_usd, witness, executor = check_result.check_dashboard()

        assert files == '4718'
        assert balance_in_usd == '0'
        assert traces == '1'
        assert seed_phrase == '0'
        assert wallet_addresses == '0'
        assert app == '0'
        assert domains == '26'
        assert usb_devices == '0'

        delete_case = DeletePage(driver)
        delete_case.delete_case()


