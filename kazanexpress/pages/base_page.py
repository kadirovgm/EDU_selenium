from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait  # import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    # constructor for BasePage
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Open browser
    def open(self):
        self.browser.get(self.url)

    # abstract method for waiting for an `element to appear`
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # abstract method for waiting for an `element NOT to appear`
    def is_not_element_present(self, how, what, timeout=1):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # an abstract method for checking that element disappears
    def is_disappeared(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # COMMON ACTIONS FROM ALL PAGES
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_BUTTON)
        link.click()

    def go_to_favorites(self):
        link = self.browser.find_element(*BasePageLocators.FAVORITES_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def go_to_main_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGO_LINK)
        link.click()

    # checking that user is authorized
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_NAME_APPEARED), "User name is not presented," \
                                                                     " probably unauthorised user"
