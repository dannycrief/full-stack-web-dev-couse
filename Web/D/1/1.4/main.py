import json
import urllib.parse
from urllib.request import urlopen, Request

url = "https://yandex.ru/"
params = {
    "auth_token": "awdafkjkuhafnaukdh",
    "length_gt": 26,  # Отфильтровать сообщения с длиной больше 26 символов
}

query_string = urllib.parse.urlencode(params)
url = url + "?" + query_string
with urlopen(url) as response:
    print(json.loads(response.read()))

import requests

url = "https://yandex.ru/"
data = {
    "auth_token": "awdafkjkuhafnaukdh",
    "length_gt": 26,  # Отфильтровать сообщения с длиной больше 26 символов
}

print(requests.get(url, params=data).json())

# Авторизация с помощью передачи токена по http заголовку с использованием requests
# requests.get(search_url, headers={'Authorization': 'Bearer {}'.format(token)})


# ошибка, связанная с превышением количества запросов в определённый промежуток времени в API твиттера
# { "errors": [ { "code": 88, "message": "Rate limit exceeded" } ] }

# Чтобы избежать этой ошибки, нужно контролировать частоту запросов. Самый простой способ — использовать time.sleep():
messages = ''

import time

for message_id in messages:
    response = requests.get("http://forum/api/messages/{}".format(message_id))
    if response.json()['errors']['code'] == 88:
        time.sleep(1)  # Подождать секунду и повторить запрос
        response = requests.get("http://forum/api/messages/{}".format(message_id))
