from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.should_be_login_page()
        ...
        self.should_be_authorized_user()




    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url in self.url, "Incorrect URL!"
        # assert self.browser.LoginPageLocators.LOGIN_FORM in self.browser.current_url, "Incorrect URL!"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def fill_register_form(self):
        # заполним форму регистрации
        ...

