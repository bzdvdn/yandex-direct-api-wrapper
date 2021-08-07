## Yandex Direct Api Wrapper (yandex direct api v5)

## Installation

Instal user `pip`...

    pip install yandex-direct-api-wrapper

## Usage

```python
from direct_api import DirectAPI

client = DirectAPI('<access_token>', '<clid>', lang='ru')

```

### AgencyClient:add

- doc: https://yandex.ru/dev/direct/doc/ref-v5/agencyclients/add-docpage/
- params:

|     name     | type | default value |
| :----------: | :--: | :-----------: |
|    login     | str  |  \*required   |
|  first_name  | str  |  \*required   |
|  last_name   | str  |  \*required   |
|   currency   | str  |  \*required   |
|    grants    | list |     None      |
| notification | dict |     None      |
|   settings   | dict |     None      |

```python

result = client.AgencyClient.add(login='<login>', first_name='<fname>', last_name='<lname>', currency='RUB')
```

### AgencyClient:get

- doc: https://yandex.ru/dev/direct/doc/ref-v5/agencyclients/get-docpage/
- params:

|    name     | type | default value |
| :---------: | :--: | :-----------: |
| field_names | list |  \*required   |
|    limit    | int  |      500      |
|   offset    | int  |       0       |
|   logins    | list |     None      |
|  archived   | str  |     None      |

```python
result = client.AgencyClient.get(field_names=["ClientId", "ClientInfo"])
```

### AgencyClient:update

- doc: https://yandex.ru/dev/direct/doc/ref-v5/agencyclients/update.html
- params:

|  name   | type | default value |
| :-----: | :--: | :-----------: |
| clients | list |  \*required   |

```python
clients = [{
        "ClientId": 1
        "ClientInfo": 'client info',
    },
]
result = client.AgencyClient.update(clients=clients)
```

### AdExtension:add

- doc: https://yandex.ru/dev/direct/doc/ref-v5/adextensions/add-docpage/
- params:

|     name      | type | default value |
| :-----------: | :--: | :-----------: |
| ad_extensions | list |  \*required   |

```python
ad_extendsions = [{
        "Callout": {"CalloutText": "<callout text>"},
    },
]
result = client.AdExtension.add(ad_extendsions=ad_extendsions)
```

### AdExtension:delete

- doc: https://yandex.ru/dev/direct/doc/ref-v5/adextensions/delete-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['1', '2', '3']
result = client.AdExtension.delete(ids)
```

### AdExtension:get

- doc: https://yandex.ru/dev/direct/doc/ref-v5/adextensions/get-docpage/
- params:

|        name         | type | default value |
| :-----------------: | :--: | :-----------: |
|     field_names     | list |  \*required   |
|         ids         | list |     None      |
|        types        | list |     None      |
|      statuses       | list |     None      |
|    modify_since     | str  |     None      |
| callout_field_names | list |     None      |
|        limit        | int  |      500      |
|       offset        | int  |       0       |

```python
field_names = ['Id', 'Type', 'Status']
result = client.AdExtension.get(field_names)
```

### AdGroup:add

- doc: https://yandex.ru/dev/direct/doc/ref-v5/adgroups/add-docpage/
- params:

|   name    | type | default value |
| :-------: | :--: | :-----------: |
| ad_groups | list |  \*required   |

```python
ad_groups = [{'Name': 'Test', 'CampaignId': '123', 'RegionIds'}]
result = client.AdGroup.add(ad_groups)
```

### AdGroup:delete

- doc: https://yandex.ru/dev/direct/doc/ref-v5/adgroups/delete-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['123', '124', '125']
result = client.AdGroup.get(ids=ids)
```

### AdGroup:get

- doc: https://yandex.ru/dev/direct/doc/ref-v5/adgroups/get-docpage/
- params:

