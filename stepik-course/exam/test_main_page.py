# pytest -v -s --tb=line --language=en test_main_page.py
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import time


# should be login page -> login_page
@pytest.mark.skip
def test_should_be_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


# можно увидеть продукты которые находятся в корзине из main page
# 1. Гость открывает главную страницу
# 2. Переходит в корзину по кнопке в шапке сайта
# 3. Ожидаем, что в корзине нет товаров
# 4. Ожидаем, что есть текст о том что корзина пуста
@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    # time.sleep(30)
    page.should_be_empty_basket()
    # page.should_have_basket_empty_message()


# объединение тестов ООП
@pytest.mark.login_guest
@pytest.mark.skip
class TestLoginFromMainPage:
    # не забываем передать первым аргументом self
    # can go -> main_page
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
        page = MainPage(browser, link)  # (base_page) инициализируем Page Object
        page.open() # base_page
        page.go_to_login_page()  # (base_page)
        # проверки на login_page
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()  # login_page

    # should see -> main_page
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
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


