import pytest
import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.favorites_page import FavoritesPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage


LINK_MAIN_PAGE = "https://kazanexpress.ru/"


@pytest.mark.e2e_4
class TestUserCanAddToBasketFromMainPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LINK_MAIN_PAGE
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.login_new_user()

    @pytest.mark.parametrize('search_elm',
                            ("SKN Рюкзак городской", "Футболка женская", "Защитное стекло Honor 10i 20 lite"))
    def test_user_can_add_product_to_basket(self, browser, search_elm):
        page_main = MainPage(browser, browser.current_url)              # 1. POM main_page
        page_main.search_and_select(search_elm)                         # 2. Search elm and select
        time.sleep(1)
        self.browser.implicitly_wait(3)
        page_product = ProductPage(browser, browser.current_url)        # 3. POM product_page
        page_product.is_color_block_exist()                             # 4. Checking for "color" block
        page_product.is_size_block_exist()                              # 5. Checking for size block
        page_product.is_count_block_exist()                             # 6. Checking for "count" block
        name, price = page_product.remember_name_price_of_product()     # 7. Remember product
        time.sleep(1)
        page_product.click_to_add_to_basket()                           # 8. Add to basket
        print("Product price from product: " + str(price))
        page_product.go_to_basket_page()                                # 9. Go to basket
        page_basket = BasketPage(browser, browser.current_url)          # 10. POM basket_page
        page_basket.should_be_filled_basket(price)                       # 11. Checking for basket element
        page_basket.click_to_remove_from_basket()                       # 12. Click to remove from basket
        page_basket.should_be_empty_basket()                            # 13. Should be empty basket

