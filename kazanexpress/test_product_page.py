import pytest
import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.favorites_page import FavoritesPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage

# need to use fixture element for testing
LINK_PRODUCT_PAGE = "https://kazanexpress.ru/product/SKN-Ryukzak-gorodskojvodonepronicaemyjs-824022"

@pytest.mark.need_review
class TestUserCanAddToBasketFromMainPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LINK_PRODUCT_PAGE
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.login_new_user()

    def test_user_can_add_product_to_basket(self, browser):
        page_main = ProductPage(browser, browser.current_url)
        ...