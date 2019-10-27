from urllib.request import urlopen, Request

response = urlopen('http://www.bing.com')
print(response.closed)

with response:
    # print(1, type(response))
    # print(2, response.status, response.reason)
    # print(3, response.geturl())
    # print(4, response.info())
    # print(5, response.read())

print(response.closed)
