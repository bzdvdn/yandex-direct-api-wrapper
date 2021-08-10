from typing import Optional, TYPE_CHECKING
from abc import ABC

from .utils import generate_params, convert
from .exceptions import ParameterError

if TYPE_CHECKING:
    from .client import DirectAPI

__all__ = (
    'Ad',
    'AdImage',
    'AdExtension',
    'AdGroup',
    'Bid',
    'AudienceTarget',
    'AgencyClient',
    'BidsModifier',
    'Campaign',
    'Change',
    'Dictionary',
    'DynamicTextAdTarget',
    'KeywordBid',
    'Keyword',
    'Lead',
    'NegativeKeywordSharedSet',
    'Sitelink',
    'KeywordsResearch',
    'RetargetingList',
    'VCard',
    'TurboPage',
    'Report',
    'Client',
)


class BaseEntity(ABC):
    service: str = ''

    def __init__(self, client: 'DirectAPI') -> None:
        self._client = client

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
        return self._client._send_api_request(
            self.service.lower(), method, params
        ).json()

    def _add(self, objects: list) -> dict:
        params = {self.service: objects}
        return self._client._send_api_request(
            self.service.lower(), 'add', params
        ).json()

    def _update(self, objects: list) -> dict:
        params = {self.service: objects}
        return self._client._send_api_request(
            self.service.lower(), 'update', params
        ).json()

    def _get(self, params: dict) -> dict:
        return self._client._send_api_request(
            self.service.lower(), 'get', params
        ).json()

    def _delete(self, ids: list) -> dict:
        return self._execute_method_by_ids('delete', ids)


class AgencyClient(BaseEntity):
    service: str = 'AgencyClients'

    def add(
        self,
        login: str,
        first_name: str,
        last_name: str,
        currency: str,
        grants: Optional[list] = None,
        notification: Optional[dict] = None,
        settings: Optional[list] = None,
    ):
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
        params: dict = {
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
        return self._client._send_api_request(
            self.service.lower(), 'add', params
        ).json()

    def get(
        self,
        field_names: list,
        logins: Optional[list] = None,
        archived: Optional[str] = None,
        limit: int = 500,
        offset: int = 0,
    ) -> dict:
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
        doc - https://yandex.ru/dev/direct/doc/ref-v5/agencyclients/update.html
        :param clients: list (list of Client object)
        :return: dict
        """
        return self._update(clients)


class AdExtension(BaseEntity):
    service: str = 'AdExtension'

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

    def get(
        self,
        field_names: list,
        ids: Optional[list] = None,
        types: Optional[list] = None,
        states: Optional[list] = None,
        statuses: Optional[list] = None,
        modify_since: Optional[str] = None,
        callout_field_names: Optional[list] = None,
        limit: int = 500,
        offset: int = 0,
    ) -> dict:
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
                ['ids', 'types', 'states', 'statuses', 'modify_since'], locals()
            ),
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset,},
        }
        if callout_field_names is not None:
            params['CalloutFieldNames'] = callout_field_names
        return self._get(params)


class AdGroup(BaseEntity):
    service: str = 'AdGroups'

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

    def get(
        self,
        field_names: list,
        ids: Optional[list] = None,
        campaign_ids: Optional[list] = None,
        types: Optional[list] = None,
        statuses: Optional[list] = None,
        serving_statuses: Optional[list] = None,
        app_icon_statuses: Optional[list] = None,
        negative_keyword_shared_set_ids: Optional[list] = None,
        limit: int = 500,
        offset: int = 0,
        mobile_app_ad_group_field_names: Optional[list] = None,
        dynamic_text_ad_group_field_names: Optional[list] = None,
        dynamic_text_feed_ad_group_field_names: Optional[list] = None,
    ) -> dict:
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
        if not ids and not campaign_ids:
            raise ParameterError(['ids', 'campaign_ids'])

        params = {
            'SelectionCriteria': generate_params(
                [
                    'campaign_ids',
                    'ids',
                    'types',
                    'statuses',
                    'serving_statuses',
                    'app_icon_statuses',
                    'negative_keyword_shared_set_ids',
                ],
                locals(),
            ),
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset},
        }
        if mobile_app_ad_group_field_names is not None:
            params['MobileAppAdGroupFieldNames'] = mobile_app_ad_group_field_names
        if dynamic_text_ad_group_field_names is not None:
            params['DynamicTextAdGroupFieldNames'] = dynamic_text_ad_group_field_names
        if dynamic_text_feed_ad_group_field_names is not None:
            params[
                'DynamicTextFeedAdGroupFieldNames'
            ] = dynamic_text_feed_ad_group_field_names
        return self._get(params)

    def update(self, ad_groups: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adgroups/update-docpage/
        :param ad_groups: list (list of AdGroups object)
        :return: dict
        """
        return self._update(ad_groups)


class AdImage(BaseEntity):
    service: str = 'AdImages'

    def add(self, ad_images: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adimages/add-docpage/
        :param ad_images: list (list of AdImage objects)
        :return: dict
        """
        return self._add(ad_images)

    def delete(self, hashes: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/adimages/delete.html
        :param hashes: list (list of image hashes)
        :return: dict
        """
        params = {'SelectionCriteria': {'AdImageHashes': hashes}}
        return self._client._send_api_request(
            self.service.lower(), 'delete', params
        ).json()

    def get(
        self,
        field_names: list,
        ad_images_hashes: Optional[list] = None,
        associated: Optional[str] = None,
        limit: int = 500,
        offset: int = 0,
    ) -> dict:
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
            'SelectionCriteria': generate_params(
                ['ad_images_hashes', 'associated'], locals()
            ),
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset,},
        }
        return self._get(params)


