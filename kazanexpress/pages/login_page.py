from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import time


class LoginPage(BasePage):

    def login_new_user(self):
        number = "79297285880"
        password = "Poi98980"
        self.go_to_login_page()                     # 1. Go to login link
        self.should_be_login_page()                 # 2. Check for login modal
        self.fill_login_form(number, password)      # 3. Fill login form
        time.sleep(1)                               # 4. Waiting for loading [Add implicitly wait here]
        self.should_be_authorized_user()            # 5. Checking for authorized

    def should_be_login_page(self):
        self.should_be_login_form()                 # 1. Checking for login form attributes
        self.should_be_login_form_name()            # 2. Checking for correct name

    def should_be_login_url(self):
        assert self.browser.current_url in self.url, "Incorrect URL!"
        # assert self.browser.LoginPageLocators.LOGIN_FORM in self.browser.current_url, "Incorrect URL!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_NUMBER), "Field for input number isn't present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Field for input password isn't present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button isn't present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FORGOT), "Forgot pass link isn't present"
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_LINK), "Register link isn't present"

    def should_be_login_form_name(self):
        assert "Вход" == self.browser.find_element(*LoginPageLocators.LOGIN_FORM_NAME).text, \
            "Login form name is not 'Вход'!"

    def fill_login_form(self, number, password):
        input_number = self.browser.find_element(*LoginPageLocators.LOGIN_NUMBER)
        input_number.send_keys(number)
        input_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        input_password.send_keys(password)
        button_login = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        button_login.click(), " probably unauthorised user"

    def should_be_authorized_user(self):
        assert "Rushat" == self.browser.find_element(*BasePageLocators.USER_NAME_APPEARED).text, \
            "User probably unathorized"