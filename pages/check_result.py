import time

from selenium.common import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from pages.base_page import NextPage
from locators.Main_Page import MainPageLocators as locators



class ResultPage(NextPage):

    def open_wallet_address_case(self, tabs_in_case, time_sleep_before_purse=0):
        time.sleep(1)
        self.element_is_visible(locators.TABS_IN_CASE[tabs_in_case]).click()
        self.scroll()
        self.element_is_visible(locators.RESULTS_FIELDS).click()
        self.element_is_visible(locators.PURSE_WALLET_BUTTON).click()
        time.sleep(time_sleep_before_purse)
        self.element_is_visible(locators.FETCH_UPDATES_BUTTON).click()
        time.sleep(1)

    def open_domain_case(self, tabs_in_case):
        time.sleep(1)
        self.element_is_visible(locators.TABS_IN_CASE[tabs_in_case]).click()
        self.scroll()
        self.element_is_visible(locators.RESULTS_FIELDS).click()
        time.sleep(0.5)

    def check_result_wallet_address(self):
        assets = self.element_is_visible(locators.RESULT_SCANING_ASSETS).text
        another_result = self.elements_are_visible(locators.RESULT_SCANING)
        wallet_address = another_result[0].text
        balance = another_result[1].text

        return assets, wallet_address, balance

    def check_result_seed_phrase(self):
        another_result = self.elements_are_visible(locators.RESULT_SCANING)
        seed_phrase = another_result[0].text
        private_key = another_result[1].text
        wallet_address = another_result[2].text
        public_key = another_result[3].text
        balance = another_result[4].text
        assets = self.element_is_visible(locators.RESULT_SCANING_ASSETS).text

        return seed_phrase, private_key, wallet_address, public_key, balance, assets

    def check_application_domains(self):
        domains = self.element_is_visible(locators.APPLICATION_DOMAINS).text

        return domains

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
        time.sleep(1)
        self.element_is_visible(locators.RESULTS_FIELDS).click()
        time.sleep(1)
        domains = self.element_is_visible(locators.EMAIL_DOMAINS)
        assert domains.text == ('KuCoin <no-reply@kucoin.com>\n'
                                'Bitstamp <noreply@bitstamp.net>\n'
                                'Google Community Team <googlecommunityteam-noreply@google.com>\n'
                                'Cex User <cexuser001@gmail.com>\n'
                                'Groupon <noreply@r.groupon.com>\n'
                                'Dex User <dexuser001@gmail.com>\n'
                                "Men's Wearhouse <customer_service@tmw.com>\n"
                                'Huobi <noreply@huobipro.com>\n'
                                'MetaMask Team <support@metamask.io>\n'
                                '"Binance.US" <hello@binance.us>\n'
                                'Kraken <noreply@kraken.com>\n'
                                'Slickdeals Alerts <deals@da.slickdeals.net>\n'
                                'Bitstamp <newsletter@team.bitstamp.net>\n'
                                'Slickdeals <deals@d.slickdeals.net>\n'
                                'Slickdeals Account Services <accountservices@slickdeals.net>\n'
                                'Groupon <notify@r.groupon.com>\n'
                                'CoinDesk <auth@coindesk.com>\n'
                                'Twitter <verify@twitter.com>\n'
                                'no-reply@kucoin.com\n'
                                'CT <d41d8cd98f00b204e9800998ecf8427e@cointelegraph.com>')

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
