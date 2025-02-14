import pytest

@pytest.fixture(scope="module")
def access_return_value():
    print("access return value")
    return "true"