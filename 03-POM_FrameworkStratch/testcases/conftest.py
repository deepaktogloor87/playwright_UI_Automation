import pytest


@pytest.fixture(scope="session")
def user_data(request):
    return request.param