# Created by Gotcha on 2017/10/10.
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import telnetlib
import random

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
proxy = {'http': 'http://#@122.114.69.82:16816'}
# url = 'http://wiki.mbalib.com/wiki/MBA%E6%99%BA%E5%BA%93%E7%99%BE%E7%A7%91:%E5%88%86%E7%B1%BB%E7%B4%A2%E5%BC%95'
url_text = 'http://www.baidu.com'
url = 'http://http://wiki.mbalib.com/wiki/ISO134'
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

proxies = [{'http': proxy1}, {'http': proxy2}, {'http': proxy3}, {'http': proxy4}, {'http': proxy5}, {'http': proxy6}, {'http': proxy7}, {'http': proxy8}, {'http': proxy9}, {'http': proxy10}]

response = requests.get(url, proxies=proxies[8], headers=headers)
print(response.text)
try:
    tn = telnetlib.Telnet('118.114.77.47', port='8080', timeout=20)
except:
    print('fail')
else:
    print('available')

# user_pwd = 'http://azurejchen:r0ih8ois@'
# proxy1 = user_pwd + '122.114.69.82:16816'
# proxy2 = user_pwd + '121.199.6.124:16816'
# proxy3 = user_pwd + '120.24.171.107:16816'
# proxy4 = user_pwd + '116.62.113.134:16816'
# proxy5 = user_pwd + '120.27.218.32:16816'
#
# proxies = [{'http': proxy1}, {'http': proxy2}, {'http': proxy3}, {'http': proxy4}, {'http': proxy5}]
#
# for i in range(5):
#     print(random.choice(proxies))
