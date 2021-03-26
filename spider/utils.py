from os import path
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'referer': 'https://baidu.com/'
}


# 获取网页字符串
def request(url, enable_cache=True):
    cache_name = list(filter(bool, url.split('/'))).pop()
    cache_file = f'dist/{cache_name}'
    if enable_cache and path.exists(cache_file):
        f = open(cache_file, mode='r', encoding='utf-8')
        cahce_text = f.read()
        f.close()
        print('使用缓存：', url)
        return cahce_text
    print('获取网页信息：', url)
    req = urllib.request.Request(url, None, headers=headers)
    res = urllib.request.urlopen(req, context=ssl._create_unverified_context())
    html_text = res.read().decode('utf-8')
    f = open(cache_file, mode='w', encoding='utf-8')
    f.write(html_text)
    f.close()
    return html_text


# 下载图片
def download(src, dist):
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-agent', 'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10')
    ]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(src, dist)
