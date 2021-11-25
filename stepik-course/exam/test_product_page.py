# pytest -v -s --tb=line --language=en test_product_page.py
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.main_page import MainPage
import pytest
import time


# REVIEW
@pytest.mark.skip
# TC1. Guest can add product to basket
@pytest.mark.parametrize('promo_offer',
                         ("?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4",
                          "?promo=offer5", "?promo=offer6",
                          pytest.param("?promo=offer7", marks=pytest.mark.xfail(reason="BUG!")),
                          "?promo=offer8", "?promo=offer9"))
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = \
        f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo_offer}"  # 1. Get link
    page = ProductPage(browser, link)                                                        # 2. Browser
    page.open()  # base_page                                                                 # 3. Open page
    page.click_to_add_basket()  # product_page                                               # 4. Add to basket
    page.solve_quiz_and_get_code()  # product_page                                           # 5. Solve quize
    page.expected_book_name()  # product_page                                                # 6. Correct book name
    page.expected_book_cost()  # product_page                                                # 7. Correct book cost
    # time.sleep(30)


@pytest.mark.skip
# TC2. Negative testing. Will failed. Success message after adding product to basket.
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()  # base_page                                                           # 1. Open page
    page.click_to_add_basket()  # product_page                                         # 2. Add to basket
    page.should_not_be_success_message()  # product_page                               # 3. Shouldn't be success mes.


@pytest.mark.skip
# TC3. Guest can't see success message before adding to basket
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()  # base_page                                               # 1. Open page
    page.should_not_be_success_message()  # product_page                   # 2. Nothing to do: there is no success mes.


@pytest.mark.skip
# TC4. Negative testing. Success message should disappear
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()  # base_page                                    # 1. Open page
    page.click_to_add_basket()  # product_page                  # 2. Add to basket
    page.should_disappear()  # product_page                     # 3. Message should disappear


# TC5. Can see login link from product_page
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()  # base_page                                    # 1. Open page
    page.should_be_login_link()  # base_page                    # 2. Can see login link


@pytest.mark.skip
# TC6. Can go to login page
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()                                                 # 1. Open page
    page.should_be_login_link()  # base_page                    # 2. Can see login link
    page.go_to_login_page()      # base_page                    # 3. Can go to login page


# REVIEW
@pytest.mark.login
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(email, password)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()  # base_page                                  # 1. Open page
        page.should_not_be_success_message()  # product_page      # 2. Nothing to do: there is no success mes.

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()  # base_page                                     # 3. Open page
        page.click_to_add_basket()  # product_page                   # 4. Add to basket
        page.solve_quiz_and_get_code()  # product_page               # 5. Solve quize
        page.expected_book_name()  # product_page                    # 6. Correct book name
        page.expected_book_cost()  # product_page
