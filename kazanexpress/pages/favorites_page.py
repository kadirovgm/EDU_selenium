from .base_page import BasePage
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