|                  name                  | type | default value |
| :------------------------------------: | :--: | :-----------: |
|              field_names               | list |  \*required   |
|                  ids                   | list |     None      |
|              campaign_ids              | list |     None      |
|                 types                  | list |     None      |
|                statuses                | list |     None      |
|            serving_statuses            | list |     None      |
|           app_icon_statuses            | list |     None      |
|    negative_keyword_shared_set_ids     | list |     None      |
|    mobile_app_ad_group_field_names     | list |     None      |
|   dynamic_text_ad_group_field_names    | list |     None      |
| dynamic_text_feed_ad_group_field_names | list |     None      |
|                 limit                  | int  |      500      |
|                 offset                 | int  |      500      |

```python
field_names = ['AdGroupId', 'Name', 'CampaignId']
result = client.AdGroup.get(field_names=field_names)
```

### AdGroup:update

- doc: https://yandex.ru/dev/direct/doc/ref-v5/adgroups/update-docpage/
- params:

|   name    | type | default value |
| :-------: | :--: | :-----------: |
| ad_groups | list |  \*required   |

```python
ad_groups = [{'Name': 'Test', 'CampaignId': '123', 'RegionIds', 'AdGroupId': '123'}]
result = client.AdGroup.update(ad_groups)
```

### AdImage:add

- doc: https://yandex.ru/dev/direct/doc/ref-v5/adimages/add-docpage/
- params:

|   name    | type | default value |
| :-------: | :--: | :-----------: |
| ad_images | list |  \*required   |

```python
ad_images = [{'Name': 'Test', 'ImageData': '<binary>'}]
result = client.AdImage.add(ad_images)
```

### AdImage:delete

- doc: https://yandex.ru/dev/direct/doc/ref-v5/adimages/delete.html
- params:

|  name  | type | default value |
| :----: | :--: | :-----------: |
| hashes | list |  \*required   |

```python
hashes = ['<hash1>', '<hash2>']
result = client.AdImage.delete(hashes)
```

### AdImage:get

- doc: https://yandex.ru/dev/direct/doc/ref-v5/adimages/get-docpage/
- params:

|       name       | type | default value |
| :--------------: | :--: | :-----------: |
|   field_names    | list |  \*required   |
| ad_images_hashes | list |     None      |
|    associated    | str  |     None      |
|      limit       | init |      500      |
|      offset      | init |       0       |

```python
field_names = ['AdImageHash', 'Name']
result = client.AdImage.get(field_names)
```

### Ad:add

- doc: https://yandex.ru/dev/direct/doc/ref-v5/ads/add-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ads  | list |  \*required   |

```python
ads = [{'AdgroupId': '<id>', 'TextAd': {}}]
result = client.Ad.add(ads)
```

### Ad:archive

- doc: https://yandex.ru/dev/direct/doc/ref-v5/ads/archive-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['123', '124']
result = client.Ad.archive(ids)
```

### Ad:delete

- doc: https://yandex.ru/dev/direct/doc/ref-v5/ads/delete-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['123', '124']
result = client.Ad.delete(ids)
```

### Ad:get

- doc: https://yandex.ru/dev/direct/doc/ref-v5/ads/get-docpage/
- params:

|                 name                 | type | default value |
| :----------------------------------: | :--: | :-----------: |
|             field_names              | list |  \*required   |
|                 ids                  | list |     None      |
|             campaign_ids             | list |     None      |
|             ad_group_ids             | list |     None      |
|                states                | list |     None      |
|               statuses               | list |     None      |
|                types                 | list |     None      |
|                mobile                | str  |     None      |
|              v_card_ids              | list |     None      |
|           sitelink_set_ids           | list |     None      |
|           ad_image_hashes            | list |     None      |
|      v_card_moderation_statuses      | list |     None      |
|     sitelink_moderation_statuses     | list |     None      |
|     ad_image_moderation_statuses     | list |     None      |
|           ad_extension_ids           | list |     None      |
|         text_ad_field_names          | list |     None      |
| text_ad_price_extension_field_names  | list |     None      |
|        mobile_app_field_names        | list |     None      |
|     dynamic_text_ad_field_names      | list |     None      |
|   mobile_app_image_ad_field_names    | list |     None      |
|    text_ad_builder_ad_field_names    | list |     None      |
| mobile_app_ad_builder_ad_field_names | list |     None      |
| cpc_video_ad_builder_ad_field_names  | list |     None      |
| cpm_banner_ad_builder_ad_field_names | list |     None      |
| cpm_video_ad_builder_ad_field_names  | list |     None      |
|                limit                 | int  |      500      |
|                offset                | int  |       0       |

