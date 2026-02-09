# import pytest
#
# def test_success_auth(api_client, request):
#     username =request.config.getoption('--username')
#     password = request.config.getoption('--password')
#     payload = {'username': username, 'password': password}
#     data = api_client.request_json('POST', '/auth/login', json=payload)
#     assert data['accessToken'] is not None
#     assert isinstance(data['accessToken'], str)
#     assert data['refreshToken'] is not None
#     assert isinstance(data['refreshToken'], str)
#
# def test_me_request_auth(api_auth_auth, request):
#     username = request.config.getoption('--username')
#     data = api_auth_auth.me()
#     assert data['username'] == username
#
# def test_success_refresh_token(api_auth_auth, tokens):
#     refresh_token = tokens['refresh']
#     data = api_auth_auth.refresh(refresh_token)
#     assert data['accessToken'] is not None
#     assert isinstance(data['accessToken'], str)
#     assert data['refreshToken'] is not None
#     assert isinstance(data['refreshToken'], str)
#
# @pytest.mark.xfail
# @pytest.mark.negative
# def test_fail_refresh_token(client_auth):
#     payload = {'refresh_token': 'invalid'}
#     response = client_auth.request('POST', path='/auth/refresh', json=payload)
#     assert response.status_code == 400
#
# @pytest.mark.negative
# def test_me_request_no_auth(api_client):
#     response = api_client.request('GET', '/auth/me')
#     assert response.status_code == 401
#
# @pytest.mark.negative
# def test_auth_with_incorrect_username(api_client, request):
#     password = request.config.getoption('--password')
#     payload = {'username': 'invalid', 'password': password}
#     response = api_client.request('POST', '/auth/login', json=payload)
#     assert response.status_code == 400
#
# @pytest.mark.negative
# def test_auth_with_incorrect_password(api_client, request):
#     username = request.config.getoption('--username')
#     payload = {'username': username, 'password': 'invalid'}
#     response = api_client.request('POST', '/auth/login', json=payload)
#     assert response.status_code == 400