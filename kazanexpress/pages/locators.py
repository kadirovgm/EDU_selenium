from selenium.webdriver.common.by import By


class BasePageLocators:
    # LOGIN_BUTTON = (By.XPATH, "//a[@data-test-id='button__auth']")
    # FAVORITES_LINK = (By.XPATH, "a[@data-test-id='button__wishes']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#main-page > div.sticky-footer > header > div:nth-child(1) > "
                                     "div.middle-header.row.center.between-mbs.middle-mbs.noselect > "
                                     "div.store-action-buttons > "
                                     "a.action-button.slightly.regular.exact-active-link.active-link")
    FAVORITES_LINK = (By.CSS_SELECTOR, "#main-page > div.sticky-footer > header > div:nth-child(1) > "
                                       "div.middle-header.row.center.between-mbs.middle-mbs.noselect > "
                                       "div.store-action-buttons > a:nth-child(2)")
    BASKET_LINK = (By.CSS_SELECTOR, "#cart-button")
    LOGO_LINK = (By.CSS_SELECTOR, "#main-page > div.sticky-footer > header > div:nth-child(1) > "
                                  "div.middle-header.row.center.between-mbs.middle-mbs.noselect > "
                                  "div.middle-header-main-logo.middle-mbs > a > span > svg")
    USER_NAME_APPEARED = (By.CSS_SELECTOR, "div.store-action-buttons > a:nth-child(1) > i")


class MainPageLocators:
    ...


class LoginPageLocators:
    """LOGIN FORM"""
    LOGIN_FORM = (By.XPATH, "/html/body/main/div[2]/div[5]/div/div")
    LOGIN_FORM_NAME = (By.XPATH, "/html/body/main/div[2]/div[5]/div/header/h4/span")
    LOGIN_NUMBER = (By.XPATH, "/html/body/main/div[2]/div[5]/div/div/div/form/div[1]/div/input")
    LOGIN_PASSWORD = (By.XPATH, "/html/body/main/div[2]/div[5]/div/div/div/form/div[2]/div/input")
    LOGIN_BUTTON = (By.XPATH, "/html/body/main/div[2]/div[5]/div/div/div/form/button")
    LOGIN_PASSWORD_FORGOT = (By.XPATH, "/html/body/main/div[2]/div[5]/div/div/div/button")
    LOGIN_REGISTER_LINK = (By.XPATH, "/html/body/main/div[2]/div[5]/div/footer/span/button")



class BasketPageLocators:
    ...


class ProductPageLocators:
    ...