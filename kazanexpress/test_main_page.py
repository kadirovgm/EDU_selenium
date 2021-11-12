import pytest
import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.favorites_page import FavoritesPage
from pages.basket_page import BasketPage

LINK_MAIN_PAGE = "https://kazanexpress.ru/"


@pytest.mark.need_review
@pytest.mark.skip
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
        favorites_page.should_be_empty_favorites()                          # 3. Go to favorites, chek it for empty

    def test_guest_can_go_to_basket(self, browser):
        link = LINK_MAIN_PAGE
        page = MainPage(browser, link)
        page.open()                                                     # 1. Open main page
        basket_page = BasketPage(browser, browser.current_url)          # 2. Initialize FavoritePage POM
        basket_page.should_be_empty_basket()                            # 3. Go to basket, chek it for empty


@pytest.mark.need_review
@pytest.mark.skip
class TestUserAddToBasketFromMainPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LINK_MAIN_PAGE
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.login_new_user()

    def test_user_can_add_product_to_favorites(self, browser):
        link = LINK_MAIN_PAGE
        page = MainPage(browser, link)
        page.open()
        page.click_to_add_to_favorites()                                    # 1. Click to add to favorites
        favorite_product_name = page.remember_favorite_product_name()       # 2. remember favorite product name
        page.go_to_favorites()                                              # 2. Go to favorites
        page_favorites = FavoritesPage(browser, browser.current_url)        # 3. Initialize Favorites POM
        page_favorites.should_have_favorite_product(favorite_product_name)  # 6. Checking for correct favorite product
