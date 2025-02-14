import pytest

@pytest.fixture(scope="function")
def access_return_value():
    print("access return value")
    return "true"