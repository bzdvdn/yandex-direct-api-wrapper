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