class Ad(BaseEntity):
    service: str = 'Ads'

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

    def get(
        self,
        field_names: list,
        ids: Optional[list] = None,
        campaign_ids: Optional[list] = None,
        ad_group_ids: Optional[list] = None,
        states: Optional[list] = None,
        statuses: Optional[list] = None,
        types: Optional[list] = None,
        mobile: Optional[str] = None,
        v_card_ids: Optional[list] = None,
        sitelink_set_ids: Optional[list] = None,
        ad_image_hashes: Optional[list] = None,
        v_card_moderation_statuses: Optional[list] = None,
        sitelink_moderation_statuses: Optional[list] = None,
        ad_image_moderation_statuses: Optional[list] = None,
        ad_extension_ids: Optional[list] = None,
        text_ad_field_names: Optional[list] = None,
        text_ad_price_extension_field_names: Optional[list] = None,
        mobile_app_field_names: Optional[list] = None,
        dynamic_text_ad_field_names: Optional[list] = None,
        mobile_app_image_ad_field_names: Optional[list] = None,
        text_ad_builder_ad_field_names: Optional[list] = None,
        mobile_app_ad_builder_ad_field_names: Optional[list] = None,
        cpc_video_ad_builder_ad_field_names: Optional[list] = None,
        cpm_banner_ad_builder_ad_field_names: Optional[list] = None,
        cpm_video_ad_builder_ad_field_names: Optional[list] = None,
        limit: int = 10000,
        offset: int = 0,
    ) -> dict:
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
        if not ids and not ad_group_ids and not campaign_ids:
            raise ParameterError(['ids', 'ad_group_ids', 'campaign_ids'])

        local_variables = locals()
        params = {
            'SelectionCriteria': generate_params(
                fields=[
                    'ids',
                    'campaign_ids',
                    'ad_group_ids',
                    'states',
                    'statuses',
                    'types',
                    'mobile',
                    'v_card_ids',
                    'sitelink_set_ids',
                    'ad_image_hashes',
                    'v_card_moderation_statuses',
                    'sitelink_moderation_statuses',
                    'ad_image_moderation_statuses',
                    'ad_extension_ids',
                ],
                function_kwargs=local_variables,
            ),
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset},
        }
        params.update(
            generate_params(
                fields=[
                    'text_ad_field_names',
                    'text_ad_price_extension_field_names',
                    'mobile_app_field_names',
                    'dynamic_text_ad_field_names',
                    'mobile_app_image_ad_field_names',
                    'text_ad_builder_ad_field_names',
                    'mobile_app_ad_builder_ad_field_names',
                    'cpc_video_ad_builder_ad_field_names',
                    'cpm_banner_ad_builder_ad_field_names',
                    'cpm_video_ad_builder_ad_field_names',
                ],
                function_kwargs=local_variables,
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
    service: str = 'AudienceTargets'

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

    def get_audience_targets(
        self,
        field_names: list,
        ids: Optional[list] = None,
        ad_group_ids: Optional[list] = None,
        campaign_ids: Optional[list] = None,
        retargeting_list_ids: Optional[list] = None,
        interest_ids: Optional[list] = None,
        states: Optional[list] = None,
        limit: int = 10000,
        offset: int = 0,
    ) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/audiencetargets/get-docpage/
        :param field_names: list
        :param ids: list
        :param ad_group_ids: list
        :param campaign_ids: list
        :param retargeting_list_ids: list
        :param interest_ids: list
        :param states: list
        :param limit: int
        :param offset: int
        :return: dict
        """
        if not ids and not ad_group_ids and not campaign_ids:
            raise ParameterError(['ids', 'ad_group_ids', 'campaign_ids'])

        params = {
            'SelectionCriteria': generate_params(
                fields=[
                    'ids',
                    'ad_groups_ids',
                    'campaign_ids',
                    'retargeting_list_ids',
                    'interest_ids',
                    'states',
                ],
                function_kwargs=locals(),
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
        params = {'Bids': bids}
        return self._client._send_api_request(
            self.service.lower(), 'setBids', params
        ).json()

    def suspend(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/audiencetargets/suspend-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('suspend', ids)


class Bid(BaseEntity):
    service: str = 'Bids'

    def get(
        self,
        field_names: list,
        keyword_ids: Optional[list],
        ad_group_ids: Optional[list],
        campaign_ids: Optional[list] = None,
        serving_statuses: Optional[list] = None,
        limit: int = 10000,
        offset: int = 0,
    ) -> dict:
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
        if not keyword_ids and not ad_group_ids and not campaign_ids:
            raise ParameterError(['keyword_ids', 'ad_group_ids', 'campaign_ids'])

        params = {
            'SelectionCriteria': generate_params(
                fields=[
                    'keyword_ids',
                    'ad_group_ids',
                    'campaign_ids',
                    'serving_statuses',
                ],
                function_kwargs=locals(),
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
        return self._client._send_api_request('bids', 'set', params).json()

    def set_auto(self, bids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/bids/setAuto-docpage/
        :param bids: list (list of BidSetAutoItem)
        :return: dict
        """
        params = {'Bids': bids}
        return self._client._send_api_request('bids', 'setAuto', params).json()


class BidsModifier(BaseEntity):
    service: str = 'BidsModifiers'

    def add(self, bid_modifiers: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/bidmodifiers/add-docpage/
        :param bid_modifiers: list
        :return: dict
        """
        return self._add(bid_modifiers)

    def delete(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/bidmodifiers/delete-docpage/
        :param ids: list
        :return: dict
        """
        return self._delete(ids)

    def get(
        self,
        field_names: list,
        ids: Optional[list] = None,
        campaign_ids: Optional[list] = None,
        ad_group_ids: Optional[list] = None,
        types: Optional[list] = None,
        levels: Optional[list] = None,
        mobile_adjustment_field_names: Optional[list] = None,
        desktop_adjustment_field_names: Optional[list] = None,
        demographics_adjustment_field_names: Optional[list] = None,
        retargeting_adjustment_field_names: Optional[list] = None,
        regional_adjustment_field_names: Optional[list] = None,
        video_adjustment_field_names: Optional[list] = None,
        limit: int = 10000,
        offset: int = 0,
    ) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/bidmodifiers/get-docpage/
        :param field_names: list
        :param ids: list
        :param campaign_ids: list
        :param ad_group_ids: list
        :param types: list
        :param levels: list
        :param mobile_adjustment_field_names: list
        :param desktop_adjustment_field_names: list
        :param demographics_adjustment_field_names: list
        :param retargeting_adjustment_field_names: list
        :param regional_adjustment_field_names: list
        :param video_adjustment_field_names: list
        :param limit: int
        :param offset: int
        :return: dict
        """
        if not ids and not campaign_ids and not ad_group_ids:
            raise ParameterError(['ids', 'campaign_ids', 'ad_group_ids'])

        local_variables = locals()
        params = {
            'SelectionCriteria': generate_params(
                fields=['ids', 'campaign_ids', 'ad_group_ids', 'types', 'levels'],
                function_kwargs=local_variables,
            ),
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset},
        }
        params.update(
            generate_params(
                fields=[
                    'mobile_adjustment_field_names',
                    'desktop_adjustment_field_names',
                    'demographics_adjustment_field_names',
                    'retargeting_adjustment_field_names',
                    'regional_adjustment_field_names',
                    'video_adjustment_field_names',
                ],
                function_kwargs=local_variables,
            )
        )
        return self._get(params)

    def set(self, bid_modifiers: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/bidmodifiers/set-docpage/
        :param bid_modifiers: list
        :return: dict
        """
        params = {'BidModifiers': bid_modifiers}
        return self._client._send_api_request(
            self.service.lower(), 'set', params
        ).json()

    def toggle(self, bid_modifier_toggle_items: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/bidmodifiers/toggle-docpage/
        :param bid_modifier_toggle_items: list
        :return: dict
        """
        params = {'BidModifierToggleItems': bid_modifier_toggle_items}
        return self._client._send_api_request(
            self.service.lower(), 'toggle', params
        ).json()


class Campaign(BaseEntity):
    service: str = 'Campaigns'

    def add(self, campaigns: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/campaigns/add-docpage/
        :param campaigns: list
        :return: dict
        """
        return self._add(campaigns)

    def archive(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/campaigns/archive-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('archive', ids)

    def delete(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/campaigns/delete-docpage/
        :param ids: list
        :return: dict
        """
        return self._delete(ids)

    def get(
        self,
        field_names: list,
        ids: Optional[list] = None,
        types: Optional[list] = None,
        states: Optional[list] = None,
        statuses: Optional[list] = None,
        statuses_payments: Optional[list] = None,
        text_campaign_field_names: Optional[list] = None,
        mobile_app_campaign_field_names: Optional[list] = None,
        dynamic_text_campaign_field_names: Optional[list] = None,
        cpm_banner_campaign_field_names: Optional[list] = None,
        limit: int = 1000,
        offset: int = 0,
    ) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/campaigns/get-docpage/
        :param field_names: list
        :param ids: list
        :param types: list
        :param states: list
        :param statuses: list
        :param statuses_payments: list
        :param text_campaign_field_names: list
        :param mobile_app_campaign_field_names: list
        :param dynamic_text_campaign_field_names: list
        :param cpm_banner_campaign_field_names: list
        :param limit: int
        :param offset: int
        :return: dict
        """
        local_variables = locals()
        params = {
            'SelectionCriteria': generate_params(
                fields=['ids', 'types', 'states', 'statuses', 'statuses_payments'],
                function_kwargs=local_variables,
            ),
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset},
        }
        params.update(
            generate_params(
                fields=[
                    'text_campaign_field_names',
                    'mobile_app_campaign_field_names',
                    'dynamic_text_campaign_field_names',
                    'cpm_banner_campaign_field_names',
                ],
                function_kwargs=local_variables,
            )
        )
        return self._get(params)

    def resume(self, ids) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/campaigns/resume-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('resume', ids)

    def suspend(self, ids) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/campaigns/suspend-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('suspend', ids)

    def unarchive(self, ids) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/campaigns/unarchive-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('unarchive', ids)

    def update(self, campaigns: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/campaigns/update-docpage/
        :param campaigns: list
        :return: dict
        """
        return self._update(campaigns)


class Change(BaseEntity):
    service: str = 'changes'

    def _check(self, method: str, params: dict) -> dict:
        """
        :param method: str
        :param params: dic
        :return: dict
        """
        params = {convert(k): v for k, v in params if k != 'self'}
        return self._client._send_api_request(
            self.service.lower(), method, params
        ).json()

    def check_dictionaries(self, timestamp: int) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/changes/checkDictionaries-docpage/
        :param timestamp: str
        :return: dict
        """
        return self._check('checkDictionaries', locals())

    def check_campaigns(self, timestamp: int) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/changes/checkDictionaries-docpage/
        :param timestamp: str
        :return: dict
        """
        return self._check('checkCampaigns', locals())

    def check(
        self,
        timestamp: int,
        field_names: list,
        campaign_ids: Optional[list] = None,
        ad_group_ids: Optional[list] = None,
        ad_ids: Optional[list] = None,
    ) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/changes/check-docpage/
        :param timestamp: str
        :param field_names: list
        :param campaign_ids: list
        :param ad_group_ids: list
        :param ad_ids: list
        :return: dict
        """
        if not campaign_ids and not ad_group_ids and not ad_ids:
            raise ValueError(
                'campaign_ids, ag_group_ids, ad_ids must be implement one of them'
            )

        return self._check('check', locals())


class Creative(BaseEntity):
    service: str = 'Creatives'

    def get(
        self,
        field_names: list,
        ids: Optional[list] = None,
        types: Optional[list] = None,
        video_extension_creative_field_names: Optional[list] = None,
        cpc_video_creative_field_names: Optional[list] = None,
        cpm_video_creative_field_names: Optional[list] = None,
        limit: int = 10000,
        offset: int = 0,
    ) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/creatives/get-docpage/
        :param field_names: list
        :param ids: list
        :param types: list
        :param video_extension_creative_field_names: list
        :param cpc_video_creative_field_names: list
        :param cpm_video_creative_field_names: list
        :param limit: int
        :param offset: int
        :return: dict
        """
        params = {
            'SelectionCriteria': generate_params(['ids', 'types'], locals()),
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset},
        }
        params.update(
            generate_params(
                fields=[
                    'video_extension_creative_field_names',
                    'cpc_video_creative_field_names',
                    'cpm_video_creative_field_names',
                ],
                function_kwargs=locals(),
            ),
        )
        return self._get(params)


class Dictionary(BaseEntity):
    service: str = 'Dictionaries'

    def get(self, dictionary_names: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/dictionaries/get-docpage/
        :param dictionary_names: list
        :return: dict
        """
        params = {'DictionaryNames': dictionary_names}
        return self._get(params)


class DynamicTextAdTarget(BaseEntity):
    service: str = 'dynamictextadtargets'

    def add(
        self,
        webpages: list,
        bid: Optional[str] = None,
        context_bid: Optional[str] = None,
        strategy_priority: Optional[str] = None,
    ) -> None:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/dynamictextadtargets/add-docpage/
        :param webpages: list
        :param bid: str
        :param context_bid: str
        :param strategy_priority: str
        :return: dict
        """
        params = {
            'Webpages': webpages,
        }
        params.update(
            generate_params(
                fields=['bid', 'context_bid', 'strategy_priority'],
                function_kwargs=locals(),
            )
        )
        return self._client._send_api_request(
            self.service.lower(), 'add', params
        ).json()

    def delete(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/dynamictextadtargets/delete-docpage/
        :param ids: list
        :return: dict
        """
        return self._delete(ids)

    def get(
        self,
        field_names: list,
        ids: Optional[list] = None,
        ad_group_ids: Optional[list] = None,
        campaign_ids: Optional[list] = None,
        states: Optional[list] = None,
        limit: int = 10000,
        offset: int = 0,
    ) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/dynamictextadtargets/get-docpage/
        :param field_names: list
        :param ids: list
        :param ad_group_ids: list
        :param campaign_ids: list
        :param states: list
        :param limit: int
        :param offset: int
        :return: dict
        """
        if not ids and not ad_group_ids and not campaign_ids:
            raise ParameterError(['ids', 'campaign_ids', 'ad_group_ids'])

        params = {
            'SelectionCriteria': generate_params(
                fields=['ids', 'ad_group_ids', 'campaign_ids', 'states'],
                function_kwargs=locals(),
            ),
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset},
        }
        return self._get(params)

    def resume(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/dynamictextadtargets/resume-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('resume', ids)

    def suspend(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/dynamictextadtargets/suspend-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('suspend', ids)

    def set_bids(self, bids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/dynamictextadtargets/setBids-docpage/
        :param bids: list
        :return: dict
        """
        params = {'Bids': bids}
        return self._client._send_api_request(
            self.service.lower(), 'setBids', params
        ).json()


class KeywordBid(BaseEntity):
    service: str = 'KeywordBids'

    def get(
        self,
        field_names,
        campaign_ids: Optional[list] = None,
        ad_group_ids: Optional[list] = None,
        keyword_ids: Optional[list] = None,
        serving_statuses: Optional[list] = None,
        search_field_names: Optional[list] = None,
        network_field_names: Optional[list] = None,
        limit: int = 10000,
        offset: int = 0,
    ) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/keywordbids/get-docpage/
        :param field_names: list
        :param campaign_ids: list
        :param ad_group_ids: list
        :param keyword_ids: list
        :param serving_statuses: list
        :param search_field_names: list
        :param network_field_names: list
        :param limit: int
        :param offset: int
        :return: dict
        """
        if not campaign_ids and not ad_group_ids and not keyword_ids:
            raise ParameterError(['campaign_ids', 'ad_group_ids', 'keyword_ids'])
        local_variables = locals()
        params = {
            'SelectionCriteria': generate_params(
                fields=[
                    'campaign_ids',
                    'ad_group_ids',
                    'keyword_ids',
                    'serving_statuses',
                ],
                function_kwargs=local_variables,
            ),
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset},
        }
        params.update(
            generate_params(
                fields=['search_field_names', 'network_field_names'],
                function_kwargs=local_variables,
            )
        )
        return self._get(params)

    def set(self, keyword_bids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/keywordbids/set-docpage/
        :param keyword_bids: list
        :return: dict
        """
        params = {'KeywordBids': keyword_bids}
        return self._client._send_api_request(self.service, 'set', params).json()

    def set_auto(self, keyword_bids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/keywordbids/setAuto-docpage/
        :param keyword_bids: list
        :return: dict
        """
        params = {'KeywordBids': keyword_bids}
        return self._client._send_api_request(self.service, 'set_auto', params).json()


class Keyword(BaseEntity):
    service: str = 'Keywords'

    def add(self, keywords: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/keywords/add-docpage/
        :param keywords: list
        :return: dict
        """
        return self._add(keywords)

    def delete(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/keywords/delete-docpage/
        :param ids: list
        :return: dict
        """
        return self._delete(ids)

    def get(
        self,
        field_names: list,
        ids: Optional[list] = None,
        ad_group_ids: Optional[list] = None,
        campaign_ids: Optional[list] = None,
        states: Optional[list] = None,
        statuses: Optional[list] = None,
        serving_statuses: Optional[list] = None,
        modified_since: Optional[str] = None,
        limit: int = 10000,
        offset: int = 0,
    ) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/keywords/get-docpage/
        :param field_names: list
        :param ids: list
        :param ad_group_ids: list
        :param campaign_ids: list
        :param states: list
        :param statuses: list
        :param serving_statuses: list
        :param modified_since: str
        :param limit: int
        :param offset: int
        :return: dict
        """
        if not ids and not ad_group_ids and not campaign_ids:
            raise ParameterError(['ids', 'ad_group_ids', 'campaign_ids'])
        params = {
            'SelectionCriteria': generate_params(
                fields=[
                    'ids',
                    'ad_group_ids',
                    'campaign_ids',
                    'states',
                    'statuses',
                    'serving_statuses',
                    'modified_since',
                ],
                function_kwargs=locals(),
            ),
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset},
        }
        return self._get(params)

    def resume(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/keywords/resume-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('resume', ids)

    def suspend(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/keywords/suspend-docpage/
        :param ids: list
        :return: dict
        """
        return self._execute_method_by_ids('suspend', ids)

    def update(self, keywords: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/keywords/update-docpage/
        :param keywords: list
        :return: dict
        """
        return self._update(keywords)


class KeywordsResearch(BaseEntity):
    service: str = 'keywordsresearch'

    def deduplicate(self, keywords: list, operation: Optional[str] = None) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/keywordsresearch/deduplicate-docpage/
        :param keywords: list
        :param operation: str (MERGE_DUPLICATES or ELIMINATE_OVERLAPPING)
        :return: dict
        """
        params: dict = {'Keywords': keywords}
        if operation is not None:
            params['operation'] = operation
        return self._client._send_api_request(
            self.service.lower(), 'deduplicate', params
        ).json()

    def has_search_volume(
        self, field_names: list, keywords: list, region_ids: list
    ) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/keywordsresearch/hasSearchVolume-docpage/
        :param field_names: list
        :param keywords: list
        :param region_ids: list
        :return: dict
        """
        params = {
            'SelectionCriteria': {'Keywords': keywords, 'RegionIds': region_ids},
            'FieldNames': field_names,
        }
        return self._client._send_api_request(
            self.service.lower(), 'hasSearchVolume', params
        ).json()


class Lead(BaseEntity):
    service: str = 'Leads'

    def get(
        self,
        field_names: list,
        turbo_page_ids: list,
        date_time_from: Optional[str] = None,
        date_time_to: Optional[str] = None,
        limit: int = 10000,
        offset: int = 0,
    ) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/leads/get-docpage/
        :param field_names: list
        :param turbo_page_ids: list
        :param date_time_from: str
        :param date_time_to: str
        :param limit: int
        :param offset: int
        :return: dict
        """
        params = {
            'SelectCriterioa': generate_params(
                fields=['turbo_page_ids', 'date_time_from', 'date_time_to'],
                function_kwargs=locals(),
            ),
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset},
        }
        return self._get(params)


class NegativeKeywordSharedSet(BaseEntity):
    service: str = 'NegativeKeywordSharedSets'

    def add(self, negative_keyword_shared_sets: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/negativekeywordsharedsets/add-docpage/
        :param negative_keyword_shared_sets: list
        :return: dict
        """
        return self._add(negative_keyword_shared_sets)

    def delete(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/negativekeywordsharedsets/delete-docpage/
        :param ids: list
        :return: dict
        """
        return self._delete(ids)

    def get(
        self,
        field_names: list,
        ids: Optional[list] = None,
        limit: int = 10000,
        offset: int = 0,
    ) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/negativekeywordsharedsets/get-docpage/
        :param field_names: list
        :param ids: list
        :param limit: int
        :param offset: int
        :return: dict
        """
        params = {'FieldNames': field_names, 'Page': {'Limit': limit, 'Offset': offset}}
        if ids:
            params['SelectionCriteria'] = {'Ids': ids}
        return self._get(params)

    def update(self, negative_keyword_shared_sets: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/negativekeywordsharedsets/update-docpage/
        :param negative_keyword_shared_sets: list
        :return: dict
        """
        return self._update(negative_keyword_shared_sets)


class RetargetingList(BaseEntity):
    service: str = 'RetargetingLists'

    def add(self, retargeting_list: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/retargetinglists/add-docpage/
        :param retargeting_list: list
        :return: dict
        """
        return self._add(retargeting_list)

    def delete(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/retargetinglists/delete-docpage/
        :param ids: list
        :return: dict
        """
        return self._delete(ids)

    def get(
        self,
        field_names: list,
        ids: Optional[list] = None,
        types: Optional[list] = None,
        limit: int = 10000,
        offset: int = 0,
    ) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/retargetinglists/get-docpage/
        :param field_names: list
        :param ids: list
        :param types: list
        :param limit: int
        :param offset: int
        :return: dict
        """
        params = {'FieldNames': field_names, 'Page': {'Limit': limit, 'Offset': offset}}
        if ids or types:
            params['SelectionCriteria'] = generate_params(['ids', 'types'], locals())

        return self._get(params)

    def update(self, retargeting_list: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/retargetinglists/update-docpage/
        :param retargeting_list: list
        :return: dict
        """
        return self._update(retargeting_list)


class Sitelink(BaseEntity):
    service: str = 'Sitelinks'

    def add(self, sitelinks_sets: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/sitelinks/add-docpage/
        :param sitelinks_sets: list
        :return: dict
        """
        return self._add(sitelinks_sets)

    def delete(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/sitelinks/delete-docpage/
        :param ids: list
        :return: dict
        """
        return self._delete(ids)

    def get(
        self,
        field_names: list,
        sitelinks_field_names: Optional[list],
        ids: Optional[list] = None,
        limit: int = 10000,
        offset: int = 0,
    ) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/sitelinks/get-docpage/
        :param field_names: list
        :param sitelinks_field_names: list
        :param ids: list
        :param limit: int
        :param offset: int
        :return: dict
        """
        params = {'FieldNames': field_names, 'Page': {'Limit': limit, 'Offset': offset}}
        if ids:
            params['SelectionCriteria'] = {'Ids': ids}
        if sitelinks_field_names:
            params['SitelinkFieldNames'] = sitelinks_field_names

        return self._get(params)


class TurboPage(BaseEntity):
    service: str = 'turbopages'

    def get(
        self,
        field_names: list,
        ids: Optional[list] = None,
        limit: int = 10000,
        offset: int = 0,
    ) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/turbopages/get-docpage/
        :param field_names: list
        :param ids: list
        :param limit: int
        :param offset: int
        :return: dict
        """
        params = {'FieldNames': field_names, 'Page': {'Limit': limit, 'Offset': offset}}
        if ids:
            params['SelectionCriteria'] = {'Ids': ids}

        return self._get(params)


class VCard(BaseEntity):
    service: str = ' VCards'

    def add(self, vcards: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/vcards/add-docpage/
        :param vcards: list
        :return: dict
        """
        return self._add(vcards)

    def delete(self, ids: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/vcards/delete-docpage/
        :param ids: list
        :return: dict
        """
        return self._delete(ids)

    def get(
        self,
        field_names: list,
        ids: Optional[list] = None,
        limit: int = 10000,
        offset: int = 0,
    ) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/vcards/get-docpage/
        :param field_names: list
        :param ids: list
        :param limit: int
        :param offset: int
        :return: dict
        """
        params = {'FieldNames': field_names, 'Page': {'Limit': limit, 'Offset': offset}}
        if ids:
            params['SelectionCriteria'] = {'Ids': ids}

        return self._get(params)


class Report(BaseEntity):
    service: str = 'reports'

    def get(
        self,
        selection_criteria: dict,
        field_names: list,
        report_name: str,
        report_type: str,
        date_range_type: str,
        processing_mode: str = 'auto',
        headers: Optional[dict] = None,
        goals: Optional[list] = None,
        attribution_models: Optional[list] = None,
        page: Optional[dict] = None,
        order_by: Optional[list] = None,
        format: str = 'TSV',
        include_vat: Optional[str] = 'YES',
        include_discount: Optional[str] = "NO",
    ) -> str:
        """
        doc - https://yandex.ru/dev/direct/doc/reports/spec-docpage/
        :param selection_criteria: dict
        :param field_names: list
        :param report_name: str
        :param processing_mode: str
        :param report_type: str
        :param date_range_type: str
        :param headers: dict
        :param goals: list
        :param attribution_models: list
        :param page: dict
        :param order_by: list
        :param format: str
        :param include_vat: str
        :param include_discount: str
        :return: str
        """

        if headers:
            headers['processingMode'] = processing_mode
        else:
            headers = {'processingMode': processing_mode}
        self._client._set_session_headers(headers)

        params = {
            'SelectionCriteria': selection_criteria,
            'FieldNames': field_names,
            'ReportName': report_name,
            'ReportType': report_type,
            'DateRangeType': date_range_type,
        }
        if include_vat is not None:
            params['IncludeVAT'] = include_vat
        params.update(
            generate_params(
                fields=[
                    'goals',
                    'attribution_models',
                    'page',
                    'order_by',
                    'format',
                    'include_discount',
                ],
                function_kwargs=locals(),
            )
        )
        return self._client._get_reports({'params': params})


class Client(BaseEntity):
    service: str = 'clients'

    def add(
        self,
        login: str,
        first_name: str,
        last_name: str,
        currency: str,
        grants: Optional[list] = None,
        notification: Optional[dict] = None,
        settings: Optional[list] = None,
    ):
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/agencyclients/add.html
        :param login: str
        :param first_name: str
        :param last_name: str
        :param currency: str
        :param grants: list
        :param notification: optional dict
        :param settings: optional list
        :return: dict
        """
        params: dict = {
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
        return self._client._send_api_request(
            self.service.lower(), 'add', params
        ).json()

    def get(
        self,
        field_names: list,
        logins: Optional[list] = None,
        archived: Optional[str] = None,
        limit: int = 500,
        offset: int = 0,
    ) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/agencyclients/get.html
        :param field_names: list
        :param logins: optional list
        :param archived: optional str
        :param limit: int
        :param offset: int
        :return: dict
        """
        params = {
            'FieldNames': field_names,
            'Page': {'Limit': limit, 'Offset': offset},
        }
        if logins or archived:
            params['SelectionCriteria'] = (
                generate_params(['logins', 'archived'], locals()),
            )
        return self._get(params)

    def update(self, clients: list) -> dict:
        """
        doc - https://yandex.ru/dev/direct/doc/ref-v5/agencyclients/update.html
        :param clients: list (list of Client object)
        :return: dict
        """
        return self._update(clients)
