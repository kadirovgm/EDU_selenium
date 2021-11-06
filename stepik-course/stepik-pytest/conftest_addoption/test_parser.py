# Если запустить тест без параметра: pytest -s -v test_parser.py
    # получаем ошибку - `_pytest.config.UsageError: --browser_name should be chrome or firefox`
# Давайте укажем параметр: pytest -s -v --browser_name=chrome test_parser.py
# Или: pytest -s -v --browser_name=firefox test_parser.py



link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")