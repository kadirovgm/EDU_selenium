# # BASIC TEMPLATE:
# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# class PythonOrgSearch(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#
#     def test_search_in_python_org(self):
#         try:
#             driver = self.driver
#             driver.get("http://www.python.org")
#             self.assertIn("Python", driver.title)
#             elem = driver.find_element_by_name("q")
#             elem.send_keys("pycon")
#             elem.send_keys(Keys.RETURN)
#             assert "No results found." not in driver.page_source
#         finally:
#             self.driver.close()
#
#     def tearDown(self):
#         self.driver.quit()
#
# if __name__ == "__main__":
#     unittest.main()

############# UNITTEST ############
# self.assertEqual(a, b, msg="Значения разные")

############ PYTEST ###############
# assert a == b, "Значения разные"


# SAMPLE

# import pytest
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
#
# def test_exception1():
#     try:
#         browser = webdriver.Chrome()
#         browser.get("http://selenium1py.pythonanywhere.com/")
#         with pytest.raises(NoSuchElementException):
#             browser.find_element_by_css_selector("button.btn")
#             pytest.fail("Не должно быть кнопки Отправить")
#     finally:
#         browser.quit()
#
# def test_exception2():
#     try:
#         browser = webdriver.Chrome()
#         browser.get("http://selenium1py.pythonanywhere.com/")
#         with pytest.raises(NoSuchElementException):
#             browser.find_element_by_css_selector("no_such_button.btn")
#             pytest.fail("Не должно быть кнопки Отправить")
#     finally:
#         browser.quit()
