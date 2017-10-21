# Created by Gotcha on 2017/9/30.
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os

pattern = re.compile('\[.*?\]')
sent_patt = re.compile('.*?。')
dir = '../cutted-paras'

def handle(path):
    count = 1
    file = open(path, encoding='utf-8')
    test = file.read()
    test = pattern.sub('', test)
    index = path.rfind('/')
    new_para = ''
    for sent_iter in sent_patt.finditer(test):
        sent = sent_iter.group()
        new_para += sent
        if len(new_para) < 200:
            continue
        else:
            new_para_path = dir + path[index:-4] + str(count) + '.txt'
            new_file = open(new_para_path, 'w', encoding='utf-8')
            new_file.write(new_para)
            print(new_para_path + 'finished. ' + 'len: ' + str(len(new_para)))
            count += 1
            new_para = ''


def main():
    for _, __, files in os.walk('E:/Mine/NLP小组/paras'):
        for file in files:
            file_name = '../paras/' + file
            handle(file_name)


if __name__ == '__main__':
    main()