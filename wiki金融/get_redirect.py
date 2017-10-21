# Created by Gotcha on 2017/10/10.
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def get(filename):
    url = 'https://zh.wikipedia.org/w/index.php?title=Special:链入页面/' + filename + '&hidelinks=1&hidetrans=1';
    htmlname = './redirect_html/' + filename + 'redirect' + '.html'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    content = soup.find(id='mw-content-text')
    if content.find_all('a', recursive=False):
        file = open(htmlname, 'w', encoding='utf-8')
        file.write(response.text)
        file.close()
        fs.set_description('%s writen'%filename)



if __name__ == '__main__':
    i = 0
    for _, __, files in os.walk('E:/Mine/NLP/WikiCrawler/data'):
        fs = tqdm(files, desc=u'file writen')
        for file in fs:
            index = file.rfind('.')
            filename = file[0:index]
            get(filename)
            i += 1