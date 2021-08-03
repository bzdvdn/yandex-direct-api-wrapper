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
