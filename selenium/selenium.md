# Useful links
### [CSS selectors](https://github.com/kadirovgm/EDU_selenium/blob/master/css_selector.md)
### [Selenium education](https://github.com/kadirovgm/EDU_selenium/blob/master/selenium.md)

# Another useful links from Stepik course 
### Common
1. https://selenium-python.com
2. http://selenium-python.readthedocs.io
3. http://chromedriver.chromium.org/getting-started
4. https://www.guru99.com/selenium-tutorial.html — Туториал на английском, ориентирован на Java
5. https://www.guru99.com/live-selenium-project.html — Можно попробовать писать автотесты для демо-сайта банка. Тоже Java.
6. http://barancev.github.io/good-locators/ — что такое хорошие селекторы
7. http://barancev.github.io/what-is-path-env-var/ — что за PATH переменная? 

### Ожидания в Selenium WebDriver

1. https://docs.seleniumhq.org/docs/04_webdriver_advanced.jsp
2. https://selenium-python.readthedocs.io/waits.html
3. https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_condition...﻿
4. https://stackoverflow.com/questions/15122864/selenium-wait-until-document-is-ready
5. https://blog.codeship.com/get-selenium-to-wait-for-page-load/
6. http://barancev.github.io/slow-loading-pages/
7. http://barancev.github.io/page-loading-complete/

# Search elm with selenium

## `driver.find_element_by...`
`find_element_by_id` - searching by elm unique id 
`find_element_by_css_selector` - searching by css selector
`find_element_by_xpath` - search by elm xpath
`find_element_by_name` — search ny attribute name
`find_element_by_tag_name` — search elm by tag;
`find_element_by_class_name` — search elm by attribute class;
`find_element_by_link_text` — searching a link in web page;
`find_element_by_partial_link_text` — searching for a link in page, if selector's text partial 

## `driver.find_element(By.ID,"submit-button")`
`By.ID` – поиск по уникальному атрибуту id элемента   
`By.CSS_SELECTOR` – поиск элементов с помощью правил на основе CSS   
`By.XPATH` – поиск элементов с помощью языка запросов XPath      
`By.NAME` – поиск по атрибуту name элемента    
`By.TAG_NAME` – поиск по названию тега  
`By.CLASS_NAME` – поиск по атрибуту class элемента
`By.LINK_TEXT` – поиск ссылки с указанным текстом
`By.PARTIAL_LINK_TEXT` – поиск ссылки по частичному совпадению текст

### Example template
    # подготовка для теста
    # открываем страницу первого товара
    # данный сайт не существует, этот код приведен только для примера
    browser.get("https://fake-shop.com/book1.html")
    
    # добавляем товар в корзину
    add_button = browser.find_element_by_css_selector(".add")
    add_button.click()
    
    # открываем страницу второго товара
    browser.get("https://fake-shop.com/book2.html")
    
    # добавляем товар в корзину
    add_button = browser.find_element_by_css_selector(".add")
    add_button.click()
    
    # тестовый сценарий
    # открываем корзину
    browser.get("https://fake-shop.com/basket.html")
    
    # ищем все добавленные товары
    goods = browser.find_elements_by_css_selector(".good")
    
    # проверяем, что количество товаров равно 2
    assert len(goods) == 2

### Example registration assert
    from selenium import webdriver
    import time
    
    try: 
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
    
        # Ваш код, который заполняет обязательные поля
        ...
    
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
    
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
    
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
    
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
    
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

