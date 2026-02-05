import pytest
from src.api.client import ApiClient

BASE_URL = 'https://httpbin.org'

@pytest.fixture
def user_data():
    return {'name': 'Ivan', 'age': 25}

@pytest.fixture
def api_client():
    return ApiClient(BASE_URL)
