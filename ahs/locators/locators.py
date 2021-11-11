from selenium.webdriver.common.by import By


class BasePageLocators:
    # LOGIN_BUTTON = (By.XPATH, "//a[@data-test-id='button__auth']")
    # FAVORITES_LINK = (By.XPATH, "a[@data-test-id='button__wishes']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a.action-button.slightly.regular.exact-active-link.active-link")
    FAVORITES_LINK = (By.CSS_SELECTOR, "div.store-action-buttons > a:nth-child(2)")
    BASKET_LINK = (By.CSS_SELECTOR, "#cart-button")
    LOGO_LINK = (By.CSS_SELECTOR, "div.middle-header-main-logo.middle-mbs > a > span > svg")
    USER_NAME_APPEARED = (By.CSS_SELECTOR, "div.store-action-buttons > a:nth-child(1) > i")

class MainPageLocators:
    ...

class LoginPageLocators:
    ...

class BasketPageLocators:
    ...