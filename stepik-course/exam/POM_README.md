# Что я понял?
`base_page.py` - тут мы храним методы которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать.

`locators.py` - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать

`main_page.py` - тут мы храним методы по конкретной странице, завернутые в класс этой странице. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py

И вот тут ступор. Файл test_main_page.py - тут мы выполняем сами тесты? по префиксу "test_" я понимаю что это для PyTest. Тут вызванные функции будут запускаться.

Здесь мы будем создавать функции, которым:

1. выдаём нужный для проверки линк
2. созаём в функции переменную page, которой передаём браузер из base_page.py(класс BasePage) и линк из шага №1
3. следом говорим "page, откройся", но методом из base_page.py(класс BasePage)
4. добавляем проверки, которые создавали методами в main_page.py


# Пример корректного кейса по ООП включая API тесты :
    @pytest.mark.login
    class TestLoginFromProductPage():
        @pytest.fixture(scope="function", autouse=True)
        def setup(self):
            self.product = ProductFactory(title = "Best book created by robot")
            # создаем по апи
            self.link = self.product.link
            yield
            # после этого ключевого слова начинается teardown
            # выполнится после каждого теста в классе
            # удаляем те данные, которые мы создали 
            self.product.delete()
            
    
        def test_guest_can_go_to_login_page_from_product_page(self, browser):
            page = ProductPage(browser, self.link)
            # дальше обычная реализация теста
    
        def test_guest_should_see_login_link(self, browser):
            page = ProductPage(browser, self.link)
            # дальше обычная реализация теста