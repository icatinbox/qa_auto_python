import requests


class ApiClient:
    def __init__(self, base_url:str, timeout:int=10):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({'Accept': 'application/json'})

    def get(self, path:str, params:dict=None) -> requests.Response:
        url = f'{self.base_url}/{path.lstrip("/")}'
        return self.session.get(url, params=params, timeout=self.timeout)