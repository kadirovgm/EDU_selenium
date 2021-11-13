from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    # заглушка
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    """Should be empty basket"""
    def should_be_empty_basket(self):
        self.go_to_basket_page()
        self.should_be_no_element()
        self.should_present_message_no_basket_elm()

    def should_be_no_element(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ELM), \
            "Basket element shouldn't present, basket is empty!"

    def should_present_message_no_basket_elm(self):
        assert "Здесь пусто :(" == self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MES).text

    """Should have element"""
    def should_be_filled_basket(self, name, price):
        self.should_be_element()
        self.should_have_correct_name_and_price(name, price)

    def should_be_element(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ELM), "Basket elm should present, but not!"

    def should_have_correct_name_and_price(self, name, price):
        product_name_in_basket = self.browser.find_element(*BasketPageLocators.BASKET_ELM_NAME).text
        print("Basket product name is: " + str(product_name_in_basket))
        assert name == str(product_name_in_basket), "Incorrect product name in basket!"

        product_price_in_basket = self.browser.find_element(*BasketPageLocators.BASKET_ELM_PRICE).text
        print("Basket product price is: " + str(product_price_in_basket))
        assert price == str(product_price_in_basket), "Incorrect product price in basket!"

    """Remove from basket"""
    def click_to_remove_from_basket(self):
        remove_button = self.browser.find_element(*BasketPageLocators.REMOVE_BUTTON)
        remove_button.click()



