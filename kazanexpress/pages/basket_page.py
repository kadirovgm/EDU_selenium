from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    # заглушка
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

        # Expectation that there is nothing in favorites (waiting for 4 sek)

    def should_be_empty_basket(self):
        self.go_to_basket_page()
        self.should_be_no_element()
        self.should_present_message_no_basket_elm()

    def should_be_no_element(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ELM), \
            "Basket element shouldn't present, basket is empty!"

    def should_present_message_no_basket_elm(self):
        assert "Здесь пусто :(" == self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MES).text
        assert "В Корзину ничего не добавлено" == self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MES_ASS).text