```python
field_names = ['Id', 'CampaignId']
result = client.Ad.get(field_names)
```

### Ad:moderate

- doc: https://yandex.ru/dev/direct/doc/ref-v5/ads/moderate-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['123', '124']
result = client.Ad.moderate(ids)
```

### Ad:resume

- doc: https://yandex.ru/dev/direct/doc/ref-v5/ads/resume-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['123', '124']
result = client.Ad.resume(ids)
```

### Ad:suspend

- doc: https://yandex.ru/dev/direct/doc/ref-v5/ads/suspend-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['123', '124']
result = client.Ad.suspend(ids)
```

### Ad:unarchive

- doc: https://yandex.ru/dev/direct/doc/ref-v5/ads/unarchive-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['123', '124']
result = client.Ad.unarchive(ids)
```

### Ad:update

- doc: https://yandex.ru/dev/direct/doc/ref-v5/ads/update-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ads  | list |  \*required   |

```python
ads = [{'AdgroupId': '<id>', 'TextAd': {}, 'Id': '<Id>'}]
result = client.Ad.update(ads)
```

### AudienceTarget:add

- doc: https://yandex.ru/dev/direct/doc/ref-v5/audiencetargets/add-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ads  | list |  \*required   |

```python
ads = [{'AdgroupId': '<id>', }]
result = client.AudienceTarget.add(ids)
```

### AudienceTarget:delete

- doc: https://yandex.ru/dev/direct/doc/ref-v5/audiencetargets/delete-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['232324353']
result = client.AudienceTarget.delete(ids)
```

### AudienceTarget:get_audience_targets

- doc: https://yandex.ru/dev/direct/doc/ref-v5/audiencetargets/get-docpage/
- params:

|         name         | type | default value |
| :------------------: | :--: | :-----------: |
|     field_names      | list |  \*required   |
|         ids          | list |     None      |
|     ad_group_ids     | list |     None      |
|     campaign_ids     | list |     None      |
| retargeting_list_ids | list |     None      |
|     interest_ids     | list |     None      |
|        states        | list |     None      |
|        limit         | int  |      500      |
|        offset        | int  |       0       |

```python
field_names = ['Id']
result = client.AudienceTarget.get_audience_targets(field_names, campaigns_ids=[123])
```

### AudienceTarget:resume

- doc: https://yandex.ru/dev/direct/doc/ref-v5/audiencetargets/resume-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['232324353']
result = client.AudienceTarget.resume(ids)
```

### AudienceTarget:set_bids

- doc: https://yandex.ru/dev/direct/doc/ref-v5/audiencetargets/setBids-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| bids | list |  \*required   |

```python
bids = [{'Id': '<id>', 'AdGroupId': '<Id>'}]
result = client.AudienceTarget.set_bids(bids)
```

### Bid:get

- doc: https://yandex.ru/dev/direct/doc/ref-v5/bids/get-docpage/
- params:

|       name       | type | default value |
| :--------------: | :--: | :-----------: |
|   field_names    | list |  \*required   |
|   keyword_ids    | list |     None      |
|   ad_group_ids   | list |     None      |
|   campaign_ids   | list |     None      |
| serving_statuses | list |     None      |
|      limit       | int  |      500      |
|      offset      | int  |       0       |

```python
field_names = ['Id']
result = client.Bid.suspend(field_names, campaign_ids=[1232424532])
```

### Bid:set

- doc: https://yandex.ru/dev/direct/doc/ref-v5/bids/set-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| bids | list |  \*required   |

