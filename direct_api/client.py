import requests
from typing import Union, Optional

class DirectAPI(object):
    def __init__(self, access_token: str, clid: str = '', refresh_token: str = '') -> None:
        self.access_token = access_token
        self.clid = clid
        self.refresh_token = refresh_token
        self.requests_session = requests.Session()
        self.requests_session.headers['Accept'] = 'application/json'
        self.requests_session.headers['Authorization'] = 'Bearer ' + self.access_token

    def send_api_request(self, method: str, service: str, params: dict) -> Union[dict, bytes]:
        pass