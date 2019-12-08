from typing import Union, Optional
from .utils import generate_params, convert

__all__ = ['Ad', 'AdImage', 'AdExtension', 'AdGroup', 'Bid', 'AudienceTarget', 'AgencyClient']


class BaseEntity(object):
    def __init__(self, client: object, service: str = '') -> None:
        self.__client = client
        self.service = service

    def __str__(self) -> str:
        return f'{self.__class__.__name__} - endpoint: {self.service}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} - endpoint: {self.service}'

    def _execute_method_by_ids(self, method: str, ids: list) -> dict:
        """
        :param method: str ('delete', 'activate', 'archive', 'unarchive', 'suspend', 'resume')
        :param service: str
        :param ids: list
        :return: dict
        """
        params = {'SelectionCriteria': {'Ids': ids}}
        return self.__client._send_api_request(self.service.lower(), method, params).json()

    def _add(self, objects: list) -> dict:
        params = {
            self.service: objects
        }
        return self.client._send_api_request(self.service.lower(), 'add', params).json()

    def _update(self, objects: list) -> dict:
        params = {
            self.service: objects
        }
        return self.__client._send_api_request(self.service.lower(), 'update', params).json()

    def _get(self, params: dict) -> dict:
        return self.__client._send_api_request(self.service.lower(), 'get', params).json()

    def _delete(self, ids: list) -> dict:
        return self._execute_method_by_ids('delete', ids)


