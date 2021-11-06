####################### setup/teardown методы и классы

#### Здесь в `первом тесте` браузер откроется один раз на весь класс
# (быстрее так как не нужно ждать загрузки браузера)
#### `Во втором тесте` браузер откроется для каждого метода класса
# (лучше, так как кеш браузера не будет влиять на следующие тесты)

# from selenium import webdriver
#
# link = "http://selenium1py.pythonanywhere.com/"
#
# class TestMainPage1():
#
#     @classmethod
#     def setup_class(self):
#         print("\nstart browser for test suite..")
#         self.browser = webdriver.Chrome()
#
#     @classmethod
#     def teardown_class(self):
#         print("quit browser for test suite..")
#         self.browser.quit()
#
#     def test_guest_should_see_login_link(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector("#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
#
# class TestMainPage2():
#
#     def setup_method(self):
#         print("start browser for test..")
#         self.browser = webdriver.Chrome()
#
#     def teardown_method(self):
#         print("quit browser for test..")
#         self.browser.quit()
#
#     def test_guest_should_see_login_link(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector("#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

############################ Sample fixture using ##################################################
# В таком случае браузеры для каждого теста откроются
# и будут ожидать завершения всего класса

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#
#     return browser
#
# class TestMainPage1():
#     # вызываем фикстуру в тесте, передав ее как параметр
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

###################################### Sample fixture using - yield ################

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")


############################# Scope - Область видимости #######################

# Допустимые значения: “function”, “class”, “module”, “session”
# @pytest.fixture(scope="class")
# @pytest.fixture(scope="function")  etc.