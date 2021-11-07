# pytest -v -s --tb=line --language=en test_product_page.py
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest
import time


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.skip
def test_basket_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()  # open Tovar page
    page.click_to_add_basket()  # add to basket
    page.solve_quiz_and_get_code()  # solve quiz and get code
    page.expected_book_name()
    page.expected_book_cost()
    # time.sleep(30)


# 1. Открываем страницу товара
# 2. Добавляем товар в корзину
# 3. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()  # open Tovar page
    page.click_to_add_basket()  # add to basket
    page.should_not_be_success_message()

# Открываем страницу товара
# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()  # open Tovar page
    page.should_not_be_success_message()

# Открываем страницу товара
# Добавляем товар в корзину
# Проверяем, что нет сообщения об успехе с помощью is_disappeared
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()  # open Tovar page
    page.click_to_add_basket()  # add to basket
    page.should_disappear()


# Видеть ссылку для логина
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# Можно перейти на страницу логина
@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

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

### Остановился тут!!!
# class TestUserAddToBasketFromProductPage:
#
#     def test_user_cant_see_success_message(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
#         page = ProductPage(browser, link)
#         page.open()  # open Tovar page
#         page.should_not_be_success_message()
#
#     def test_user_can_add_product_to_basket(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#         page = ProductPage(browser, link)
#         page.open()  # open Tovar page
#         page.click_to_add_basket()  # add to basket
#         page.solve_quiz_and_get_code()  # solve quiz and get code
#         page.expected_book_name()
#         page.expected_book_cost()




