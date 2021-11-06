# Когда тестов становится много, хорошо иметь способ разделять тесты не только по названиям,
# но также по каким-нибудь заданным нами категориям.
# Например, мы можем выбрать небольшое количество критичных тестов (smoke),
# которые нужно запускать на каждый коммит разработчиков,
# а остальные тесты обозначить как регрессионные (regression)
# и запускать их только перед релизом.

# Для маркировки теста нужно написать декоратор вида @pytest.mark.mark_name

# Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку:
# pytest -s -v -m smoke test_marking.py

# import pytest
# from selenium import webdriver
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#
#     @pytest.mark.smoke
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")
#
#     @pytest.mark.regression
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector(".basket-mini .btn-group > a")


########################## Task #######################
# pytest -v -m "smoke and not beta_users" test_task_run_1.py
import pytest


class TestMainPage():
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        assert True


class TestBasket():
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        assert True


@pytest.mark.skip
class TestBookPage():
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        assert True


# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    assert True
