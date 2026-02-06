import requests
import allure


def _attach_allure(url:str, response: requests.Response, json: dict | None = None, params: dict | None = None):
    allure.attach(url, name='requests URL', attachment_type=allure.attachment_type.TEXT)
    allure.attach(str(params), name='Request params', attachment_type=allure.attachment_type.TEXT)
    allure.attach(str(json), name='Request params', attachment_type=allure.attachment_type.JSON)
    allure.attach(str(response.status_code), name='Response status', attachment_type=allure.attachment_type.TEXT)
    allure.attach(str(response.text[:2000]), name='Response body first 2000 chars', attachment_type=allure.attachment_type.TEXT)


class ApiClient:
    def __init__(self, base_url:str, timeout:int=10):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({'Accept': 'application/json'})

    def get(self, path:str, params:dict=None, raise_for_status: bool = True) -> requests.Response:
        url = f'{self.base_url}/{path.lstrip("/")}'
        response = self.session.get(url, params=params, timeout=self.timeout)
        _attach_allure(url, response, params=params)
        if raise_for_status:
            response.raise_for_status()
        return response

    def post(self, path:str, json:dict | None = None, raise_for_status: bool = True) -> requests.Response:
        url = f'{self.base_url}/{path.lstrip("/")}'
        response = self.session.post(url, json=json, timeout=self.timeout)
        _attach_allure(url, response, json=json)
        if raise_for_status:
            response.raise_for_status()
        return response