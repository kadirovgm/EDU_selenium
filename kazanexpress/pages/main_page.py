from .base_page import BasePage
from .locators import MainPageLocators
import time


class MainPage(BasePage):

    """Add to favorites"""
    def click_to_add_to_favorites(self):
        favorite_icon = self.browser.find_element(*MainPageLocators.FAV_ICON_ELM)
        favorite_icon.click()
        time.sleep(1)
        self.should_be_red_fav_icon()

    def should_be_red_fav_icon(self):
        assert self.is_element_present(*MainPageLocators.FAV_ICON_SELECTED), "Probably Element isn't in favorites"

    """Remember product name"""
    def remember_product_name(self):
        product_name = self.browser.find_element(*MainPageLocators.PRODUCT_NAME)
        product_name_text = product_name.text
        return product_name_text

    """Remember product price"""
    def remember_product_price(self):
        product_price = self.browser.find_element(*MainPageLocators.PRODUCT_PRICE)
        product_price_text = product_price.text
        return product_price_text

    """Click to product"""
    def click_to_product(self):
        product_elm = self.browser.find_element(*MainPageLocators.PRODUCT_ELM)
        product_elm.click()
