import requests
import allure


def _attach_allure(url:str, response: requests.Response, json: dict | None = None, params: dict | None = None):
    allure.attach(url, name='requests URL', attachment_type=allure.attachment_type.TEXT)
    if params is not None:
        allure.attach(str(params), name='Request params', attachment_type=allure.attachment_type.TEXT)
    if json is not None:
        allure.attach(str(json), name='Request json', attachment_type=allure.attachment_type.TEXT)
    allure.attach(str(response.status_code), name='Response status', attachment_type=allure.attachment_type.TEXT)
    allure.attach(str(response.text[:2000]), name='Response body first 2000 chars', attachment_type=allure.attachment_type.TEXT)


class ApiClient:
    def __init__(self, base_url:str, timeout:int=10):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({'Accept': 'application/json'})

    def get(self, url:str, params:dict=None, raise_for_status: bool = True) -> requests.Response:
        response = self.session.get(url, params=params, timeout=self.timeout)
        _attach_allure(url, response, params=params)
        if raise_for_status:
            response.raise_for_status()
        return response

    def post(self, url:str, json:dict | None = None, raise_for_status: bool = True) -> requests.Response:
        response = self.session.post(url, json=json, timeout=self.timeout)
        _attach_allure(url, response, json=json)
        if raise_for_status:
            response.raise_for_status()
        return response

    @staticmethod
    def json(response:requests.Response):
        if response.status_code == 204:
            return None
        if response.text.strip() == "":
            return None
        try:
            return response.json()
        except Exception as e:
            raise AssertionError(f'Response is not json: status={response.status_code}, response={response.text[:200]}') from e

    def get_json(self, path:str, params:dict=None, raise_for_status:bool = True):
        url = f'{self.base_url}/{path.lstrip("/")}'
        response = self.get(url, params=params, raise_for_status=raise_for_status)
        return ApiClient.json(response)

    def post_json(self, path:str, json:dict | None = None, raise_for_status:bool = True):
        url = f'{self.base_url}/{path.lstrip("/")}'
        response = self.post(url, json=json, raise_for_status=raise_for_status)
        return ApiClient.json(response)

    def close_session(self):
        self.session.close()