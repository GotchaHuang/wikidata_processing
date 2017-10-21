# Created by Gotcha on 2017/10/9.
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
from tqdm import tqdm

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def get(filename):
    url = 'https://zh.wikipedia.org/wiki/' + filename
    htmlname = './html_data/' + filename + '.html'
    response = requests.get(url, headers=headers)
    file = open(htmlname, 'w', encoding='utf-8')
    file.write(response.text)
    file.close()


if __name__ == '__main__':
    i = 0
    for _, __, files in os.walk('E:/Mine/NLP/WikiCrawler/data'):
        fs = tqdm(files, desc=u'0 done')
        for file in fs:
            index = file.rfind('.')
            filename = file[0:index]
            get(filename)
            i += 1
            fs.set_description(u'%s done'%i)

