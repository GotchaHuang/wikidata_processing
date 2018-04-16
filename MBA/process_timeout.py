# Created by Gotcha on 2017/10/13.
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
import random
import time
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

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


def re_get(item_name):
    item_url = 'http://wiki.mbalib.com/wiki/' + item_name
    proxy = random.choice(proxies)
    try:
        item_response = requests.get(item_url, timeout=10, proxies=proxy, headers=headers)
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
            item_name = item_name[:index] + item_name[index+1:]
        else:
            break

    filename = './MBA_' + dir_name + '/' + item_name + '.html'
    new_file = open(filename, 'w', encoding='utf-8')
    new_file.write(item_response.text)
    print(item_name + ' done')


def category_get(category):
    subtitle_url = 'http://wiki.mbalib.com/wiki/Category:' + category
    proxy = random.choice(proxies)
    try:
        subtitle_response = requests.get(subtitle_url, timeout=10, proxies=proxy, headers=headers)
    except Exception as e:
        print('subcategory ' + category + ' timeout')
        category_get(category)
        return
    sub_soup = BeautifulSoup(subtitle_response.text, 'lxml')
    subtitle_response.close()
    content = sub_soup.find(id='bodyContent')

    if content:
        lis = content.find_all('li')
        for li in lis:
            links = li.find_all('a')
            if links[0]:
                if links[0].get_text() == '+':
                    category_get(links[1].get_text())
                else:
                    re_get(links[0].get_text())
    print('category %s done' % category)


def handle(text):
    # pattern = re.compile('item (.*) timeout')
    # file = open('./timeout.txt', encoding='utf-8')
    # text = file.read()
    # names = pattern.findall(text)
    # for name in names:
    #     re_get(name)
    #
    # cate_pattern = re.compile('category (.*) timeout')
    # categories = cate_pattern.findall(text)
    # for category in categories:
    #     category_get(category)

    pattern_remove = re.compile('(.*) removed')
    for item in pattern_remove.findall(text):
        removed_file.write(item + '\n')


if __name__ == '__main__':
    removed_file = open('./removed_list_经济百科.txt', 'w', encoding='utf-8')
    file = open('./timeout.txt', encoding='utf-8')
    alltext = file.read()
    # part_pattern = re.compile('====head====([\s\S]*?)====tail====')
    # texts = part_pattern.findall(alltext)
    # print('====head====')
    # dir_name = 'timeout'
    handle(alltext)
    # print('====tail====')
    # print('====head====')
    # dir_name = '经济百科_supply'
    # handle(texts[1])
    # print('====tail====')