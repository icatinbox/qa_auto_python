import requests
import pytest
from src.api.assertions import assert_status_code

def test_get_name(api_client):
    response = api_client.get('/get', params={"name": "Ivan"})
    data = response.json()
    assert 'name' in data['args']
    assert data['args']["name"] == "Ivan"

def test_404_error(api_client):
    response = api_client.get('/status/404', raise_for_status=False)
    assert_status_code(response, 404)

def test_api_headers(api_client):
    response = api_client.get('/headers')
    data = response.json()
    assert 'headers' in data
    accept_values = data['headers'].get('Accept')
    assert 'application/json' in accept_values

def test_api_post(api_client):
    response = api_client.post('/post', json={'title': 'hello', 'count': 3})
    data = response.json()
    assert data['json']['title'] == 'hello'
    assert data['json']['count'] == 3

def test_status_204(api_client):
    response = api_client.get('/status/204')
    assert response.text == ''