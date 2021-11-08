# pytest -v -s --tb=line --language=en test_main_page.py
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import time

LINK_MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.skip
# TC1. Should be empty basket for guest from main page
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = LINK_MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()  # base_page
    # time.sleep(30)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()  # basket_page
    # page.should_have_basket_empty_message()


@pytest.mark.skip
@pytest.mark.login_guest
# TC2. Common tests. Login from main page
class TestLoginFromMainPage:

    # TC 2.1. Can go to Login page
    def test_guest_can_go_to_login_page(self, browser):
        link = LINK_MAIN_PAGE
        page = MainPage(browser, link)
        page.open()  # base_page
        page.go_to_login_page()  # (base_page)
        # проверки на login_page
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()  # login_page

    # TC 2.2. Should see Login link from main_page
    def test_guest_should_see_login_link(self, browser):
        link = LINK_MAIN_PAGE
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()  # base_page


################# ВАЖНО! Корректная форма ООП ###########################
# @pytest.mark.login
# class TestLoginFromProductPage():
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self):
#         self.product = ProductFactory(title="Best book created by robot")
#         # создаем по апи
#         self.link = self.product.link
#         yield
#         # после этого ключевого слова начинается teardown
#         # выполнится после каждого теста в классе
#         # удаляем те данные, которые мы создали
#         self.product.delete()
#
#     def test_guest_can_go_to_login_page_from_product_page(self, browser):
#         page = ProductPage(browser, self.link)
#         # дальше обычная реализация теста
#
#     def test_guest_should_see_login_link(self, browser):
#         page = ProductPage(browser, self.link)
#         # дальше обычная реализация теста
