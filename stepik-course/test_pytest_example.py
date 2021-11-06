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
#         driver = self.driver
#         driver.get("http://www.python.org")
#         self.assertIn("Python", driver.title)
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." not in driver.page_source
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == "__main__":
#     unittest.main()

# Здесь переписан код из task_registration_Important.py под требования unittest-pytest
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestRegistrationUnittest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.link1 = "http://suninjuly.github.io/registration1.html"
        self.link2 = "http://suninjuly.github.io/registration2.html"

    def test_registration(self):
        browser = self.browser
        browser.get(self.link1)

        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class .first")
        first_name.send_keys("Test")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class .second")
        last_name.send_keys("Test")
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class .third")
        email.send_keys("test@mail.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be equal")

    def test_registration_2(self):
        browser = self.browser
        browser.get(self.link2)

        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class .first")
        first_name.send_keys("Test")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class .second")
        last_name.send_keys("Test")
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class .third")
        email.send_keys("test@mail.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be equal")

    def tearDown(self):
        time.sleep(5)
        self.browser.close()


if __name__ == "__main__":
    unittest.main()