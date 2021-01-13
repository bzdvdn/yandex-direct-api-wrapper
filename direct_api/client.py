import requests
from time import sleep
from typing import Union, Optional

from .exceptions import YdAPIError
from .utils import generate_params, convert
from . import entities


class DirectAPI(object):
    API_URL = 'https://api.direct.yandex.com/json/v5/'

    def __init__(
        self, access_token: str, clid: str, refresh_token: str = '', lang: str = 'ru'
    ) -> None:
        """
        :param access_token: str
        :param clid: str
        :param refresh_token: str
        :param lang: str (ru, en, tr, uk)
        """
        self._access_token = access_token
        self._clid = clid
        self.refresh_token = refresh_token
        self._session = requests.Session()
        self._lang = lang
        self._session.headers['Accept'] = 'application/json'
        self._session.headers['Authorization'] = f'Bearer {self._access_token}'
        self._session.headers.update(
            {"Accept-Language": self._lang, "Client-Login": self._clid}
        )
        self.__generate_attrs_by_entities()

    def __generate_attrs_by_entities(self) -> None:
        for attr in entities.__all__:
            setattr(self, attr.lower(), property(getattr(entities, attr)(client=self)))

    def set_clid(self, clid: str) -> None:
        self._clid = clid
        self.set_session_headers({"Accept-Language": "ru", "Client-Login": clid})

    def set_session_headers(self, headers: dict) -> None:
        self._session.headers.update(**headers)

    def set_lang(self, lang: str) -> None:
        """
        :param lang: str (ru, en, tr, uk)
        :return: None
        """
        self._lang = lang
        self.set_session_headers({"Accept-Language": self._lang})

    def set_access_token(self, access_token: str) -> None:
        self._access_token = access_token
        self.set_session_headers({"Authorization": f'Bearer {self._access_token}'})

    @property
    def clid(self) -> str:
        return self._clid

    @property
    def lang(self) -> str:
        return self._lang

    @property
    def access_token(self) -> str:
        return self._access_token

    def _get_reports(self, params: dict) -> str:
        url = f'{self.API_URL}reports/'
        while True:
            req = self._session.post(url, json=params, timeout=10)
            req.encoding = 'utf-8'
            if req.status_code == 200:
                return req.content.decode('utf-8')
            elif req.status_code == 201:
                # print("Report apply to offline que")
                retryIn = int(req.headers.get("retryIn", 10))
                sleep(retryIn)
            elif req.status_code == 202:
                retryIn = int(req.headers.get("retryIn", 10))
                sleep(retryIn)
            else:
                error = req.json()['error']
                raise YdAPIError(error)

    def _send_api_request(
        self, service: str, method: str, params: dict, timeout: int = 30
    ) -> requests.Response:
        """
        :param service: str
        :param method: str
        :param params: dict
        :param timeout: int, default=30
        :return: response object
        """
        request_body = {'method': method, 'params': params}
        url = f'{self.API_URL}{service}'
        response = self._session.post(url, json=request_body, timeout=timeout)
        response.raise_for_status()
        if response.status_code > 204:
            error_data = response.json()
            raise YdAPIError(error_data['error'])
        return response
