import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage

LINK_MAIN_PAGE = "https://kazanexpress.ru/"


class TestGuestCanUseHeader:
    def test_guest_can_login(self, browser):
        link = LINK_MAIN_PAGE
        page = MainPage(browser, link)
        page.open()                                             # 1. Open main page
        login_page = LoginPage(browser, browser.current_url)    # 2. Initialize LoginPage POM
        login_page.login_new_user()                             # 3. Login as user




@pytest.mark.skip
def test_guest_can_login(self, browser):
    link = LINK_MAIN_PAGE
    page = MainPage(browser, link)
    page.open()  # base_page
    page.go_to_login_page()  # (base_page)
    # проверки на login_page
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()  # login_page


@pytest.mark.skip
class TestUserAddToBasketFromMainPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        number = "79297285880"
        password = "Poi98980"
        self.page.go_to_login_page()
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(email, password)

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()  # base_page                                     # 3. Open page
        page.click_to_add_basket()  # product_page                   # 4. Add to basket
        page.solve_quiz_and_get_code()  # product_page               # 5. Solve quize
        page.expected_book_name()  # product_page                    # 6. Correct book name
        page.expected_book_cost()  # product_page
