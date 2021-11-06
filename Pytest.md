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


