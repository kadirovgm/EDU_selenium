from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    # заглушка
    def __init__(self, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)

    """Correct product in product page"""
    def should_have_chosen_product(self, product_name, product_price):
        self.should_have_any_product()
        self.should_have_correct_name_and_price_of_product(product_name, product_price)

    def should_have_any_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT), "Error, there is no element!"

    def should_have_correct_name_and_price_of_product(self, name, price):
        product_name_in_products = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_products_text = product_name_in_products.text
        print("Product name is: " + str(product_name_in_products_text))
        assert product_name_in_products_text == name, "Incorrect name of chosen produce!"

        product_price_in_products = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_in_products_text = product_price_in_products.text
        print("Product price is: " + str(product_price_in_products_text))
        assert product_price_in_products_text == price, "Incorrect price of chosen produce!"



