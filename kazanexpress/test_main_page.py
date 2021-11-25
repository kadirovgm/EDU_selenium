import pytest
import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.favorites_page import FavoritesPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage

LINK_MAIN_PAGE = "https://kazanexpress.ru/"


@pytest.mark.e2e_1
class TestGuestCanUseHeader:

    def test_guest_can_login(self, browser):
        link = LINK_MAIN_PAGE
        page = MainPage(browser, link)
        page.open()                                             # 1. Open main page
        login_page = LoginPage(browser, browser.current_url)    # 2. Initialize LoginPage POM
        login_page.login_new_user()                             # 3. Login as user

    def test_guest_can_go_to_favorites(self, browser):
        link = LINK_MAIN_PAGE
        page = MainPage(browser, link)
        page.open()                                                         # 1. Open main page
        favorites_page = FavoritesPage(browser, browser.current_url)        # 2. Initialize FavoritePage POM
        favorites_page.go_to_favorites()                                    # 3. Go to favorites
        favorites_page.should_be_empty_favorites()                          # 4. Chek it for empty

    def test_guest_can_go_to_basket(self, browser):
        link = LINK_MAIN_PAGE
        page = MainPage(browser, link)
        page.open()                                                     # 1. Open main page
        basket_page = BasketPage(browser, browser.current_url)          # 2. Initialize FavoritePage POM
        basket_page.should_be_empty_basket()                            # 3. Go to basket, chek it for empty


@pytest.mark.e2e_2
class TestUserAddToFavoritesFromMainPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LINK_MAIN_PAGE
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.login_new_user()

    def test_user_can_add_product_to_favorites(self, browser):
        page_main = MainPage(browser, browser.current_url)
        page_main.click_to_add_to_favorites()                               # 1. Click to add to favorites
        favorite_product_name = page_main.remember_product_name()           # 2. remember favorite product name
        page_main.go_to_favorites()                                         # 3. Go to favorites
        page_favorites = FavoritesPage(browser, browser.current_url)        # 4. Initialize Favorites POM
        page_favorites.should_have_favorite_product(favorite_product_name)  # 5. Checking for correct favorite product
        page_favorites.click_to_remove_from_favorites()                     # 6. Remove from favorites
        page_favorites.should_be_empty_favorites()                          # 7. Checking for empty favorites


@pytest.mark.e2e_3
class TestUserCanSeeLastSeeingProduct:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LINK_MAIN_PAGE
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.login_new_user()

    def test_user_can_see_last_product_in_favorites(self, browser):
        page_main = MainPage(browser, browser.current_url)                  # 1. POM main_page
        remembered_product_name = page_main.remember_product_name()         # 2. Remember name of product
        remembered_product_price = page_main.remember_product_price()       # 3. Remember price of product
        page_main.click_to_product()                                        # 4. Go to Product page
        page_product = ProductPage(browser, browser.current_url)            # 5. POM product_page
        page_product.should_have_chosen_product\
            (remembered_product_name, remembered_product_price)             # 6. Checking for correct product
        self.page.go_to_favorites()                                         # 7. Go to favorites
        page_favorites = FavoritesPage(browser, browser.current_url)        # 8. POM favorites_page
        page_favorites.should_be_suggestions_down_of_favorites\
            (remembered_product_name, remembered_product_price)             # 9. Checking for having early clicked product in favorite's suggestions

    # def test_user_can_see_last_product_in_basket(self, browser):
    #     ...

    # everything is good for attestation
    # unittests learning path


