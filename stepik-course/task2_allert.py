# Для взаимодействия с allert окнами

# Переключиться на окно allert
# alert = browser.switch_to.alert
# alert.accept()

# Получаем текст из объекта allert
# alert = browser.switch_to.alert
# alert_text = alert.text

# Confirmation window (Ok, Cancel)
# confirm = browser.switch_to.alert
# confirm.accept()                  # ok
# confirm.dismiss()                 # cancel

# Promt window - окно с вводом данных
# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    select_x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = select_x.text

    def count(a):
        return math.log(abs(12 * math.sin(int(a))))

    y = str(count(x))

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()