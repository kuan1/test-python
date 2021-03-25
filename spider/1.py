import ssl
import urllib.request
import os
from pyquery import PyQuery as pq

url = "https://www.hippopx.com/zh"

headers = {
    'cookie': '__cfduid=d40daf477167ae94b007fc99a7f3618ed1616660612; _ga=GA1.2.602292106.1616660615; _gid=GA1.2.1257895581.1616660615; __gads=ID=25a6965ee260d6ef-22c56e95d6c6007c:T=1616663722:RT=1616663722:S=ALNI_MboNcdxGJhzq0EfUffNnAZp4-QJIA',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
}

req = urllib.request.Request(url, None, headers=headers)

print('start...')
res = urllib.request.urlopen(req, context=ssl._create_unverified_context())

html = pq(str(res.read(), encoding='utf-8'))

images = html('figure img').items()

# 下载图片函数


def download(src):
    ssl._create_default_https_context = ssl._create_unverified_context
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-agent', 'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10')
    ]
    urllib.request.install_opener(opener)
    dist = os.path.join(
        os.path.dirname(__file__),
        'images',
        src.split('/').pop()
    )
    urllib.request.urlretrieve(src, dist)


for img in images:
    src = img.attr('src')
    print(src)
    download(src)
