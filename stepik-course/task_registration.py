from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import random

try:
    # link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля!!!

    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class .form-control.first")
    first_name.send_keys("Test")
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class .second")
    last_name.send_keys("Test")
    email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class .third")
    email.send_keys("test@mail.ru")

    # elements = browser.find_elements(By.CSS_SELECTOR, "[required]")
    # for element in elements:
    #     element.send_keys("Какой то текст" + str(random.randint(1, 1000)))

    time.sleep(10)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()