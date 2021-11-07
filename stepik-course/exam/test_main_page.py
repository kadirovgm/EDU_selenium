# pytest -v -s --tb=line --language=en test_main_page.py
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import time


# can go -> main_page
# !переместить на test_login_page.py
@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)   # (base_page) инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # (base_page) открываем страницу
    page.go_to_login_page()          # (base_page) переход на страницу логина
    # проверки на login_page
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()  # login_page


# should see -> main_page
@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()  # base_page


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
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    # time.sleep(30)
    page.should_be_empty_basket()
    # page.should_have_basket_empty_message()







