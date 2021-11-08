from selenium.webdriver.common.by import By


# pair: how, what
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "/html/body/header/div[1]/div/div[2]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    ...


class LoginPageLocators:
    # forms
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    # register forms
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-primary")


class ProductPageLocators:
    ADD_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")

    MESSAGE_AFTER_ADDING = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/strong")
    BOOK_NAME = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/h1")

    COST_BUSKET = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")
    COST_BOOK = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]")

    SUCCESS_MESSAGE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div")


class BasketPageLocators:
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ELM = (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/div/div")
