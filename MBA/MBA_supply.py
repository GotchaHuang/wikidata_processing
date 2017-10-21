# Created by Gotcha on 2017/10/14.
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import random
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

url = 'http://wiki.mbalib.com/wiki/MBA%E6%99%BA%E5%BA%93%E7%99%BE%E7%A7%91:%E5%88%86%E7%B1%BB%E7%B4%A2%E5%BC%95'
user_pwd = 'http://azurejchen:r0ih8ois@'
proxy1 = user_pwd + '120.26.167.140:16816'
proxy2 = user_pwd + '115.28.146.28:16816'
proxy3 = user_pwd + '120.24.171.107:16816'
proxy4 = user_pwd + '116.62.113.134:16816'
proxy5 = user_pwd + '120.27.125.149:16816'
proxy6 = user_pwd + '114.215.174.49:16816'
proxy7 = user_pwd + '121.42.148.121:16816'
proxy8 = user_pwd + '122.114.69.82:16816'
proxy9 = user_pwd + '121.199.6.124:16816'
proxy10 = user_pwd + '120.27.218.32:16816'
proxy11 = user_pwd + '43.226.164.60:16816'
proxy12 = user_pwd + '122.114.69.239:16816'
proxy13 = user_pwd + '182.61.31.60:16816'
proxy14 = user_pwd + '117.48.198.205:16816'
proxy15 = user_pwd + '116.62.112.142:16816'
proxy16 = user_pwd + '116.196.107.90:16816'
proxy17 = user_pwd + '121.42.140.113:16816'
proxy18 = user_pwd + '122.114.234.157:16816'
proxy19 = user_pwd + '120.25.71.27:16816'
proxy20 = user_pwd + '122.114.214.159:16816'

proxies = [{'http': proxy1}, {'http': proxy2}, {'http': proxy3}, {'http': proxy4}, {'http': proxy5}, {'http': proxy6}, {'http': proxy7}, {'http': proxy8}, {'http': proxy9}, {'http': proxy10}, {'http': proxy11}, {'http': proxy12}, {'http': proxy13}, {'http': proxy14}, {'http': proxy15}, {'http': proxy16}, {'http': proxy17}, {'http': proxy18}, {'http': proxy19}, {'http': proxy20}]

proxyfirst = random.choice(proxies)
response = requests.get(url, proxies=proxyfirst, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
response.close()
divs = soup.find(id='bodyContent').find_all('div', recursive=False)


def get(category, *subcategories):
    count = 1
    for div in divs:
        h3 = div.find('h3')
        if h3 and h3.get_text().find(category) != -1:
            if not subcategories:
                ps = div.find_all('p')
                p = ps[len(ps)-1]
                a = p.find_all('a')
                if a:
                    sum = len(a)
                    for link in a:
                        subtitle = link.get_text()
                        print('%s processing %d/%d' % (subtitle, count, sum))
                        get_item(subtitle)
                        count += 1


def get_item(subtitle):
    subtitle_url = 'http://wiki.mbalib.com/wiki/Category:' + subtitle
    proxy = random.choice(proxies)
    try:
        subtitle_response = requests.get(subtitle_url, timeout=4, proxies=proxy, headers=headers)
    except Exception as e:
        print('subcategory ' + subtitle + ' timeout')
        return
    sub_soup = BeautifulSoup(subtitle_response.text, 'lxml')
    subtitle_response.close()
    content = sub_soup.find(id='bodyContent')
    if content:
        lis = content.find_all('li')
        for li in lis:
            links = li.find_all('a')
            if links[0].get_text() == '+':
                get_item(links[1].get_text())
            else:
                get_html(links[0].get_text())
                print('%s done' % links[0].get_text())


def get_html(item_name):
    item_url = 'http://wiki.mbalib.com/wiki/' + item_name
    proxy = random.choice(proxies)
    try:
        item_response = requests.get(item_url, timeout=2, proxies=proxy, headers=headers)
    except Exception as e:
        print('item ' + item_name + ' timeout')
        return
    index = item_name.find('/')
    if index != -1:
        item_name = item_name[:index] + item_name[index+1:]
    while True:
        index = item_name.find('"')
        if index != -1:
            item_name = item_name[:index] + item_name[index+1:]
        else:
            break
    while True:
        index = item_name.find("'")
        if index != -1:
            item_name   = item_name[:index] + item_name[index+1:]
        else:
            break
    filename = './MBA_' + dir_name + '/' + item_name + '.html'
    file = open(filename, 'w', encoding='utf-8')
    file.write(item_response.text)


requests.adapters.DEFAULT_RETRIES = 5

if __name__ == '__main__':
    print('====head====')
    dir_name = '金融百科_supply'
    get('金融百科')
    print('====tail====')
    print(time.clock())
