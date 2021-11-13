# pytest -s -v --browser_name=chrome test_parser.py
# pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py - for rerun
# pytest --language=es test_items.py - for language

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# default options
def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language',
                     action='store',
                     default="None",
                     help="Choose language: ru, en")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    # browser = None
    user_language = request.config.getoption("language")
    user_language = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nStart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()                   # maximize window
        browser.implicitly_wait(3)                  # implicitly wait
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nStart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

# Basic browser
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
