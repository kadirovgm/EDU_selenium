from selenium.webdriver.common.by import By

# pair: how, what
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    MESSAGE_AFTER_ADDING = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BOOK_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")

