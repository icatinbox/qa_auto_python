import pytest
from src.api.client import ApiClient


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://httpbin.org",
        help="Base URL for API requests",
    ),
    parser.addoption(
        "--timeout",
        default=10,
        type=int,
        help="Timeout for API requests",
    )

@pytest.fixture
def api_client(request):
    base_url = request.config.getoption('--base-url')
    timeout = request.config.getoption('--timeout')
    client = ApiClient(base_url=base_url, timeout=timeout)
    yield client
    client.close_session()

