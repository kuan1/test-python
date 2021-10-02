import requests

url = 'https://api.github.com/events'

response = requests.get(url)

print(response)
print(response.status_code)
print(response.headers)

print('===== text text text text text text')
print(response.text[0:100])

print('===== json json json json json json')
print(response.json())

