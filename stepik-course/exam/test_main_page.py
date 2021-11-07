# pytest -v -s --tb=line --language=en test_main_page.py

from pages.main_page import MainPage
from pages.login_page import LoginPage

# can go -> main_page
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)   # (base_page) инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # (base_page) открываем страницу
    page.go_to_login_page()          # (main_page) выполняем метод страницы — переходим на страницу логина
    # переход на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# should see -> main_page
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# should be login page -> login_page
def test_should_be_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()