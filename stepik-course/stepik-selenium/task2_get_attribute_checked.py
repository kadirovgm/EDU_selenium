# robots_radio = browser.find_element_by_id("robotsRule")
# robots_checked = robots_radio.get_attribute("checked")
# assert robots_checked is None

import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(a):
        return str(math.log(abs(12*math.sin(int(a)))))

    treasure = browser.find_element(By.CSS_SELECTOR, "#treasure")
    valuex = treasure.get_attribute("valuex")

    y = calc(valuex)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()
    time.sleep(0.5)
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    submit = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > div > button")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()