class AgencyClient(BaseEntity):
    def __init__(self, client: object, service='AgencyClients'):
        super().__init__(client, service)

    def add(self, login: str, first_name: str, last_name: str, currency: str,
            grants: Optional[list] = None, notification: Optional[dict] = None,
            settings: Optional[list] = None):
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
        return self.__client._send_api_request(self.service.lower(), 'add', params).json()

    def get(self, field_names: list, logins: Optional[list] = None,
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
        return self._get(params)

    def update(self, clients: list) -> dict:
        """
        :param clients: list (list of Client object)
        :return: dict
        """
        return self._update(clients)


class AdExtension(BaseEntity):
    def __init__(self, client: object, service: str = 'AdExtension') -> None:
        super().__init__(client, service)

    def add(self, ad_extensions: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adextensions/add-docpage/
        :param ad_extensions: list (List of AdExtensions objects)
        :return: dict
        """
        return self._add(ad_extensions)

    def delete(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adextensions/delete-docpage/
        :param ids: list (AdExtension ids)
        :return: dict
        """
        return self._delete(ids)

    def get(self, field_names: list, ids: Optional[list] = None, types: Optional[list] = None,
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
        return self._get(_params)


class AdGroup(BaseEntity):
    def __init__(self, client: object, service: str = 'AdGroups') -> None:
        super().__init__(client, service)

    def add(self, ad_groups: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adgroups/add-docpage/
        :param ad_groups: list (lit of AdGroups objects)
        :return: dict
        """
        return self._add(ad_groups)

    def delete(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adgroups/delete-docpage/
        :param ids: list (list of AdGroup ids)
        :return: dict
        """
        return self._delete(ids)

    def get(self, field_names: list, ids: Optional[list] = None, campaign_ids: Optional[list] = None,
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
        return self._get(params)

    def update(self, ad_groups: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adgroups/update-docpage/
        :param ad_groups: list (list of AdGroups object)
        :return: dict
        """
        return self._update(ad_groups)


class AdImage(BaseEntity):
    def __init__(self, client: object, service: str = 'AdImages') -> None:
        super().__init__(client, service)

    def add(self, ad_images: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adimages/add-docpage/
        :param ad_images: list (list of AdImage objects)
        :return: dict
        """
        return self._add(ad_images)

    def delete(self, hashes: list) -> dict:
        """
        :param hashes: list (list of image hashes)
        :return: dict
        """
        params = {
            'SelectionCriteria': {
                'AdImageHashes': hashes
            }
        }
        return self.__client._send_api_request(self.service.lower(), 'delete', params).json()

    def get(self, field_names: list, ad_images_hashes: Optional[list] = None,
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
        return self._get(params)


class Ad(BaseEntity):
    def __init__(self, client: object, service: str = 'Ads') -> None:
        super().__init__(client=client, service=service)

    def add(self, ads: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/add-docpage/
        :param ads: list (list of Ad objects)
        :return: dict
        """
        return self._add(ads)

    def archive(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/archive-docpage/
        :param ids: list (list of Ad ids)
        :return:
        """
        return self._execute_method_by_ids('archive', ids)

    def delete(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/delete-docpage/
        :param ids: list (list of Ad ids)
        :return: dict
        """
        return self._delete(ids)

    def get(self, field_names: list, ids: Optional[list] = None, campaign_ids: Optional[list] = None,
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
        return self._get(params)

    def moderate(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/moderate-docpage/
        :param ids: list (list of Ad objects)
        :return: dict
        """
        return self._execute_method_by_ids('moderate', ids)

    def resume(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/resume-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('resume', ids)

    def suspend(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/suspend-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('suspend', ids)

    def unarchive(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/unarchive-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('unarchive', ids)

    def update(self, ads: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/ads/update-docpage/
        :param ads: list
        :return: dict
        """
        return self._update(ads)


class AudienceTarget(BaseEntity):
    def __init__(self, client: object, service: str = 'AudienceTargets') -> None:
        super().__init__(client, service)

    def add(self, targets: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/audiencetargets/add-docpage/
        :param targets: list
        :return: dict
        """
        return self._add(targets)

    def delete(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/audiencetargets/delete-docpage/
        :param ids: list
        :return: dict
        """
        return self._delete(ids)

    def get_audience_targets(self, field_names: list, ids: Optional[list] = None,
                             ad_groups_ids: Optional[list] = None, campaign_ids: Optional[list] = None,
                             retargeting_list_ids: Optional[list] = None, interest_ids: Optional[list] = None,
                             states: Optional[list] = None, limit: int = 10000, offset: int = 0) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/audiencetargets/get-docpage/
        :param field_names: list
        :param ids: list
        :param ad_groups_ids: list
        :param campaign_ids: list
        :param retargeting_list_ids: list
        :param interest_ids: list
        :param states: list
        :param limit: int
        :param offset: int
        :return: dict
        """
        params = {
            'SelectCriteria': generate_params(
                fields=['ids', 'ad_groups_ids', 'campaign_ids', 'retargeting_list_ids', 'interest_ids', 'states'],
                function_kwargs=locals()
            ),
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset},
        }
        return self._get(params)

    def resume(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/audiencetargets/resume-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('resume', ids)

    def set_bids(self, bids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/audiencetargets/setBids-docpage/
        :param bids: list (list of Bid objects)
        :return: dict
        """
        params = {
            'Bids': bids
        }
        return self.__client._send_api_request(self.service.lower(), 'setBids', params).json()

    def suspend(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/audiencetargets/suspend-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('suspend', ids)


class Bid(BaseEntity):
    def __init_(self, client: object, service: str = 'Bids') -> None:
        super().__init__(client, service)

    def get(self, field_names: list, keyword_ids: Optional[list], ad_group_ids: Optional[list],
            campaign_ids: Optional[list] = None, serving_statuses: Optional[list] = None,
            limit: int = 10000, offset: int = 0) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/bids/get-docpage/
        :param field_names: list
        :param keyword_ids: list
        :param ad_group_ids: list
        :param campaign_ids: list
        :param serving_statuses: list
        :param limit: int
        :param offset: int
        :return: dict
        """
        params = {
            'SelectCriteria': generate_params(
                fields=['keyword_ids', 'ad_group_ids', 'campaign_ids', 'serving_statuses'],
                function_kwargs=locals()
            ),
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset},
        }
        return self._get(params)

    def set(self, bids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/bids/set-docpage/
        :param bids: list (list of Bid objects)
        :return: dict
        """
        params = {'Bids': bids}
        return self.__client._send_api_request('bids', 'set', params).json()

    def set_auto(self, bids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/bids/setAuto-docpage/
        :param bids: list (list of BidSetAutoItem)
        :return: dict
        """
        params = {'Bids': bids}
        return self.__client._send_api_request('bids', 'setAuto', params).json()
