import requests
from typing import Union, Optional

from .exceptions import YdAPIError
from .utils import generate_params, convert
from . import entities


class DirectAPI(object):
    API_URL = 'https://api.direct.yandex.com/json/v5/'

    def __init__(self, access_token: str, clid: str, refresh_token: str = '', lang: str = 'ru') -> None:
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
        self._session.headers.update({"Accept-Language": self._lang, "Client-Login": self._clid})
        self.__generate_attrs_by_entities()

    def __generate_attrs_by_entities(self) -> None:
        for attr in entities.__all__:
            setattr(self, attr.lower(), property(getattr(entities, attr)(client=self)))

    def set_clid(self, clid: str) -> None:
        self._clid = clid
        self._session.headers.update({"Accept-Language": "ru", "Client-Login": clid})

    def set_lang(self, lang: str) -> None:
        """
        :param lang: str (ru, en, tr, uk)
        :return: None
        """
        self._lang = lang
        self._session.headers["Accept-Language"] = self._lang

    def set_access_token(self, access_token: str) -> None:
        self._access_token = access_token
        self._session.headers['Authorization'] = f'Bearer {self._access_token}'

    @property
    def clid(self) -> str:
        return self._clid

    @property
    def lang(self) -> str:
        return self._lang

    @property
    def access_token(self) -> str:
        return self._access_token

    def _send_api_request(self, service: str, method: str, params: dict) -> requests.Response:
        """
        :param service: str
        :param method: str
        :param params: dict
        :return: response object
        """
        request_body = {'method': method, 'params': params}
        url = f'{self.API_URL}{service}'
        response = self._session.post(url, json=request_body, timeout=timeout)
        response.raise_for_status()
        if response.status_code > 204:
            error_data = requests.json()
            raise YdAPIError(error_data['error'])
        return response
