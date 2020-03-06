import requests

req = requests.put(' http://google.com/', params={"message": "Изменённое сообщение"})
# requests.delete('http://forum/api/messages/25')
print(req)