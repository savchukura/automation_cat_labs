from test_application import *
from test_browser import *
from test_document import *
from test_emails import *
from test_Image import *
from test_usb_history import *
from test_dash_board import *


class EthereumTest:
    def test_eth_full_seed_phrase(self):
        test = Test_Create_image_case()
        test.test_identify_image_file_ethereum_valid_screen(driver)

    def test_application(self):
        test = Test_Create_application_case()



if __name__ == '__main__':
    print(...)

