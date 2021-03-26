from utils import request, download
from pyquery import PyQuery as pq
from os import path

url = "https://www.hippopx.com/zh"


print('start...')

html = pq(request(url))

images = html('figure img').items()


# 下载图片函数
def download_image(src):
    dist = path.join(
        path.dirname(__file__),
        '..',
        'dist',
        'images',
        list(filter(bool, src.split('/'))).pop()
    )
    download(src, dist)


# 循环下载
for img in images:
    src = img.attr('src')
    print(src)
    download_image(src)
