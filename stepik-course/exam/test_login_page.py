import pytest
from pages.login_page import LoginPage

LINK_LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


# REVIEW
@pytest.mark.skip
# TC1. Login page contains all required elements
def test_should_be_login_page(browser):
    link = LINK_LOGIN_PAGE
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()  # login_page