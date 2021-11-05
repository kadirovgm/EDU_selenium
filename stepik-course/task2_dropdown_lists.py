from selenium import webdriver
from selenium.webdriver.common.by import By

# link = ""
# browser = webdriver.Chrome()
# browser.get(link)
# ---------------------------Stupid method----------------------------------
# browser.find_element_by(By.TAG_NAME, "select").click()                    ## click to list for dropdown
# browser.find_element_by(By.CSS_SELECTOR, "option:nth-child(2)").click()   ## select option
# or browser.find_element_by_css_selector("[value='1']").click()            ## select option
# ---------------------------Advanced methods: webdriver.select-------------
# from selenium.webdriver.support.ui import Select                          # import Select
# select = Select(browser.find_element_by_tag_name("select"))
# select.select_by_value("1")                                               # ищем элемент с текстом "Python"
#       or
#       select.select_by_visible_text("text")                               # search by visible text
#       select.select_by_index(index)                                       # search by number or index

import math
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    def sum(a, b):
        return str(int(a)+int(b))
    a = browser.find_element(By.CSS_SELECTOR, "#num1").text
    print("a=" + str(a))
    b = browser.find_element(By.CSS_SELECTOR, "#num2").text
    print("b=" + str(b))
    c = sum(a, b)
    print("sum="+c)
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(c))
    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()