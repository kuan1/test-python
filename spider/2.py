import urllib.request as request
import ssl
from os import path
from pyquery import PyQuery as pq


def getHtml(i=1):
    page = (f'p{i}/' if (i != 1) else (''))
    url = 'https://zz.anjuke.com/sale/' + page

    print('当前爬取网址', url)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'referer': 'https://shanghai.anjuke.com/'
    }
    req = request.Request(url, None, headers=headers)
    res = request.urlopen(req, context=ssl._create_unverified_context())
    html_text = res.read().decode('utf-8')
    # f = open('dist/test.html', mode='w+', encoding='utf-8')
    # f.write(html_text)
    # f.close()
    # html_text = open('dist/test.html', mode='r', encoding='utf-8').read()
    return pq(html_text)


def start():
    html = getHtml()
    print(html)
    list = html('.property').items()
    for item in list:
        print(item.text())


# 开始爬虫
if __name__ == '__main__':
    start()
