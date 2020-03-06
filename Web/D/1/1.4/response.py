import requests
import urllib.request

response = requests.get('http://google.com')
print(response)

response = urllib.request.urlopen('http://google.com')
print(response)
