from .base_page import BasePage
from .main_page import MainPage
from .locators import FavoritesPageLocators
import time


class FavoritesPage(BasePage):

    # Expectation that there is nothing in favorites (waiting for 4 sek)
    def should_be_empty_favorites(self):
        self.go_to_favorites()
        self.should_be_no_element()
        self.should_present_message_no_favorites()

    def should_be_no_element(self):
        assert self.is_not_element_present(*FavoritesPageLocators.FAVORITE_ELM), \
            "Favorites element shouldn't present, favorites is empty!"

    def should_present_message_no_favorites(self):
        assert "Здесь пусто :(" == self.browser.find_element(*FavoritesPageLocators.FAVORITE_EMPTY_MES).text
        assert "У Вас пока нет желаний." == self.browser.find_element(*FavoritesPageLocators.FAVORITE_EMPTY_MES_ADD).text

    def should_have_favorite_product(self, product_name_from_main_page):
        self.should_have_any_favorite_product()
        self.should_have_correct_name_of_favorite_product(product_name_from_main_page)

    def should_have_any_favorite_product(self):
        assert self.is_element_present(*FavoritesPageLocators.FAVORITE_ELM), \
            "Favorite element should present, but it's not"

    def should_have_correct_name_of_favorite_product(self, product_name_from_main_page):
        product_name_in_favorites = self.browser.find_element(*FavoritesPageLocators.FAVORITE_PRODUCT_NAME)
        product_name_in_favorites_text = product_name_in_favorites.text
        print("FAVORITE PRODUCT NAME IS " + str(product_name_in_favorites_text))
        assert product_name_in_favorites_text == product_name_from_main_page, \
            "Incorrect favorite product name"
