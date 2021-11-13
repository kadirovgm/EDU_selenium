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
        page_product.is_color_block_exist()                         # 4. Checking for "color" block
        page_product.is_count_block_exist()                         # 5. Checking for "count" block
        time.sleep(1)
        page_product.click_to_add_to_basket()                       # 6. Add to basket
        name, price = page_product.remember_name_price_of_product() # 7. Remember product
        print("Product name from product: " + str(name))
        print("Product price from product: " + str(price))
        page_product.go_to_basket_page()                            # 8. Go to basket
        page_basket = BasketPage(browser, browser.current_url)      # 9. POM basket_page
        page_basket.should_be_filled_basket(name, price)            # 10. Checking for basket element
        page_basket.click_to_remove_from_basket()                   # 11. Click to remove from basket
        page_basket.should_be_empty_basket()                        # 12. Should be empty basket

