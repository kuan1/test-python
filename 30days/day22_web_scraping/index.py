from os import path, makedirs
import requests
from pyquery import PyQuery


url = 'https://www.hippopx.com/zh'


def get_html():
    response = requests.get(url)
    cache_file = path.join(path.dirname(__file__), 'temp.html')
    html = ''
    if path.exists(cache_file):
        with open(cache_file, 'r', encoding='utf-8') as f:
            html = f.read()
    else:
        with open(cache_file, 'w', encoding='utf-8') as f:
            f.write(response.text)
            html = response.text
    return html


def download(data):
    dist = path.join(path.dirname(__file__), 'dist')
    if not path.exists(dist):
        makedirs(dist)

    for src in data:
        name = path.basename(src)
        save_dist = path.join(dist, name)
        r = requests.get(src, stream=True)
        with open(save_dist, 'wb') as f:
            f.write(r.content)
            print(name)


def spider():
    html = get_html()
    d = PyQuery(html)
    images = d('.item figure img')

    data = []

    images.each(
        lambda i, img: data.append(PyQuery(img).attr('src'))
    )

    download(data)


spider()
