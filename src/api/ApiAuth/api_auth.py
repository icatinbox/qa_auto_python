

class ApiAuth:
    def __init__(self, client):
        self.client = client

    def login(self, email, password):
        payload = {'username': email, 'password': password}
        return self.client.request_json(method='POST', path='/auth/login', json=payload)

    def refresh(self, refresh_token):
        payload = {'refresh_token': refresh_token}
        return self.client.request_json(method='POST', path='/auth/refresh', json=payload)

    def me(self):
        return self.client.request_json(method='GET', path='/auth/me')