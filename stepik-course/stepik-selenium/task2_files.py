# Working with files
# import os
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)
# or
# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(2)")
    name.send_keys("Name")

    last_name = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(4)")
    last_name.send_keys("last name")

    email = browser.find_element(By.CSS_SELECTOR,"body > div > form > div > input:nth-child(6)")
    email.send_keys("test@mail.ru")

    file = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
