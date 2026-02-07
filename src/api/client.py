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

    def set_bearer_token(self, token:str):
        self.session.headers.update({f'Authorization': f'Bearer {token}'})

    def request(self,
                method: str,
                path: str,
                params: dict | None = None,
                json: dict | None = None,
                headers: dict | None = None,
                ) -> requests.Response:
        url = f'{self.base_url}/{path.lstrip("/")}'
        return self.session.request(method=method, url=url, params=params, json=json, headers=headers, timeout=self.timeout)

    def request_json(self,
                     method: str,
                     path: str,
                     **kwargs):
        response = self.request(method=method, path=path, **kwargs)
        response.raise_for_status()
        return response.json()

    def close_session(self):
        self.session.close()