```python
bids = [{'Bid': '<long>'}]
result = client.Bid.set(bids)
```

### Bid:set_auto

- doc: https://yandex.ru/dev/direct/doc/ref-v5/bids/setAuto-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| bids | list |  \*required   |

```python
bids = [{'CampaignID': '<long>', 'Scope': 'SEARCH'}]
result = client.Bid.set_auto(bids)
```

### BidsModifier:add

- doc: https://yandex.ru/dev/direct/doc/ref-v5/bidmodifiers/add-docpage/
- params:

|     name      | type | default value |
| :-----------: | :--: | :-----------: |
| bid_modifiers | list |  \*required   |

```python
bid_modifiers = [{'MobileAdjustment': {'BidModifier': '<id>'}}]
result = client.BidsModifier.add(bid_modifiers)
```

### BidsModifier:delete

- doc: https://yandex.ru/dev/direct/doc/ref-v5/bidmodifiers/delete-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['1312324343']
result = client.BidsModifier.delete(ids)
```

### BidsModifier:get

- doc: https://yandex.ru/dev/direct/doc/ref-v5/bidmodifiers/get-docpage/
- params:

|                name                 | type | default value |
| :---------------------------------: | :--: | :-----------: |
|             field_names             | list |  \*required   |
|                 ids                 | list |     None      |
|            campaign_ids             | list |     None      |
|            ad_group_ids             | list |     None      |
|                types                | list |     None      |
|               levels                | list |     None      |
|    mobile_adjustment_field_names    | list |     None      |
|   desktop_adjustment_field_names    | list |     None      |
| demographics_adjustment_field_names | list |     None      |
| retargeting_adjustment_field_names  | list |     None      |
|   regional_adjustment_field_names   | list |     None      |
|    video_adjustment_field_names     | list |     None      |
|                limit                | list |      500      |
|               offset                | list |       0       |

```python
field_names = ['Id', 'CampaignId', 'Type']
result = client.BidsModifier.get(field_names, campaign_ids=['123453534'])
```

### BidsModifier:set

- doc: https://yandex.ru/dev/direct/doc/ref-v5/bidmodifiers/set-docpage/
- params:

|     name      | type | default value |
| :-----------: | :--: | :-----------: |
| bid_modifiers | list |  \*required   |

```python
ids = [{'Id': '<id>', 'BidModifier': 124242}]
result = client.BidsModifier.set(bid_modifiers)
```

### BidsModifier:toggle

- doc: https://yandex.ru/dev/direct/doc/ref-v5/bidmodifiers/toggle-docpage/
- params:

|           name            | type | default value |
| :-----------------------: | :--: | :-----------: |
| bid_modifier_toggle_items | list |  \*required   |

```python
bid_modifier_toggle_items = [{'CampaignId': '<id>', 'Type': "DEMOGRAPHICS_ADJUSTMENT","Enabled": "YES"}]
result = client.BidsModifier.toggle(bid_modifier_toggle_items)
```

### Campaign:add

- doc: https://yandex.ru/dev/direct/doc/ref-v5/campaigns/add-docpage/
- params:

|   name    | type | default value |
| :-------: | :--: | :-----------: |
| campaigns | list |  \*required   |

```python
campaign_item = {} # campaign object
campaigns = [campaign_item]
result = client.Campaign.add(campaigns)
```

### Campaign:archive

- doc: https://yandex.ru/dev/direct/doc/ref-v5/campaigns/archive-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['12312535', '345345345', '23432325345']
result = client.Campaign.archive(ids)
```

### Campaign:delete

