from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def element_not_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();", element)
        

class NextPage:

    def __init__(self, driver):
        self.driver = driver

    def element_is_visible(self, locator, timeout=25):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def element_not_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();", element)

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0,1800)")

    def refresh_page(self):
        self.driver.refresh()
