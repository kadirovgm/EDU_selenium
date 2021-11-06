import pytest

@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")  # один раз выполняется в классе
    yield
    print(":3", "\n")  # выполняется когда бразуер закрывается

@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")  # выполняется только когда вызовут

@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")  # выполняется на все методы

class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        print("test_first_smiling_faces")

    def test_second_smiling_faces(self, prepare_faces):
        print("test_second_smiling_faces")