- doc: https://yandex.ru/dev/direct/doc/ref-v5/campaigns/delete-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['12312535', '345345345', '23432325345']
result = client.Campaign.delete(ids)
```

### Campaign:get

- doc: https://yandex.ru/dev/direct/doc/ref-v5/campaigns/get-docpage/
- params:

|               name                | type | default value |
| :-------------------------------: | :--: | :-----------: |
|            field_names            | list |  \*required   |
|                ids                | list |     None      |
|               types               | list |     None      |
|              states               | list |     None      |
|             statuses              | list |     None      |
|         statuses_payments         | list |     None      |
|     text_campaign_field_names     | list |     None      |
|  mobile_app_campaign_field_names  | list |     None      |
| dynamic_text_campaign_field_names | list |     None      |
|  cpm_banner_campaign_field_names  | list |     None      |
|               limit               | int  |      500      |
|              offset               | int  |       0       |

```python
field_names = ['Id', 'Name', 'Type']
result = client.Campaign.get(field_names=field_names)
```

### Campaign:resume

- doc: https://yandex.ru/dev/direct/doc/ref-v5/campaigns/resume-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['12312535', '345345345', '23432325345']
result = client.Campaign.resume(ids)
```

### Campaign:suspend

- doc: https://yandex.ru/dev/direct/doc/ref-v5/campaigns/suspend-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['12312535', '345345345', '23432325345']
result = client.Campaign.suspend(ids)
```

### Campaign:unarchive

- doc: https://yandex.ru/dev/direct/doc/ref-v5/campaigns/unarchive-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['12312535', '345345345', '23432325345']
result = client.Campaign.unarchive(ids)
```

### Campaign:update

- doc: https://yandex.ru/dev/direct/doc/ref-v5/campaigns/update-docpage/
- params:

|   name    | type | default value |
| :-------: | :--: | :-----------: |
| campaigns | list |  \*required   |

```python
campaigns = [{'Id': '12312535','Name': 'updated!']
result = client.Campaign.unarchive(campaigns)
```

### Change:check_dictionaries

- doc: https://yandex.ru/dev/direct/doc/ref-v5/changes/checkDictionaries-docpage/
- params:

|   name    | type | default value |
| :-------: | :--: | :-----------: |
| timestamp | int  |  \*required   |

```python
from time import time

timestamp = int(time.now()- 1800)
result = client.Change.check_dictionaries(timestamp)
```

### Change:check_campaigns

- doc: https://yandex.ru/dev/direct/doc/ref-v5/changes/checkDictionaries-docpage/
- params:

|   name    | type | default value |
| :-------: | :--: | :-----------: |
| timestamp | int  |  \*required   |

```python
from time import time

timestamp = int(time.now()- 1800)
result = client.Change.check_campaigns(timestamp)
```

### Change:check

- doc: https://yandex.ru/dev/direct/doc/ref-v5/changes/checkDictionaries-docpage/
- params:

|     name     | type | default value |
| :----------: | :--: | :-----------: |
|  timestamp   | int  |  \*required   |
| field_names  | list |  \*required   |
| campaign_ids | list |     None      |
| ad_group_ids | list |     None      |
|    ad_ids    | list |     None      |

```python
from time import time

timestamp = int(time.now()- 1800)
field_names = ['Id', 'Name']
result = client.Change.check(timestamp, fiel_names)
```

### Creative:get

- doc: https://yandex.ru/dev/direct/doc/ref-v5/creatives/get-docpage/
- params:

|                 name                 | type | default value |
| :----------------------------------: | :--: | :-----------: |
|             field_names              | list |  \*required   |
|                 ids                  | list |     None      |
|                types                 | list |     None      |
| video_extension_creative_field_names | list |     None      |
|    cpc_video_creative_field_names    | list |     None      |
|    cpm_video_creative_field_names    | list |     None      |
|                limit                 | int  |     10000     |
|                offset                | int  |       0       |

```python
field_names = ['Id', 'Name', 'Type', 'PreviewUrl']
result = client.Creative.get(field_names)
```

### Dictionary:get

- doc: https://yandex.ru/dev/direct/doc/ref-v5/dictionaries/get-docpage/
- params:

|       name       | type | default value |
| :--------------: | :--: | :-----------: |
| dictionary_names | list |  \*required   |

