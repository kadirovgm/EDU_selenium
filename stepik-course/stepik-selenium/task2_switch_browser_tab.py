# Switch to another window
# browser.switch_to.window(window_name)

# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles,
# который возвращает массив имён всех вкладок.
# Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
# new_window = browser.window_handles[1]

# Также можем запомнить имя текущей вкладки, чтобы вернуться:
# first_window = browser.window_handles[0]

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    button.click()

################# important part
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
#################
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