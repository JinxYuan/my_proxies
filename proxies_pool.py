import requests
from lxml import etree
import time
from concurrent.futures import ThreadPoolExecutor


tpe = ThreadPoolExecutor(max_workers=3)


def write_proxies(proxy):
    print(proxy)
    with open('proxies.txt', 'a') as f:
        f.write(proxy + '\n')


def parse(html):
    tr_list = html.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
    for tr in tr_list:
        type = tr.xpath('./td[4]/text()')[0]
        ip = tr.xpath('./td[1]/text()')[0]
        port = tr.xpath('./td[2]/text()')[0]
        proxy = type + '://' + ip + ':' + port
        tpe.submit(write_proxies, proxy)
        time.sleep(2)


def request_url(star_page, end_page):
    for i in range(star_page, end_page):
        url_str = 'https://www.kuaidaili.com/free/inha/%d/' % star_page
        response = requests.get(url_str, headers=request_head())
        html = etree.HTML(response.content)
        parse(html)


def request_head():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    return headers


def main():
    request_url(1, 3)


if __name__ == "__main__":
    main()
