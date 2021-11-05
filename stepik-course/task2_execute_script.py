from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# browser = webdriver.Chrome()
# browser.execute_script("alert('Robots at work');")
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
# browser.execute_script("return arguments[0].scrollIntoView(true);") # scroll page until view=true

# Scroll until click
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    select_x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = select_x.text

    def count(a):
        return math.log(abs(12 * math.sin(int(a))))
    y = str(count(x))

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true)", radio)
    time.sleep(0.5)
    radio.click()

    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true)", submit)
    time.sleep(0.5)
    submit.click()

finally:
    time.sleep(10)
    browser.quit()