```python
dictionary_names = ['TimeZones', 'Currencies']
result = client.Dictionary.get(dictionary_names)
```

### DynamicTextAdTarget:add

- doc: https://yandex.ru/dev/direct/doc/ref-v5/dynamictextadtargets/add-docpage/
- params:

|       name        | type | default value |
| :---------------: | :--: | :-----------: |
|     webpages      | list |  \*required   |
|        bid        | list |     None      |
|    context_bid    | str  |     None      |
|    context_bid    | str  |     None      |
| strategy_priority | str  |     None      |

```python
webpages = [{'Name': 'Test', 'AdGroupId': '123242453253'}]
result = client.DynamicTextAdTarget.add(webpages)
```

### DynamicTextAdTarget:delete

- doc: https://yandex.ru/dev/direct/doc/ref-v5/dynamictextadtargets/delete-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['213232432432']
result = client.DynamicTextAdTarget.delete(ids)
```

### DynamicTextAdTarget:get

- doc: https://yandex.ru/dev/direct/doc/ref-v5/dynamictextadtargets/get-docpage/
- params:

|     name     | type | default value |
| :----------: | :--: | :-----------: |
| field_names  | list |  \*required   |
|     ids      | list |     None      |
| ad_group_ids | list |     None      |
| campaign_ids | list |     None      |
|    states    | list |     None      |
|    limit     | int  |     10000     |
|    offset    | int  |       0       |

```python
ids = ['AdGroupId', 'Bid']
result = client.DynamicTextAdTarget.get(ids)
```

### DynamicTextAdTarget:resume

- doc: https://yandex.ru/dev/direct/doc/ref-v5/dynamictextadtargets/resume-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['213232432432']
result = client.DynamicTextAdTarget.resume(ids)
```

### DynamicTextAdTarget:suspend

- doc: https://yandex.ru/dev/direct/doc/ref-v5/dynamictextadtargets/suspend-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| ids  | list |  \*required   |

```python
ids = ['213232432432']
result = client.DynamicTextAdTarget.suspend(ids)
```

### DynamicTextAdTarget:set_bids

- doc: https://yandex.ru/dev/direct/doc/ref-v5/dynamictextadtargets/suspend-docpage/
- params:

| name | type | default value |
| :--: | :--: | :-----------: |
| bids | list |  \*required   |

```python
set_bit_item = {} # set bid item from doc
bids = [set_bit_item]
result = client.DynamicTextAdTarget.set_bids(bids)
```

### KeywordBid:get

- doc: https://yandex.ru/dev/direct/doc/ref-v5/keywordbids/get-docpage/
- params:

|        name         | type | default value |
| :-----------------: | :--: | :-----------: |
|     field_names     | list |  \*required   |
|    campaign_ids     | list |     None      |
|    ad_group_ids     | list |     None      |
|     keyword_ids     | list |     None      |
|  serving_statuses   | list |     None      |
| search_field_names  | list |     None      |
| network_field_names | list |     None      |
|        limit        | int  |     10000     |
|       offset        | int  |       0       |

```python
field_names = ['Id']
campaign_ids = ['123123212353']
result = client.KeywordBid.get(field_names, campaign_ids=campaign_ids)
```

### KeywordBid:set

- doc: https://yandex.ru/dev/direct/doc/ref-v5/keywordbids/get-docpage/
- params:

|     name     | type | default value |
| :----------: | :--: | :-----------: |
| keyword_bids | list |  \*required   |

```python
set_bit_item = {} # set bid item from doc
keyword_bids = [set_bit_item]
result = client.KeywordBid.set(keyword_bids)
```

### KeywordBid:set_auto

- doc: https://yandex.ru/dev/direct/doc/ref-v5/keywordbids/setAuto-docpage/
- params:

|     name     | type | default value |
| :----------: | :--: | :-----------: |
| keyword_bids | list |  \*required   |

```python
set_bit_item = {} # set bid item from doc
keyword_bids = [set_bit_item]
result = client.KeywordBid.set_auto(keyword_bids)
```
