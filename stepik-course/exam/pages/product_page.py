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

    def expected_result_after_busket(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_AFTER_ADDING)
        book = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        assert book in message, "Incorrect book was added to baket!"
