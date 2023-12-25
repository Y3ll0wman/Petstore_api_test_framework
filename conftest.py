import pytest


@pytest.fixture
def api_url():
    return 'https://petstore.swagger.io/v2'


@pytest.fixture
def headers():
    headers = \
        {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
    return headers
