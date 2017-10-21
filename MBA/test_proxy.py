# Created by Gotcha on 2017/10/13.
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

url = 'http://www.xicidaili.com/nn/1'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
ips = soup.findAll('tr')

for x in range(1,len(ips)):
    ip = ips[x]
    tds = ip.findAll("td")
    ip_temp = tds[2].contents[0]+"\t"+tds[3].contents[0]+"\n"
    # print tds[2].contents[0]+"\t"+tds[3].contents[0]
    print(ip_temp)
