import pytest
from src.api.ApiAuth.api_auth import ApiAuth
from src.api.ApiProducts.api_products import ApiProducts
from src.api.client import ApiClient

def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://dummyjson.com",
        help="Base URL for API requests",
    ),
    parser.addoption(
        "--timeout",
        default=10,
        type=int,
        help="Timeout for API requests",
    ),
    parser.addoption(
        "--username",
        default="emilys",
        type=str,
    ),
    parser.addoption(
        "--password",
        default="emilyspass",
        type=str,
    )

@pytest.fixture
def api_client(request):
    base_url = request.config.getoption('--base-url')
    timeout = request.config.getoption('--timeout')
    client = ApiClient(base_url=base_url, timeout=timeout)
    yield client
    client.close_session()

@pytest.fixture
def tokens(api_client, request):
    email = request.config.getoption('--username')
    password = request.config.getoption('--password')
    auth = ApiAuth(api_client)
    data = auth.login(email, password)
    return {'access': data['accessToken'], 'refresh': data['refreshToken']}

@pytest.fixture
def client_auth(api_client, tokens):
    api_client.set_bearer_token(tokens['access'])
    return api_client

@pytest.fixture
def api_auth_auth(client_auth):
    return ApiAuth(client_auth)

@pytest.fixture
def api_auth_products(client_auth):
    return ApiProducts(client_auth)

@pytest.fixture
def id_product(api_auth_products):
    data = api_auth_products.get_all_products(params={'limit': 1})
    return data['products'][0]['id']