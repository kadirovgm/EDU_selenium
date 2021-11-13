import pytest
import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.favorites_page import FavoritesPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage

# need to use fixture element for testing
LINK_MAIN_PAGE = "https://kazanexpress.ru/"
LINK_PRODUCT_PAGE = "https://kazanexpress.ru/product/SKN-Ryukzak-gorodskojvodonepronicaemyjs-824022"
SEARCH_ELM = "SKN Рюкзак городской"

@pytest.mark.need_review
class TestUserCanAddToBasketFromMainPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LINK_MAIN_PAGE
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.login_new_user()

    def test_user_can_add_product_to_basket(self, browser):
        page_main = MainPage(browser, browser.current_url)          # 1. POM main_page
        page_main.search_and_select(SEARCH_ELM)                     # 2. Search elm and select
        time.sleep(1)
        page_product = ProductPage(browser, browser.current_url)    # 3. POM product_page
        page_product.is_color_block_exist()                         # 4. Checking for color block
        page_product.is_count_block_exist()                         # 5. Checking for count block
        time.sleep(3)

# Второй вариант с параметризацией линков к продуктам (не серч)