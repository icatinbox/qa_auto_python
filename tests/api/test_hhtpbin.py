def test_get_name(api_client):
    data = api_client.get_json('/get', params={'name': 'Ivan'})
    assert 'name' in data['args']
    assert data['args']["name"] == "Ivan"

# def test_404_error(api_client):
#     response = api_client.get_json('/status/404', raise_for_status=False)
#     assert response.status_code == 404

def test_api_headers(api_client):
    data = api_client.get_json('/headers')
    assert 'headers' in data
    accept_values = data['headers'].get('Accept')
    assert 'application/json' in accept_values

def test_api_post(api_client):
    data = api_client.post_json('/post', json={'title': 'hello', 'count': 3})
    assert data['json']['title'] == 'hello'
    assert data['json']['count'] == 3

def test_status_204(api_client):
    data = api_client.get_json('/status/204')
    assert data is None