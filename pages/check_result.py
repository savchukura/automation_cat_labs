import time

from selenium.common import NoSuchElementException

from pages.base_page import NextPage
from locators.Main_Page import MainPageLocators as locators



class ResultPage(NextPage):

    def check_image_result_with_seed_phrase(self, tabs_in_case):
        self.elements_are_visible(locators.TABS_IN_CASE)[tabs_in_case].click()
        self.element_is_visible(locators.RESULT).click()
        self.element_is_visible(locators.PURSE_WALLET_BUTTON).click()
        time.sleep(100)
        self.element_is_visible(locators.FETCH_UPDATES_BUTTON).click()
        seed = self.element_is_visible(locators.RESULT_SCANING_SEED)
        another_result = self.elements_are_visible(locators.RESULT_SCANING)
        assets = self.element_is_visible(locators.RESULT_SCANING_ASSETS).text
        assert seed.text == ('Seed phrase:\n'
                             'teach indoor drip tunnel ladder among accident cargo viable license pulp urge')
        assert another_result[0].text == "Wallet Address: 0x3f3cebCb1b485Dab11C2aC9899FFaD8b253D83b0"
        assert another_result[
                   1].text == "Public Key: 02c5e6438944d5a86f83f9adb23bca705c4b1f02164887f8182b044bf933ffa641"
        assert another_result[2].text == "Private Key: 0614b8b234b84a6bc456f9e7edc9baf34c2b1734e89585cafe72fa4d2c5c00f3"
        assert another_result[3].text == "Balance: 2.61 USD"

        assert assets == ('Assets:\n'
                          '3.000000000000000000 MATIC')

    def check_eth_wallet_address(self, tabs_in_case, time_sleep_before_purse, file_type):
        time.sleep(1)
        self.element_is_visible(locators.TABS_IN_CASE[tabs_in_case]).click()
        self.scroll()
        self.element_is_visible(locators.RESULTS_FIELDS).click()
        self.element_is_visible(locators.PURSE_WALLET_BUTTON).click()
        time.sleep(time_sleep_before_purse)
        self.element_is_visible(locators.FETCH_UPDATES_BUTTON).click()
        time.sleep(0.5)
        assets = self.element_is_visible(locators.RESULT_SCANING_ASSETS).text
        another_result = self.elements_are_visible(locators.RESULT_SCANING)

        assert another_result[0].text == ('Wallet Address |' + file_type + '\n'
                                          '0x1c805E92F3542794d701fA7134Afe34b08a895c2')
        assert another_result[1].text == ('Balance\n'
                                          '0.00 USD')
        assert assets == ('Assets:\n'
                          '0.000000000000032000 ETH')

    def check_browser_result_safari(self):
        time.sleep(1)
        self.element_is_visible(locators.TABS_IN_CASE[1]).click()
        self.scroll()
        self.element_is_visible(locators.RESULTS_FIELDS).click()
        domains = self.element_is_visible(locators.HISTORY_DOMAINS)
        assert domains.text == ('www.coinbase.com\n'
                                'www.bybit.com\n'
                                'www.gitkraken.com\n'
                                'url1137.crypto.com\n'
                                'crypto.com\n'
                                'oauth2.crypto.com\n'
                                'capital.com\n'
                                'thecapital.com.ua\n'
                                'www.blockchain.com\n'
                                'metamask.app.link\n'
                                'metamask.io\n'
                                'metamask.zendesk.com\n'
                                'cex.io\n'
                                'www.fragrancex.com\n'
                                'docs.pancakeswap.finance\n'
                                'pancakeswap.finance\n'
                                'hledger.org\n'
                                'coinmarketcap.com\n'
                                'academy.binance.com\n'
                                'accounts.binance.com\n'
                                'www.binance.com\n'
                                'pro.coinlist.co\n'
                                'www.blockchain.com\n'
                                'cex.io\n'
                                'www.fragrancex.com\n'
                                'iancoleman.io')

    def check_email_domain_result_safari(self):
        time.sleep(1)
        self.element_is_visible(locators.TABS_IN_CASE[2]).click()
        self.scroll()
        try:
            pagination = self.element_is_visible(locators.PAGINATION_NEXT)
            if pagination.is_displayed():
                pagination.click()

        except NoSuchElementException:
            print("...")

        time.sleep(1)
        self.element_is_visible(locators.RESULTS_FIELDS).click()
        domains = self.element_is_visible(locators.EMAIL_DOMAINS)
        assert domains.text == ('KuCoin <no-reply@kucoin.com>\n'
                                'Kraken <noreply@kraken.com>\n'
                                '"Binance.US" <hello@binance.us>\n'
                                'MetaMask Team <support@metamask.io>\n'
                                'Bitstamp <noreply@bitstamp.net>'
                                )

    def check_document_result_with_seed_phrase(self):
        self.element_is_visible(locators.TABS_IN_CASE)[3].click()
        self.element_is_visible(locators.RESULT).click()
        self.element_is_visible(locators.PURSE_WALLET_BUTTON).click()
        time.sleep(100)
        self.element_is_visible(locators.FETCH_UPDATES_BUTTON).click()
        seed = self.element_is_visible(locators.RESULT_SCANING_SEED)
        another_result = self.elements_are_visible(locators.RESULT_SCANING)
        assets = self.element_is_visible(locators.RESULT_SCANING_ASSETS).text
        assert seed.text == ('Seed phrase:\n'
                             'teach indoor drip tunnel ladder among accident cargo viable license pulp urge')
        assert another_result[0].text == "Wallet Address: 0x3f3cebCb1b485Dab11C2aC9899FFaD8b253D83b0"
        assert another_result[
                   1].text == "Public Key: 02c5e6438944d5a86f83f9adb23bca705c4b1f02164887f8182b044bf933ffa641"
        assert another_result[2].text == "Private Key: 0614b8b234b84a6bc456f9e7edc9baf34c2b1734e89585cafe72fa4d2c5c00f3"
        assert another_result[3].text == "Balance: 2.61 USD"

        assert assets == ('Assets:\n'
                          '3.000000000000000000 MATIC')

    def check_usb_history_result(self):
        time.sleep(1)
        self.element_is_visible(locators.TABS_IN_CASE[4]).click()
        self.scroll()
        self.element_is_visible(locators.RESULTS_FIELDS).click()
        usb_history = self.elements_are_visible(locators.USB_RESULTS)
        assert usb_history[0].text == 'USB Device | USB History'
        assert usb_history[1].text == ('VID(0x)\n'
                                       '2b24')
        assert usb_history[2].text == ('Vendor Name\n'
                                       'KeepKey')
        assert usb_history[3].text == ('PID(0x)\n'
                                       '*')
        assert usb_history[4].text == ('Device Description\n'
                                       'Bitcoin Wallet')

    def check_result_with_eth_seed_phrase(self, tabs_in_case, time_sleep_before_purse, file_type):
        time.sleep(1)
        self.element_is_visible(locators.TABS_IN_CASE[tabs_in_case]).click()

        self.scroll()
        self.element_is_visible(locators.RESULTS_FIELDS).click()
        self.element_is_visible(locators.PURSE_WALLET_BUTTON).click()
        time.sleep(time_sleep_before_purse)
        self.element_is_visible(locators.FETCH_UPDATES_BUTTON).click()
        assets = self.element_is_visible(locators.RESULT_SCANING_ASSETS).text
        another_result = self.elements_are_visible(locators.RESULT_SCANING)
        assert another_result[0].text == ('Seed Phrase |' + file_type + '\n'
                                          'slab wise seat vague tennis section black scare father inmate ostrich follow')
        assert another_result[1].text == ('Private Key\n'
                                          'e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a')
        assert another_result[2].text == ('Wallet Address |' + file_type + '\n'
                                          '0x1c805E92F3542794d701fA7134Afe34b08a895c2')
        assert another_result[3].text == ('Public Key\n'
                                          '03625a51b1447fd8b1e85a3898725a4bd08986e833501cd3f92cf8a29389f45466')
        assert another_result[4].text == ('Balance\n'
                                          '0.00 USD')
        assert assets == ('Assets:\n'
                          '0.000000000000032000 ETH')
