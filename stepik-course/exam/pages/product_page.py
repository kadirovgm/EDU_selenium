from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла

import math


class ProductPage(BasePage):
    def click_to_add_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def expected_book_name(self):
        # првоеряем что правильная книга была добавлена в корзину
        message_book_name = self.browser.find_element(*ProductPageLocators.MESSAGE_AFTER_ADDING)
        book = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        assert str(book) in str(message_book_name), "Incorrect book was added to baket!"

    def expected_book_cost(self):
        # проверяем что стоитмость корзины совпадает с ценой товара
        cost_book = self.browser.find_element(*ProductPageLocators.COST_BOOK)
        cost_busket = self.browser.find_element(*ProductPageLocators.COST_BUSKET)
        assert str(cost_book) == str(cost_busket), "Incorrect cost of book"


