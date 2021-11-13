from .base_page import BasePage
from .locators import ProductPageLocators
import random
import pytest, time
from selenium.webdriver.common.by import By


# static method
def click_to_plus_button(count):
    n = random.randint(1, 10)
    for i in range(n):
        count.click()
    return n


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

    """Checking for color block!"""
    def is_color_block_exist(self):
        if self.is_element_present(*ProductPageLocators.PRODUCT_COLOR_BLOCK):
            print("Color block exist!")
            select_color = self.browser.find_element(*ProductPageLocators.PRODUCT_COLOR_SELECT)
            select_color.click()
            assert self.is_element_present(*ProductPageLocators.PRODUCT_COLOR_SELECT_CHECK), "Color can't be selected!"
        else:
            print("Color block does not exist!")

    """Checking for size block"""
    def is_size_block_exist(self):
        if self.is_element_present(*ProductPageLocators.PRODUCT_SIZE_BLOCK):
            print("Size block exist!")
            select_size = self.browser.find_element(*ProductPageLocators.PRODUCT_SIZE_SELECT)
            select_size.click()
        else:
            print("Size block does not exist")

    """Checking for count block (required block)"""
    def is_count_block_exist(self):
        if self.is_element_present(*ProductPageLocators.PRODUCT_COUNT_BLOCK):
            print("Count block exist!")
            self.checking_for_correct_counting()
        else:
            print("Count block does not exist")
            assert "Count block should exist!"

    # delete rubles next to sum, and remove probels
    def checking_for_correct_counting(self):
        price_old = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text[:-2].replace(' ', '')
        add_count = self.browser.find_element(*ProductPageLocators.PRODUCT_COUNT_BLOCK_PLUS)
        click_count = click_to_plus_button(add_count)
        price_new = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text[:-2].replace(' ', '')
        print("PRICE OLD = " + str(price_old))
        print("PRICE NEW = " + str(price_new))
        actual_click_count = click_count + 1
        print("CLICK = " + str(actual_click_count))

        assert int(price_new) == int(price_old) * actual_click_count, "Incorrect final sum after adding count"

    """Remember Price and Name of Product"""
    def remember_name_price_of_product(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return str(name), str(price)

    """Add to basket"""
    def click_to_add_to_basket(self):
        if self.is_element_present(*ProductPageLocators.PRODUCT_ADD_TO_BASKET):
            add_button = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET)
            add_button.click()
        else:
            assert "Can't find add to basket button, try to check that blocks are filled!"

