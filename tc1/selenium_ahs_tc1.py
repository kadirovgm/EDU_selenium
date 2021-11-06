from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

"""Login->Active positions->"""



try:
    link = "http://192.168.52.122/login"
    browser = webdriver.Chrome()
    browser.get(link)

    # login to admin account
    email = browser.find_element(By.CSS_SELECTOR, "#email")
    email.send_keys("admin@admin.com")
    password = browser.find_element(By.CSS_SELECTOR, "#password")
    password.send_keys("P@ssw0rd1")

    button_login = browser.find_element(By.CSS_SELECTOR, "div.ant-row.ant-form-item.sc-fznLxA.gQRraV > div > div > div > button")
    button_login.click()

    # browser.get(link)  # refresh (it's a bug)
    time.sleep(5)
    search = browser.find_element(By.CSS_SELECTOR, "#root > section > section > main > div.ant-row.ant-row-space-between.ant-row-middle > div:nth-child(1) > div > div:nth-child(1) > span > input")
    search.send_keys("Rushat")

    active_positions = browser.find_elements(By.CSS_SELECTOR, ".ant-table-row.ant-table-row-level-0")
    for position in active_positions:
        position = browser.find_element(By.CSS_SELECTOR, "#root > section > section > main > div > div > div > div > div > div > div > table > tbody > tr > td:nth-child(2)")
        position_title = position.text
        print("Priiint:" + str(position_title))
        assert "Rushat" in position_title, "Search incorrect"

finally:
    time.sleep(5)
    browser.quit()

