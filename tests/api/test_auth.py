def test_auth_token(auth_token):
    assert auth_token is not None
    assert isinstance(auth_token, str)

def test_refresh_token(refresh_token):
    assert refresh_token is not None
    assert isinstance(refresh_token, str)

def test_me_request_no_auth(api_client):
    response = api_client.request('GET', '/auth/me')
    assert response.status_code == 401

def test_me_request_auth(client_auth, request):
    username = request.config.getoption('--username')
    data = client_auth.request_json('GET', '/auth/me')
    assert data['username'] == username