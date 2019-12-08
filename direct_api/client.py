import requests
from typing import Union, Optional

from .exceptions import YdAPIError
from .utils import generate_params, convert


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

    def _add_or_update(self, service: str, objects: list, update: bool = False) -> dict:
        """
        :param service: str
        :param objects: list
        :param update: bool
        :return: dict
        """
        service = convert(service)
        params = {service: objects}
        method = 'update' if update else 'add'
        return self._send_api_request(service.lower(), method, params).json()

    def _execute_method_by_ids(self, service: str, method: str, ids: list) -> dict:
        """
        :param method: str ('delete', 'activate', 'archive', 'unarchive', 'suspend')
        :param service: str
        :param ids: list
        :return: dict
        """
        params = {'SelectionCriteria': {'Ids': ids}}
        return self._send_api_request(service, method, params).json()

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

    def get_agency_clients(self, field_names: list, logins: Optional[list] = None,
                           archived: Optional[str] = None, limit: int = 500, offset: int = 0) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/agencyclients/get-docpage/
        :param field_names: list
        :param logins: optional list
        :param archived: str (YES or NO)
        :param limit: int
        :param offset: int
        :return: dict
        """
        params = {
            'SelectionCriteria': generate_params(['logins', 'archived'], locals()),
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset},
        }
        return self._send_api_request('agencyclients', 'get', params).json()

    def update_agency_client(self, clients: list) -> dict:
        """
        :param clients: list (list of Client object)
        :return: dict
        """
        return self._add_or_update('AgencyClients', clients, update=True)

    def add_ad_extensions(self, ad_extensions: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adextensions/add-docpage/
        :param ad_extensions: list (List of AdExtensions objects)
        :return: dict
        """
        return self._add_or_update('AdExtensions', ad_extensions, update=False)

    def delete_ad_extensions(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adextensions/delete-docpage/
        :param ids: list (AdExtension ids)
        :return: dict
        """
        return self._execute_method_by_ids('adextensions', 'delete', ids)

    def get_ad_extensions(self, field_names: list, ids: Optional[list] = None, types: Optional[list] = None,
                          states: Optional[list] = None, statuses: Optional[list] = None,
                          modify_since: Optional[str] = None, callout_field_names: Optional[list] = None,
                          limit: int = 500, offset: int = 0) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adextensions/get-docpage/
        :param field_names: list
        :param ids: optional list
        :param types: optional list
        :param states: optional list
        :param statuses: optional list
        :param modify_since: optional str
        :param callout_field_names: optional list
        :param limit: int
        :param offset: int
        :return: dict
        """
        params = {
            'SelectionCriteria': generate_params(
                ['ids', 'types', 'states', 'statuses', 'modify_since'],
                locals()),
            'FieldNames': field_names,
            'Page': {
                'Limit': limit,
                'Offset': offset,
            }
        }
        if callout_field_names is not None:
            params['CalloutFieldNames'] = callout_field_names
        return self._send_api_request('adextensions', 'update', params).json()

    def add_ad_groups(self, ad_groups: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adgroups/add-docpage/
        :param ad_groups: list (lit of AdGroups objects)
        :return: dict
        """
        return self._add_or_update('AdGroups', ad_groups, update=False)

    def delete_ad_groups(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adgroups/delete-docpage/
        :param ids: list (list of AdGroup ids)
        :return: dict
        """
        return self._execute_method_by_ids('AdGroups', 'delete', ids)

    def get_ad_groups(self, field_names: list, ids: Optional[list] = None, campaign_ids: Optional[list] = None,
                      types: Optional[list] = None, statuses: Optional[list] = None,
                      serving_statuses: Optional[list] = None, app_icon_statuses: Optional[list] = None,
                      negative_keyword_shared_set_ids: Optional[list] = None, limit: int = 500,
                      offset: int = 0, mobile_app_ad_group_field_names: Optional[list] = None,
                      dynamic_text_ad_group_field_names: Optional[list] = None,
                      dynamic_text_feed_ad_group_field_names: Optional[list] = None) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adgroups/get-docpage/
        :param field_names: list (list of fields)
        :param ids: list (list of AdGroups ids)
        :param campaign_ids: list (list of campaign ids)
        :param types: list (list of types)
        :param statuses: list (list of statuses)
        :param serving_statuses: list (list of serving statuses)
        :param app_icon_statuses: list (list of app icon statuses)
        :param negative_keyword_shared_set_ids: list (list of keyword ids)
        :param mobile_app_ad_group_field_names: list (list of mobile ids field_names)
        :param dynamic_text_ad_group_field_names: list (list of dynamic ids field_names)
        :param dynamic_text_feed_ad_group_field_names: list (list of dynamic feed ids field_names)
        :param limit int
        :param offset int
        :return: dict
        """
        params = {
            'SelectionCriteria': generate_params(
                ['campaign_ids', 'ids', 'types', 'statuses', 'serving_statuses',
                 'app_icon_statuses', 'negative_keyword_shared_set_ids'], locals()
            ),
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset}
        }
        if mobile_app_ad_group_field_names is not None:
            params['MobileAppAdGroupFieldNames'] = mobile_app_ad_group_field_names
        if dynamic_text_ad_group_field_names is not None:
            params['DynamicTextAdGroupFieldNames'] = dynamic_text_ad_group_field_names
        if dynamic_text_feed_ad_group_field_names is not None:
            params['DynamicTextFeedAdGroupFieldNames'] = dynamic_text_feed_ad_group_field_names
        return self._send_api_request('adgroups', 'get', params).json()

    def update_ad_group(self, ad_groups: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adgroups/update-docpage/
        :param ad_groups: list (list of AdGroups object)
        :return: dict
        """
        return self._add_or_update('AdGroups', ad_groups, update=True)

    def add_ad_images(self, ad_images: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adimages/add-docpage/
        :param ad_images: list (list of AdImage objects)
        :return: dict
        """
        return self._add_or_update('AdImages', ad_images, update=False)

    def delete_ad_images(self, hashes: list) -> dict:
        """
        :param hashes: list (list of image hashes)
        :return: dict
        """
        params = {
            'SelectionCriteria': {
                'AdImageHashes': hashes
            }
        }
        return self._send_api_request('adimages', 'delete', params).json()

    def get_ad_images(self, field_names: list, ad_images_hashes: Optional[list] = None,
                      associated: Optional[str] = None, limit: int = 500, offset: int = 0) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adimages/get-docpage/
        :param field_names: list (list of field_names)
        :param ad_images_hashes: list (list of hashes)
        :param associated: str (YES or NO)
        :param limit: int
        :param offset: int
        :return: dict
        """
        params = {
            'SelectionCriteria': generate_params(['ad_images_hashes', 'associated'], locals()),
            'FieldNames': field_names,
            'Page': {
                'Limit': limit,
                'Offset': offset,
            }
        }
        return self._send_api_request('adimages', 'get', params).json()

    def add_ads(self, ads: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/add-docpage/
        :param ads: list (list of Ad objects)
        :return: dict
        """
        return self._add_or_update('Ads', ads, update=False)

    def archive_ads(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/archive-docpage/
        :param ids: list (list of Ad ids)
        :return:
        """
        return self._execute_method_by_ids('ads', 'archive', ids)

    def delete_ads(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/delete-docpage/
        :param ids: list (list of Ad ids)
        :return: dict
        """
        return self._execute_method_by_ids('ads', 'delete', ids)

    def get_ads(self, field_names: list, ids: Optional[list] = None, campaign_ids: Optional[list] = None,
                ad_group_ids: Optional[list] = None, states: Optional[list] = None, statuses: Optional[list] = None,
                types: Optional[list] = None, mobile: Optional[str] = None, v_card_ids: Optional[list] = None,
                sitelink_set_ids: Optional[list] = None, ad_image_hashes: Optional[list] = None,
                v_card_moderation_statuses: Optional[list] = None, sitelink_moderation_statuses: Optional[list] =
                None, ad_image_moderation_statuses: Optional[list] = None, ad_extension_ids: Optional[list] = None,
                text_ad_field_names: Optional[list] = None, text_ad_price_extension_field_names: Optional[list] =
                None, mobile_app_field_names: Optional[list] = None, dynamic_text_ad_field_names: Optional[list] =
                None, mobile_app_image_ad_field_names: Optional[list] = None,
                text_ad_builder_ad_field_names: Optional[list] = None,
                mobile_app_ad_builder_ad_field_names: Optional[list] = None,
                cpc_video_ad_builder_ad_field_names: Optional[list] = None,
                cpm_banner_ad_builder_ad_field_names: Optional[list] = None,
                cpm_video_ad_builder_ad_field_names: Optional[list] = None,
                limit: int = 10000, offset: int = 0) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/get-docpage/
        :param field_names: list
        :param ids: list
        :param campaign_ids: list
        :param ad_group_ids: list
        :param states: list
        :param statuses: list
        :param types: list
        :param mobile: str
        :param v_card_ids: list
        :param sitelink_set_ids: list
        :param ad_image_hashes: list
        :param v_card_moderation_statuses: list
        :param sitelink_moderation_statuses: list
        :param ad_image_moderation_statuses: list
        :param ad_extension_ids: list
        :param text_ad_field_names: list
        :param text_ad_price_extension_field_names: list
        :param mobile_app_field_names: list
        :param dynamic_text_ad_field_names: list
        :param mobile_app_image_ad_field_names: list
        :param text_ad_builder_ad_field_names: list
        :param mobile_app_ad_builder_ad_field_names: list
        :param cpc_video_ad_builder_ad_field_names: list
        :param cpm_banner_ad_builder_ad_field_names: list
        :param cpm_video_ad_builder_ad_field_names: list
        :param limit: int
        :param offset: int
        :return: dict
        """
        local_variables = locals()
        params = {
            'SelectionCriteria': generate_params(
                fields=['ids', 'campaign_ids', 'ad_group_ids', 'states', 'statuses',
                        'types', 'mobile', 'v_card_ids', 'sitelink_set_ids', 'ad_image_hashes',
                        'v_card_moderation_statuses', 'sitelink_moderation_statuses', 'ad_image_moderation_statuses',
                        'ad_extension_ids'],
                function_kwargs=local_variables
            ),
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset}
        }
        params.update(
            generate_params(
                fields=['text_ad_field_names', 'text_ad_price_extension_field_names', 'mobile_app_field_names',
                        'dynamic_text_ad_field_names', 'mobile_app_image_ad_field_names',
                        'text_ad_builder_ad_field_names', 'mobile_app_ad_builder_ad_field_names',
                        'cpc_video_ad_builder_ad_field_names', 'cpm_banner_ad_builder_ad_field_names',
                        'cpm_video_ad_builder_ad_field_names'],
                function_kwargs=local_variables
            )
        )
        return self._send_api_request('ads', 'get', params).json()

    def moderate_ads(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/moderate-docpage/
        :param ids: list (list of Ad objects)
        :return: dict
        """
        return self._execute_method_by_ids('ads', 'moderate', ids)

    def resume_ads(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/resume-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('ads', 'resume', ids)

    def suspend_ads(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/suspend-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('suspend', 'resume', ids)

    def unarchive_ads(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/unarchive-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('suspend', 'unarchive', ids)

    def update_ads(self, ads: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/update-docpage/
        :param ads: list
        :return: dict
        """
        return self._add_or_update('Ads', ads, update=True)
