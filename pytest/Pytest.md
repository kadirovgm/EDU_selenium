# Pytest: advantages and disadvantages
### Pluses:
1. PyTest is fully backward compatible with the `unittest` and `nose` frameworks.
2. Detailed report
3. Py Test does not require writing additional specific constructs in tests, as required by unit test
4. Standart assert from Python used for checks
5. The ability to create dynamic fixtures (special functions that configure test environments and prepare test data).
6. Additional options for setting up fixtures
7. Parameterization of tests — different parameters can be set for one test (the test will run several times with different test data).
8. The presence of markings that allow marking tests for their selective launch.
9. The ability to pass additional parameters via the command line to configure test environments.
10. A large number of plugins that expand the capabilities of PyTest and allow you to solve highly specialized problems, which can save a lot of time.

### Minuses
1. PyTest требуется устанавливать дополнительно, так как он не входит в стандартный пакет библиотек Python, в отличие от unittest. Нужно не забывать об этом, когда вы будете настраивать автоматический запуск тестов с помощью CI-сервера.
2. Using PyTest requires a deeper understanding of Python to figure out how to apply fixtures, parameterization and other features of PyTest

# [Useful commands for Pytest](https://gist.github.com/amatellanes/12136508b816469678c2)

# [List of plagins](https://docs.pytest.org/en/latest/reference/plugin_list.html)

# Recommendations:
#### For cleaner terminal executing:
    $ pytest --tb=line -v

# Useful links
### Git
1. https://learngitbranching.js.org/ — отличный интерактивный туториал
2. https://git-scm.com/book/ru/v2/ — лучшая книга вообще 
3. https://hyperskill.org/learn/topic/257/﻿
4. https://stepik.org/course/4138/﻿
5. http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/ru/index.html
6. https://habr.com/company/intel/blog/344962/
7. https://githowto.com/ru
### Тестирование веб-приложений
1. https://realpython.com/python-testing/ — инструменты для тестирования кода в Python
2. [Пирамида тестов на практике](https://habr.com/ru/post/358950/)
3. [unittest — документация](https://docs.python.org/3/library/unittest.html)
### Тестирование с помощью PyTest
1. [Статья про PyTest](https://habr.com/ru/post/269759/)
3. [Документация PyTest](https://docs.pytest.org/en/latest/)
4. [Conventions for Python test discovery](https://docs.pytest.org/en/stable/goodpractices.html)
5. [Полезные флаги pytest](https://gist.github.com/amatellanes/12136508b816469678c2)
### Использование фикстур в PyTest
7. [Фикстуры — определение](https://en.wikipedia.org/wiki/Test_fixture#Software)
8. [Фикстуры в PyTest](https://docs.pytest.org/en/stable/fixture.html)
9. [setup и teardown методы](https://docs.pytest.org/en/stable/xunit_setup.html)
10. https://habr.com/ru/company/yandex/blog/242795/
11. https://medium.com/@dmrlx/%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-pytest-cc6175c7d0dc
12. [Skip and xfail: dealing with tests that cannot succeed](https://pytest.org/en/stable/skipping.html)
### Параметризация, конфигурирование, плагины
14. [Parametrizing fixtures and test functions](https://selenium-python.com/install-geckodriver)
15. [Инструкции по установке geckodriver](https://selenium-python.com/install-geckodriver)
16. [Передача параметров в PyTest из командной строки](https://docs.pytest.org/en/stable/example/simple.html?highlight=addoption)
17. [Список плагинов PyTest](https://docs.pytest.org/en/stable/plugins.html)
18. [Полный список доступных плагинов с описаниями](https://plugincompat.herokuapp.com/)
19. [Настройка вывода PyTest](https://docs.pytest.org/en/stable/usage.html#modifying-python-traceback-printing)