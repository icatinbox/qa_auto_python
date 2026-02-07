

class ApiAuth:
    def __init__(self, client, email, password):
        self.client = client
        self.email = email
        self.password = password

    def login(self):
        payload = {'username': self.email, 'password': self.password}
        return self.client.request_json(method='POST', path='/auth/login', json=payload)