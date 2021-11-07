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
        message_book_name = self.browser.find_element(*ProductPageLocators.MESSAGE_AFTER_ADDING).text
        book = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        print("print book name:"+str(book))
        print("print message:" + str(message_book_name))

        assert str(book) == str(message_book_name), "Incorrect book was added to baket!"

    def expected_book_cost(self):
        # проверяем что стоитмость корзины совпадает с ценой товара
        cost_book = self.browser.find_element(*ProductPageLocators.COST_BOOK).text
        cost_busket = self.browser.find_element(*ProductPageLocators.COST_BUSKET).text
        print("print book cost:" + str(cost_book))
        print("print busket cost:" + str(cost_busket))
        assert str(cost_book) == str(cost_busket), "Incorrect cost of book"

    # "Элемент не появляется на странице": упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    # "Элемент исчезет из страницы": будет ждать до тех пор, пока элемент не исчезнет.

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message appeared, but should disappeare"




