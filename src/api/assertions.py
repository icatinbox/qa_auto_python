import requests

def assert_status_code(response:requests.Response, expected_status_code:int):
    assert response.status_code == expected_status_code, f'expected status {expected_status_code}, got {response.status_code}, body: {response.text[:200]}'