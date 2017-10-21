# Created by Gotcha on 2017/9/29.
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import threading
from bs4 import BeautifulSoup
import re
import os

count = 14762

def crawler(url, title):
    # title_index = url.rfind('/')
    # url_title = url[title_index+1:]
    # url_file = dir + url_title + '.txt'
    # if os.path.exists(url_file):
    #     return

    global count
    if url.find('index.php') != -1 or count == 100000:
        return
    # response = requests.request("GET", url, headers=headers)
    try:
        response = requests.get(url, timeout=1, headers=headers)
    except Exception as e:
        print(e)
        return

    soup = BeautifulSoup(response.text, "lxml")
    content = soup.find(attrs={'class' : 'mw-parser-output'})

    text = ''
    if content:
        for para in content.find_all('p', recursive=False):
            para_text = para.get_text(strip=True)
            if para_text.find('维基百科目前还没有与上述标题相同的条目') != -1:
                return
            text += para_text

        text = pattern.sub('', text)

        file_name = dir + title + '.txt'
        if len(text) > 50 and not os.path.exists(file_name):
            file = open(file_name, 'w', encoding='utf-8')
            file.write(text)
            count += 1
            print(title + ' writen ' + 'file_num: ' + str(count))

        for link in content.find('p').find_all('a'):
            sub_href = link.get('href')
            if sub_href:
                index = sub_href.rfind('/')
                title = link.get('title')
                if index != 0 and index != -1 and title:
                    url_file = dir + title + '.txt'
                    if not os.path.exists(url_file):
                        href = prefix + sub_href[index:]
                        get_para(href, title)


def get_para(url, title):
    th = threading.Thread(target=crawler, args=(url, title))
    th.start()


def main():
    crawler('https://zh.wikipedia.org/zh-cn/%E5%91%A8%E6%9D%B0%E5%80%AB', '周杰伦')


if __name__ == '__main__':
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"
    }
    prefix = 'https://zh.wikipedia.org/zh-cn'
    pattern = re.compile('\[.*\]')
    dir = 'E:/Mine/NLP小组/paras/'
    requests.adapters.DEFAULT_RETRIES = 5
    main()
