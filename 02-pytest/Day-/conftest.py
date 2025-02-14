import pytest


@pytest.fixture(scope="session")
def open_close_browser():
    print("open the browser")
    yield
    print("close the browser")

@pytest.fixture(scope="module")
def access_return_value():
    print("access return value")
    return "true"