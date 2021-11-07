# Параметризация позволяет запускать один тест с несколькими параметрами.
# Например в данном случае запустятся два теста с указанием параметра ru или en-gb
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    res = " "
    links = [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ]

    @pytest.mark.parametrize('link', links)
    def test_task_inoplonet(self, browser, link):
        browser.get(link)
        # browser.implicity_wait(10)
        time.sleep(2)
        answer = math.log(int(time.time()))

        #find textarea
        textarea = browser.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[2]/div/div/div/textarea")
        textarea.send_keys(str(answer))

        # click button
        submit = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/div/div/div[2]/div/pre"))
        )
        submit.click()

        answer_check = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/div/div/div[2]/div/pre"))
        )
        answer_check_text = answer_check.text

        if(answer_check_text != "Correct!"):
            print(self.res + str(answer_check_text))

