import requests
from typing import Union, Optional

from .exceptions import YdAPIError
from .utils import generate_select_criteria


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
        self._session.headers.update({"Accept-Language": self._lang, "Client-Login": clid})

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
        url = f'{self.API_URL}{service}?json'
        response = self._session.post(url, json=request_body, timeout=timeout)
        response.raise_for_status()
        if response.status_code > 204:
            error_data = requests.json()
            raise YdAPIError(error_data['error'])
        return response

    def add_agency_client(self, login: str, first_name: str, last_name: str, currency: str,
                          grants: Optional[list] = None, notification: Optional[dict] = None,
                          settings: Optional[list] = None) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/agencyclients/add-docpage/
        :param login: str
        :param first_name: str
        :param last_name: str
        :param currency: str
        :param grants: list
        :param notification: optional dict
        :param settings: optional list
        :return: dict
        """
        params = {
            'Login': login,
            'FirstName': first_name,
            'LastName': last_name,
            'Currency': currency,
        }
        if grants is not None:
            params['Grants'] = grants
        if notification is not None:
            params['Notification'] = notification
        if settings is not None:
            params['Settings'] = settings
        return self._send_api_request('agencyclients', 'add', params).json()

    def get_agency_clients(self, fieldnames: list, logins: Optional[list] = None,
                           archived: Optional[str] = None, limit: int = 500, offset: int = 0) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/agencyclients/get-docpage/
        :param fieldnames: list
        :param logins: optional list
        :param archived: str (YES or NO)
        :param limit: int
        :param offset: int
        :return: dict
        """
        params = {
            'SelectionCriteria': generate_select_criteria(['logins', 'archived'], locals()),
            'FieldNames': fieldnames,
            'Page': {'Limit': limit, 'Offset': offset},
        }
        return self._send_api_request('agencyclients', 'get', params).json()

    def update_agency_client(self, clients: list) -> dict:
        """
        :param clients: list (list of Client object)
        :return: dict
        """
        params = {'Clients': clients}
        return self._send_api_request('agencyclients', 'update', params).json()

    def add_ad_extensions(self, ad_extensions: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adextensions/add-docpage/
        :param ad_extensions: list (List of AdExtensions objects)
        :return: dict
        """
        params = {'AdExtensions': ad_extensions}
        return self._send_api_request('adextensions', 'add', params).json()

    def delete_ad_extensions(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adextensions/delete-docpage/
        :param ids: list (AdExtension ids)
        :return: dict
        """
        params = {'SelectionCriteria': {'Ids': ids}}
        return self._send_api_request('adextensions', 'delete', params).json()

    def get_ad_extensions(self, fieldnames: list, ids: Optional[list] = None, types: Optional[list] = None,
                          states: Optional[list] = None, statuses: Optional[list] = None,
                          modify_since: Optional[str] = None, callout_fieldnames: Optional[list] = None,
                          limit: int = 500, offset: int = 0) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adextensions/get-docpage/
        :param fieldnames: list
        :param ids: optional list
        :param types: optional list
        :param states: optional list
        :param statuses: optional list
        :param modify_since: optional str
        :param callout_fieldnames: optional list
        :param limit: int
        :param offset: int
        :return: dict
        """
        params = {
            'SelectionCriteria': generate_select_criteria(
                ['ids', 'types', 'states', 'statuses', 'modify_since'],
                locals()),
            'FieldNames': fieldnames,
            'Page': {
                'Limit': limit,
                'Offset': offset,
            }
        }
        if callout_fieldnames is not None:
            params['CalloutFieldNames'] = callout_fieldnames
        return self._send_api_request('adextensions', 'update', params).json()
