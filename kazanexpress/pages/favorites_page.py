from .base_page import BasePage
from .main_page import MainPage
from .locators import FavoritesPageLocators
import time


class FavoritesPage(BasePage):

    """Click to remove from favorites"""
    def click_to_remove_from_favorites(self):
        favorite_icon = self.browser.find_element(*FavoritesPageLocators.FAVORITE_ICON)
        favorite_icon.click()

    """Should have empty favorites"""
    def should_be_empty_favorites(self):
        self.should_be_no_element()
        self.should_present_message_no_favorites()

    def should_be_no_element(self):
        assert self.is_not_element_present(*FavoritesPageLocators.FAVORITE_ELM), \
            "Favorites element shouldn't present, favorites is empty!"

    def should_present_message_no_favorites(self):
        assert "Здесь пусто :(" == self.browser.find_element(*FavoritesPageLocators.FAVORITE_EMPTY_MES).text
        assert "У Вас пока нет желаний." == self.browser.find_element(*FavoritesPageLocators.FAVORITE_EMPTY_MES_ADD).text

    """ Should have favorite product"""
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

    """Suggestions"""
    def should_be_suggestions_down_of_favorites(self, name, price):
        self.should_have_any_suggestion()
        self.should_have_correct_name_and_price_of_suggestion(name, price)

    def should_have_any_suggestion(self):
        assert self.is_element_present(*FavoritesPageLocators.SUGGESTION_ELM), "There is no suggestions!"

    def should_have_correct_name_and_price_of_suggestion(self, name, price):
        suggestion_product_name = self.browser.find_element(*FavoritesPageLocators.SUGGESTION_ELM_NAME).text
        print("Favorites: Suggestion product name is: " + str(suggestion_product_name))
        assert suggestion_product_name == name, "Incorrect name of chosen produce!"

        suggestion_product_price = self.browser.find_element(*FavoritesPageLocators.SUGGESTION_ELM_PRICE).text
        print("Favorites: Suggestion product price is: " + str(suggestion_product_price))
        assert suggestion_product_price == price, "Incorrect price of chosen produce!"


