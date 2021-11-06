# Fixtures
#### Важной составляющей в использовании PyTest является концепция фикстур. 
#### Фикстуры в контексте PyTest — это вспомогательные функции для наших тестов, которые не являются частью тестового сценария.

Классический способ работы с фикстурами — создание `setup-` и `teardown-` методов в файле с тестами [документация в PyTest](https://docs.pytest.org/en/latest/how-to/xunit_setup.html?highlight=teardown).

### Запуск pytest с выводом print() в консоль:
    $ pytest -s test_fixture1.py
    $ pytest -v -s --tb=line


   
    