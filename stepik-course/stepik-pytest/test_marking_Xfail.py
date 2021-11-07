# Можем отметить тест как явно падающий
# Когда баг починят, мы это узнаем, так как теперь тест будет отмечен как:
# XPASS (“unexpectedly passing” — неожиданно проходит).

# запускать pytest -rx

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector(".basket-mini .btn-group > a")
#
#     @pytest.mark.xfail(reason="fixing this bug right now") ###################################
#     def test_guest_should_see_search_button_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector("button.favorite")

import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False