import requests
import pytest


def test_get_name(api_client):
    response = api_client.get('/get', params={"name": "Ivan"})
    response.raise_for_status()
    data = response.json()
    assert 'name' in data['args']
    assert data['args']["name"] == "Ivan"

def test_404_error(api_client):
    response = api_client.get('/status/404')
    assert response.status_code == 404
    with pytest.raises(requests.HTTPError):
        response.raise_for_status()

def test_api_headers(api_client):
    response = api_client.get('/headers')
    response.raise_for_status()
    data = response.json()
    assert 'headers' in data
    accept_values = data['headers'].get('Accept')
    assert 'application/json' in accept_values