# Чтобы тест был надежным, нам нужно не только найти кнопку на странице,
# но и дождаться, когда кнопка станет кликабельной

# Для этого используются явные ожидания - Explicity Waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait             # import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    # import EC
from selenium import webdriver
import time
import math

# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text
#
# # Если хотим проверять, что кнопка становится неактивной после отправки данных:
# # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
# button = WebDriverWait(browser, 5).until_not(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )

# Another methods for EC:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # нужно взять price когда price=100
    check = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )

    book = browser.find_element(By.CSS_SELECTOR, "#book")
    book.click()

    select_x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = select_x.text

    def count(a):
        return math.log(abs(12 * math.sin(int(a))))

    y = str(count(x))

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, "#solve")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()