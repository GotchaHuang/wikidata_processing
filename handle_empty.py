# Created by Gotcha on 2017/10/14.
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
import random
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


def handle(dir):
    for root, dirs, files in os.walk(dir):
        for f in files:
            index = f.find('.')
            item_name = f[:index]
            filename = os.path.join(root, f)
            size = os.path.getsize(filename)
            if size == 0:
                item_url = 'http://wiki.mbalib.com/wiki/' + item_name
                proxy = random.choice(proxies)
                try:
                    item_response = requests.get(item_url, timeout=10, proxies=proxy, headers=headers)
                    soup = BeautifulSoup(item_response.text, "lxml")
                    item_response.close()
                except Exception as e:
                    print('item ' + item_name + ' timeout')
                    continue
                cont = soup.find(id='content')
                if cont:
                    h = cont.find('h1', recursive=False)
                    if h.get_text() == '首页':
                        os.remove(filename)
                        print(item_name + ' removed')
                        continue
                new_file = open(filename, 'w', encoding='utf-8')
                new_file.write(item_response.text)
                print(item_name + ' reloaded')



handle('../MBAdata/MBA_法律百科')
# handle('./MBA_timeout')