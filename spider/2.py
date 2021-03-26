from pyquery import PyQuery as pq
from utils import request
import json
from time import sleep


def get_html(i=1):
    page = f'p{i}/' if (i != 1) else ('')
    url = 'https://zz.anjuke.com/sale/' + page
    return pq(request(url))


def get_text(item):
    return item.text().replace(' ', '').replace('\n', ' ')


def html_to_json(html):
    items = html('.list-left .property').items()
    ls = []
    for item in items:
        title = get_text(item.find('.property-content-title-name'))
        info = get_text(item.find('.property-content-info'))
        address_name = get_text(item.find('.property-content-info-comm-name'))
        address = get_text(item.find('.property-content-info-comm-address'))
        extra = get_text(item.find('.property-extra'))
        price = get_text(item.find('.property-price-total'))
        average = get_text(item.find('.property-price-average'))
        href = item.find('.property-ex').attr('href')
        data = {
            "title": title,
            "info": info,
            "address_name": address_name,
            "address": address,
            "extra": extra,
            "price": price,
            "average": average,
            "href": href
        }
        ls.append(data)
    return json.dumps(ls, ensure_ascii=False, indent=2)


def start():
    for i in range(25):
        index = i + 1
        html = get_html(index)
        data = html_to_json(html)
        with open(f'dist/data/{index}.json', 'w', encoding='utf-8') as f:
            f.write(data)
            print(f'第{index}页数据写入成功')
        sleep(3)


# 开始爬虫
if __name__ == '__main__':
    start()
