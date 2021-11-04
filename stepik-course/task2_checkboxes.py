from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(a):
        return str(math.log(abs(12*math.sin(int(a)))))
        #lg(abs(12*sin(x)))

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    text = browser.find_element(By.CSS_SELECTOR, "#answer")
    text.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()