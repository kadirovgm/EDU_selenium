from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # заглушка
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    # Ожидаем что в корзине нет товаров
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ELM), \
            "Basket elm shouldn't present, basket is empty!"

    # Ожидаем, что есть надпись о том, что корзина пуста
    def should_have_basket_empty_message(self):
        message_basket_empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert "Your basket is empty." == str(message_basket_empty), \
            "Should be 'Your basket is empty.' message!"
