from test_application import *
from test_browser import *
from test_wallet_address import *
from test_emails import *
from test_seed_phrase import *
from test_usb_history import *
from test_dash_board import *
from test_login import *
from test_alert import *
from test_create_case import *


class EthereumTest:

    def test_eth_full_seed_phrase(self):
        test = TestCreateSeedCase()
        test.test_1_create_image_case_eth_full_seed_png(driver)


if __name__ == '__main__':
    print(...)

