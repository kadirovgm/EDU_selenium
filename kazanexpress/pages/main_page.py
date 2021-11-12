from .base_page import BasePage
from .locators import MainPageLocators
import time

class MainPage(BasePage):
    # заглушка
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def click_to_add_to_favorites(self):
        self.click_to_favorite_icon()
        # self.should_be_red_fav_icon()

    def click_to_favorite_icon(self):
        link = self.browser.find_element(*MainPageLocators.FAV_ICON_ELM)
        link.click()

    # НА ПОДУМАТЬ, ТАК КАК ТУТ НАДО ВЗЯТЬ СТРОКУ С ТИПА, А НЕ ИСПОЛЬЗОВАТЬ .text
    def should_be_red_fav_icon(self):
        fav_icon_elm = self.browser.find_element(*MainPageLocators.FAV_ICON_SELECTED)
        fav_icon_elm_text = fav_icon_elm.text
        print("OUTPUTGGG" + str(fav_icon_elm_text))
        assert "Убрать из избранного" in fav_icon_elm_text, "Probably Element isn't in favorites"

    def remember_favorite_product_name(self):
        product_name = self.browser.find_element(*MainPageLocators.PRODUCT_NAME)
        product_name_text = product_name.text
        return product_name_text


