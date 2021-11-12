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
    FAV_ICON_ELM = (By.XPATH, "/html/body/main/div[2]/div[2]/div/div[2]/section/div/div/div[1]/a/div/div[1]/button/img")
    FAV_ICON_SELECTED=(By.XPATH, "/html/body/main/div[2]/div[2]/div/div[2]/section/div/div/div[1]/a/div/div[1]/button")
    PRODUCT_NAME = (By.XPATH,"/html/body/main/div[2]/div[2]/div/div[2]/section/div/div/div[1]/a/div/div[2]/div[1]/span")



class LoginPageLocators:
    """LOGIN FORM"""
    LOGIN_FORM = (By.XPATH, "/html/body/main/div[2]/div[5]/div/div")
    LOGIN_FORM_NAME = (By.XPATH, "/html/body/main/div[2]/div[5]/div/header/h4/span")
    LOGIN_NUMBER = (By.XPATH, "/html/body/main/div[2]/div[5]/div/div/div/form/div[1]/div/input")
    LOGIN_PASSWORD = (By.XPATH, "/html/body/main/div[2]/div[5]/div/div/div/form/div[2]/div/input")
    LOGIN_BUTTON = (By.XPATH, "/html/body/main/div[2]/div[5]/div/div/div/form/button")
    LOGIN_PASSWORD_FORGOT = (By.XPATH, "/html/body/main/div[2]/div[5]/div/div/div/button")
    LOGIN_REGISTER_LINK = (By.XPATH, "/html/body/main/div[2]/div[5]/div/footer/span/button")


class FavoritesPageLocators:
    FAVORITE_ELM = (By.XPATH, "/html/body/main/div[2]/div[2]/div[1]/div[2]/div/div/div[1]/a/div")
    FAVORITE_EMPTY_MES = (By.XPATH, "/html/body/main/div[2]/div[2]/div[1]/div[2]/div/div/div/div/span")
    FAVORITE_EMPTY_MES_ADD = (By.XPATH, "/html/body/main/div[2]/div[2]/div[1]/div[2]/div/div/div/div/p")
    FAVORITE_PRODUCT_NAME = (By.XPATH, "/html/body/main/div[2]/div[2]/div[1]/div[2]"
                                       "/div/div/div[1]/a/div/div[2]/div[1]/span")


class BasketPageLocators:
    BASKET_ELM = (By.XPATH, "/html/body/main/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div/div[2]/div")
    BASKET_EMPTY_MES = (By.XPATH, "//span[@data-test-id='text__empty']")
    BASKET_EMPTY_MES_ADD = (By.CSS_SELECTOR, ".slightly.transparent.regular.hug")



class ProductPageLocators:
    ...