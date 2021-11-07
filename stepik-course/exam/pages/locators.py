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

    COST_BUSKET = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")
    COST_BOOK = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]")
